---
id: Afn2yh
title: Strip Engine Code
createdAt: "2022-06-11 15:04:55"
updated: "2026-06-17 10:11:00"
tags:
    - Unity
tag_ids:
    - FjODty
categories:
    - 安全与逆向
category_ids:
    - 35S97K
published: true
hideInList: false
feature: ""
isTop: false
---

Strip Engine Code

![](/post-images/youdao-strip-engine-code-01.png)

[link.xml](/post-images/youdao-strip-engine-code-attachment-01-link.xml)

```xml
<linker>

        <assembly fullname="UnityEngine">

                <type fullname="UnityEngine.AnimationClip" preserve="all"/>

                <type fullname="UnityEngine.SkinnedMeshRenderer" preserve="all"/>

                <type fullname="UnityEngine.Collider" preserve="all"/>

                <type fullname="UnityEngine.BoxCollider" preserve="all"/>

                <type fullname="UnityEngine.Avatar" preserve="all"/>

                <type fullname="UnityEngine.ParticleSystem" preserve="all"/>

                <type fullname="UnityEngine.ParticleSystemRenderer" preserve="all"/>

                <type fullname="UnityEngine.TrailRenderer" preserve="all"/>

        </assembly>

        <assembly fullname="Assembly-CSharp" preserve="all">

                <type fullname="UnityGameFramework" preserve="all"/>

                <type fullname="GameFramework" preserve="all"/>

                <type fullname="MLGF" preserve="all"/>

                <type fullname="MLSpace" preserve="all"/>

        </assembly>

</linker>
```

如果游戏不正常，在安卓中包错或者其他问题

如

    粒子不显示

        <type fullname="UnityEngine.ParticleSystem" preserve="all"/>

        <type fullname="UnityEngine.ParticleSystemRenderer" preserve="all"/>

    碰撞不触发等

        <type fullname="UnityEngine.BoxCollider" preserve="all"/>

Unity 官方ID 查阅 https://docs.unity3d.com/Manual/ClassIDReference.html
