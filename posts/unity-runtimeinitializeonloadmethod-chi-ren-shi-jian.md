---
id: rphcSC
title: Unity RuntimeInitializeOnLoadMethod 吃人事件
createdAt: "2023-03-14 15:16:17"
updated: "2026-06-16 17:26:22"
tags:
    - UnityEngine
tag_ids:
    - UNR80K
categories:
    - Unity
published: true
hideInList: false
feature: ""
isTop: false
---

## 问题

使用 RuntimeInitializeOnLoadMethod 进行自动初始化一个常驻节点并添加一个挂载一个脚本
```
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
static void Init()
{
    if (Instance == null)
    {
        Instance = EventGameObject.GetOrAddComponent<StoreGiveCardEventCenter>();
    }
}
```
在初始化Awake 注册了事件，在PC 能正常监听事件，在Android真机测试没有事件触发

## 测试解决方案
经过Debug 测试

### 在应用程序注册之后
```
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]

protected virtual void Awake()
{
    m_binder.Init(this);
    Debug.Log("Event Test  Init " + gameObject.name + "  " + this.GetType());
}

protected virtual void OnDestroy()
{
    m_binder.Dispose();
    Debug.Log("Event Test  Dispose " + gameObject.name + "  " + this.GetType());
}
```
真机实测
```
2023-03-10 15:15:42.611 7303-7412/com.hg.heromaking D/sdk5Events: logEvent failed eventsTracker doesn't exist
2023-03-10 15:15:42.669 7303-7303/com.hg.heromaking D/sdk5Events: logEvent failed eventsTracker doesn't exist
2023-03-10 15:15:42.776 7303-7303/com.hg.heromaking D/sdk5Events: logEvent failed eventsTracker doesn't exist
2023-03-10 15:15:42.776 7303-7303/com.hg.heromaking D/sdk5Events: logEvent failed eventsTracker doesn't exist
2023-03-10 15:15:42.915 7303-7366/com.hg.heromaking I/Unity: Event Test  Init GameEventCenter  StoreGiveCardEventCenter
    UnityEngine.Logger:Log(LogType, Object)
    UnityEngine.GameObject:AddComponent()
    StoreGiveCardEventCenter:Init()
2023-03-10 15:15:43.525 7303-7528/com.hg.heromaking D/sdk5Events: logEvent failed eventsTracker doesn't exist
2023-03-10 15:15:45.050 7303-7366/com.hg.heromaking I/Unity: Event Test  Dispose GameEventCenter  StoreGiveCardEventCenter
    UnityEngine.Logger:Log(LogType, Object)
```
Event Test  Dispose 调用的销毁 离谱！分析的原因可能现在场景都没有，节点没处挂载。
### 在场景加载之后
```
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]

一切正常
``` 

### 直接挂载场景中的Awake 和 这个RuntimeInitializeOnLoadMethod Awake
## Unity 编辑器
+ [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
+ 直接挂载在场景中的Awake
+ [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
## Android 平台
+ 同编辑器平台