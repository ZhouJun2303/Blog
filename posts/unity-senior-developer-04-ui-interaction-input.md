---
id: csEUEO
title: Unity 开发高级/资深 04：UI、交互与输入
createdAt: "2026-06-10 21:54:00"
updated: "2026-06-17 10:10:59"
tags:
    - Unity
    - 开发高级/资深
    - UI
tag_ids:
    - FjODty
    - P46nOZ
    - 6wRaJA
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: true
feature: ""
isTop: false
---

[返回总览](https://zhoujun2303.github.io/post/unity-senior-developer-skills/)

![Unity 开发高级/资深工具链地图](/post-images/unity-senior-developer-toolchain-map.svg)

<a id="ui-framework"></a>
## UI 框架

- UI 分层：HUD、普通面板、全屏面板、弹窗、Toast、引导、Loading、系统提示。
- 生命周期：打开、关闭、隐藏、恢复、缓存、销毁、重复打开、快速关闭。
- 面板栈：返回键、遮罩层、互斥面板、弹窗优先级、二次确认。
- 异步加载：面板资源加载中取消、加载失败重试、加载完成时状态是否仍有效。
- 数据绑定：手动刷新、事件刷新、响应式绑定的成本和适用范围。
- 红点系统：数据源、依赖树、聚合规则、缓存、刷新频率、调试视图。
- 通用组件：奖励格子、货币栏、页签、列表、筛选、排序、确认框、Loading。
- 适配：安全区、刘海屏、平板、PC 窗口、超宽屏、横竖屏。
- 性能：Canvas 拆分、避免频繁 Rebuild、图集、字体、ScrollView 虚拟列表。

### 需要掌握的工具

- UGUI：Canvas、Graphic、Layout、EventSystem、Mask、ScrollRect。
- TextMeshPro：字体资产、Fallback、富文本、缺字处理。
- UI Toolkit：了解适用场景，尤其是编辑器工具和部分运行时 UI。
- Unity Profiler UI 模块：分析 Canvas Rebuild、Batch、Layout 和 GC。
- Frame Debugger：检查 UI Draw Call、图集和材质切换。
- Device Simulator：验证安全区、分辨率、横竖屏和屏幕比例。
- Figma、Sketch、Photoshop 标注：对齐视觉尺寸、切图、字体和交互动效。
- FairyGUI、UGUI Extension 或项目自研 UI 工具：根据团队技术栈掌握。

### 可继续细分方向

- UI 生命周期和面板栈。
- 红点系统和功能入口。
- UI 适配和多语言布局。
- UI 性能、图集和虚拟列表。

<a id="interaction-input"></a>
## 交互与输入

- 输入抽象：触控、键鼠、手柄、快捷键统一成项目内的输入事件。
- UI 与场景隔离：点击 UI 时不触发场景射线，拖拽时不误触点击。
- 射线检测：地面、NPC、建筑、道具、怪物、UI 的 Layer 和优先级清楚。
- 交互距离：可点击、可靠近、自动寻路、距离不足提示、交互冷却。
- 手势：拖拽、滑动、双指缩放、长按、短按、惯性、边界限制。
- 键鼠：悬停提示、右键菜单、快捷键冲突、输入框焦点。
- 手柄：焦点导航、确认/取消、摇杆移动、功能轮盘。
- 防误触：连点保护、点击穿透、Loading 遮罩、网络请求中的按钮状态。

### 需要掌握的工具

- Unity Input System：抽象触控、键鼠、手柄、快捷键和重绑定。
- EventSystem、Graphic Raycaster、Physics Raycaster：处理 UI 和场景点击优先级。
- Physics Debugger：排查射线、碰撞层和交互触发问题。
- Cinemachine：处理镜头跟随、缩放、碰撞和交互聚焦。
- Device Simulator 与真机调试：验证触控、手势、安全区和设备返回键。
- 自研输入调试面板：显示当前输入源、命中对象、射线路径和焦点状态。

### 可继续细分方向

- UI 输入与场景输入隔离。
- 触控手势。
- 键鼠和手柄适配。
- 射线交互、防误触和焦点系统。

## UI 架构常见模块

- UIManager：统一打开、关闭、查找、层级、返回、缓存。
- WindowBase：面板生命周期、资源句柄、事件注册、动画状态。
- ViewModel 或 Presenter：隔离表现和业务数据。
- RedDotManager：红点树、节点刷新、调试路径。
- GuideLayer：引导遮罩、聚焦目标、点击穿透、步骤恢复。
- SafeAreaAdapter：统一处理设备安全区。
- ListVirtualizer：大量列表复用和增量刷新。

## 开发高级/资深关注点

- UI 打开失败是否有日志和用户可恢复路径。
- UI 关闭后是否释放事件、异步回调和资源引用。
- 红点是否能解释“为什么亮”和“为什么不亮”。
- 适配是否用规则解决，而不是每个界面手动调。
- 列表、背包、邮件、排行榜等高频 UI 是否做虚拟化和增量刷新。