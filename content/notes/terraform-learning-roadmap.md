---
title: "Terraform 课程知识地图"
---

共 20 个章节，按「先地基 → 再语言 → 再规模化 → 最后团队协作」顺序排列。

## 阶段 0 · 起步

### 第 1 章 · 课程介绍与导航

`1 - Introduction`

**目标**：了解课程范围、三段式结构与配套仓库，把 60 多个练习和 5 个项目的用法记清楚

- **课程地图与三段式结构**：从基础设施即代码的价值与最佳实践讲起，先过 HashiCorp 配置语言，再学资源块、数据源、输入变量、本地变量与输出；高级部分进入工作区、对象验证、模块与状态操作，最后覆盖 Terraform Cloud。
- **练习代码与仓库资源位置**：课程由三个 GitHub 仓库组成，主仓库按章节建文件夹，模块章节拆成三个便于分离练习；练习文件夹列出全部可用练习，练习文件在每节课的资源区也能下载。

共 2 节课
  - Course Introduction
  - How to Navigate the Course

### 第 2 章 · 工具与环境搭建

`2 - Tools and Setup`

**目标**：把 AWS 账号、Terraform 与 AWS CLI、VS Code 扩展在本机装好，并验证已能访问 AWS

- **AWS 账号与 IAM 用户安全**：从零注册 AWS 账号并选定 eu-west-1 区域；给 root 用户绑定 MFA，再建一个同样带 MFA 的 IAM 管理员用户用于日常操作，避免一直使用 root 凭证。
- **Terraform CLI 安装与验证**：按官方文档在 macOS、Linux、Windows 上安装。macOS 用 Homebrew 前必须先添加 HashiCorp 的 tap，否则会装到过时的旧版本；装完用 terraform version 验证。
- **AWS CLI 安装与凭证认证**：安装 AWS CLI v2（官方 macOS 说明未列 Homebrew，但可用 brew 或 asdf 插件），再为管理员用户创建访问密钥并导出为环境变量，让 aws s3 ls 从报错变为成功。
- **VS Code 编辑器扩展**：最重要的是 HashiCorp Terraform 扩展，提供自动补全、语法校验与语法高亮；HashiCorp HCL 只面向 .hcl 文件、不含 Terraform 高亮，可选装。

共 9 节课
  - AWS Account Setup - Creating the Account
  - AWS Account Setup - Adding MFA to the Root User
  - AWS Account Setup - Creating a New Admin User
  - Windows only users - Installing Windows Subsystem for Linux
  - Windows only users - Windows Subsystem for Linux Features
  - ... 等 9 节

## 阶段 1 · 地基

### 第 3 章 · IaC 与 Terraform 导论

`3 - Introduction to Infrastructure as Code (IaC) and Terraform`

**目标**：理解 IaC 的价值、Terraform 的插件架构与 plan/apply/destroy 生命周期

- **IaC 是什么、解决什么痛点**：用代码而非控制台点击来预置和管理基础设施。命令式做法必须记住大量 CLI 命令、特性、执行顺序，面对 VPC、成百 EC2 这类庞大设施极易配置出错。
- **手工建资源 vs 代码建资源**：以创建 VPC 加公有/私有子网为例：控制台里每一步都要点，还要应付默认 VPC、命名易混等问题；换成 Terraform 则只是几段资源声明。
- **为什么选 Terraform**：对比 Pulumi、CloudFormation：平台无关可跨多个 provider、不与平台耦合、模块可组合复用，state 保存部署状态省去重复推演因而更快。
- **Terraform 架构：Core + Provider 插件**：核心负责组织与调度，provider 插件实现约定接口，封装与远程 API 交互的读取、创建、更新、删除逻辑；任何人都可按规范编写 provider。
- **Provision 阶段：plan/apply/destroy**：plan 用配置文件与 state 对比远程真实状态并输出变更计划，apply 接收并执行该计划，destroy 则彻底抹除 Terraform 管理的全部内容。

共 11 节课
  - What Is Infrastructure as Code (IaC)
  - Benefits of Infrastructure as Code
  - Creating Infrastructure Manually in AWS（任务预览） ✅
  - Creating Infrastructure Manually in AWS ✅
  - Creating Infrastructure with Terraform（任务预览） ✅
  - ... 等 11 节

### 第 4 章 · Terraform 积木块

`4 - Terraform's Building Blocks`

**目标**：手写一份可 apply 的 HCL 配置，并把 state 托管到 S3 远端后端

