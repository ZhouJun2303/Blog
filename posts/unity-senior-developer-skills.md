---
id: VDzWPP
title: Unity 开发高级/资深技能总览
createdAt: "2026-06-10 21:50:00"
updated: "2026-06-16 17:26:22"
tags:
    - Unity
    - 开发高级/资深
    - 客户端架构
    - 性能优化
tag_ids:
    - FjODty
    - P46nOZ
    - 4zUHdL
    - HBW449
categories: []
published: true
hideInList: false
feature: /post-images/unity-senior-developer-skill-map.svg
isTop: false
---

> “开发高级/资深”不是只负责写最难的代码，而是负责把 Unity 项目的技术方向、模块边界、性能质量、发版稳定性和团队交付串起来。本文采用“总分”结构：本文件是总览入口，下面的分文档展开每个方向的具体技能点。

![Unity 开发高级/资深技能地图](/post-images/unity-senior-developer-skill-map.svg)

## 阅读方式

- 总览入口：当前文档负责列出全部方向、能力地图、学习路线和自检清单。
- 分文档：每个专题都有独立 Markdown，适合继续补充案例、代码片段和项目复盘。
- 细分方式：每个分文档内继续按小方向拆分；如果某个方向后续需要更深案例，可以在同目录下继续新增专题文档。
- 可跳转：目录表中的方向名都可以直接跳到对应分文档或分文档内的小节。
- 工具要求：每个方向都列出了开发高级/资深需要掌握或至少能判断适用边界的工具。
- 图片资源：本专题图片都放在 `LocalBK/post-images/` 下，正文统一使用 `/post-images/...` 引用。

## 分文档导航

