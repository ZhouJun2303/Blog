---
title: 'Unity 开发高级/资深 08：性能、内存与包体'
date: 2026-06-10 21:58:00
tags: [Unity,开发高级/资深,性能优化,内存优化]
published: true
hideInList: true
feature: 
isTop: false
---
[返回总览](https://zhoujun2303.github.io/post/unity-senior-developer-skills/)

![Unity 开发高级/资深学习路线](https://zhoujun2303.github.io/post-images/unity-senior-developer-learning-roadmap.svg)

性能优化不是“感觉哪里慢就改哪里”，而是用数据证明瓶颈、用工具定位原因、用对比验证收益、用规则防止回退。开发高级/资深需要建立一套能被团队重复执行的性能流程。

## 性能优化基本原则

- 先测量再优化：没有 Profiler、真机数据和复现场景，不做大规模改动。
- 先分清瓶颈：先判断 CPU、GPU、内存、IO、网络、Shader 编译还是资源实例化。
- 先解决主链路：启动、热更、登录、进主城、进战斗、打开高频 UI、切场景。
- 先优化高频问题：每帧调用、同屏大量对象、频繁打开 UI、频繁加载资源。
- 先做低风险收益：减少 GC、降频 Update、拆 Canvas、合并资源、裁剪动画。
- 保留对比证据：优化前后要有相同机型、相同场景、相同操作路径的数据。
- 建立回归门槛：性能预算、包体预算、内存预算进入提测和发版 Checklist。

## 推荐性能预算

不同项目预算会变，下面是开发高级/资深制定项目预算时的参考起点。

| 场景 | 低端移动设备 | 中端移动设备 | 高端移动设备/PC | 说明 |
| --- | --- | --- | --- | --- |
| 目标帧率 | 30 FPS | 30 或 45 FPS | 60 FPS 或更高 | 项目先定目标，再倒推预算 |
| 单帧总预算 | 33.3 ms | 22.2 到 33.3 ms | 16.6 ms | 60 FPS 下 CPU+GPU 都要进 16.6 ms |
| 主线程 CPU | 12 到 18 ms | 8 到 12 ms | 5 到 8 ms | 脚本、动画、物理、UI 都在抢 |
| 渲染线程 | 4 到 8 ms | 3 到 6 ms | 2 到 4 ms | SetPass、DrawCall、提交命令 |
| GPU | 12 到 20 ms | 8 到 14 ms | 5 到 10 ms | 阴影、透明、后处理、分辨率 |
| 每帧 GC Alloc | 0 B | 0 B | 0 B | 允许加载阶段分配，不允许战斗每帧分配 |
| 主城内存峰值 | 1.0 到 1.5 GB | 1.5 到 2.5 GB | 按平台定 | 需要留系统、SDK、后台余量 |
| 战斗加载 | 5 到 15 秒 | 3 到 8 秒 | 1 到 5 秒 | 受网络、磁盘、资源体积影响 |
| UI 打开耗时 | 100 到 300 ms | 50 到 200 ms | 50 到 120 ms | 超过 300 ms 应有 Loading 或骨架屏 |

预算不能只写在文档里，应该进入自动化采集和版本对比。开发高级/资深至少要保证“性能变差时能被发现”。

## 标准排查流程

1. 固定复现场景：记录机型、系统、Unity 版本、包版本、画质、账号、地图、操作步骤。
2. 确认构建类型：线上问题优先用 Release 或接近 Release 的包复现，Development Build 只用于定位。
3. 采集基线数据：记录平均 FPS、最低 FPS、主线程、渲染线程、GPU、GC、内存峰值。
4. 判断瓶颈归属：CPU 高看 Profiler Timeline，GPU 高看 Frame Debugger/RenderDoc，内存高看 Memory Profiler。
5. 缩小范围：关 UI、关特效、关阴影、减怪物、减玩家、切画质、切分辨率，逐项验证。
6. 修改最小闭环：每次只改一个主要变量，避免不知道收益来自哪里。
7. 对比验证：同机型、同账号、同路径至少采样 3 次，取平均和最差帧。
8. 固化规则：把问题变成资源规范、代码规范、导入规则、CI 检查或线上告警。

## 性能采样规范

- 真机优先：编辑器数据只用于初筛，最终结论必须来自目标平台真机。
- 避免 Deep Profile 常驻：Deep Profile 会显著改变性能，只用于短时间定位函数级问题。
- 固定操作脚本：主城绕行、打开背包、进入战斗、释放技能，用同一套路径采样。
- 采样时间足够：稳定场景至少 60 秒，战斗至少一局或固定 3000 帧。
- 记录峰值和均值：平均 FPS 好看不代表不卡，最低帧和卡顿次数更关键。
- 记录资源版本：性能回退经常来自资源、配置、Shader Variant，而不是代码。

<a id="performance"></a>
## 性能优化

### 需要掌握的工具

- Unity Profiler：CPU、Rendering、Physics、Animation、UI、Timeline 分析。
- Profile Analyzer：多帧采样、多版本对比和性能回归分析。
- Frame Debugger：查看 Draw Call、Pass、Batch、SetPass 和材质切换。
- RenderDoc：分析 GPU Pass、纹理、Buffer、Overdraw 和渲染结果。
- Android Studio Profiler、Xcode Instruments：平台级 CPU、GPU、线程、内存和功耗分析。
- Xcode GPU Frame Capture、Android GPU Inspector：定位移动端 GPU 瓶颈。
- 自研性能面板：线上 FPS、卡顿、内存、同屏数量、场景耗时和设备信息采样。

### CPU 优化

CPU 优化先看主线程是否超预算，再看渲染线程、Job Worker、加载线程是否阻塞。常见症状是 `PlayerLoop`、`Scripts`、`Canvas.SendWillRenderCanvases`、`Animator.Update`、`Physics.Simulate`、`GC.Collect` 过高。

#### Update 治理

- 禁止大量空 Update：空 Update 也有调度成本，几千个组件会明显拖慢。
- 高频逻辑集中调度：用 Tick 管理器按 1 帧、3 帧、10 帧、1 秒分组。
- 远距离对象降频：屏外 NPC、远处怪物、远处特效不需要每帧刷新。
- 可事件驱动就不要轮询：背包红点、任务状态、活动入口优先用数据变更事件触发。
- 暂停不可见逻辑：关闭 UI、隐藏场景块、离开战斗后停止对应 Tick。

```csharp
public interface ITickable
{
    void Tick(float deltaTime);
}

public sealed class TickGroup
{
    private readonly List<ITickable> _items = new();
    private readonly int _interval;
    private int _frame;

    public TickGroup(int interval)
    {
        _interval = Math.Max(1, interval);
    }

    public void Add(ITickable item)
    {
        if (!_items.Contains(item))
        {
            _items.Add(item);
        }
    }

    public void Remove(ITickable item)
    {
        _items.Remove(item);
    }

    public void Update(float deltaTime)
    {
        _frame++;
        if (_frame % _interval != 0)
        {
            return;
        }

        for (int i = _items.Count - 1; i >= 0; i--)
        {
            _items[i].Tick(deltaTime * _interval);
        }
    }
}
```

#### GC 与托管分配

- 战斗、主城、滚动列表中每帧 GC Alloc 应为 0 B。
- 避免每帧 LINQ、闭包、字符串拼接、装箱、`new List<T>()`。
- 日志在 Release 包要分级关闭，字符串插值会产生分配。
- 物理查询使用 NonAlloc API，缓存数组，超出容量时记录告警。
- UI 文本频繁刷新时先判断值是否变化，不要每帧赋值。

```csharp
private readonly Collider[] _hits = new Collider[64];

public int QueryEnemies(Vector3 center, float radius, LayerMask mask)
{
    int count = Physics.OverlapSphereNonAlloc(center, radius, _hits, mask);
    for (int i = 0; i < count; i++)
    {
        // 处理命中目标
    }

    if (count == _hits.Length)
    {
        Debug.LogWarning("Overlap buffer is full, consider increasing capacity.");
    }

    return count;
}
```

#### 反射、序列化和查找

- `FindObjectOfType`、`GameObject.Find`、`GetComponentsInChildren` 不应出现在高频路径。
- 反射、Attribute 扫描、配置反序列化放在启动或加载阶段，并做缓存。
- JSON 解析不要在战斗中每帧执行，大配置应启动阶段或进场景阶段加载。
- 频繁访问组件时缓存引用，避免反复 `GetComponent`。
- 热更层桥接调用如果很频繁，要评估桥接成本。

#### UI CPU

- `Canvas.SendWillRenderCanvases` 高说明 Canvas Rebuild 或 Layout Rebuild 过多。
- 动态列表必须虚拟化，排行榜、背包、邮件、任务列表不能一次实例化几百项。
- 避免频繁修改 LayoutGroup 下的子节点尺寸、文本和 Active 状态。
- 动态数字、倒计时、红点建议拆到独立 Canvas 或低频刷新。
- Mask、RectMask2D、大量 Image Alpha 会增加 CPU 和 GPU 压力。

#### 动画 CPU

- 同屏 Animator 数量要有上限，远距离角色使用 Culling Mode 或低频刷新。
- 复杂 Animator Controller 要减少 Layer、Blend Tree 和无用参数。
- NPC 待机动作可以降帧或使用简单 Animation。
- 动画事件不要驱动关键逻辑唯一入口，丢帧或跳转可能漏事件。
- 骨骼数、挂点数、换装部件数需要预算。

#### 物理 CPU

- Layer Collision Matrix 要严格配置，不相关层不参与碰撞。
- 避免复杂 MeshCollider 参与动态碰撞。
- Raycast、Overlap、SphereCast 做批量和降频，不要每个对象每帧扫。
- Trigger 回调里不要做复杂逻辑，先收集事件，再统一处理。
- 物理步长和 FixedUpdate 次数要监控，卡顿时可能一帧补多次物理。

### GPU 优化

GPU 优化先判断是否 GPU Bound：如果主线程不高但帧率低，降低分辨率或 Render Scale 后明显变快，通常是 GPU 或带宽瓶颈。

#### Draw Call、SetPass 和批处理

- SetPass 比 Draw Call 更值得关注，材质和 Shader 切换会打断批处理。
- 开启 SRP Batcher 后，Shader 写法和材质属性要符合要求。
- 静态物体优先 Static Batching 或合批，但要注意内存增加。
- 大量相同物体使用 GPU Instancing，例如草、石头、子弹残影、装饰件。
- UI 图集、角色材质、场景材质要减少材质实例数量。

#### Overdraw 和透明物体

- 粒子、半透明 UI、全屏特效、雾效、玻璃、水面会造成 Overdraw。
- 大粒子贴图要裁剪透明边，不要用大面积透明图片。
- UI 弹窗背景、遮罩、模糊效果要控制层数和分辨率。
- 移动端谨慎使用多层半透明叠加和屏幕空间特效。
- 用 Scene View Overdraw、Frame Debugger、RenderDoc 验证。

#### 阴影、光照和后处理

- 低端机减少实时阴影、阴影距离、级联数量和分辨率。
- 主城可优先用烘焙光照、Light Probe、Reflection Probe。
- Bloom、AO、景深、Motion Blur、SSR 要有画质档位。
- 后处理尽量合并 Pass，避免多个全屏 Blit。
- 实时光数量要有预算，动态角色受光也要限制。

#### 分辨率和带宽

- 移动端 GPU 很多时候卡在带宽，过大的 RenderTexture、后处理和 MSAA 会放大成本。
- Render Scale、动态分辨率、半分辨率特效是常用兜底。
- 大贴图优先 ASTC/ETC2 等平台压缩格式。
- UI 大图、活动图、公告图要控制尺寸，避免 4K 资源直接上屏。

### UI 专项优化

| 问题 | 典型症状 | 具体处理 |
| --- | --- | --- |
| Canvas Rebuild 高 | 打开面板或刷新文本卡顿 | 静态和动态拆 Canvas，变化频繁的倒计时、红点独立 Canvas |
| Layout Rebuild 高 | 列表刷新掉帧 | 少用嵌套 LayoutGroup，批量刷新时先禁用 Layout 或用固定尺寸 |
| ScrollView 卡 | 背包、邮件、排行榜滚动掉帧 | 虚拟列表，只保留可见项和少量缓冲项 |
| 图集切换多 | UI Draw Call 异常高 | 同界面资源进同图集，公共图集和活动图集分开 |
| 文本刷新频繁 | GC 或 Rebuild 增加 | 值变化才刷新，倒计时按秒刷新，避免每帧设置 text |
| Mask 多 | GPU Overdraw 高 | 能不用 Mask 就不用，或改 RectMask2D，复杂遮罩减少层级 |

### 加载与卡顿优化

- 异步加载不等于不卡，资源加载完成后的 Instantiate、Awake、OnEnable 仍可能卡主线程。
- 大量对象实例化要分帧，或者提前对象池预热。
- Shader 首次编译和变体加载会造成明显卡顿，需要收集和预热。
- Addressables 加载要记录每个资源耗时、依赖下载耗时、实例化耗时。
- Loading 进度要区分下载、加载、实例化、初始化，不要只显示假进度。
- 切场景前先停输入、停网络重复请求、停旧场景 Tick，避免旧逻辑和新场景抢主线程。

```csharp
public static IEnumerator InstantiateInBatches<T>(
    IReadOnlyList<T> prefabs,
    Transform parent,
    int batchSize
) where T : UnityEngine.Object
{
    int count = 0;
    for (int i = 0; i < prefabs.Count; i++)
    {
        UnityEngine.Object.Instantiate(prefabs[i], parent);
        count++;

        if (count >= batchSize)
        {
            count = 0;
            yield return null;
        }
    }
}
```

### 性能回归监控

每个版本至少记录以下数据：

- 启动到登录界面耗时。
- 登录到主城首帧耗时。
- 主城静止 60 秒平均 FPS、最低 FPS、内存峰值。
- 主城跑动 60 秒平均 FPS、最低 FPS、卡顿次数。
- 核心战斗 1 局平均 FPS、最低 FPS、GC Alloc、内存峰值。
- 打开背包、邮件、排行榜、活动面板的耗时。
- 包体大小、首包大小、热更下载大小。
- 崩溃率、OOM 率、加载失败率。

### 可继续细分方向

- CPU、Update 和 GC 优化。
- GPU、Draw Call 和 Overdraw 优化。
- UI、动画、物理专项优化。
- 加载卡顿、Shader 预热和性能回归监控。

<a id="memory"></a>
## 内存控制

内存优化的重点不是“看到数字大就删资源”，而是区分托管堆、原生内存、显存、资源缓存和插件内存。开发高级/资深要能回答：谁占用、谁持有、何时加载、何时释放、为什么释放不掉。

### 需要掌握的工具

- Unity Memory Profiler：快照、引用链、重复资源、托管堆和原生对象。
- Unity Profiler Memory 模块：观察运行时内存趋势和 GC。
- Xcode Instruments Allocations/Leaks：分析 iOS 内存和泄漏。
- Android Studio Memory Profiler：分析 Android Java、Native 和图形内存。
- ADB、Logcat、Xcode Device Logs：查看 OOM、Low Memory 和后台切换日志。
- 资源引用链分析工具：定位资源为什么卸载不掉。

### 内存类型

| 类型 | 常见来源 | 排查重点 |
| --- | --- | --- |
| 托管堆 | C# 对象、集合、字符串、闭包 | GC Alloc、静态引用、事件未解绑 |
| 原生内存 | Texture、Mesh、AudioClip、AnimationClip、AssetBundle | 资源是否释放、引用链是否残留 |
| 显存 | 贴图、RenderTexture、FrameBuffer、阴影图 | 贴图格式、分辨率、后处理、RT 生命周期 |
| 资源缓存 | Addressables、对象池、场景常驻资源 | 引用计数、缓存策略、切场景清理 |
| 插件内存 | SDK、视频、WebView、Native 插件 | 平台日志、插件生命周期、释放 API |

### 内存快照对比方法

1. 启动后进入登录界面，采第一张快照。
2. 进入主城并稳定 30 秒，采第二张快照。
3. 打开并关闭高频 UI，比如背包、邮件、活动，采第三张快照。
4. 进入战斗并退出回主城，采第四张快照。
5. 重复步骤 3 到 4 三次，采第五张快照。
6. 对比对象数量和资源数量，如果只增不降，就查引用链。

### 常见泄漏来源

- 静态 List、Dictionary 持有场景对象或 UI 对象。
- 事件注册后没有在 OnDisable/Dispose 中解绑。
- 协程、Timer、Tween 在对象销毁后仍持有回调。
- Addressables 句柄没有 Release。
- 对象池只进不出，或者池容量没有上限。
- RenderTexture、Texture2D、Mesh 运行时创建后没有 Destroy。
- SDK、WebView、视频播放器没有正确释放 Native 资源。
- DontDestroyOnLoad 常驻对象越来越多。

### 资源内存具体优化

- 贴图：按平台使用 ASTC、ETC2、PVRTC、DXT，关闭不需要的 Read/Write。
- 模型：关闭 Read/Write，控制顶点属性，删除无用 UV、Color、Tangent。
- 动画：裁剪无用曲线，降低精度，拆分常用动作和罕见动作。
- 音频：长 BGM 使用 Streaming，短音效使用压缩或预加载。
- 字体：控制字体 Atlas 尺寸，多语言字体分包，缺字扫描。
- RenderTexture：按需创建，离开场景释放，低端机降低分辨率。
- Shader Variant：剔除无用变体，减少包体和加载内存。

### 低内存设备策略

- 进入场景前根据设备内存决定画质、贴图清晰度、同屏数量。
- 低端设备减少常驻 UI 缓存，关闭高成本后处理。
- 切场景时主动释放旧场景资源，并调用 `Resources.UnloadUnusedAssets`，但不要在战斗中频繁调用。
- 收到 iOS Memory Warning 或 Android Low Memory 时，释放可重建缓存。
- 对象池设置上限，超过上限直接销毁，避免“为了性能”吃光内存。

### 可继续细分方向

- 托管内存和 GC。
- 原生内存、显存和资源缓存。
- 泄漏定位和引用链分析。
- 低内存设备策略和平台 OOM 排查。

<a id="package-loading"></a>
## 包体与加载

包体和加载不是资源同学一个人的事。开发高级/资深需要把资源规范、Bundle 分组、热更策略、下载体验、加载流程和线上监控连起来。

### 需要掌握的工具

- Build Report Inspector：分析 Unity 构建产物和包体组成。
- Addressables Analyze 与 Build Layout Report：分析 Bundle、依赖和重复资源。
- AssetStudio：辅助查看构建产物中的资源内容和体积。
- Texture Importer、Audio Importer、Model Importer：控制贴图、音频、模型体积。
- CDN 日志和下载统计：分析资源下载失败、速度和回源问题。
- 自研包体差异工具：比较版本之间资源增量、重复资源和异常增长。

### 包体拆分策略

- 首包只放启动、登录、基础 UI、热更模块和新手必须资源。
- 主城、战斗、活动、语音、高清资源、多语言资源尽量拆成可下载包。
- 活动资源单独分组，活动结束后可以下线和清理缓存。
- 公共资源单独分组，但要避免公共包过大导致小改动牵连全量更新。
- 渠道差异资源单独分组，避免所有渠道都带无关 SDK 或图片。

### 加载流程拆解

| 阶段 | 具体工作 | 优化点 |
| --- | --- | --- |
| 检查版本 | 请求版本、清单、服务器开关 | 超时重试、错误码、灰度、回滚 |
| 下载资源 | 下载 Bundle、配置、图片、语音 | 断点续传、并发数、磁盘空间、CDN 切换 |
| 加载资源 | 解析 Bundle、加载依赖、加载 Prefab | 异步、优先级、预加载、失败重试 |
| 实例化 | Instantiate、Awake、OnEnable | 分帧、对象池、预热、减少初始化逻辑 |
| 初始化业务 | 配置绑定、网络请求、UI 刷新 | 并行化、缓存、延迟非关键逻辑 |
| 首帧展示 | 相机、UI、角色、场景可见 | 先显示关键内容，非关键资源延迟 |

### 包体压缩具体做法

- 贴图优先检查尺寸，其次检查压缩格式，最后检查是否重复。
- UI 大图和活动图按显示尺寸导入，不要用 2048 图显示 300 像素。
- 模型删除无用骨骼、BlendShape、顶点色、Tangent 和多余 UV。
- 动画关闭不需要的 Rig 数据，裁剪无用曲线和无用帧。
- 音频根据用途选择 Decompress On Load、Compressed In Memory、Streaming。
- Shader Variant 数量要进构建报告，异常增长必须追责到具体 Shader 或 Keyword。
- 多语言资源按语言分包，不要所有语言都进首包。

### 下载和磁盘问题

- 下载前检查磁盘空间，至少预留下载包、解压空间和系统余量。
- CDN 失败要有备用域名或重试策略。
- 下载清单和 Bundle 都要做 hash 校验。
- 断点续传要处理本地文件损坏、服务器清单变化和缓存过期。
- 下载失败的错误要能区分网络、磁盘、校验、权限、服务器。

### 加载卡顿具体处理

- 进场景前预加载常用 Shader、角色骨骼、UI 公共图集和音效。
- 大 Prefab 拆分：首帧必要对象先加载，装饰、远景、低优先级 NPC 延迟加载。
- 复杂 UI 面板拆成基础骨架和子模块，打开时先显示骨架。
- 场景切片：主城、活动区、室内、远景分块加载。
- 使用对象池预热高频对象，比如伤害数字、子弹、技能特效、怪物。
- 对慢资源记录加载耗时排行，按版本追踪。

### 可继续细分方向

- 首包、分包和 DLC。
- 资源压缩、贴图格式和音频格式。
- Loading 流程、异步加载和 Shader 预热。
- 下载失败、磁盘空间和边玩边下。

## 常见性能问题速查

| 症状 | 优先检查 | 常见原因 | 处理方向 |
| --- | --- | --- | --- |
| 战斗周期性卡顿 | Profiler GC Alloc、GC.Collect | 每帧分配、日志、LINQ、字符串 | 消除分配、对象池、缓存字符串 |
| 打开 UI 卡顿 | UI Profiler、Timeline | 一次实例化太多、Layout Rebuild | 虚拟列表、分帧、拆 Canvas |
| 主城帧率低 | CPU/GPU 分界、同屏数量 | NPC、玩家、动画、透明特效多 | 降频、LOD、Cull、特效降级 |
| GPU 高 | RenderDoc、Frame Debugger | 后处理、阴影、Overdraw、分辨率 | 降画质、半分辨率、减少透明 |
| 切场景黑屏久 | 加载耗时日志 | 下载、加载、实例化、初始化混在一起 | 拆阶段、预加载、分帧实例化 |
| 内存只涨不降 | Memory Profiler Diff | 静态引用、事件、Addressables 未 Release | 查引用链、解绑、释放句柄 |
| 包体突然变大 | Build Report Diff | 贴图、音频、Shader Variant、重复资源 | 查增量、压缩、拆包、剔除 |
| 低端机 OOM | 平台日志、Memory Snapshot | 贴图过大、常驻缓存、RT 过多 | 降清晰度、释放缓存、降低 RT |

## 性能优化交付物

开发高级/资深做性能优化时，建议最终产出这些东西：

- 性能预算表：按平台、场景、画质列出 FPS、CPU、GPU、内存、加载、包体目标。
- 性能采样脚本：固定操作路径，能重复采集主城、战斗、UI、加载数据。
- 性能对比报告：优化前后数据、机型、版本、截图、Profiler 文件。
- 资源规范：贴图、模型、动画、音频、Shader Variant、图集、特效预算。
- 线上性能看板：FPS、卡顿、OOM、加载失败、下载失败、机型分布。
- 回归 Checklist：提测和发版前必须检查的性能项目。
- 降级策略：低端设备画质、同屏数量、特效、后处理、分辨率的降级规则。

## 发版前性能 Checklist

- Release 包在目标低端机完成主城、战斗、UI、加载采样。
- 主城和战斗每帧 GC Alloc 为 0 B，加载阶段分配有解释。
- 主线程、渲染线程、GPU 都在预算内，没有单项长期超标。
- 打开高频 UI 不超过预算，滚动列表没有明显掉帧。
- 首包、热更包、活动包体积有版本对比，没有异常增长。
- Memory Profiler 对比没有明显泄漏，重复进出战斗内存能回落。
- Shader Variant 数量、预热耗时和首次卡顿有记录。
- 低端机画质降级生效，关闭高成本特效后帧率有明显改善。
- 线上性能埋点、崩溃、OOM、加载失败、下载失败都能查询。
- 性能风险和未解决项已经写进版本风险清单。