- **HCL 语法：block/attribute/expression**：新建 hcl.tf，认识 terraform 块与 resource 块的区别；resource 块由「类型标签 + 属性标签 + 表达式」三部分组成，标签与资源类型的组合必须全局唯一。
- **terraform 块与 required_providers**：terraform 块只允许常量，不能引用输入变量；用它声明 required_version、required_providers，以及 backend、cloud 等项目级设置，并学会用 =、>= 等运算符约束版本范围。
- **核心 CLI 命令实操**：在真实项目里跑通 terraform init / plan / apply / fmt / validate。Terraform 不需要 import，只扫描当前目录不进入子目录；新增 provider 后必须重新 init。
- **Terraform State 的作用**：state 是配置文件与真实资源之间的映射，含敏感值、outputs 与依赖关系元数据；缺了它 Terraform 无法工作，也会因此出现配置漂移问题，存储位置必须严加控制。
- **本地与远端 state 检查**：未定义 backend 时 state 默认落在本地 terraform.tfstate，apply 后才生成并附带备份文件；用 show 查看内容、确认资源、provider 归属与 outputs 都记录其中。
- **Backend：S3 与 partial backend**：backend 决定 state 存在哪，分为本地、Terraform Cloud、第三方远程三类；S3 需自建桶并用 -migrate-state 迁移，还可用 .tfbackend 文件加 -backend-config 实现按环境注入。
- **Provider 的安装、版本与命名**：provider 是 Terraform 与远程 API 的桥梁，独立开发并遵循插件架构；通过 required_providers 声明 source 与版本，本地名称可改但会导致重复 provider 报错。

共 17 节课
  - The HashiCorp Configuration Language (HCL)（任务预览） ✅
  - Introduction to HashiCorp Configuration Language (HCL)
  - Terraform Configuration
  - Our First Terraform Project（任务预览） ✅
  - Our First Terraform Project - Creating Resources ✅
  - ... 等 17 节

## 阶段 2 · 核心

### 第 5 章 · 资源与依赖

`5 - Resources`

**目标**：能从零搭出 VPC + EC2 全套基础设施，并讲清资源依赖与创建顺序

- **resource 块语法**：Terraform 配置的主体构建块，用资源类型、本地名称和属性参数管理 EC2、S3 桶等对象；参数随 provider 变化并会被校验，敏感属性不可随意输出。
- **资源依赖与创建顺序**：属性引用即隐式依赖：IAM 角色提到某个 S3 桶或引用 VPC 信息就会串起来；互不相关的资源并行创建，必要时用 replace_triggered_by 显式处理替换。
- **meta-arguments 元参数**：depends_on 定顺序，count/for_each 批量创建同类资源，provider 指定用哪个 provider，lifecycle 的 create_before_destroy 先建后拆，另有 precondition/postcondition 校验对象。
- **VPC+EC2 全流程实战**：建 VPC、公有子网、互联网网关、路由表与关联，再自定义安全组、启动 EC2 并换成免费 nginx AMI，最后整体销毁，全程只靠命令行完成。
- **公共标签抽取（locals）**：同样的 tags 要在 VPC、子网、互联网网关、路由表四处重复；locals 像函数体内的临时变量，集中定义后用 merge 函数与资源自身标签合并。
- **销毁与资源清理**：先用 terraform state list 盘点项目管理的全部资源，再执行 terraform destroy；destroy 只是带 destroy 标志的 apply，会先刷新状态再逐个回收。

共 12 节课
  - Introduction to Resources
  - Resource Dependencies
  - Meta-Arguments
  - VPC and EC2 Project - Project Overview
  - VPC and EC2 Project - Launching the VPC and Subnet
  - ... 等 12 节

### 第 6 章 · 项目：S3 静态网站

`6 - Project - S3 Static Website`

**目标**：用 Terraform 完整交付 S3 静态站点：建桶、放开公共访问、配网站配置并托管 HTML

- **S3 存储桶与版本约束**：新建 proj01-s3-static-website 目录，provider.tf 中写 required_version >= 1.7.0 且 < 2.0.0 并指定 AWS 区域；桶名全局唯一，所以在 provider 里拼上一段随机后缀，再 terraform fmt 后 apply。
- **关闭公共访问阻止**：新增 aws_s3_bucket_public_access_block 资源，把 block_public_acls、block_public_policy、ignore_public_acls、restrict_public_buckets 全设为 false，并配合桶策略允许任何人读取对象。
- **静态网站托管配置**：只开公共访问还不算网站，需 aws_s3_bucket_website_configuration 指定索引文档与错误文档并打好描述性标签；站点端点必须用 output 暴露，不能中途进控制台查看。
- **用 aws_s3_object 托管文件**：先永久删除控制台手动上传的文件，改用 aws_s3_object 声明式上传并指定 bucket 与 key；注意标识符是资源类型加标签的组合，destroy 时对象先删、桶最后删。

