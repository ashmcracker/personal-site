#!/usr/bin/env python3
"""扫描仓库中的 HTML 文档，并生成/更新 index.html 的索引区块。

用法：
    python scripts/gen_index.py            # 有变化时写入 index.html
    python scripts/gen_index.py --check    # 仅检查是否最新（有变化时退出码 1，用于 CI）

设计要点：
* 只依赖 Python 标准库，无需安装任何包。
* 幂等：生成结果与文件中已有内容一致时不写文件、不产生 diff。
* 统一使用 LF 换行，避免 Windows / Linux 之间来回产生无意义 diff。
"""

import argparse
import html
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.html"
START_MARK = "<!-- NOTES:START -->"
END_MARK = "<!-- NOTES:END -->"

# 这些目录下的 HTML 不进索引
SKIP_DIRS = {".git", ".github", "scripts", "node_modules", "vendor", "dist", "build", "__pycache__"}
# 这些文件不进索引
SKIP_FILES = {"index.html", "404.html"}
# 非内容目录：模板/样式/附件，不纳入文档列表
ASSET_DIRS = {"assets", "static", "public", "images", "img", "files"}

# 分组展示顺序，未列出的按字母序排在后面
GROUP_ORDER = ["notes", "resume", "cv", "docs", "blog", "projects", "labs", "demos"]

MAX_DESC = 150


def clean_text(raw: str) -> str:
    """去掉标签、压缩空白，得到可读纯文本。"""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_title(source: str, fallback: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", source, re.I | re.S)
    if m and clean_text(m.group(1)):
        return clean_text(m.group(1))
    m = re.search(r"<h1[^>]*>(.*?)</h1>", source, re.I | re.S)
    if m and clean_text(m.group(1)):
        return clean_text(m.group(1))
    return fallback


def extract_desc(source: str) -> str:
    """优先 meta description，其次正文首个段落。"""
    patterns = [
        r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']',
        r'<meta[^>]+content=["\'](.*?)["\'][^>]*name=["\']description["\']',
        r'<meta[^>]+property=["\']og:description["\'][^>]*content=["\'](.*?)["\']',
    ]
    for pat in patterns:
        m = re.search(pat, source, re.I | re.S)
        if m and clean_text(m.group(1)):
            return clean_text(m.group(1))[:MAX_DESC]

    body = re.search(r"<body[^>]*>(.*?)</body>", source, re.I | re.S)
    body_text = body.group(1) if body else source
    body_text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body_text, flags=re.I | re.S)
    m = re.search(r"<p[^>]*>(.*?)</p>", body_text, re.I | re.S)
    if m and clean_text(m.group(1)):
        return clean_text(m.group(1))[:MAX_DESC]
    m = re.search(r"<h[12][^>]*>(.*?)</h[12]>", body_text, re.I | re.S)
    if m and clean_text(m.group(1)):
        return clean_text(m.group(1))[:MAX_DESC]
    return ""


def git_last_commit_time(rel_path: str):
    """取文件最后一次提交时间（UTC），无 git 历史时返回 None。"""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", rel_path],
            cwd=ROOT, capture_output=True, text=True, timeout=20,
        )
        value = (out.stdout or "").strip()
        if value:
            dt = datetime.fromisoformat(value).astimezone(timezone.utc)
            return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    return None


def human_size(num: int) -> str:
    if num < 1024:
        return f"{num} B"
    if num < 1024 * 1024:
        return f"{num / 1024:.1f} KB"
    return f"{num / 1024 / 1024:.1f} MB"


def collect():
    """返回按分组排序的文档列表。"""
    docs = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        parts = rel.parts
        if any(p.startswith(".") or p.startswith("_") for p in parts[:-1]):
            continue
        if parts[0] in SKIP_DIRS:
            continue
        if parts[0] in ASSET_DIRS and len(parts) > 1:
            continue
        if path.name in SKIP_FILES and len(parts) == 1:
            continue

        posix = rel.as_posix()
        try:
            source = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue

        parent = parts[0] if len(parts) > 1 else ""
        title = extract_title(source, path.stem)
        desc = extract_desc(source)
        date = git_last_commit_time(posix)
        if date is None:
            date = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d")

        docs.append({
            "path": posix,
            "file": path.name,
            "group": parent,
            "title": title,
            "desc": desc,
            "size": human_size(path.stat().st_size),
            "date": date,
        })

    def group_rank(name: str) -> int:
        try:
            return GROUP_ORDER.index(name)
        except ValueError:
            return len(GROUP_ORDER)

    docs.sort(key=lambda d: (group_rank(d["group"]), d["group"], d["file"].lower()))
    return docs


def group_label(name: str) -> str:
    return name if name else "根目录"


def render(docs) -> str:
    lines = [START_MARK]
    if not docs:
        lines.append('<p class="empty">仓库里还没有 HTML 文档，把文件丢进来后运行 <code>python scripts/gen_index.py</code> 即可。</p>')
        lines.append(END_MARK)
        return "\n".join(lines)

    groups = []
    for doc in docs:
        if doc["group"] not in groups:
            groups.append(doc["group"])

    for group in groups:
        items = [d for d in docs if d["group"] == group]
        label = group_label(group)
        lines.append(
            f'<div class="group"><h2>{html.escape(label)}</h2>'
            f'<span class="rule"></span><span class="n">{len(items)} 篇</span></div>'
        )
        lines.append('<div class="grid">')
        for d in items:
            search = " ".join([d["title"], d["desc"], d["path"], label]).lower()
            chip = (
                f'<span class="chip">{html.escape(label)}</span>'
                if group else ""
            )
            desc_html = (
                f'<p class="desc">{html.escape(d["desc"])}</p>' if d["desc"] else ""
            )
            lines.append(
                f'<article class="note" data-search="{html.escape(search, quote=True)}">'
                f'<a class="note-inner" href="{html.escape(d["path"], quote=True)}">'
                f'<div class="note-head"><h3 class="title">{html.escape(d["title"])}</h3>{chip}</div>'
                f'{desc_html}'
                f'<div class="meta"><code>{html.escape(d["path"])}</code>'
                f'<span>{html.escape(d["size"])}</span>'
                f'<span>{html.escape(d["date"])}</span></div>'
                f'</a></article>'
            )
        lines.append("</div>")

    lines.append(END_MARK)
    return "\n".join(lines)


def splice(current: str, block: str) -> str:
    start = current.find(START_MARK)
    end = current.find(END_MARK)
    if start == -1 or end == -1 or end < start:
        raise SystemExit("index.html 中未找到 NOTES:START / NOTES:END 标记，无法更新索引。")
    return current[:start] + block + current[end + len(END_MARK):]


def main() -> int:
    parser = argparse.ArgumentParser(description="生成个人站点首页索引")
    parser.add_argument("--check", action="store_true", help="只检查，不写入；索引过期时退出码 1")
    args = parser.parse_args()

    if not INDEX.exists():
        raise SystemExit(f"未找到 {INDEX}")

    current = INDEX.read_text(encoding="utf-8")
    docs = collect()
    block = render(docs)
    updated = splice(current, block)
    changed = updated != current

    if args.check:
        print("索引已是最新。" if not changed else "索引已过期，请运行 python scripts/gen_index.py")
        return 1 if changed else 0

    if changed:
        INDEX.write_text(updated, encoding="utf-8", newline="\n")
        print(f"索引已更新：收录 {len(docs)} 篇文档。")
    else:
        print(f"索引无需更新（{len(docs)} 篇文档）。")
    return 0


if __name__ == "__main__":
    sys.exit(main())