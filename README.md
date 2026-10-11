# Ashm's Corner

个人学习笔记、技术文档与实验记录的**静态站点**，由 GitHub Pages 托管。

线上地址：<https://ashmcracker.github.io/personal-site/>

---

## 这是什么

一个零依赖、零构建的纯静态仓库：

- 任何 `.html` 文件丢进仓库，push 之后就能通过 URL 直接访问
- 首页是一个自动生成的目录页，可搜索、按分类浏览
- GitHub Actions 会在每次 push 后自动重建索引，你不需要手动维护首页

## 目录结构

```
personal-site/
├── index.html                 # 首页目录页（索引区块由脚本自动维护）
├── .nojekyll                  # 让 Pages 原样发布，不走 Jekyll 处理
├── notes/                     # 学习笔记、日常文档
├── resume/                    # （预留）简历与作品集
├── assets/                    # （预留）图片、样式等静态资源
├── scripts/
│   └── gen_index.py           # 扫描 HTML → 生成首页索引
└── .github/workflows/
    └── sync-index.yml         # push 后自动同步索引
```

## 怎么加一篇笔记

1. 把写好的 HTML 放进对应目录，例如 `notes/我的新笔记.html`
   - 单文件 HTML 最省事：CSS 直接写在 `<style>` 里，不要依赖同级文件
   - 需要共享样式时，把 CSS 放到 `assets/`，用相对路径引用（如 `../assets/style.css`）
2. commit 并 push：

   ```bash
   cd personal-site
   git add .
   git commit -m "docs: add 新笔记"
   git push
   ```

3. GitHub Actions 会自动更新首页索引，Pages 会在一两分钟内重新部署。

### 本地预览索引效果

改完 HTML 后，本地跑一下就能看到和线上一致的首页：

```bash
python scripts/gen_index.py     # 有变化才写入 index.html
python -m http.server 8000      # 然后打开 http://localhost:8000
```

`python scripts/gen_index.py --check` 只做检查不写入，索引过期时返回退出码 1（CI 校验用）。

## 本地怎么用

```bash
cd personal-site
git remote -v
git pull
# ...编辑...
git add .
git commit -m "docs: xxx"
git push
```

## 标题与描述怎么写

脚本按下面顺序抓取信息显示在首页卡片上，所以建议在 HTML 里写完整：

1. `<title>` → 卡片标题
2. `<meta name="description" content="...">` → 卡片摘要
3. 没有 meta description 时，会自动取正文第一个 `<p>` 的文字

## 约定

- 放进 `assets/`、`static/` 等目录下的 HTML 不会出现在首页索引里（当作资源而非文档）
- `index.html`、`404.html` 本身不进索引
- `.github/`、`scripts/`、`.gitignore` 等开头的目录会被跳过

## 未来计划

- [ ] 加入 `resume/` 放简历，做一个个人主页
- [ ] 把首页重构为真正的博客（按时间线 + 标签）