| 编号 | 分文档 | 覆盖方向 |
| --- | --- | --- |
| 01 | [引擎、C# 与客户端架构](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/) | Unity 基础、C#、架构分层、启动流程、模块边界 |
| 02 | [工程规范与可维护性](https://zhoujun2303.github.io/post/unity-senior-developer-02-engineering-maintainability/) | 代码规范、目录规范、Review、技术债、文档 |
| 03 | [资源管理与热更新](https://zhoujun2303.github.io/post/unity-senior-developer-03-assets-hot-update/) | Addressables、AssetBundle、资源生命周期、热更、Shader Variant |
| 04 | [UI、交互与输入](https://zhoujun2303.github.io/post/unity-senior-developer-04-ui-interaction-input/) | UI 框架、红点、适配、输入、场景交互 |
| 05 | [网络通信与多人同步](https://zhoujun2303.github.io/post/unity-senior-developer-05-network-sync/) | 协议、长连接、弱网、AOI、移动同步、断线重连 |
| 06 | [玩法、战斗与动画](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/) | 技能、Buff、属性、状态机、Timeline、IK |
| 07 | [渲染、Shader 与 TA 协作](https://zhoujun2303.github.io/post/unity-senior-developer-07-rendering-shader-ta/) | 渲染管线、Shader、光照、特效、美术预算 |
| 08 | [性能、内存与包体](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/) | 性能预算、CPU/GPU/UI/动画/物理优化、内存泄漏、包体加载、回归看板 |
| 09 | [编辑器工具、配置与本地数据](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/) | Editor 工具、导表、配置校验、存档、本地缓存 |
| 10 | [构建发布、CI/CD 与 SDK](https://zhoujun2303.github.io/post/unity-senior-developer-10-build-release-cicd-sdk/) | 自动化构建、多平台发版、渠道包、登录支付 SDK |
| 11 | [测试、监控、线上排障与安全](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/) | 自动化测试、日志、崩溃、线上开关、反作弊 |
| 12 | [跨平台、本地化、音视频、AI 与物理](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/) | 平台差异、多语言、音视频、寻路、物理碰撞 |
| 13 | [技术领导力、项目管理与表达](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/) | 任务拆解、风险控制、团队协作、方案评审、复盘 |

## 全部方向清单

| # | 方向 | 开发高级/资深需要掌握的核心问题 | 跳转 |
| --- | --- | --- | --- |
| 1 | Unity 引擎基础 | 生命周期、序列化、场景、Prefab、PlayerLoop、编辑器与运行时边界 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#unity-engine) |
| 2 | C# 与代码基本功 | 泛型、委托、事件、集合、GC、异步、线程、IL2CPP/AOT | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#csharp) |
| 3 | 客户端架构设计 | 分层、模块边界、启动流程、服务注册、异步流程、状态机 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#client-architecture) |
| 4 | 工程规范与可维护性 | 目录、命名、Review、错误处理、可测试性、技术债治理 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-02-engineering-maintainability/#engineering-standards) |
| 5 | 资源管理 | 资源分组、依赖、引用计数、预加载、卸载、缓存 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-03-assets-hot-update/#asset-management) |
| 6 | 热更新 | 资源热更、脚本热更、版本匹配、补丁、回滚、兼容 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-03-assets-hot-update/#hot-update) |
| 7 | UI 框架 | 面板生命周期、层级、返回栈、红点、适配、虚拟列表 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-04-ui-interaction-input/#ui-framework) |
| 8 | 交互与输入 | 点击、射线、手势、键鼠、手柄、交互距离、防误触 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-04-ui-interaction-input/#interaction-input) |
| 9 | 网络通信 | TCP/UDP/HTTP/WebSocket/KCP、协议、心跳、重连、弱网 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-05-network-sync/#network) |
| 10 | 多人同步与 AOI | 位置、动作、外观、兴趣管理、插值、纠偏、分线 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-05-network-sync/#multiplayer-aoi) |
| 11 | 战斗系统 | 技能、Buff、属性、伤害、碰撞、服务器权威、回放 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#combat) |
| 12 | 玩法系统 | 任务、背包、活动、奖励、红点、条件、通用业务框架 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#gameplay) |
| 13 | 动画与演出 | Animator、Blend Tree、Playable、Timeline、IK、挂点、动作打断 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#animation) |
| 14 | 渲染管线与 Shader | URP/HDRP、Batch、Pass、Keyword、光照、后处理、Shader Variant | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-07-rendering-shader-ta/#rendering) |
| 15 | TA 与美术管线 | 资源预算、导入规范、特效规范、材质规范、验收工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-07-rendering-shader-ta/#technical-art) |
| 16 | 性能优化 | 性能预算、采样规范、CPU/GPU/UI/动画/物理、加载卡顿、回归监控 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#performance) |
| 17 | 内存控制 | 托管堆、原生内存、显存、资源泄漏、快照、低内存策略 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#memory) |
| 18 | 包体与加载 | 首包、分包、DLC、压缩、异步加载、Shader 预热、Loading | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#package-loading) |
| 19 | 编辑器工具 | EditorWindow、CustomEditor、批处理、Gizmos、导入规则 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#editor-tools) |
| 20 | 配置数据系统 | 导表、索引、校验、公式、多语言、热更、兼容 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#config-data) |
| 21 | 存档与本地数据 | PlayerPrefs、JSON、SQLite、加密、迁移、缓存、账号切换 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#local-save) |
| 22 | 构建发布与 CI/CD | Unity Build Pipeline、渠道包、符号、产物归档、灰度、回滚 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-10-build-release-cicd-sdk/#build-release) |
| 23 | 平台与 SDK 接入 | Android/iOS 桥接、登录、支付、广告、推送、隐私合规 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-10-build-release-cicd-sdk/#platform-sdk) |
| 24 | 测试与质量保障 | 单元测试、PlayMode、资源巡检、冒烟测试、长稳测试 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#testing) |
| 25 | 日志监控与线上排障 | 崩溃、ANR、符号解析、埋点、线上开关、事故复盘 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#observability) |
| 26 | 安全与反作弊 | 客户端不可信、协议签名、重放保护、支付校验、风控日志 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#security) |
| 27 | 跨平台适配 | 屏幕、安全区、图形 API、文件路径、权限、平台宏隔离 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#cross-platform) |
| 28 | 多语言与本地化 | 文本、字体、图片、语音、时区、数字格式、敏感词 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#localization) |
| 29 | 音频与视频 | AudioMixer、3D 音效、音频压缩、视频播放、字幕、平台兼容 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#audio-video) |
| 30 | AI、寻路与物理 | NavMesh、行为树、状态机、碰撞、Trigger、FixedUpdate、调试 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#ai-physics) |
| 31 | 团队管理与技术领导力 | 拆任务、带人、跨岗位沟通、技术评审、事故止血 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#leadership) |
| 32 | 项目管理与风险控制 | 里程碑、关键路径、风险清单、降级方案、技术债清单 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#project-risk) |
| 33 | 文档与表达能力 | 技术方案、接口文档、流程图、复盘、非技术沟通 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#communication) |

## 具体交付物索引

这张表用来避免文档空泛。开发高级/资深掌握一个方向，最终应该能交付可运行、可验证、可维护的结果。

| 方向 | 具体交付物 |
| --- | --- |
| Unity 引擎基础 | 项目启动流程图、生命周期规范、Prefab/Scene 使用规范、Unity 版本升级风险清单 |
| C# 与代码基本功 | 代码规范、GC 零分配示例、异步取消模板、IL2CPP/AOT 问题处理记录 |
| 客户端架构设计 | 模块依赖图、启动状态机、全局服务注册表、异步加载和失败恢复流程 |
| 工程规范与可维护性 | 目录规范、Review Checklist、错误码规范、模块 README、技术债清单 |
| 资源管理 | Addressables/Bundle 分组表、引用计数规则、资源释放规范、重复资源报告 |
| 热更新 | 资源清单、版本匹配规则、下载失败恢复流程、灰度和回滚方案 |
| UI 框架 | UI 层级规范、面板生命周期、返回栈规则、红点树、虚拟列表组件 |
| 交互与输入 | 输入抽象层、UI/场景射线隔离规则、手势规范、手柄焦点导航规则 |
| 网络通信 | 协议封装层、心跳和重连状态机、请求超时规则、协议日志和抓包说明 |
| 多人同步与 AOI | AOI 可视化调试、实体生命周期表、移动插值和纠偏规则、同步频率预算 |
| 战斗系统 | 技能释放流程、Buff 生命周期、属性公式表、回放/战报调试工具 |
| 玩法系统 | 任务/活动/奖励配置规范、条件系统、GM 调试入口、玩法埋点表 |
| 动画与演出 | Animator 规范、Timeline 接入模板、挂点规范、动画压缩和降级规则 |
| 渲染管线与 Shader | URP/HDRP 配置、Shader 规范、光照方案、RenderDoc/Frame Debugger 分析记录 |
| TA 与美术管线 | 美术资源预算、导入规则、资源扫描报告、材质和特效验收标准 |
| 性能优化 | 性能预算表、真机采样脚本、Profiler 对比报告、卡顿问题复盘、性能回归看板 |
| 内存控制 | Memory Profiler 对比报告、资源引用链分析、低内存设备策略、泄漏修复记录 |
| 包体与加载 | Build Report 差异报告、包体拆分方案、Loading 阶段耗时表、下载失败处理流程 |
| 编辑器工具 | EditorWindow 工具、批处理脚本、Gizmos 可视化、工具使用说明和错误报告 |
| 配置数据系统 | 导表流程、强类型配置访问、配置校验报告、配置版本兼容规则 |
| 存档与本地数据 | 本地数据结构、加密和校验方案、版本迁移脚本、账号切换和清缓存流程 |
| 构建发布与 CI/CD | 一键构建脚本、CI 流水线、产物归档、符号上传、发版 Checklist |
| 平台与 SDK 接入 | Android/iOS 桥接层、SDK 初始化流程、支付补单流程、隐私权限说明 |
| 测试与质量保障 | 单元测试、PlayMode 测试、资源巡检、冒烟测试脚本、长稳测试报告 |
| 日志监控与线上排障 | 日志字段规范、崩溃符号解析流程、线上开关后台、事故复盘模板 |
| 安全与反作弊 | 协议签名规则、支付验签流程、风控日志字段、作弊行为检测规则 |
| 跨平台适配 | 平台能力封装、安全区适配、权限处理、图形 API 兼容表、机型黑名单 |
| 多语言与本地化 | 文本表规范、字体回退方案、伪本地化测试、缺 Key/缺字扫描报告 |
| 音频与视频 | AudioMixer 分组、音频加载策略、视频播放兼容方案、后台音频策略 |
| AI、寻路与物理 | NavMesh 烘焙规范、AI 调试视图、碰撞矩阵、路径连通性巡检 |
| 团队管理与技术领导力 | 任务拆解模板、技术评审模板、Review 规则、带教计划、事故响应流程 |
| 项目管理与风险控制 | 里程碑计划、关键路径、风险清单、降级方案、灰度和回滚预案 |
| 文档与表达能力 | 技术方案、接口文档、流程图、状态图、排障文档、版本复盘 |

## 工具速查总览

![Unity 开发高级/资深工具链地图](/post-images/unity-senior-developer-toolchain-map.svg)

| 方向 | 需要掌握的工具 | 跳转 |
| --- | --- | --- |
| Unity 引擎基础 | Unity Editor、Package Manager、Project Settings、Profiler、Frame Debugger、Scripting API | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#unity-engine) |
| C# 与代码基本功 | Rider/Visual Studio、Roslyn Analyzer、dotTrace/dotMemory、ILSpy/dnSpy、Unit Test Runner | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#csharp) |
| 客户端架构设计 | Assembly Definition、UML/PlantUML/Mermaid、draw.io、Notion/Confluence、Unity Profiler | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-01-engine-csharp-architecture/#client-architecture) |
| 工程规范与可维护性 | Git、GitHub/GitLab、UnityYAMLMerge、EditorConfig、StyleCop/Roslyn、Jira/TAPD | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-02-engineering-maintainability/#engineering-standards) |
| 资源管理 | Addressables、AssetBundle Browser、Build Layout Report、Memory Profiler、Texture Importer | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-03-assets-hot-update/#asset-management) |
| 热更新 | Addressables Content Update、HybridCLR/xLua、CDN、hash 校验工具、灰度后台 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-03-assets-hot-update/#hot-update) |
| UI 框架 | UGUI、UI Toolkit、TextMeshPro、PSD/Sketch/Figma 标注、Canvas Profiler、FairyGUI 可选 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-04-ui-interaction-input/#ui-framework) |
| 交互与输入 | Input System、EventSystem、Physics Raycaster、Cinemachine、Device Simulator | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-04-ui-interaction-input/#interaction-input) |
| 网络通信 | Protobuf、Postman/Apifox、Wireshark、Charles、tcpdump、Network Link Conditioner | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-05-network-sync/#network) |
| 多人同步与 AOI | Unity Multiplayer Tools、Netcode/Mirror 参考、Gizmos、网络模拟器、Replay 工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-05-network-sync/#multiplayer-aoi) |
| 战斗系统 | Timeline、Cinemachine、技能编辑器、Excel/Google Sheets、帧同步/回放调试器 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#combat) |
| 玩法系统 | 配置导表工具、GM 后台、活动后台、状态机调试器、埋点看板 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#gameplay) |
| 动画与演出 | Animator、Timeline、Playable Graph Visualizer、Animation Rigging、Spine/Live2D 可选 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-06-gameplay-combat-animation/#animation) |
| 渲染管线与 Shader | URP/HDRP、Shader Graph、Frame Debugger、RenderDoc、Xcode GPU Frame Capture | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-07-rendering-shader-ta/#rendering) |
| TA 与美术管线 | DCC 工具、TexturePacker、Substance、资源扫描器、Shader Variant 工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-07-rendering-shader-ta/#technical-art) |
| 性能优化 | Unity Profiler、Profile Analyzer、Frame Debugger、RenderDoc、Android Studio Profiler | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#performance) |
| 内存控制 | Memory Profiler、Xcode Instruments、Android Studio Profiler、ADB、引用链分析工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#memory) |
| 包体与加载 | Build Report Inspector、Addressables Analyze、AssetStudio、Texture/Audio Importer、CDN 日志 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#package-loading) |
| 编辑器工具 | EditorWindow、CustomEditor、PropertyDrawer、AssetPostprocessor、Odin Inspector 可选 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#editor-tools) |
| 配置数据系统 | Excel/Google Sheets、导表脚本、JSON/Protobuf、SQLite、配置校验器 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#config-data) |
| 存档与本地数据 | PlayerPrefs、SQLite、File API、Keychain/Keystore、加密和迁移工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-09-editor-config-local-data/#local-save) |
| 构建发布与 CI/CD | Unity Batchmode、Jenkins/GitHub Actions、Fastlane、Gradle、Xcodebuild、符号上传工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-10-build-release-cicd-sdk/#build-release) |
| 平台与 SDK 接入 | Android Studio、Xcode、Gradle、CocoaPods、ADB、Logcat、Device Console | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-10-build-release-cicd-sdk/#platform-sdk) |
| 测试与质量保障 | Unity Test Framework、AltTester、Airtest/Poco、资源巡检脚本、设备农场 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#testing) |
| 日志监控与线上排障 | Firebase/Crashlytics、Bugly、Sentry、ELK/Grafana、符号解析、Logcat/Xcode Logs | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#observability) |
| 安全与反作弊 | HTTPS/TLS、签名工具、混淆工具、风控后台、支付验签工具、抓包和重放测试工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-11-testing-observability-security/#security) |
| 跨平台适配 | Device Simulator、Unity Remote、ADB、Xcode Devices、BrowserStack/云真机、平台宏检查 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#cross-platform) |
| 多语言与本地化 | Unity Localization、TextMeshPro Font Asset Creator、伪本地化工具、LQA 表、缺字扫描 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#localization) |
| 音频与视频 | Audio Mixer、FMOD/Wwise 可选、VideoPlayer、Audacity、平台视频编码工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#audio-video) |
| AI、寻路与物理 | NavMesh、AI Navigation、Physics Debugger、Gizmos、行为树编辑器、碰撞矩阵工具 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-12-cross-platform-localization-audio-ai-physics/#ai-physics) |
| 团队管理与技术领导力 | Jira/TAPD、GitHub Projects、Miro、Notion/Confluence、代码评审平台 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#leadership) |
| 项目管理与风险控制 | 甘特图/里程碑工具、风险清单、灰度后台、监控看板、事故复盘模板 | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#project-risk) |
| 文档与表达能力 | Markdown、Mermaid、PlantUML、draw.io、Notion/Confluence、PPT/Keynote | [查看](https://zhoujun2303.github.io/post/unity-senior-developer-13-tech-leadership-project-communication/#communication) |

## 能力分层图

![开发高级/资深架构分层](/post-images/unity-senior-developer-architecture-layers.svg)

开发高级/资深能力可以按四层理解：

- 基础层：Unity、C#、数据结构、生命周期、平台差异。
- 框架层：资源、UI、网络、配置、事件、对象池、构建。
- 质量层：性能、内存、测试、日志、监控、安全、稳定性。
- 领导层：技术方案、风险控制、团队协作、发版节奏、线上复盘。

## 交付闭环图

![开发高级/资深交付闭环](/post-images/unity-senior-developer-delivery-loop.svg)

开发高级/资深的判断标准不是“我写完了”，而是闭环是否完整：

- 需求能拆清楚。
- 方案能评审。
- 接口能对齐。
- 开发能落地。
- 测试能验证。
- 构建能稳定产出。
- 上线能监控。
- 事故能回滚和复盘。

## 推荐学习路线

![Unity 开发高级/资深学习路线](/post-images/unity-senior-developer-learning-roadmap.svg)

1. 第一阶段：Unity 基础、C# 基础、UGUI、资源加载、协程与异步。
2. 第二阶段：UI 框架、网络协议、配置系统、事件系统、对象池、状态机。
3. 第三阶段：AssetBundle/Addressables、热更新、构建发布、平台 SDK。
4. 第四阶段：Profiler、Frame Debugger、Memory Profiler、加载优化、包体优化。
5. 第五阶段：战斗、动画、渲染、Shader、TA 协作、复杂业务框架。
6. 第六阶段：线上监控、事故排查、自动化测试、风险管理、团队带教。

## 开发高级/资深自检 Checklist

- 项目启动链路是否清晰，热更、登录、进场景失败时是否能定位具体阶段。
- 核心模块是否有明确边界，是否存在严重循环依赖和跨模块乱调。
- 资源加载、引用计数、卸载、版本、下载、回滚是否形成闭环。
- UI、网络、配置、红点、音频、对象池是否有统一框架和示例。
- 性能预算是否明确，是否有版本级别的 CPU、GPU、内存、包体回归数据。
- 构建是否自动化，是否能稳定产出不同平台、渠道和环境的包。
- 崩溃、异常、卡顿、加载失败、资源缺失是否能在线上追踪。
- SDK、支付、隐私、权限、审核差异是否有平台级兜底方案。
- 测试是否覆盖配置、资源、核心逻辑、冒烟流程和长稳场景。
- 新人是否能通过文档、模板和示例快速接入项目。
- 需求变更时，是否能说明影响范围、风险、工期和回滚方案。
- 团队是否知道遇到问题该看日志、看工具、找文档还是找负责人。

## 专题文件结构

```text
LocalBK/posts/unity-senior-developer-skills.md
LocalBK/posts/unity-senior-developer-01-engine-csharp-architecture.md
LocalBK/posts/unity-senior-developer-02-engineering-maintainability.md
LocalBK/posts/unity-senior-developer-03-assets-hot-update.md
LocalBK/posts/unity-senior-developer-04-ui-interaction-input.md
LocalBK/posts/unity-senior-developer-05-network-sync.md
LocalBK/posts/unity-senior-developer-06-gameplay-combat-animation.md
LocalBK/posts/unity-senior-developer-07-rendering-shader-ta.md
LocalBK/posts/unity-senior-developer-08-performance-memory-package.md
LocalBK/posts/unity-senior-developer-09-editor-config-local-data.md
LocalBK/posts/unity-senior-developer-10-build-release-cicd-sdk.md
LocalBK/posts/unity-senior-developer-11-testing-observability-security.md
LocalBK/posts/unity-senior-developer-12-cross-platform-localization-audio-ai-physics.md
LocalBK/posts/unity-senior-developer-13-tech-leadership-project-communication.md
LocalBK/post-images/unity-senior-developer-skill-map.svg
LocalBK/post-images/unity-senior-developer-toolchain-map.svg
LocalBK/post-images/unity-senior-developer-architecture-layers.svg
LocalBK/post-images/unity-senior-developer-delivery-loop.svg
LocalBK/post-images/unity-senior-developer-learning-roadmap.svg
```