共 5 节课
  - Project Overview
  - Deploying an S3 Bucket
  - Disabling Public Access Block
  - Configuring the S3 Static Website
  - Uploading Files to S3 via Terraform

## 阶段 3 · 进阶

### 第 7 章 · 数据源 Data Sources

`7 - Data Sources`

**目标**：能把 AWS 上已有但不由自己管理的资源接进配置作为输入

- **data 块：读而非建**：数据源用于查询远程 provider API 或其他 Terraform 项目里的已有资源，比如别人管理的 VPC 和角色；Terraform 按过滤条件找到它们并返回对象供引用，而不会把它们纳入本项目的 state 管理。
- **拉取 AMI 数据**：用 data aws_ami 解决硬编码 AMI ID 的问题，按过滤条件筛出最新的 Ubuntu AMI 再交给 aws_instance 的 ami；写法与 resource 类似，只是开头是 data，标签组合必须唯一才能被引用。
- **获取账户 ID 与区域**：data aws_caller_identity 来自 STS 部分，可拿到 account_id，用在 IAM 策略或资源 ARN 上；data aws_region 提供当前区域信息，写资源描述或 EC2 端点时很有用。
- **拉取 VPC 信息**：对控制台手动创建（模拟别的团队管理）的 VPC，用 data aws_vpc 配 tags 过滤条件查回信息并 output vpc_id，替代硬编码 ID；但最终仍要自己确认查到的确实是正确那个 VPC。
- **data.aws_availability_zones**：获取 AWS 自身底层设施信息而非自己项目的信息：用 state = available 过滤出可用区（不写会列出所有可能状态），拿到 1a/1b/1c 这类字符串后即可在代码里引用指定可用区。
- **用 data 定义 IAM 策略文档**：data aws_iam_policy_document 用 HCL 写 statement 块（effect / actions / resources）来生成策略 JSON，替代 jsonencode 手拼字符串；多个 statement 就写多个块组成数组，resource 可引用 S3 桶的 arn。

共 10 节课
  - Introduction to Data Sources
  - Fetching AMI Data（任务预览） ✅
  - Fetching AMI Data ✅
  - Fetching AWS Account Information and Region（任务预览） ✅
  - Fetching AWS Account Information and Region ✅
  - ... 等 10 节

### 第 8 章 · 输入变量、Locals 与输出

`8 - Input Variables, Locals and Outputs`

**目标**：掌握 variable、locals、output，用类型、校验与 tfvars 写出可复用可传参的配置

- **variable 声明与类型校验**：在 variables.tf 中用 variable 块声明，配置 type、default、description，引用写 var.名称；用 validation 条件块配合 contains、startswith 等函数校验取值。
- **Map 与 Object 变量**：object({...}) 用键值对声明固定结构，适合组合式配置；map 允许任意键但强制值类型，适合 additional_tags 这类无法预知键名的场景。
- **.tfvars 与变量优先级**：terraform.tfvars 默认自动加载，*.auto.tfvars 优先级更高并覆盖前者；不含 .auto.tfvars 的 override 文件需 -var-file 显式传入，TF_VAR_ 环境变量优先级最低。
- **local 表达式**：用 locals 块定义配置内部的中间值，可以引用变量和其他 locals，但不能从外部赋值；适合跨资源复用标签、名称等公共属性。
- **output 与敏感值**：在 outputs.tf 用 output 块暴露结果，terraform output 可查询、-json 会附带额外属性；sensitive = true 只遮蔽显示，state 中仍是明文。
- **代码整理与拆分**：把变量、资源、输出分别放进 variables.tf、compute.tf、outputs.tf 管理，并清理会意外部署产生费用的 tfvars 与 auto.tfvars 覆盖项。

共 19 节课
  - Input Variables
  - Declaring and Using Input Variables（任务预览） ✅
  - Declaring and Using Input Variables ✅
  - Typing and Validating Input Variables（任务预览） ✅
  - Typing and Validating Input Variables ✅
  - ... 等 19 节

### 第 9 章 · 表达式与函数

`9 - Expressions and Functions`

**目标**：熟练使用 for、splat 表达式转换集合，并用内置函数完成字符串与数值处理

