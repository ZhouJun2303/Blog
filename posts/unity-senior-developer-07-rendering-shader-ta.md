---
id: 7oWg0w
title: Unity 开发高级/资深 07：渲染、Shader 与 TA 协作
createdAt: "2026-06-10 21:57:00"
updated: "2026-06-17 10:10:59"
tags:
    - Unity
    - 开发高级/资深
    - 渲染
    - Shader
tag_ids:
    - FjODty
    - P46nOZ
    - WIyoEq
    - Shader
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

<a id="rendering"></a>
## 渲染管线与 Shader

- 管线选择：Built-in、URP、HDRP 的效果、性能、平台和团队成本。
- 渲染流程：Queue、Pass、Batch、SetPass、Draw Call、Overdraw、深度。
- SRP Batcher：材质属性、Shader 写法、常量缓冲区、兼容规则。
- Shader 基础：顶点、片元、光照、采样、Keyword、Variant、宏、Include。
- 常见效果：角色 Rim、描边、溶解、流光、水、玻璃、草、雪、受击闪白。
- 光照系统：实时光、烘焙光、混合光、Light Probe、Reflection Probe、阴影。
- 后处理：Bloom、Color Grading、AO、景深、抗锯齿、移动端降级。
- 调试工具：Frame Debugger、RenderDoc、Profiler、GPU Profiler。
- 平台差异：Metal、Vulkan、OpenGLES、DirectX 的 Shader 兼容问题。

### 需要掌握的工具

- URP/HDRP Render Pipeline Asset：管理渲染质量、阴影、后处理和平台参数。
- Shader Graph 与手写 HLSL：实现和维护项目 Shader。
- Frame Debugger：查看渲染顺序、Pass、SetPass 和 Draw Call。
- RenderDoc：分析 GPU 渲染、纹理采样、Buffer、Pass 输出。
- Xcode GPU Frame Capture、Android GPU Inspector：定位平台 GPU 问题。
- Unity Profiler GPU 模块：查看渲染线程、GPU 耗时和瓶颈。
- Shader Variant Collection 与自研统计工具：控制变体数量和预热。

### 可继续细分方向

- URP/HDRP 管线配置。
- Shader Graph 与 HLSL。
- 光照、阴影和后处理。
- 渲染调试、GPU 分析和平台兼容。

<a id="technical-art"></a>
## TA 与美术管线

- 资源预算：模型面数、骨骼数、贴图尺寸、材质数、特效粒子数。
- 导入规则：贴图压缩、模型 Rig、动画裁剪、Read/Write、MipMap、sRGB。
- 材质规范：公共材质、实例材质、贴图通道复用、命名和参数范围。
- 特效规范：粒子数量、透明面积、Overdraw、生命周期、对象池兼容。
- 场景规范：LOD、Occlusion、静态合批、Lightmap、Probe、碰撞体。
- 验收工具：资源扫描、材质扫描、Shader Variant 统计、贴图尺寸统计。
- 美术协作：效果目标、性能预算、低端降级、资源提交检查。
- 版本控制：大资源锁定、Meta 文件、Prefab 冲突和材质覆盖。

### 需要掌握的工具

- Blender、Maya、3ds Max：理解模型、骨骼、UV、动画和导出问题。
- Photoshop、Substance Painter/Designer：理解贴图通道、压缩和材质输入。
- TexturePacker、SpriteAtlas：管理 UI 和 2D 资源图集。
- Unity AssetPostprocessor：自动设置模型、贴图、音频和动画导入规则。
- 资源扫描器：检查面数、骨骼、贴图尺寸、材质数量、Read/Write。
- Shader Variant 统计工具：追踪美术效果带来的变体和包体变化。
- Perforce/Git LFS/Plastic SCM：管理大资源、锁文件和美术协作流程。

### 可继续细分方向

- 美术资源导入规范。
- 场景、角色、特效和 UI 资源预算。
- 材质、贴图和 Shader 参数规范。
- 自动验收、资源扫描和提交检查。

## 开发高级/资深关注点

- 效果上线前是否知道它的 CPU、GPU、内存和包体成本。
- Shader Keyword 是否受控，Variant 是否爆炸。
- 移动端低端机是否有替代材质、替代特效和画质分级。
- 美术资源是否能自动校验，而不是靠人工记忆规范。
- 渲染问题是否能用工具定位到具体 Pass、材质、贴图或特效。