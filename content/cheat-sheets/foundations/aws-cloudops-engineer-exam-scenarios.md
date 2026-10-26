---
title: "Exam Scenarios for AWS CloudOps Engineer Associate"
---

下表中的场景和解决方案将帮助你备考 [AWS Certified CloudOps Engineer Associate](https://digitalcloud.training/aws-certified-cloudops-engineer-associate/) 认证考试。通过这些考试场景，你可以更深入地了解通过这门颇具挑战性的考试所需的知识类型。你可以在 Digital Cloud Training 物超所值的[视频课程](https://learn.digitalcloud.training/course/aws-certified-cloudops-engineer-associate-video-course)中学到所有这些知识以及更多内容，并获得数百个额外的考试场景。这些场景以及更多内容也涵盖在我们针对 SOA-C03 考试的[模拟测试课程](https://learn.digitalcloud.training/course/aws-certified-cloudops-engineer-associate-practice-exams)中。

## Amazon EC2 和 AWS Lambda

| **考试场景** | **解决方案** |
| --- | --- |
| 管理员需要检查是否有 [Amazon EC2](https://digitalcloud.training/amazon-ec2/) 实例会受到计划中的硬件维护影响 | 查看 AWS Personal Health Dashboard |
| 计划中的硬件维护将影响一个关键 EC2 实例 | 停止并启动实例，将其迁移到不同的底层硬件 |
| 启动 EC2 实例时遇到 InsufficientInstanceCapacity 错误 | 这意味着 AWS 目前没有足够的容量来满足该实例类型的请求。尝试换一个 AZ 或实例类型 |
| 启动 EC2 实例时遇到 InstanceLimitExceeded 错误 | 已达到 EC2 实例数量上限，需要联系 support 申请提升限额 |
| 某个 EC2 实例的系统状态检查（system status check）失败 | 停止并重新启动，以迁移到新主机 |

## Elastic Load Balancing 和 Auto Scaling

| **考试场景** | **解决方案** |
| --- | --- |
| 需要设计一个高可用且安全的网站：EC2 上部署 Web 层并使用 [ALB](https://digitalcloud.training/aws-elastic-load-balancing-aws-elb/)，数据库部署在 EC2 上 | ALB 部署在公有 subnet，Web 服务器部署在私有 subnet，数据库层部署在私有 subnet——所有层都跨 AZ |
| 某个 ALB 的 HealthyHostCount 指标从 6 降到 2，需要确定原因 | 目标 EC2 实例的健康检查失败 |
| 挂载在 ALB 下的某个实例连续健康检查失败次数超过 UnhealthyThresholdCount，会发生什么？ | 健康检查会继续进行，ALB 会将该实例移出服务 |
| 需要追踪客户端的源 IP 以及处理请求的实例 | 查看 ALB 访问日志获取这些信息 |
| 出现 503 和 504 错误，且实例 CPU 利用率很高 | 使用 [EC2 Auto Scaling](https://digitalcloud.training/amazon-ec2-auto-scaling/) 动态扩展 |

## Amazon EBS、EFS 和 AWS Storage Gateway

| **考试场景** | **解决方案** |
| --- | --- |
| 用户删除了 [Amazon EBS](https://digitalcloud.training/amazon-ebs/) 卷中的一些数据，且有一个最近的快照 | 可以从快照创建一个新的 EBS 卷，挂载到实例上，然后把被删除的文件拷贝回来 |
| EBS 卷空间耗尽，需要防止再次发生 | 在 EC2 上使用 CloudWatch agent，并通过 CloudWatch alarm 监控磁盘指标 |
| 办公室需要对镜像文件的低延迟访问，并同步备份到异地。需要本地访问能力和灾难恢复 | 使用配置为 stored volume 的 [AWS Storage Gateway](https://digitalcloud.training/aws-storage-gateway/) volume gateway |
| EBS 卷扩容后看不到新增空间 | 需要扩展卷的文件系统才能使用额外空间 |
| 需要替换用户共享驱动器。必须支持 POSIX 权限和 NFS 协议，并且可以从本地服务器和 EC2 访问 | 使用 [Amazon EFS](https://digitalcloud.training/amazon-efs/) |

## AWS Systems Manager

| **考试场景** | **解决方案** |
| --- | --- |
| 运行在 EC2 上的应用需要数据库登录凭证，凭证以 secure string 形式存储在 SSM Parameter Store 中 | 为实例创建一个 IAM role，并授予读取参数的权限 |
| Linux 实例通过 [Systems Manager Patch Manager](https://digitalcloud.training/aws-systems-manager/) 打补丁。打补丁期间应用变慢 | 调整维护窗口，每次只给 patch group 中 10% 的实例打补丁 |
| 自定义 Linux AMI 配合 AWS Systems Manager 使用，但在 Session Manager 控制台中找不到实例 | 需要为 instance profile 添加权限，并在实例上安装 SSM agent |
| 多个环境需要外部服务的身份验证凭证，使用 CloudFormation 部署 | 将凭证存储在 SSM Parameter Store 中，并在 CloudFormation 模板中通过参数传入环境标签 |  |
| 使用 IAM access key 通过 CLI 管理 EC2 实例。公司策略要求 access key 在 60 天后自动禁用 | 使用 AWS Config rule 识别不合规的密钥，创建自定义的 AWS Systems Manager Automation document 进行修复 |

## AWS CloudFormation

| **考试场景** | **解决方案** |
| --- | --- |
| 需要在生产环境部署之前审查 [AWS CloudFormation](https://digitalcloud.training/aws-cloudformation/) stack 的更新 | 使用 change set |
| stack 部署后被手动修改过，需要捕获这些更改并更新模板 | 使用 drift detection，并利用其输出更新模板后重新部署 stack |
| 需要更新 EC2 和 ALB 上的应用新版本。必须避免 DNS 变更，且能够回滚 | 在模板中使用 AutoScalingReplacingUpdate 策略并执行更新 |
| 需要编写一个可跨多个环境/区域部署的单一模板 | 使用 parameter 输入自定义值，并使用 Ref 内部函数引用参数 |
| 用一个正常工作的模板在另一个区域启动实例却失败了 | 很可能是 AMI ID 不正确 |

## Amazon Virtual Private Cloud (VPC)

| **考试场景** | **解决方案** |
| --- | --- |
| 需要找出通过 NAT gateway 产生流量最多的实例 | 在 NAT gateway 的 ENI 上使用 [VPC flow log](https://digitalcloud.training/amazon-vpc/)，并用 CloudWatch Insights 按源 IP 地址过滤 |
| NAT 实例的延迟上升，需要一个能随需求扩展且具有成本效益的解决方案 | 换成 NAT gateway |
| NAT gateway 不能跨 AZ 高可用，只能在单个 AZ 内高可用 | 使用多个 NAT gateway 实现跨 AZ 的高可用 |
| 部署了 NAT 实例但不工作 | 确保禁用 source/destination check |
| 需要让实例不使用公有 IP 地址访问 S3 | 使用 NAT gateway 或 VPC endpoint |

## Amazon Route 53

| **考试场景** | **解决方案** |
| --- | --- |
| 使用 [Route 53](https://digitalcloud.training/amazon-route-53/) 基于健康检查进行分流：返回 (2xx) 的流量到主站点，其他响应到备用站点 | 需要为每台服务器创建一条 A 记录，以及一个 HTTP（而非 TCP）健康检查 |
| Route 53 健康检查对“/html”使用字符串匹配，告警显示健康检查失败 | 搜索字符串必须完整出现在响应体的前 5,120 字节内 |
| 需要让网站促销内容只对特定国家的用户可见 | 使用 Route 53 geolocation 路由策略 |
| 新网站运行在 ALB 后面的 EC2 上。需要在 Route 53 中创建记录指向域名 apex（例如 example.com） | 使用 alias 记录 |
| hosted zone 在账户 A，ALB 在账户 B。需要最具成本效益且高效的方案指向该 ALB | 在账户 A 中创建一条指向账户 B 中 ALB 的 Alias 记录 |

## Amazon S3 和 CloudFront

| **考试场景** | **解决方案** |
| --- | --- |
| [Amazon S3](https://digitalcloud.training/amazon-s3-and-glacier/) 上的静态网站使用自定义域名 | 要求 bucket 名称与 Route 53 中的 DNS 名称/记录集名称一致 |
| 新网站在数千用户访问时出现 503 错误 | 请求速率过高 |
| bucket 控制台与 CloudWatch 中的对象数量不一致 | 使用 Amazon S3 Inventory 来准确确定 bucket 中的对象数量 |
| 需要强制对上传到 bucket 的所有对象加密 | 使用 bucket policy，针对 PutObject 添加 "Condition": { "Bool": { "aws:SecureTransport": "false" 语句，并将 resource 设置为该 bucket |
| 有未授权用户尝试连接 S3 bucket。需要知道哪些 bucket 被盯上以及是谁在尝试访问 | 使用 S3 server access log 和 Athena 查询 HTTP 403 错误，并查找发起请求的 IAM 用户或角色 |

## Amazon RDS 和 ElastiCache

| **考试场景** | **解决方案** |
| --- | --- |
| multi-AZ 数据库发生了自动故障转移 | 可能是主数据库的存储故障，或者实例类型被更改过 |
| 需要加密一个未加密的 RDS 数据库 | 拍摄快照，加密快照，然后从快照恢复出一个新的加密实例 |
| [RDS 数据库](https://digitalcloud.training/amazon-rds/)查询延迟高，CPU 利用率达 100% | 使用更大的实例类型向上扩展 |
| 需要跨账户共享 RDS 数据库快照，数据必须加密 | 使用 AWS KMS key 加密，更新 key policy 授予其他账户访问权限，然后共享快照 |
| 数据库需要实现高可用以防止故障，且更新不能在营业时间影响用户 | 在营业时间之外切换为 Multi-AZ |

## 管理、治理与计费

| **考试场景** | **解决方案** |
| --- | --- |
| 审计联合身份用户向 [AWS Organizations](https://digitalcloud.training/aws-organizations/) 发起的创建新账户请求 | 使用 CloudTrail，查找联合身份用户名 |
| 员工创建了不受管控的个人 AWS 账户。安全团队需要将它们纳入 AWS Organizations | 从中心组织向每个账户发送邀请 |
| 需要限制特定团队/账户启动特定实例类型的能力 | 使用 Organizations SCP 拒绝启动非 T2 的实例类型，并在账户中创建 IAM group，向相关用户授予 T2 实例的访问权限 |
| 需要测试 [CloudWatch](https://digitalcloud.training/amazon-cloudwatch/) alarm 与 SNS 的通知设置 | 使用 set-alarm-state CLI 命令进行测试 |
| 需要自动禁用超过 90 天的 access key | 使用 [AWS Config](https://digitalcloud.training/aws-config/) rule 识别不合规的密钥，并使用 Systems Manager Automation 进行修复 |

## 安全与合规

| **考试场景** | **解决方案** |
| --- | --- |
| 公司希望强制用户定期更改密码 | 创建 [IAM password policy](https://digitalcloud.training/aws-iam/) 并启用密码过期 |
| 需要基于源 IP 范围限制对某个 bucket 的访问 | 使用带有 "Condition": "NotIpAddress": 语句的 bucket policy |
| 需要控制对具有特定标签的一组 EC2 实例的访问 | 使用带 condition 元素的 IAM policy，基于标签授予访问权限，并将该 IAM policy 附加到需要访问权限的用户或组 |
| SQS 队列的 IAM policy 权限过大。谁负责纠正该问题？ | 根据 AWS 责任共担模型，这是客户的责任 |
| 数据使用 [AWS KMS](https://digitalcloud.training/aws-cloudhsm/) 客户托管 CMK 加密。需要启用轮换，同时确保数据仍然可读 | 直接在 AWS KMS 中为该 CMK 启用密钥轮换即可（轮换的是 backing key，data key 不变） |