- **运算符与表达式基础**：在 locals 中用乘法、负数等数学运算符演示原始运算，并用 required_version 约束版本区间；数字主要靠运算符，其他值类型更多依赖函数。
- **for 表达式处理 list 与 map**：[for v in list : expr] 生成列表、{for k, v in map : k => expr} 生成映射；list 只有一个临时变量，map 有键和值两个，末尾都可加 if 过滤子句。
- **list 与 map 互相转换**：以 users 对象列表为例，遍历列表生成映射、再反向遍历映射生成列表，用 ... 省略号简化重复结构，并通过反复执行 plan 验证输出。
- **splat 表达式**：用 splat 一行取出列表中所有元素的某个属性，替代冗长的 for 循环；它只适用于列表及类列表值类型，不能用于 map，map 场景可用 values() 等函数。
- **内置函数分类总览**：查阅路径是 developer.hashicorp.com 的 Terraform 主页 → 文档 → 配置语言 → 函数；含数值、字符串、集合等函数，不能自定义函数，can 常用于变量校验。
- **综合练习：函数实战**：在 10-functions 目录用 locals 试 name、age 等示例，练习字符串与数值函数的嵌套组合，并反复用 terraform plan 验证、terraform fmt 整理格式。

共 12 节课
  - Operators in Terraform（任务预览） ✅
  - Operators in Terraform ✅
  - Using for Expressions with Lists（任务预览） ✅
  - Using for Expressions with Lists ✅
  - Using for Expressions with Maps（任务预览） ✅
  - ... 等 12 节

## 阶段 4 · 规模化

### 第 10 章 · 批量创建资源

`10 - Creating Multiple Resources`

**目标**：用 count 与 for_each 批量创建子网与 EC2 实例，并用 validation 约束变量配置

- **count 元参数**：决定要创建的资源实例个数，可写在单个资源或模块里，既能硬编码也能取自变量；必须在 Terraform 执行任何远程操作之前就确定下来。
- **for_each 元参数**：接受一个映射或字符串集合（如 toset 结果），块内用 each.key、each.value 取值；只要键保持稳定，Terraform 就能准确找到对应资源。
- **引用 count 创建的资源**：aws_instance.name[索引] 访问某一个具体实例，只写 aws_instance.name 则拿到全部实例；常把 count.index 拼进 Name 标签区分实例，也是销毁时定位的依据。
- **基于 List 变量批量建 EC2**：list(object({instance_type, ami})) 配 count = 列表长度，用 count.index 取出元素配置实例，并用取模运算轮询分配子网；调整列表顺序会导致实例被重建。
- **基于 Map 变量批量建 EC2**：改用 map(object) + for_each，每个键就是一个稳定标识、each.value 是该键对应的配置；重排顺序不会引发销毁重建，更适合长期维护。
- **变量 validation 进阶**：对 object 列表逐元素校验：用 for 表达式先映射成字符串列表，再映射成布尔列表，最后检查是否全为 true；断言失败要给出可读的错误信息。
- **接收 Subnet 信息**：把硬编码的子网数量变量换成 map(object({cidr_block})) 的 subnet_config，子网用 for_each 创建，实例即可按 key 精确引用对应子网。

共 17 节课
  - Working with count and for_each
  - Creating Multiple Subnets with the Count Meta-Argument（任务预览） ✅
  - Creating Multiple Subnets with the Count Meta-Argument ✅
  - Referencing Resources with the Count Meta-Argument（任务预览） ✅
  - Referencing Resources with the Count Meta-Argument ✅
  - ... 等 17 节

## 阶段 5 · 项目

### 第 11 章 · 项目：IAM 用户管理

`11 - Project - IAM User Management`

**目标**：用 YAML 数据驱动完整实现 IAM 用户、角色与最小权限模型并验证

- **用 YAML 存用户/角色数据**：user_roles.yaml 里 users 是对象数组，每项含 username 与 roles 列表。比直接改 .tf 更解耦，产品负责人等非技术人员也能自行添加用户，但仍需了解 YAML 语法。
- **for_each + yamldecode 建用户**：用 file() 读取、yamldecode() 解码得到 users_from_yaml，再用 splat 表达式映射出用户名列表配 for_each 批量建 aws_iam_user，并为每个用户创建 login_profile。
- **用户密码输出与安全提醒**：password_length 至少 8 个字符，传更短会失败。课程为了测试登录直接把密码输出到控制台，并强调生产环境绝不能这么做，应把密码安全地交付给用户。
- **AWS 托管策略 vs 自定义策略**：托管策略由 AWS 预置，如 ReadOnlyAccess、AdministratorAccess、SecurityAudit 以及各服务的 FullAccess。角色本身默认什么都做不了，必须附加策略才真正有权限。
- **创建 IAM Role 与 assume role policy**：用 aws_iam_role 加 for_each 建只读/管理员/审计员/开发者四个角色，先由 data aws_iam_policy_document 生成 assume_role_policy，再用 aws_iam_policy_attachment 把托管策略挂上去。
- **限制可扮演角色的 Principal**：为每个角色单独生成一份 assume role policy，标识列表里只放 YAML 中该角色 users 列表内的用户，修掉此前「任何用户都能代入所有角色」的安全隐患。
- **测试与清理**：逐个用新建用户登录控制台，验证只能切换到分配给自己的角色、权限确实生效，确认无误后用 terraform destroy 一次性回收所有用户、角色与策略。

