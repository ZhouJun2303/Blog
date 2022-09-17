---
title: 'Attributes'
date: 2022-03-02 14:31:49
tags: [Unity,UnityEngine]
published: true
hideInList: false
feature: 
isTop: false
---
```
[AddComponentMenu("Transform/AddComponentMenuT", 0)]
可在Component里面快速增加脚本

[AssemblyIsEditorAssembly]
视为编辑器类，讲道理不会被打包

[ColorUsage(true, true)]
 public Color Corlor;
 作用于 Color 类型变量上，使其可在取色面板配置显示 Alpha 和采用 HDR 标准

[ContextMenu("WarlG Context Menu")]
void CustomContext()
{
  Debug.Log("WarlGContext");
}
作用于非静态方法上，在脚本 Inspector 的 context menu
上添加额外操作（Inspector 上脚本右击菜单）

[ContextMenuItem("ResetString", "ResetSampleString")]
public string SampleString = "";
void ResetSampleString()
{
      SampleString = "WarlGSampleString";
}
作用于变量上，给作用的变量在Inspector上添加右键菜单方法

[CreateAssetMenu(fileName = "WarlGAssetSample.asset", menuName = "WarlGAssetMenu/WarlGAssetItem")]
public class WarlGAssetMenuSample : ScriptableObject
{
    public string assetName = "WarlGAssetSample";
}
作用于可脚本化的类上，自动列入Assets/Create 的子菜单中，添加创建".asset"文件的快捷路径

[DisallowMultipleComponent]
作用于类上，禁止 GameObject 添加多个相同类型组件

 [ExecuteAlways]
    public class ExecuteAlwaysT : MonoBehaviour
    {
        private void Update()
        {
            Debug.Log("1");
        }
    }
无论是编辑器模式还是运行模式都会执行
[ExecuteInEditMode]    
在编辑器模式下执行同上

[Header("WarlGHeader")] 
public string header;
作用于变量上，给变量在 Inspector 中添加标题头

[HelpURL("https://warl-g.github.io/")]
public class WarlGAttributeSample : MonoBehaviour
{
}
作用于类上，为类添加说明链接，可在 Inspector 脚本组件上的"?"标志跳转

[Min(10)]
public int minValue;
作用于 int 和 float 约束变量最小值

[MultilineAttribute(30)]
        public string hhhh = "@向量（Vector3）在虚拟的游戏世界中，3D数学决定了游戏，+" +
            "如何计算和模拟出开发者以及玩家看到的每一帧画面。学习基础的3D数学知识可以帮主用户对游戏引擎产生更深刻的了解。" +
            " 向量定义：既有大小又有方向的量叫做向量。在空间中，向量用一段有方向的线段来表示。应用十分广泛，可用于描述具有大小和" +
            "方向两个属性的物理量，例如物体运动的速度、加速度、摄像机观察方向、刚体受到的力等都是向量。因此向量是物理" +
            "动画、三维图形的基础。 与向量相对的量成为标量:即只有大小没有方向的量。例如物体移动中的平均速率、路程。 " +
            "模：向量的长度标准化（Normalizing）：保持方向不变，将向量的长度变为1." +
            "单位向量：长度为1的向量。 零向量：各分量均为0的向量向量运算——加减：" +
            "向量的加法（减法）为各个分量分别相加（相减）。在物理上可以用来计算两个里的合力，或者几个速度份量的叠加。 ";
作用于 string ，使 string 在 Inspector 显示多行文本区
30 行数
Tips : string太长可以前面+ @ 之后回车可随意换行

 [RequireComponent(typeof(Rigidbody))]
 作用于类， 在挂载该脚本同时会自动挂载该脚本依赖的组件，且删除时弹出警告

  [RuntimeInitializeOnLoadMethodAttribute(RuntimeInitializeLoadType.AfterAssembliesLoaded)]
        static void RuntimeInitializeOnLoadMethodAttributeTT()
        {
            Debug.Log("RuntimeInitializeOnLoadMethodAttribute");
        }
作用于静态方法，允许运行时情况下加载游戏后，无需用户行为即可初始化运行时类方法；

[SelectionBaseAttribute]
作用于类，使被挂载的 GameObject 优先被选中；如当前 GameObject 为子物体，当点击该物体时会默认选中父物体，
在该特性脚本挂载到子物体后会优先选中子物体

[InitializeOnEnterPlayModeAttribute]
作用于静态方法，使编辑器类方法在进入 Play Mode 时初始化
```