---
id: vcgRwO
title: Laya 常见问题
createdAt: "2020-07-10 14:39:23"
updated: "2026-06-17 10:11:00"
tags:
    - Laya
tag_ids:
    - 1UVSeu
categories:
    - Cocos / Laya
category_ids:
    - Lwedfg
published: true
hideInList: false
feature: ""
isTop: false
---

```
高动态光渲染 低端手机不支持
ml.camera._enableHDR = false
```
```
摄像机自动裁剪  默认为 True
ml.camera.useOcclusionCulling = true;
```
```
静态物体合批
Laya.StaticBatchManager.combine(this.owner);
```