共 9 节课
  - Project Overview
  - Storing User and Role Information in YAML
  - Creating Users in AWS
  - Creating User Passwords
  - Understanding AWS Managed Policies
  - ... 等 9 节

## 阶段 6 · 工程化

### 第 12 章 · 模块 Modules

`12 - Modules`

**目标**：掌握模块设计最佳实践，独立实现并测试一个 VPC 模块，最终发布到 Terraform Registry

- **模块是什么与复用价值**：从技术上讲模块只是保存在同一目录下的一组 Terraform 文件；区分 root module 与 child module，模块用来组织、封装、复用常一起使用的资源。
- **标准模块目录结构**：LICENSE、main.tf、variables.tf、outputs.tf、README.md 组成的推荐最小文件集；main.tf 只是惯例，复杂模块可按资源拆成 vpc.tf 等命名贴切的文件。
- **在 Registry 浏览公开模块**：在 registry.terraform.io 首页点 Browse Modules 浏览列表，顶部可在 provider 与 module 间切换；模块依赖 provider（如 AWS），本身只是资源的封装集合。
- **读懂 AWS VPC/EC2 模块源码**：从 Registry 模块页的 Source code 跳到 GitHub 仓库，看 main.tf 里的 resources 与 locals 分区、variables.tf 对应页面 inputs，以及与 Registry 一致的 README。
- **调用公开 VPC/EC2 模块**：写 module 块指定 source（terraform-aws-modules/vpc/aws 等）与固定 version，用 locals 收敛 cidr、项目名与公共标签；init 会把模块下载到 .terraform/modules。
- **模块设计最佳实践**：识别值得抽取的抽象边界与强关联资源组、隐藏内部细节；相关变量归入 object，稳定资源与频繁变更资源分模块，保持精简扁平可组合，不做大而全。
- **自建 VPC 模块全流程**：从本地模块骨架到 object 变量、map(object) 子网配置、可用区 validation、公私子网与 IGW 路由，最后定义 vpc_id 与子网 ID 等 outputs。
- **用 EC2 实例测试模块**：根模块建 compute.tf，复制 AMI 数据源与 aws_instance 资源，直接用 module.vpc 输出的 subnet_1_id 验证模块；验证完销毁资源，避免实例产生费用。
- **补齐 LICENSE 与 README**：选定 MIT 等许可证并考虑复用传染性；README 写清支持的 Terraform/provider、输入输出与用法示例，examples 目录放不同使用模式，Registry 用它生成文档。
- **发布模块到 Registry**：满足公开 GitHub 仓库、README、LICENSE、标准模块结构等要求，在 Registry 发布新 tag 即可被 module source 引用；建议用 CI/CD 流水线自动发布。

共 26 节课
  - What Are Modules
  - The Standard Module Structure
  - Browsing Public Modules in the Terraform Registry
  - Exploring the AWS VPC Module GitHub Repository
  - Using the Public AWS VPC Module（任务预览） ✅
  - ... 等 26 节

### 第 13 章 · 对象校验

`13 - Object Validation`

**目标**：用 precondition、postcondition 与 check 在 plan 阶段就挡住非法配置

- **precondition 与 postcondition**：两者都写在资源或数据块的 lifecycle 块中；precondition 不能引用资源自身，只能校验资源外部的数据或变量，postcondition 则可以引用定义它的那个资源本身。
- **check 断言块**：较新的 Terraform 版本才提供，内部用 assert 写 condition 与 error_message；用于非关键检查，失败只发出警告，不会中断 terraform apply 的执行。
- **校验的执行时机与顺序**：plan 阶段先判断校验所需信息是否已可用，可用就当场执行、不可用则推迟到 apply；plan 阶段就失败的校验会让 Terraform 报错退出，不进入 apply。

共 8 节课
  - Preconditions and Postconditions
  - Working with Preconditions（任务预览） ✅
  - Working with Preconditions ✅
  - Working with Postconditions（任务预览） ✅
  - Working with Postconditions ✅
  - ... 等 8 节

