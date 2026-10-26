---
title: "AWS Front-End Web and Mobile"
---

AWS Front-End Web and Mobile 服务支持原生 iOS/Android、React Native 和 JavaScript 开发者的开发工作流。你可以使用 AWS 托管服务开发应用，并进行交付、测试和监控。

## AWS AppSync 功能

![AWS Data Engineer Cheat Sheet](/cheat-sheets/images/2022-02-AWS-Front-End-Web-and-Mobile-1.png")

- AWS AppSync 是一种全托管服务，可以轻松开发 GraphQL API。
- 安全地连接到 AWS DynamoDB、Lambda 等数据源。
- 添加缓存以提升性能，通过 subscription 支持实时更新，并通过客户端数据存储让离线客户端保持同步。
- AWS AppSync 自动扩缩你的 GraphQL API 执行引擎，以应对 API 请求量的变化。

## GraphQL

- AWS AppSync 使用 GraphQL——一种数据语言，使客户端应用能够从服务器获取、修改和订阅数据。
- 在 GraphQL 查询中，客户端指定服务器返回数据时的结构。
- 这使得客户端可以只查询它需要的数据，并以它需要的格式返回。
- GraphQL 还包含一个名为“introspection（内省）”的功能，让项目中的新开发者无需了解后端即可发现可用的数据。

## 实时数据访问与更新

- AWS AppSync 允许你使用 GraphQL Subscription 指定哪些部分的数据应以实时方式提供。
- GraphQL Subscription 是应用代码中的简单语句，告诉服务哪些数据应该实时更新。

## 离线数据同步

- Amplify DataStore 为 Web、移动和 IoT 开发者提供可查询的设备端 DataStore。
- 与 AWS AppSync 结合使用时，DataStore 可以利用云端的高级版本控制、冲突检测与解决能力。
- 这允许自动合并来自不同客户端的数据，同时保证数据的一致性和完整性。

## 应用中的数据查询、过滤和搜索

- AWS AppSync 让客户端应用能够用 GraphQL 指定数据需求，从而只获取所需的数据，同时支持服务端和客户端过滤。
- AWS AppSync 支持 AWS Lambda、Amazon DynamoDB 和 Amazon Elasticsearch。
- GraphQL 操作可以是简单的查找、复杂的查询与映射、全文搜索、模糊/关键词搜索或地理位置查找。

## 服务端缓存

- AWS AppSync 的服务端数据缓存能力减少了直接访问数据源的需求。
- 数据通过高速内存托管缓存以低延迟交付。
- AppSync 是全托管的，消除了管理缓存集群的运维开销。
- 可以灵活地选择性地缓存 GraphQL schema 中定义的数据字段和操作，并支持自定义过期时间。

## 安全与访问控制

- AWS AppSync 根据应用需求支持多个级别的数据访问和授权。
- 简单的访问可以通过 API key 保护。
- 更严格的访问控制可以使用 AWS IAM role。
- AWS AppSync 还集成了：
- Amazon Cognito User Pool，提供邮箱和密码功能
- 社交身份提供商（Facebook、Google+ 和 Login with Amazon）。
- 基于 SAML 的企业联合认证。

客户可以使用 Group 功能对用户和角色进行逻辑组织，并使用 OAuth 功能进行应用访问。

## 自定义域名

- AWS AppSync 允许客户为其 AWS AppSync API 使用自定义域名，以访问其 GraphQL endpoint 和实时 endpoint。
- 与 AWS Certificate Manager（ACM）证书配合使用。
- 自定义域名可以关联到你账户中任何可用的 AppSync API。
- 当 AppSync 在自定义域名 endpoint 上收到请求时，会将其路由到关联的 API 进行处理。
