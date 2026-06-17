---
id: nlaJfF
title: Unity Spine融合动画
createdAt: "2023-03-02 09:25:09"
updated: "2026-06-17 10:11:00"
tags:
    - Spine
tag_ids:
    - YR4Yni
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

## 解决需求
边走路边砍人，边走路边挥手
## 单层动画播放
```
  skeletonAnimation.AnimationState.SetAnimation(0, animationName, loop);
```
## 多层融合
## Unity导入Spine 动画后，在Unity端导出Animation Referance Assets
![](/post-images/1677721091327.jpg)
## 代码中使用
```
//Step1: 加载并缓存 AnimationReferenceAsset 文件
 AnimationReferenceAsset asset = LoaderCtrl.Instance.Load<AnimationReferenceAsset>(path) as AnimationReferenceAsset;
            CachedAnimationReferenceAsset.Add(type, asset);
//Step2: 播放的时候使用不同的trackIndex
 CachedSkeletonAnimation.AnimationState.SetAnimation(0, SpineAssetLoaderHelper.GetAnimationReferenceAssetByType(AnimationReferenceType.TankMove), true);
                CachedSkeletonAnimation.AnimationState.SetAnimation(1, SpineAssetLoaderHelper.GetAnimationReferenceAssetByType(AnimationReferenceType.TankAttrack), false);
   
```