### 第 14 章 · 状态操作 State Manipulation

`14 - State Manipulation`

**目标**：掌握 state 操作，安全重构代码、纳管已有资源与强制替换异常资源

- **state 操作总览**：说明 state 的作用与何时需要手工操作：资源异常损坏、已有资源想纳管、只想停止跟踪，或需要强制解除卡住的状态锁、从远程后端拉取推送状态。
- **重构资源：state mv 与 moved**：移动资源有两条路径：terraform state mv 命令与 moved 块；配合 terraform fmt -recursive、init 与 apply 验证，改资源地址或拆文件而不重建实例。
- **导入已有资源**：对已在 AWS 手工创建、或由别的团队从其 Terraform 中移交出来的资源，用 CLI 或 import 块导入；先查 provider 文档的 import 说明，块可放资源旁或单独文件。
- **移除但不销毁资源**：把资源注释掉会让 plan 提议销毁；正确做法是用 CLI 命令或 removed 块把对象从 state 中移除，让 Terraform 停止跟踪而 AWS 上的真实资源保留。
- **taint 强制重建**：资源进入无效或失败状态、但配置本身没改动时，用 terraform taint 标记后由下一次 apply 强制替换重建，用 untaint 取消标记。

共 9 节课
  - Introduction to State Manipulation
  - Refactoring Terraform Resources（任务预览） ✅
  - Refactoring Terraform Resources ✅
  - Importing Existing Infrastructure into Terraform（任务预览） ✅
  - Importing Existing Infrastructure into Terraform ✅
  - ... 等 9 节

## 阶段 7 · 项目

### 第 15 章 · 项目：导入 Lambda 资源

`15 - Project - Importing Lambda Resources`

**目标**：完整走通一次已有服务纳管：把手工创建的 Lambda 及其角色、策略、日志组全部导入并重构

- **手工创建 Lambda 并盘点资源**：在控制台用 Hello World 模板创建函数并新建带基本 Lambda 权限的角色，再逐项检查后台生成了哪些资源，为后续导入建立清单。
- **导入 Lambda 函数本体**：建 project03 目录与 provider.tf，查 AWS provider 文档的 import 部分复制 import 块；此时 plan 会因缺 filename、image URI 或 S3 选项而失败。
- **导入函数代码：zip 打包**：Lambda 部署包只支持容器镜像或 zip 归档；filename 不能直接指向 JS 文件，需引入 archive provider 与 archive_file 数据源打包。
- **导入执行角色与信任策略**：从权限页取角色名导入 aws_iam_role，并用 aws_iam_policy_document 数据源生成 sts:AssumeRole 信任策略，替换硬编码的转义 JSON。
- **策略重构为 policy document**：把内联策略迁进 aws_iam_policy_document 数据源，resource 用 aws_caller_identity 与 aws_region 数据源限定账户与区域，行为保持不变。
- **导入 CloudWatch Log Group**：日志组不属于 IAM，放在 CloudWatch 文件中；查文档选 aws_cloudwatch_log_group 资源按名称 import，注意与只读 data source 的区别。
- **default_tags 与新增资源**：provider 加 default_tags 后四个资源批量打标；再新增 aws_lambda_function_url（授权 aws_iam 或 none），最后 destroy 验证纳管结果。

共 9 节课
  - Project Overview
  - Creating a Lambda Function Manually
  - Importing the Lambda Function
  - Importing the Function Code
  - Importing the Function Role
  - ... 等 9 节

### 第 16 章 · 项目：RDS 模块

`16 - Project - RDS Module`

**目标**：独立完成带变量与网络校验的生产级 RDS 模块，并正确销毁全部资源

