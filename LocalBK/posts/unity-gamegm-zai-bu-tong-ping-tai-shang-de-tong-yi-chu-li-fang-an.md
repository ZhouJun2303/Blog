---
title: 'Unity GameGM 在不同平台上的统一处理方案'
date: 2023-07-20 15:57:18
tags: []
published: true
hideInList: false
feature: 
isTop: false
---
## 设计思路 利用反射拿到自定一的特性值，在不同平台上渲染的方案
## code
### ScriptableObject 文件
```
[GUIColor("@Color.red")]
[GameGMRunTimeAttribute("设置版本号", true, true)]
[Button("设置版本号", ButtonSizes.Medium)]
[FoldoutGroup("通用功能")]
public void SetTestGameVersion()
{
    if (!Application.isPlaying) return;
    AdsCtrl.Instance.TestGameVersion = TempValue;
}
```
### UnityEditor的展示
实现基于Odin 的 ``Button`` 和 ``FoldoutGroup`` 特性在编辑器面板上展示.asset显示
Odin 的使用可参考 [Odin Inspector](https://zhoujun2303.github.io/post/odin-inspector/);
### 真机平台如何使用
#### 必要知识 [反射](https://zhoujun2303.github.io/post/unity-fan-she-reflection/)
#### GameGMRunTimeAttribute
```
using System;
using System.Collections;
using System.Collections.Generic;
using System.Reflection;
using UnityEngine;


[AttributeUsage(AttributeTargets.All, AllowMultiple = false, Inherited = true)]
public class GameGMRunTimeAttribute : Attribute
{
    /// <summary>
    /// 作用域
    /// </summary>
    public static readonly BindingFlags EffectFlags = BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static | BindingFlags.Instance;

    /// <summary>
    /// 显示方法名
    /// </summary>
    public string FunName { private set; get; }

    /// <summary>
    /// 是否使用参数
    /// </summary>
    public bool UseParameter { private set; get; }

    /// <summary>
    /// 是否在移动端展示
    /// </summary>
    public bool HideInMobile { private set; get; }

    /// <summary>
    /// GM runtime 特性
    /// </summary>
    /// <param name="funName"></param>
    public GameGMRunTimeAttribute(string funName)
    {
        FunName = funName;
    }

    /// <summary>
    /// 在真机状态显示的方法名
    /// </summary>
    /// <param name="funName">方法名</param>
    /// <param name="useParameter">是否需要使用参数配合</param>
    public GameGMRunTimeAttribute(string funName, bool useParameter)
    {
        FunName = funName;
        UseParameter = useParameter;
    }

    /// <summary>
    ///  GM runtime 特性
    /// </summary>
    /// <param name="funName">方法名</param>
    /// <param name="useParameter">是否需要使用参数配合</param>
    /// <param name="hideInMobile">真机隐藏按钮</param>
    public GameGMRunTimeAttribute(string funName, bool useParameter, bool hideInMobile)
    {
        FunName = funName;
        UseParameter = useParameter;
        HideInMobile = hideInMobile;
    }
}
```
#### 核心代码
```
private void Init()
{
    if (GameGMSettingSo == null) return;
    Type t = typeof(GameGMSettingSo);
    _methods = t.GetMethods(BindingFlags.NonPublic | BindingFlags.Public | BindingFlags.Static | BindingFlags.Instance);
    for (int i = 0; i < _methods.Length; i++)
    {
        var attribute = _methods[i].GetCustomAttribute<GameGMRunTimeAttribute>();
        if (null == attribute) continue;
        if (attribute.HideInMobile) continue;
        string funcName = attribute.FunName;
        GameObject go = GameObject.Instantiate(_tempButton.gameObject, _GMNode);
        RunTimeGMItem runTimeGMItem = new RunTimeGMItem();
        runTimeGMItem.OnShowNode(go, i, funcName, attribute.UseParameter, OnButtonClick);
    }
}
```

