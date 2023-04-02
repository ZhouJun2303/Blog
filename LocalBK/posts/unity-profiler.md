---
title: 'Unity Profiler'
date: 2023-03-25 18:08:02
tags: [UnityEditor]
published: true
hideInList: false
feature: 
isTop: false
---
## Stats面板
![](https://zhoujun2303.github.io/post-images/1680420126719.jpg)
+ Render thread 渲染线程，渲染一帧需要多少ms
+ Batches 批次，需要分几个批次提交给GPU
+ Saved by batching  有多少物体是同一批次提交给GPU（合批数量）
+ Tris: 三角形数（面数）
+ Verts:顶点数
+ Screen：屏幕分辨率大小，越大内存消耗越高
+ SetPassCalls 一次完整的渲染流程切换Shader的次数
+ Shadow casters 阴影开销
+ Visible skinned meshes: 可见骨骼meshs数量，可见蒙皮骨骼

## Profiler
[Up主讲解](https://www.bilibili.com/video/BV1Rd4y1q7jt/?spm_id_from=333.788.top_right_bar_window_history.content.click&vd_source=6f81433b8f1dda2a8d9fd1f770a72ef3)
Profiler(Standalone Process) 单独开启一个线程进行分析，对现有游戏影响较小
![](https://zhoujun2303.github.io/post-images/1680423428267.jpg)
使用一个循环来伪造有问题的代码
```
using System.Collections;
using System.Collections.Generic;
using System.Text;
using Unity.Profiling;
using UnityEngine;
using UnityEngine.Profiling;

public class ProfilerTest : MonoBehaviour
{
    // Start is called before the first frame update
    private int _loopCount = 50000;
    private StringBuilder _stringBuilder = new StringBuilder();
    void Start()
    {
        ProfilerMarker test1 = new ProfilerMarker("Test1");
        test1.Begin();
        //test1
        for (int i = 0; i < _loopCount; i++)
        {
            Debug.Log(i+"Test");
        }
        test1.End();
        //
        Profiler.BeginSample("TTT");
        Profiler.EndSample();
        //test2
        StartCoroutine(DelayShowLoop());
    }

    // Update is called once per frame
    void Update()
    {
       
    }

    IEnumerator DelayShowLoop()
    {
       for(int i = 0; i < 100000; i++)
        {
            yield return new WaitForFixedUpdate();
            _stringBuilder.Clear();
            _stringBuilder.Append(i);
            Debug.Log($"{_stringBuilder}");
        }
    }
}

```
+ 通过Hierarchy面板可以观察到在游戏开始的时候 Scripts处于异常状态，因为在一帧内做了50000次循环
+ 通过``ProfilerMarker``的``Begin``和``End`` 来定位有问题的代码开销
+ 在Profiler Start看到自定义的ProfilerMarker Test1占用了87.2%的开销，其中最耗内存的是`` LogStringToConsole``
+ 在协程中的打印看到几乎没有什么波动
## 真机调试定位
+ 通过打出Debug包进行观察，在莫个时候非常卡的时候，可以快速定位或者录制
+ 一般定位出某一时间段波动幅度非常到，如果是Script颜色占比非常高，大概率是莫个方法性能开销
+ 如果是Rendering 则要考虑，同屏渲染是否开销过大，或者某个物体定点面数是否过于精细