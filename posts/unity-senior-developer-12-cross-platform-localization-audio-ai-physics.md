---
id: o6CWyQ
title: Unity 开发高级/资深 12：跨平台、本地化、音视频、AI 与物理
createdAt: "2026-06-10 22:02:00"
updated: "2026-06-17 10:10:59"
tags:
    - Unity
    - 开发高级/资深
    - 跨平台
    - 本地化
tag_ids:
    - FjODty
    - P46nOZ
    - 8XtUrb
    - zii89F
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: true
feature: ""
isTop: false
---

[返回总览](/post/unity-senior-developer-skills/)

![Unity 开发高级/资深工具链地图](/post-images/unity-senior-developer-toolchain-map.svg)

<a id="cross-platform"></a>
## 跨平台适配

- 屏幕适配：安全区、刘海屏、异形屏、平板、PC 窗口、超宽屏。
- 输入差异：触控、键鼠、手柄、遥控器、快捷键、系统返回键。
- 图形 API：OpenGLES、Vulkan、Metal、DirectX 的 Shader 和性能差异。
- 文件系统：StreamingAssets、PersistentDataPath、缓存目录、权限限制。
- 后台行为：切后台、锁屏、来电、音频暂停、网络断开、恢复。
- 权限合规：相册、相机、麦克风、通知、定位、广告标识。
- 平台宏：平台差异集中封装，避免业务代码到处写条件编译。
- 设备兼容：GPU 黑名单、驱动 Bug、内存等级、画质默认值。

### 需要掌握的工具

- Device Simulator：验证分辨率、安全区、横竖屏和基础设备差异。
- Unity Remote 和真机调试：验证输入、性能、传感器和设备返回键。
- ADB、Logcat：Android 安装、权限、日志、崩溃、ANR 和设备信息。
- Xcode Devices、Console.app：iOS 真机日志、崩溃和配置问题。
- BrowserStack、云真机、测试机房：覆盖机型、系统和地区差异。
- 平台宏检查脚本：避免平台差异散落在业务代码中。
- 图形 API 调试工具：RenderDoc、Xcode GPU Capture、Android GPU Inspector。

### 可继续细分方向

- 屏幕、安全区和输入适配。
- Android、iOS、PC、WebGL 平台差异。
- 图形 API 和机型兼容。
- 权限、后台行为和文件系统路径。

<a id="localization"></a>
## 多语言与本地化

- 文本系统：文本表、Key、变量占位符、富文本、换行规则。
- 字体系统：字体回退、字体包拆分、动态字体、缺字检测。
- 图片本地化：图集拆分、活动图、商店图、公告图、下载策略。
- 语音本地化：语言包、字幕、音频加载、口型匹配。
- 格式差异：日期、时间、货币、数字、小数点、单位、时区。
- 排版差异：英文长度、日文换行、韩文、泰文、阿拉伯文 RTL。
- 敏感词：聊天、昵称、签名、公会名、地区差异。
- 测试工具：伪本地化、长文本测试、缺 Key 扫描、缺字扫描。

### 需要掌握的工具

- Unity Localization：String Table、Asset Table、语言切换和资源本地化。
- TextMeshPro Font Asset Creator：制作字体资产、Fallback 和缺字检查。
- 伪本地化工具：模拟长文本、特殊字符和 RTL 问题。
- LQA 表和缺 Key 扫描器：跟踪翻译状态、缺失文本和错误占位符。
- 敏感词工具：检查昵称、聊天、签名和地区差异词库。
- 多语言截图工具：批量截图，给测试和翻译验收。

### 可继续细分方向

- 文本表、变量和富文本。
- 字体、缺字和 Fallback。
- 图片、语音和资源本地化。
- 时区、货币、敏感词和 LQA 流程。

<a id="audio-video"></a>
## 音频与视频

- 音频架构：BGM、环境音、UI 音效、角色音效、语音、战斗音效。
- AudioMixer：音量分组、静音、淡入淡出、混响、区域切换。
- 3D 音效：距离衰减、空间位置、优先级、同屏数量限制。
- 资源优化：压缩格式、流式加载、预加载、内存和延迟平衡。
- 视频播放：首帧黑屏、跳过、暂停、字幕、平台解码兼容。
- 后台策略：切后台暂停、恢复、系统音乐共存、耳机插拔。

### 需要掌握的工具

- Audio Mixer：音量分组、混音、淡入淡出、快照和效果。
- FMOD、Wwise 可选：大型项目音频中间件、事件和混音流程。
- Unity VideoPlayer：视频播放、跳过、字幕、首帧和平台兼容。
- Audacity、Adobe Audition：查看音频格式、响度、裁剪和压缩。
- 平台视频编码工具：H.264/H.265、码率、分辨率和容器格式验证。
- Profiler Audio 模块：观察音频内存、播放数量和 CPU 开销。

### 可继续细分方向

- BGM、环境音、UI 音效和角色音效。
- 音频压缩、加载和内存。
- 视频播放、字幕和平台解码。
- 后台音频策略和系统音频共存。

<a id="ai-physics"></a>
## AI、寻路与物理

- NavMesh：烘焙、区域成本、OffMeshLink、动态障碍、路径失败。
- AI 模型：状态机、行为树、规则系统、简单 GOAP 的适用边界。
- NPC 行为：巡逻、追击、逃跑、避让、返回、交互、剧情控制。
- 物理基础：Rigidbody、Collider、Trigger、Layer Collision Matrix。
- FixedUpdate：物理步长、插值、连续碰撞、输入与物理同步。
- 碰撞优化：层级过滤、检测频率、碰撞体简化、Raycast 批处理。
- 调试视图：路径、感知范围、碰撞盒、状态、目标、阻塞原因。

### 需要掌握的工具

- NavMesh、AI Navigation：烘焙、动态障碍、区域成本、OffMeshLink。
- Physics Debugger：查看碰撞体、Trigger、Layer Collision Matrix 和物理状态。
- Gizmos、Handles：可视化巡逻路径、感知范围、攻击范围和碰撞盒。
- 行为树编辑器或自研 AI 调试器：查看 AI 当前节点、目标和黑板数据。
- Profiler Physics 模块：分析物理检测、碰撞回调和 FixedUpdate 成本。
- 自动寻路测试脚本：巡检路径连通性、卡点和不可达目标。

### 可继续细分方向

- NavMesh 和自动寻路。
- AI 状态机、行为树和调试。
- Rigidbody、Collider、Trigger 和碰撞层。
- 物理性能、Raycast 和卡点排查。

## 开发高级/资深关注点

- 平台差异要封装成平台层能力，不让业务层承担复杂性。
- 本地化要从 UI 设计阶段介入，而不是上线前硬塞长文本。
- 音频、视频和寻路都容易产生隐藏性能成本，需要预算。
- 物理问题要能用调试视图定位，而不是靠猜。