---
title: "Amazon Athena"
---

![Amazon Athena Services](/cheat-sheets/images/2022-01-Amazon-Athena-1024x652.png)

- Amazon Athena 是一项交互式查询服务，可以使用标准 SQL 轻松分析 Amazon S3 中的数据。
- Athena 是无服务器产品，因此使用 Amazon Athena 时 AWS 会为你管理所有基础设施，你只需为运行的查询付费。
- AWS 让 Amazon Athena 的使用变得极其简单——只需指向你在 Amazon S3 中的数据，定义 schema，然后就可以开始使用标准 SQL 进行查询。
- Amazon Athena 使用 Presto，完整支持标准 SQL，并兼容多种标准数据格式，包括 CSV、JSON、ORC、Apache Parquet 和 Avro。
- Amazon Athena 非常适合快速的即席查询，并与 Amazon QuickSight 集成以便轻松实现可视化，同时它也能处理复杂分析，包括大型 join、窗口函数和数组。
- Amazon Athena 使用托管的 Data Catalog 来存储你为存储在 Amazon S3 中的数据所创建的数据库和表的信息及 schema。
- 使用 Amazon Athena，你无需担心管理或调优集群即可获得快速性能。
- Amazon Athena 针对 Amazon S3 的快速性能进行了优化。
- Amazon Athena 自动并行执行查询，因此即使在大型数据集上，你也能在几秒内获得查询结果。
- 大多数结果都能在几秒内返回。
- 使用 Amazon Athena，无需复杂的 ETL 作业来为分析准备数据。
- 这让任何具备 SQL 技能的人都能快速分析大规模数据集。
- Amazon Athena 开箱即用地与 AWS Glue Data Catalog 集成，允许你跨各种服务创建统一的元数据存储库，爬取数据源以发现 schema 并用新建和修改的表及分区定义填充 Catalog，并维护 schema 版本控制。
- 你还可以使用 Glue 完全托管的 ETL 功能来转换数据或将其转换为列式格式，以优化成本并提升性能。

## Amazon Athena 功能特性

- 你可以使用标准 SQL 查询 Amazon Athena。
- Amazon Athena 使用 Presto——一个开源的分布式 SQL 查询引擎，针对低延迟交互式数据分析进行了优化。
- Athena 支持多种数据格式，如 CSV、JSON、ORC、Avro 或 Parquet。
- 借助 Athena 的联合数据源连接器，你可以查询其他数据存储，并将数据与存储在 Amazon S3 中的数据进行 join。
- 你可以通过 Athena 控制台、API、CLI、AWS SDK 访问 Athena 并运行查询。
- 在 Amazon Athena 上，AWS 支持通过 Athena 的 JDBC 和 ODBC 驱动与商业智能和 SQL 开发应用集成。
- Amazon Athena 使用 AWS 高度冗余的全球基础设施来保持高可用性。
- 每当某个设施不可用时，Amazon Athena 会根据可用的计算资源将查询路由到另一个设施。
- Amazon Athena 使用 Amazon S3 作为数据源，使你的数据具备高可用性和持久性。
- 除了为保存重要数据提供持久的基础设施外，Amazon S3 在单个对象层面的设计持久性达到 99.999999999%。
- Amazon Athena 与 Identity and Access Management 直接集成，你也可以利用 S3 中的 bucket policy。
- 通过向 IAM 用户授予 IAM policy，你可以轻松控制用户的 S3 bucket。通过控制对 S3 中数据的访问，你可以限制用户使用 Athena 查询这些数据。
- 此外，Athena 允许你查询存储在 Amazon S3 中的加密数据，并将加密后的结果写回你的 bucket。
- Athena 为企业数据源提供连接器，包括 Amazon DynamoDB、Amazon Redshift、Amazon OpenSearch、MySQL、PostgreSQL、Redis 以及其他流行的第三方数据存储。

## Amazon Athena 的局限性

- 在优化能力方面，AWS Athena 提供的能力不多。
- 尽管 Amazon Athena 是一项高度可扩展且可靠的服务，但它托管在多租户环境中。 这种多租户方式可能会不时触发限流，从而带来潜在问题。
- Amazon Athena 不包含任何用于插入、删除和更新数据的数据操作接口。
- 如果你希望高效运行 SQL 查询，可能需要对存储在 Amazon S3 中的数据集进行分区。你创建的分区数量将显著影响查询速度和性能。
- Amazon Athena 原生不支持索引。

## 使用场景

