---
id: uC3gHM
title: Physics.Raycast （LayerMask 参数避坑）
createdAt: "2021-10-29 14:13:53"
updated: "2026-06-16 17:26:22"
tags:
    - Physics
    - Unity
tag_ids:
    - vjxojo
    - FjODty
categories:
    - Unity
published: true
hideInList: false
feature: ""
isTop: false
---

```
LayerMask mask1 = 1 << (LayerMask.NameToLayer("Default"));//
LayerMask mask2 = 1 << (LayerMask.NameToLayer("Monster"));

//检测 Mask1 和 Mask2
if (Physics.Raycast(ray, out hit, 50, mask1 | mask2))
//除了Mask1 其他层都检测
if (Physics.Raycast(ray, out hit, 50, ~mask1 ))
//打开所有的层
~(1 << 0) 
```