---
title: 'BUG #endif'
date: 2022-06-13 15:07:52
tags: [Unity,Bug]
published: true
hideInList: false
feature: /post-images/bug-endif.png
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