- **拆解需求与校验点**：先建 project04 目录和 README.md，把要做的事列成清单：先理解 RDS 资源与它依赖的资源，再建标准结构的模块，然后实现并测试变量校验，全部通过后才部署实例。
- **AWS RDS 资源属性**：通读 aws_db_instance 的 provider 文档，关注实例类型、低停机时间更新和基本用法；不显式传参时 Terraform 会用默认 VPC、默认安全组和默认子网，必须自备并传入。
- **模块变量设计**：在 modules/rds 下拆成 variables.tf、outputs.tf、providers.tf；变量含 name、instance_class、storage_size、engine 等，可加默认值并直接写 validation 的 condition。
- **测试变量 validation**：在 project04 建 rds.tf 以 module + source 调用模块，先补齐必填变量和 provider 配置，再用 terraform validate 逐条确认 condition 真的会在非法输入时报错。
- **subnet_ids 与 sg_ids 变量**：不传子网与安全组就会落到 AWS 默认值，因此新增两个输入变量；注意变量的 validation 块做不了这种复杂校验，需要借助 data 源和 postcondition 另做方案。
- **默认 VPC 与私有标签校验**：模块内不创建子网，用 data aws_subnet 拿信息，在 postcondition 中确保子网不在默认 VPC，并检查 access 标签取小写后等于 private。
- **安全组规则校验**：先用 aws_vpc_security_group_rules 按安全组 ID 过滤拿到规则 ID，再 for_each 逐条评估，确保没有任何入站规则放行 IP 或 CIDR，流量只能来自其他安全组。
- **部署与清理**：用 locals 把 postgres-latest 等友好选项映射为 engine、version、family，创建 aws_db_subnet_group 与 aws_db_instance，最后一条 terraform destroy 按依赖顺序删掉全部资源。

共 14 节课
  - Project Overview
  - Defining the Necessary Steps and Validations
  - Exploring the AWS RDS Resource in Terraform
  - Defining Necessary Module Variables
  - Testing Variable Validation
  - ... 等 14 节

## 阶段 8 · 团队

### 第 17 章 · 工作区 Workspaces

`17 - Terraform Workspaces`

**目标**：用 workspace 隔离 dev/staging/prod 三套环境，并用 tfvars 承载差异配置

- **CLI workspace 的作用**：用单一代码库管理多个环境：复用同一个配置目录，靠不同的 state 文件区分，减少代码重复，也不用安装多份 module 和 provider；切到某工作区后其他工作区的资源不会被纳入。
- **创建与切换 workspace**：terraform init 会自动创建 default 工作区；terraform workspace --help 看子命令，new 创建、list 列出、select 切换、show 查看当前；不能删除当前所处的工作区，必须先切走。
- **多 workspace 并行管理**：每个工作区对应独立的 state 文件（放在 terraform.tfstate.d 下的子目录），资源互不可见；配置中可用 terraform.workspace 表达式感知当前环境，把环境名拼进资源名。
- **.tfvars 存环境差异配置**：用 touch 建 dev.tfvars、staging.tfvars、prod.tfvars 存放各环境差异值，apply / destroy 时用 -var-file 传入；这比在代码里堆 if 与三元表达式可维护得多。
- **资源与 workspace 清理**：逐个 terraform workspace select 进入目标工作区后 terraform destroy 销毁其资源，再 terraform workspace delete 删除工作区，对应的 state 子目录会随之消失。

共 8 节课
  - Introduction to CLI Workspaces
  - Creating Workspaces in the CLI（任务预览） ✅
  - Creating Workspaces in the CLI ✅
  - Working with Multiple Workspaces（任务预览） ✅
  - Working with Multiple Workspaces ✅
  - ... 等 8 节

### 第 18 章 · Terraform Cloud

`18 - Terraform Cloud`

**目标**：用 Terraform Cloud 把 Terraform 接入远程执行、审批与团队协作流程

- **Terraform Cloud 是什么**：HashiCorp 提供的远程执行平台：变更审批的访问控制、安全的 state 与机密存储、资源图形化视图、组织内共享模块的私有 Registry、策略管控，以及 plan/apply 运行历史；分免费与付费两档，资源归入 workspace，workspace 再归入 project。
- **TFC Workspace 模型**：任何代码不关联 workspace 就无法放进 TFC；workspace 是 RBAC 核心，可按工作区授予读或写权限，付费计划还提供健康检查与告警。配置不再存本地磁盘，而是通过 API/CLI 推送或 VCS 拉取，变量传递方式也不同。
- **CLI 登录与 cloud 配置**：用 terraform login 打开浏览器授权，API 凭证写入本地文件；随后在 provider.tf 的 terraform/cloud 块里指定 organization 与 hostname，把本地项目与云端 workspace 绑定，目录不对会导致连错项目。
- **用环境变量认证 AWS**：运行实际发生在 TFC 的 agent 上，读不到本地环境变量，必须把 AWS_ACCESS_KEY_ID 与 AWS_SECRET_ACCESS_KEY 设为 workspace 作用域的环境变量；只适合实验，长期使用应换成 OIDC 短期凭证。
- **Workspace 变量与变量集**：区分 Terraform 变量与环境变量：代码里写 variable 定义并加 validation，再到 workspace 变量页用同名 key 注入值，可标记为 HCL；Variable Sets 能把同一组配置共享给多个 workspace。
- **State 历史与面板**：左侧 States 面板保留每次运行的状态快照，可逐个打开对比（随机 ID → S3 存储桶 → EC2 实例）；工作区概览还会列出资源与输出值，付费计划另有持续校验与自动漂移检测。
- **接入 GitHub 走 VCS 流程**：建私有仓库并加 .gitignore 与 README，授权 GitHub App，让 TFC 能访问该仓库；在项目下新建 VCS 驱动的 workspace 并选择仓库，之后每次 push 仓库变更都会自动触发一次 plan。
- **PR 触发 speculative plan**：从特性分支创建 Pull Request 后，TFC 自动对该 PR 跑一次 speculative plan；它挂在 PR 上而非 workspace 页面，用来判断这次改动会给真实基础设施带来什么影响，评审通过再合并到默认分支。
- **私有 Registry 发布模块**：在 TFC 首页的 Registry 点 publish module，选已装好的 GitHub App，按 terraform-<provider>-<name> 命名筛选出仓库并按 tag 发布；之后 source 指向 app.terraform.io 加组织与模块名即可引用私有模块。
- **清理工作区与模块**：在 Settings 的 Destruction and Deletion 中排队 destroy plan、输入 workspace 名称确认并 apply 清空资源，再取消发布私有模块、删除 workspace，让 Terraform Cloud 回到干净状态。

