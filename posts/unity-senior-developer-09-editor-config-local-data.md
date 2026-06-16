---
id: 80WgAX
title: Unity 开发高级/资深 09：编辑器工具、配置与本地数据
createdAt: "2026-06-10 21:59:00"
updated: "2026-06-16 17:26:21"
tags:
    - Unity
    - 开发高级/资深
    - UnityEditor
    - 配置
tag_ids:
    - FjODty
    - P46nOZ
    - J7VXMO
    - UTkVfb
categories: []
published: true
hideInList: true
feature: ""
isTop: false
---

[返回总览](https://zhoujun2303.github.io/post/unity-senior-developer-skills/)

![Unity 开发高级/资深工具链地图](https://zhoujun2303.github.io/post-images/unity-senior-developer-toolchain-map.svg)

<a id="editor-tools"></a>
## 编辑器工具

- EditorWindow：配置编辑器、关卡编辑器、技能编辑器、剧情编辑器。
- CustomEditor：改善复杂组件 Inspector，减少错误填写。
- PropertyDrawer：统一显示 ID、资源引用、条件、枚举、范围。
- MenuItem：批处理入口、构建入口、资源检查入口。
- Gizmos：场景摆点、怪物范围、任务区域、交互距离、相机边界。
- AssetPostprocessor：模型、贴图、音频、动画导入时自动设置。
- 批处理：命名检查、引用检查、缺失脚本、重复资源、资源替换。
- 工具产品化：参数保存、进度显示、错误报告、可撤销、可重复执行。

### 需要掌握的工具

- EditorWindow：开发配置、关卡、技能、资源检查和构建工具窗口。
- CustomEditor、PropertyDrawer：改善组件和配置对象的编辑体验。
- AssetPostprocessor：自动设置模型、贴图、音频、动画导入参数。
- Gizmos、Handles：在 Scene 视图中可视化范围、路径、触发器和摆点。
- Odin Inspector 可选：快速构建复杂 Inspector 和工具面板。
- Unity Test Framework：给工具逻辑、导表校验和资源扫描写测试。
- 自研工具日志和报告页：让策划、美术、QA 能看懂工具失败原因。

### 可继续细分方向

- Inspector 与配置编辑体验。
- 资源导入和批处理。
- Scene Gizmos 和可视化编辑。
- 构建面板、渠道参数和工具产品化。

<a id="config-data"></a>
## 配置数据系统

- 配置格式：Excel、CSV、JSON、二进制、ScriptableObject 的取舍。
- 数据结构：ID、索引、引用、条件、公式、多语言、平台差异。
- 导表流程：策划填写、校验、导出、生成代码、打包、热更。
- 运行时访问：强类型接口、索引缓存、避免字符串查找和重复解析。
- 校验规则：资源存在、ID 唯一、引用合法、任务链闭环、奖励合法。
- 版本兼容：新增字段默认值、旧字段保留、配置回滚、客户端兼容。
- 公式管理：可读、可测、可追踪，关键公式与服务器保持一致。
- 多环境：开发、测试、预发布、正式环境配置隔离。

### 需要掌握的工具

- Excel、Google Sheets、飞书表格：策划配置源。
- 导表脚本：生成 JSON、二进制、Protobuf 或 C# 强类型访问代码。
- JSON Schema 或自研校验器：检查字段类型、范围、引用和条件。
- SQLite、LiteDB 或二进制索引：处理本地查询和大量配置数据。
- Diff 工具：比较配置版本差异，定位线上数据变更。
- CI 校验任务：提交或构建时自动检查配置合法性。

### 可继续细分方向

- 配置表结构设计。
- 导表、代码生成和强类型访问。
- 配置校验、Diff 和版本兼容。
- 多语言、公式和服务器一致性。

<a id="local-save"></a>
## 存档与本地数据

- 存储方式：PlayerPrefs、JSON 文件、SQLite、二进制、平台 Keychain。
- 本地缓存：账号、最近服务器、设置、音量、画质、资源版本、公告缓存。
- 数据安全：加密、校验、防篡改、敏感信息不落地或少落地。
- 版本迁移：字段新增、字段删除、结构变化、旧数据修复。
- 读写性能：异步 IO、批量保存、延迟落盘、避免主线程卡顿。
- 多账号：账号隔离、角色隔离、清缓存、游客转正。
- 服务端边界：关键经济数据、战斗结果、支付状态不能只信客户端。

### 需要掌握的工具

- PlayerPrefs：少量非敏感设置和简单状态。
- File API：JSON、二进制、本地缓存和资源版本文件。
- SQLite：较复杂的本地索引、离线数据和缓存查询。
- Keychain/Keystore：保存敏感 Token 或平台安全数据。
- 加密与 hash 工具：基础加密、完整性校验和迁移验证。
- 数据迁移脚本：处理版本升级、字段变更和坏数据修复。

### 可继续细分方向

- 本地设置和缓存。
- 存档加密、校验和防篡改。
- 版本迁移和坏数据修复。
- 多账号、本地缓存清理和服务端边界。

## 开发高级/资深关注点

- 策划填错配置时是否能在导表阶段发现。
- 编辑器工具是否能减少重复劳动，而不是制造新的维护负担。
- 工具失败时是否有可读错误，而不是静默生成错误数据。
- 本地数据升级失败是否会导致玩家无法进游戏。
- 配置、资源、代码、协议之间的版本关系是否清楚。