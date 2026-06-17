---
id: aSEE9o
title: 'BUG #endif'
createdAt: "2022-06-13 15:07:52"
updated: "2026-06-16 17:26:22"
tags:
    - Unity
    - Bug
tag_ids:
    - FjODty
    - T3SmZT
categories:
    - Unity
published: true
hideInList: false
feature: ""
isTop: false
---

- #if (UNITY_IOS || UNITY_ANDROID) #endif
正确写法
```
  private string GetABTestConfig(string key, string def)
        {
            string va = def;
#if UNITY_EDITOR
            return va;
#endif
#if (UNITY_IOS || UNITY_ANDROID)
            va = GameAnalytics.GetRemoteConfigsValueAsString(key, def);
            return va;
#endif
        }
```
错误写法
```
  private string GetABTestConfig(string key, string def)
        {
            string va = def;
#if UNITY_EDITOR
            return va;
#endif
#if (UNITY_IOS || UNITY_ANDROID)
            va = GameAnalytics.GetRemoteConfigsValueAsString(key, def);
            return va;
        }
#endif
```
错误写法在Visual studio上没有问题，但是在vsCode 上会存在
```
Assets\GameMain\Scripts\Manager\ABTestHelper.cs(125,2): error CS1513: } expected
```
离谱！