共 22 节课
  - What is Terraform Cloud
  - Terraform Cloud Workspaces
  - Triggering Runs in Terraform Cloud
  - - Creating a Workspace in Terraform Cloud（任务预览） ✅
  - - Creating a Workspace in Terraform Cloud ✅
  - ... 等 22 节

### 第 19 章 · 项目：Terraform Cloud OIDC

`19 - Project - Terraform Cloud OIDC`

**目标**：用 OIDC 让 TFC 动态 assume AWS 角色，并把已有 AWS 资源导入 Terraform 管理

- **在 AWS 建 OIDC IdP**：先到安全凭证页停用并删除此前给 TFC 用的长期访问密钥，再在 IAM 创建 Web identity 类型的身份提供商，provider 选 app.terraform.io、audience 与 Terraform Cloud 保持一致，并记下它的 ARN。
- **角色信任策略与权限**：创建 Web identity 角色，信任策略中填入 OIDC provider 的 ARN 与 app.terraform.io:sub 条件，限定组织、项目、workspace 以及 run phase（plan 与 apply 都要能 assume）；再附加 AdministratorAccess 策略。
- **CLI 驱动项目初始化**：新建 project-05/tf-cloud-oidc 目录，用 terraform login 生成有效期 30 天的 API token；写 provider.tf 绑定到 default workspace，运行 terraform init 与 terraform workspace show 确认生效。
- **配置 Variable Set**：TFC 侧只需两个环境变量：TFC_AWS_PROVIDER_AUTH 设为 true，TFC_AWS_RUN_ROLE_ARN 填角色 ARN；配好后重跑 plan/apply 就能以该角色认证到 AWS，不存储任何静态密钥。
- **导入三个 AWS 资源**：用 import 块接管 aws_iam_openid_connect_provider（需 url、client_id_list、thumbprint_list）、aws_iam_role（用 data aws_iam_policy_document 写 assume policy）与 aws_iam_role_policy_attachment。
- **扩展到第二个 workspace**：在同一项目下新建 terraform-cli-2，项目级 Variable Set 会自动应用到新 workspace；若再在 workspace 级挂同名变量集，其取值会覆盖项目级，正好可用于多环境隔离。
- **收尾与资源清理**：验证 plan/apply 通过后，删掉本地测试目录、oidc-admin-role 变量集，以及项目下的 workspace 和整个项目，确保 AWS 与 Terraform Cloud 两侧都不留残留。

共 10 节课
  - Project Overview
  - Creating the Identity Provider in AWS
  - Implementing the Terraform Cloud Role
  - Attaching the Necessary Role Policies
  - Initializing the Terraform Cloud CLI-Driven Project
  - ... 等 10 节

## 阶段 9 · 收尾

### 第 20 章 · 课程总结

`20 - Conclusion`

**目标**：原课程此节没有配套视频，作为整门课复盘与后续规划的占位

- **全流程回顾**：原课程在此未提供讲解视频。建议自行把前三阶段串起来回顾：state 是唯一事实来源，module 是复用单元，workspace 与 Terraform Cloud 是协作与隔离手段。
- **后续学习路径建议**：可接续的方向：Terraform Cloud 私有 Registry、多环境流水线拆分、Terraform Cloud OIDC 免密钥、Terratest 模块单元测试，以及跨云的 Crossplane / Kubernetes Operator。
