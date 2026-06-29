---
id: nKnFpw
title: Unity 开发高级/资深 01：引擎、C# 与客户端架构
createdAt: "2026-06-10 21:51:00"
updated: "2026-06-29 15:42:42"
tags:
    - Unity
    - 开发高级/资深
    - C#
    - 架构
tag_ids:
    - FjODty
    - P46nOZ
    - fOiXzM
    - 78c4Tb
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

相关图示：[能力分层图](/post/unity-senior-developer-skills/#architecture-layers)

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
- 版本意识：Unity LTS 选择、升级风险、插件兼容。
- 渲染管线差异：[单独阅读](/post/unity-senior-developer-01-01-render-pipeline-differences/) Built-in、URP、HDRP 的定位、资源兼容、Shader/材质、后处理、性能和迁移成本。

### 坐标、旋转与父子变换

坐标系统不要死记名词，核心是先问一句：这个值是相对于谁的？

- 世界坐标：相对于整个 Scene 的坐标。`transform.position`、`transform.rotation` 表示物体在世界里的位置和旋转，适合做寻路、相机跟随、子弹飞行、怪物距离判断。
- 本地坐标：相对于父节点的坐标。`transform.localPosition`、`transform.localRotation`、`transform.localScale` 表示子节点在父节点空间里的偏移，适合做挂点、武器、特效、UI 子节点布局。
- 屏幕坐标：相对于屏幕像素的坐标。鼠标、触摸、`Camera.WorldToScreenPoint` 得到的通常是屏幕坐标，常用于点击检测、血条跟随角色、把 3D 位置投到屏幕上。
- UI 坐标：相对于某个 `RectTransform` 或 Canvas 的坐标。UGUI 里不要直接把屏幕坐标当成 `anchoredPosition`，通常要用 `RectTransformUtility.ScreenPointToLocalPointInRectangle` 做转换。

常用转换可以按这个顺序理解：

```csharp
// 子节点挂点：本地偏移 -> 世界位置
Vector3 worldPoint = weaponRoot.TransformPoint(localOffset);

// 判断一个世界点在某个物体自己的前后左右：世界位置 -> 本地位置
Vector3 localPoint = transform.InverseTransformPoint(enemy.position);
bool enemyInFront = localPoint.z > 0f;

// 角色头顶世界坐标 -> 屏幕坐标 -> UI 面板坐标
Vector3 screenPoint = Camera.main.WorldToScreenPoint(head.position);
RectTransformUtility.ScreenPointToLocalPointInRectangle(
    hpBarRoot,
    screenPoint,
    uiCamera,
    out Vector2 uiPoint
);
hpBar.anchoredPosition = uiPoint;
```

角色头顶是 3D 世界坐标，血条是 2D UI 坐标，二者不能直接赋值。先转成屏幕坐标，是因为屏幕是相机投影后的共同参照：`WorldToScreenPoint` 会把世界点经过相机位置、朝向、FOV、透视投影和分辨率，变成屏幕上的像素点；然后再用 `ScreenPointToLocalPointInRectangle` 转成某个 UI 容器下的本地坐标。实际项目里还要判断 `screenPoint.z`，如果角色在相机背后，血条应该隐藏。

四元数和矩阵可以先按“工具”理解，不用一开始就钻数学细节。

- 四元数 `Quaternion` 用来表示旋转。它比欧拉角稳定，不容易遇到万向锁。业务代码里不要直接改 `x/y/z/w`，优先用 `Quaternion.Euler`、`Quaternion.LookRotation`、`Quaternion.AngleAxis`、`Quaternion.Slerp`。
- 矩阵 `Matrix4x4` 可以把位置、旋转、缩放合成一次变换。Unity 的 `Transform` 背后本质就是矩阵变换：`localToWorldMatrix` 把本地空间转到世界空间，`worldToLocalMatrix` 反过来。日常业务优先用 `TransformPoint`、`InverseTransformPoint`，写 Shader、批量渲染、自定义骨骼或大量数学计算时再直接碰矩阵。
- 父子节点变换的关系是：父节点的世界变换乘上子节点的本地变换，得到子节点的世界变换。父节点移动、旋转、缩放，子节点会一起变化；子节点改 `localPosition`，是在父节点空间里调整偏移。

万向锁是欧拉角的典型问题：3D 旋转本来有三个自由度，但在某些角度下，两个旋转轴会重合，实际只剩两个有效方向。表现到 Unity 里，就是连续改 `transform.eulerAngles` 时可能出现角度跳变、方向怪、某个轴像是转不动。欧拉角适合 Inspector 显示和配置，四元数更适合代码里的旋转计算、插值和组合。

几个容易踩坑的点：

- `position` 和 `localPosition` 不是一回事。没有父节点时两者看起来一样，有父节点后差异会立刻出现。
- `TransformPoint` 会受位置、旋转、缩放影响；`TransformDirection` 只处理方向，不处理位置。算方向时不要用点位转换硬减。
- `SetParent(parent, true)` 会尽量保持当前世界位置不变，并重新计算本地坐标；`SetParent(parent, false)` 会保留当前本地值，世界位置可能变化。
- 父节点有非等比缩放时，子节点旋转、碰撞体、粒子和 UI 都可能出现奇怪结果。项目里尽量不要把复杂逻辑挂在被拉伸的父节点下面。
- UI 的 Overlay、Screen Space Camera、World Space 三种 Canvas 模式转换方式不同。遇到“血条位置偏了”“点击区域不对”，先检查 Canvas 模式、相机参数和坐标转换函数。

实际项目里，能把坐标系统讲清楚的人，通常能更快定位这类问题：角色头顶血条漂移、子弹方向不对、特效挂点偏移、拖拽 UI 跟手异常、相机跟随抖动、换父节点后物体瞬移。

### PlayerLoop 与每帧执行链

PlayerLoop 可以理解成 Unity 一帧内部的执行流水线。开发时不需要背完整源码，但要知道脚本、物理、动画和渲染大致先后发生在哪里。

简化顺序可以这样看：

```text
输入与时间更新
↓
FixedUpdate，可能 0 次、1 次或多次
↓
物理模拟
↓
Update
↓
动画、状态机、协程等更新
↓
LateUpdate
↓
相机、剔除、渲染提交
↓
画面显示
```

`FixedUpdate` 按固定时间步长执行，不是每帧一定一次。帧率低时 Unity 可能连续执行多次来追物理时间，帧率高时也可能一次都不执行。`Rigidbody` 移动、加力、物理前控制适合放这里。

`Update` 基本每帧一次，适合输入、普通业务逻辑、角色状态、技能冷却、UI 刷新等。`LateUpdate` 在所有 `Update` 后执行，适合相机跟随、角色后处理、需要等别人先动完再修正自己的逻辑。

渲染在脚本逻辑之后。也就是说这一帧在 `Update` 或 `LateUpdate` 改了位置、材质、显隐，后面的渲染阶段才会把变化画出来。理解 PlayerLoop，主要是为了排查物理抖动、相机抖动、输入延迟、动画覆盖位移、UI 跟随 3D 角色偏一帧、协程时机不符合预期这类问题。

### 输入系统与动作抽象

输入系统的核心不是 API 名字，而是不要让业务代码到处直接读具体设备。角色、战斗、UI、交互系统应该关心“玩家想做什么”，而不是关心这个输入来自键盘、鼠标、触屏还是手柄。

旧 `Input` 常见写法是直接读按键：

```csharp
if (Input.GetKeyDown(KeyCode.Space))
{
    Jump();
}
```

这种方式简单，适合小项目和旧项目。但平台一多，业务代码里会散落很多 `GetKeyDown`、`GetMouseButtonDown`、`GetTouch`，后面支持手柄、改键位、做触屏虚拟摇杆都会很难收。

New Input System 更推荐先定义 Action：

```text
Move：移动
Look：视角旋转
Jump：跳跃
Attack：攻击
Interact：交互
OpenMenu：打开菜单
```

一个 Action 可以绑定多个输入来源：

```text
Move
- Keyboard：WASD
- Gamepad：Left Stick
- Touch：Virtual Joystick

Attack
- Mouse：Left Button
- Gamepad：Right Trigger
- Touch：攻击按钮
```

业务层只读统一动作：

```csharp
Vector2 move = moveAction.ReadValue<Vector2>();
```

它不应该关心这个 `Vector2` 是键盘、摇杆还是虚拟摇杆来的。

`Action Map` 是一组输入动作的集合，通常按当前游戏状态划分：

```text
Gameplay
- Move
- Look
- Jump
- Attack
- Interact

UI
- Navigate
- Submit
- Cancel
- Point
- Click

Vehicle
- Steer
- Brake
- Accelerate
```

分 Action Map 的意义是防止状态混乱。比如 `Esc` 在 Gameplay 里是打开菜单，在 UI 里是关闭弹窗；打开背包时应该禁用 Gameplay，启用 UI，避免“点 UI 的同时角色还在攻击或移动”。

```csharp
gameplayMap.Disable();
uiMap.Enable();
```

设备热插拔指游戏运行中设备随时接入或断开。玩家可能先用键鼠，进入游戏后插入手柄；也可能中途拔掉手柄切回键鼠。New Input System 可以监听设备变化：

```csharp
InputSystem.onDeviceChange += (device, change) =>
{
    if (change == InputDeviceChange.Added)
    {
        Debug.Log($"设备接入: {device.displayName}");
    }

    if (change == InputDeviceChange.Removed)
    {
        Debug.Log($"设备断开: {device.displayName}");
    }
};
```

中大型项目里，一般会再包一层 `InputService` 或 `InputReader`：

```text
New Input System
↓
InputReader / InputService
↓
统一动作数据
↓
角色、UI、战斗、交互系统
```

这样 UI 提示可以根据当前设备显示“按 E 交互”或“按 A 交互”，业务逻辑也不会因为新增触屏、手柄、键位重绑而大面积修改。

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
- [渲染管线差异与升级迁移](/post/unity-senior-developer-01-01-render-pipeline-differences/)。
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