- 像 Amazon Athena 这样的查询服务、像 Amazon Redshift 这样的数据仓库，以及像 Amazon EMR 这样的复杂数据处理框架，分别满足不同的需求和使用场景。
- Amazon Redshift 为企业报表和商业智能工作负载提供最快的查询性能，尤其是涉及多 join 和子查询的极其复杂的 SQL。
- 与本地部署相比，Amazon EMR 让运行 Hadoop、Spark 和 Presto 等高度分布式处理框架变得简单且经济高效。Amazon EMR 非常灵活——你可以运行自定义应用和代码，并定义特定的计算、内存、存储和应用参数来优化你的分析需求。
- Amazon Athena 提供了对 S3 中的数据运行即席查询的最简单方式，无需搭建或管理任何服务器。
- 借助 Athena，你可以分析存储在 Amazon S3 中的非结构化、半结构化和结构化数据。例如 CSV、JSON，或 Apache Parquet 和 Apache ORC 等列式数据格式。
- 在 Athena 中，可以即席运行 ANSI SQL 查询，无需聚合或加载数据。
- 通过与 Amazon QuickSight 集成，Athena 让数据可视化变得简单。
- 使用 Athena，你可以借助连接到 JDBC 或 ODBC 驱动的商业智能工具或 SQL 客户端来生成报表或探索数据。
- 借助 AWS Glue Data Catalog，Athena 与你的数据集成，在 Amazon S3 中创建持久的元数据存储，让你可以从任何地方访问数据。
- 借助 AWS Glue，你可以通过一个在 AWS 账户范围内可访问的中央元数据存储来创建表并在 Athena 中查询数据。
- 为了排查网站的性能问题，Athena 非常适合对 Web 日志运行快速查询。你可以用 Athena 快速为数据定义一张表，然后立即开始使用标准 SQL 进行查询。
- 如果你想与存储在 S3 中的成本和使用情况报告（Cost and Usage Report）交互，以获取关于 AWS 账单如何计算的非常具体的信息，你应该使用 Amazon Athena。这可以在控制台中原生完成。
- 下表展示了几个 AWS 查询和分析服务的主要使用场景和适用情形：

| **AWS 服务** | **主要使用场景** | **何时使用** |
| --- | --- | --- |
| Amazon Athena | 查询 | 直接对 Amazon S3 中的数据运行交互式查询，无需担心数据格式化或管理基础设施。可与 Amazon RedShift 等其他服务配合使用 |
| Amazon RedShift | 数据仓库 | 从多个来源拉取数据，对其进行格式化和组织、存储，并支持生成业务报表的复杂高速查询。 |
| Amazon EMR | 数据处理 | Hadoop、Spark 和 Presto 等高度分布式处理框架。为机器学习、图分析、数据转换、流数据等应用运行各种横向扩展的数据处理任务。 |
| AWS Glue | ETL 服务 | 转换数据并将其移动到各种目标。用于为分析准备和加载数据。数据源可以是 S3、RedShift 或其他数据库。Glue Data Catalog 可被 Athena、EMR 和 RedShift Spectrum 查询 |

## 最佳实践

Athena 性能的[**最佳实践**](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)：

- **对数据进行分区** —— 将表划分为多个部分，并根据日期、国家、区域等列值将相关数据放在一起。Athena 支持 Hive 分区。
- **对数据进行分桶** —— 在单个分区内对数据进行分桶。
- **使用压缩** —— AWS 建议使用 Apache Parquet 或 Apache ORC。
- **优化文件大小** —— 当读取数据可以并行化且数据块可以顺序读取时，查询运行效率更高。
- **优化列式数据存储的生成** —— Apache Parquet 和 Apache ORC 是流行的列式数据存储。
- **优化 ORDER BY** —— ORDER BY 子句按排序顺序返回查询结果。
- **优化 GROUP BY** —— GROUP BY 运算符根据 GROUP BY 列将行分发到工作节点，工作节点将 GROUP BY 值保存在内存中。
- **使用近似函数** —— 对于探索大型数据集，一个常见用例是使用 COUNT(DISTINCT column) 查找某列的不重复值数量。
- **只包含你需要的列** —— 运行查询时，将最终的 SELECT 语句限制为仅需要的列，而不是选择所有列。

## 定价

- 使用 Amazon Athena，你只需为运行的查询付费。
- 费用根据每个查询扫描的数据量计算。
- 通过压缩、分区或将数据转换为列式格式，你可以显著节省成本并提升性能，因为每种操作都能减少 Athena 执行查询时需要扫描的数据量。

## Amazon Athena 常见问题（FAQ）

- 问：我可以用 Amazon Athena 做什么？
- 使用 Amazon Athena，你可以分析存储在 Amazon S3 中的数据。Athena 支持使用 ANSI SQL 进行交互式分析，无需聚合或加载数据。数据集可以是非结构化、半结构化或结构化的。你可以将 Amazon Athena 与 Amazon QuickSight 结合使用，可视化 CSV、JSON、Avro 或 Apache Parquet 和 Apache ORC 等列式数据格式。
- 问：如何开始使用 Amazon Athena？
- 使用 Amazon Athena 非常简单，只需登录 Athena 的 AWS 管理控制台，编写 DDL 语句或使用创建表向导即可。内置的查询编辑器让你可以查询数据。
- 问：Amazon Athena、Amazon EMR 和 Amazon Redshift 之间有什么区别？
- Amazon Redshift 平台为企业报表和商业智能工作负载提供最快的查询性能，尤其是具有多 join 的 SQL。
- 与本地部署相比，Amazon EMR 让 Hadoop、Spark 和 Presto 等高度分布式处理框架变得简单且经济高效。
- Amazon EMR 允许你运行自定义应用和代码，并定义特定的计算、内存、存储和应用参数。
- Amazon Athena 无需搭建或管理任何服务器，即可对 S3 数据进行交互式查询。
- 问：什么时候应该使用像 Amazon Redshift 这样功能齐全的企业数据仓库，而不是像 Amazon Athena 这样的查询服务？
- 问：如何为存储在 Amazon S3 上的数据创建表和 schema？
