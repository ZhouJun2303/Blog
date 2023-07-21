---
title: 'Unity Docs Key Words'
date: 2023-07-19 20:22:44
tags: [keyword,UnityEngine,UnityEditor]
published: true
hideInList: false
feature: 
isTop: true
---
# 见识少的人才会极其自信
[官方文档2020.3.33](https://docs.unity.cn/cn/2020.3/Manual/VisualStudioIntegration.html)
## Unity Editor
### 预设的覆盖，预设的变体
### IPreprocessBuildWithReport 打包构建前的接口
```
using UnityEditor;
using UnityEngine;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;

public class OnPreBuildProcessor : IPreprocessBuildWithReport
{
    public int callbackOrder { get { return 0; } }

    public void OnPreprocessBuild(BuildReport report)
    {
        // 在打包之前执行的操作
        Debug.Log("Pre-processing build...");
        // 可以在这里添加任何你需要在打包之前执行的操作
        //todo 加入构建Scene
        //导表
        ExportExcel.ExportExcels();
    }
}
```
### ProjectSetting/Editor/Numbering Scheme/Game Object Naming 
- 编辑器快速Ctrl + D 创建Object 的名字设置
### Preferences/General/Auto Refresh+Script Changes While Playing 
- 可以结合使用，在制作UI界面时，在VS和Unity端切换时，Unity不会自动编译，节省时间
但需要手动编译，快捷键 Ctrl + R (Unity 使用的是自己的C#编译器，实际上我们在代码时Visual Studio 已经在预编译，两者是独立的，既Unity端只有写完当前所有代码才需要编辑，实际上Auto Refresh 是可以关闭，改为手动关闭更快捷)
### ProjectSetting/Script Execution Order 
- 此设置窗口中指定的执行顺序不会影响以 RuntimeInitializeOnLoadMethod 属性标记的函数的顺序
### RuntimeInitializeOnLoadMethodAttribute
- 允许在运行时加载游戏时不通过用户操作 初始化一个运行时类方法。
- 游戏加载后，将调用标记为 [RuntimeInitializeOnLoadMethod] 的 方法。这是在调用 Awake 方法后进行的。
- 注意：标记为 [RuntimeInitializeOnLoadMethod] 的方法的执行顺序是不确定的
- [RuntimeInitializeOnLoadMethod 吃人事件](https://zhoujun2303.github.io/post/unity-runtimeinitializeonloadmethod-chi-ren-shi-jian/)
### RenderDoc  
- todo 后续应该单独研究
### [UnityProfiler](https://zhoujun2303.github.io/post/unity-profiler/)
### [Unity的垃圾回收](https://docs.unity.cn/cn/2020.3/Manual/performance-garbage-collector.html)
### Unity中的优化
#### 资源优化
- 使用AssetPostprocessor对导入的一些资源进行特殊规则设定
```
预处理资源导入器调用：
OnPreprocessAsset
OnPreprocessAnimation
OnPreprocessAudio
OnPreprocessModel
OnPreprocessSpeedTree
OnPreprocessTexture
后处理资源导入器调用：

OnAssignMaterialModel
OnPostprocessAnimation
OnPostprocessAssetbundleNameChanged
OnPostprocessAudio
OnPostprocessCubemap
OnPostprocessGameObjectWithAnimatedUserProperties
OnPostprocessGameObjectWithUserProperties
OnPostprocessMaterial
OnPostprocessMeshHierarchy
OnPostprocessModel
OnPostprocessSpeedTree
OnPostprocessSprites
OnPostprocessTexture
所有导入完成后触发的最后一个后处理回调是 OnPostprocessAllAssets。
```
#### [纹理方面的优化](https://zhoujun2303.github.io/post/wen-li-nei-cun-you-hua/)
#### [字符串和文本的优化及其他官方优化](https://docs.unity.cn/cn/current/Manual/BestPracticeUnderstandingPerformanceInUnity5.html)可以直接看官方文档
### 特殊文件夹命名
- Assets 资源主文件夹
- Editor 编辑器脚本，可以存在多个，构建之后里面一切资源都会剥离
- Editor Default Resources (Editor 脚本可以使用通过 EditorGUIUtility.Load 函数按需加载的资源文件。只能有一个 Editor Default Resources 文件夹，且必须将其放在项目的根目录中；直接位于 Assets 文件夹中。)
- Gizmos Gizmos.DrawIcon 函数在场景中放置一个图标
  ```
  void OnDrawGizmos()
    {
        // Draws the Light bulb icon at position of the object.
        // Because we draw it inside OnDrawGizmos the icon is also pickable
        // in the scene view.

        Gizmos.DrawIcon(transform.position, "Light Gizmo.tiff", true);
    }
  ```
- Resources 动态加载的文件，可以有多个，但最好一个，如果位于Editor 中，则会从构建中剥离
- Standard Assets Unity官方标准资源包
- StreamingAssets 只读不写的文件夹，且打包之后资源文件保持原始格式，不会被压缩；脚本文件则不会参与编译
### AssetBundle 
- todo详细文档
- 先说几个注意点吧
    - ab包打包的时候尽量相互依赖的贴图，材质球，等打在同一个ab包里面，可以减少启动耗时
    - 举个例子，新手可能在游戏的前30会出现，30分钟之后就没有了，如果把ab包的资源混合在其他包里面，启动的时候通过依赖关系，所有的ab可能全都要加载，而不是用到才加载。
## UnityEngine
### Unity的协程（满足一些幻想）
- [批处理模式和内置协程兼容性](https://docs.unity.cn/cn/2020.3/Manual/CLIBatchmodeCoroutines.html)
- WaitUntil 非常有用
