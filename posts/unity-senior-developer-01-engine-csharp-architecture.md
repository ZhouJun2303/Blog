---
title: 'Unity 开发高级/资深 01：引擎、C# 与客户端架构'
date: 2026-06-10 21:51:00
tags: [Unity,开发高级/资深,C#,架构]
published: true
hideInList: true
feature: 
isTop: false
---
[返回总览](https://zhoujun2303.github.io/post/unity-senior-developer-skills/)

![开发高级/资深架构分层](https://zhoujun2303.github.io/post-images/unity-senior-developer-architecture-layers.svg)

<a id="unity-engine"></a>
## Unity 引擎基础

- 生命周期：Awake、OnEnable、Start、Update、LateUpdate、FixedUpdate、OnDisable、OnDestroy 的调用顺序和适用边界。
- 场景与对象：GameObject、Component、Prefab、Scene、ScriptableObject 的职责和引用关系。
- 坐标系统：世界坐标、本地坐标、屏幕坐标、UI 坐标、四元数、矩阵、父子节点变换。
- 序列化规则：Unity 可序列化字段、非序列化字段、Inspector 引用、Prefab Override、丢引用问题。
- PlayerLoop：理解 Unity 每帧执行链，知道脚本、物理、动画、渲染大致发生在哪些阶段。
- 场景管理：单场景、多场景 Additive、异步加载、切场景状态、常驻对象管理。
- 时间系统：Time.deltaTime、fixedDeltaTime、timeScale、真实时间、服务器时间、本地时间。
- 输入系统：旧 Input、新 Input System、触控、键鼠、手柄在架构中的抽象方式。
- 编辑器与运行时：Editor 代码隔离、Assembly Definition、条件编译、打包裁剪。
- 版本意识：Unity LTS 选择、升级风险、插件兼容、渲染管线差异。

### 需要掌握的工具

- Unity Editor：Scene、Game、Inspector、Hierarchy、Project、Console、Profiler 等核心窗口。
- Package Manager：管理官方包、第三方包和本地包依赖。
- Project Settings：质量、输入、物理、图形、脚本后端、平台参数。
- Unity Profiler：查看脚本、物理、动画、渲染、加载的基础耗时。
- Frame Debugger：理解渲染顺序和 Draw Call。
- Unity Scripting API/Manual：查生命周期、组件 API 和版本差异。

### 可继续细分方向

- 生命周期与 PlayerLoop。
- 场景、Prefab 与序列化。
- Unity 平台参数与构建设置。
- 编辑器扩展与运行时代码隔离。

<a id="csharp"></a>
## C# 与代码基本功

- 语法能力：泛型、委托、事件、Attribute、扩展方法、反射、迭代器、Lambda。
- 类型理解：值类型、引用类型、装箱拆箱、可空类型、struct 拷贝成本。
- 集合选择：Array、List、Dictionary、HashSet、Queue、Stack、LinkedList 的使用场景和性能差异。
- GC 控制：闭包分配、LINQ 分配、foreach 分配、字符串拼接、装箱、临时 List。
- 异步能力：Coroutine、async/await、Task、UniTask、回调之间的取舍。
- 线程意识：Unity API 主线程限制、后台线程 IO、锁、并发队列、主线程调度。
- 错误处理：异常、错误码、Result、断言、日志等级、失败回调。
- IL2CPP/AOT：泛型裁剪、反射保留、link.xml、AOT 泛型补充、符号堆栈。
- 代码表达：命名清楚、函数短小、参数明确、避免魔法值、避免过深嵌套。

### 需要掌握的工具

- Rider 或 Visual Studio：调试、重构、代码导航、性能提示。
- Roslyn Analyzer：静态检查空引用、命名、分配和风格问题。
- Unity Test Framework：验证纯逻辑、配置解析、状态机和公式。
- ILSpy/dnSpy：查看程序集、IL、第三方库结构和 AOT 问题线索。
- dotTrace/dotMemory 或 Rider Profiler：分析 C# 层耗时和托管内存。
- link.xml 与 Unity Managed Stripping 工具链：处理裁剪和反射保留。

### 可继续细分方向

- C# 基础语法与工程写法。
- GC、内存分配与性能敏感写法。
- async/await、Coroutine、UniTask 与线程模型。
- IL2CPP、AOT、反射和泛型裁剪。

<a id="client-architecture"></a>
## 客户端架构设计

- 分层架构：入口层、框架层、业务层、表现层、数据层、平台层。
- 模块边界：登录、资源、UI、网络、战斗、任务、背包、活动、音频、引导等模块互不乱调。
- 启动流程：初始化配置、日志、热更、SDK、资源系统、网络、登录、进场景。
- 全局服务：事件系统、计时器、对象池、音频、输入、红点、埋点、权限、时间同步。
- 依赖治理：避免循环依赖、隐式单例、静态状态污染和跨模块直接访问。
- 状态机：登录态、热更态、游戏态、切场景态、重连态、战斗态、后台态。
- 异步规范：加载取消、超时、失败重试、重复请求合并、资源释放、异常捕获。
- Assembly 拆分：Runtime、Editor、Tests、ThirdParty、HotUpdate 独立边界。
- 可演进性：给业务留扩展点，同时避免为了“未来可能需要”过度抽象。

### 需要掌握的工具

- Assembly Definition：拆分 Runtime、Editor、Tests、HotUpdate 和第三方依赖。
- Mermaid、PlantUML、draw.io：画模块图、流程图、状态图和时序图。
- Notion/Confluence/飞书文档：沉淀架构说明、接入流程和排障文档。
- Unity Profiler 与自定义埋点：验证架构链路中的耗时和失败点。
- GitHub/GitLab Code Review：让架构约束通过评审持续落地。
- 依赖分析脚本：检查 Assembly、命名空间、资源和模块引用边界。

### 可继续细分方向

- 启动流程与游戏状态机。
- 模块边界与依赖治理。
- 全局服务、事件系统和对象池。
- 异步流程、取消、超时和异常恢复。

## 开发高级/资深判断标准

- 新人能否在一天内理解项目启动流程。
- 一个业务模块能否独立开发、测试、替换和定位问题。
- 切场景、热更失败、断线重连等复杂链路是否有明确状态。
- 框架代码是否稳定，业务迭代是否不用频繁改底层。
- 出问题时能否通过日志和状态快速定位是哪一层失败。

## 常见风险

- 所有模块都依赖一个巨大的 GameManager。
- 单例过多，模块之间直接互相调用，测试和替换困难。
- 异步流程没有取消和超时，切场景后回调继续修改已销毁对象。
- Editor 脚本混入 Runtime，导致打包失败或包体膨胀。
- 为了“架构漂亮”写出团队难以理解的抽象。
