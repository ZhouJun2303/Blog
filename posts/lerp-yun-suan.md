---
id: zO3RAN
title: Lerp运算
createdAt: "2020-01-02 11:05:51"
updated: "2026-06-16 17:26:22"
tags:
    - 随口说
tag_ids:
    - CtJG2N
categories:
    - 编程基础
published: true
hideInList: false
feature: ""
isTop: false
---

cocos 中
```
this.mapcamra.node.x = cc.misc.lerp(this.mapcamra.node.x, targetPos.x, 0.1);
this.mapcamra.node.y = cc.misc.lerp(this.mapcamra.node.y, targetPos.y, 0.1);
```
Laya 中
```
Laya.Vector3.lerp()
```
Unity 
```
等我有空
```
理解
```
设 从spos(x,y,z) 移动到 tmpPos(x,y,z);
假设每帧移动 this.lerps = 0.05相对距离
   spos.x = spos.x + this.lerps * (tmpPos.x - spos.x);
   spos.y = spos.y + this.lerps * (tmpPos.y - spos.y);
   spos.z = spos.z + this.lerps * (tmpPos.z - spos.z);
   永远追不上 
```
————————————————
版权声明：本文为CSDN博主「长胖是个梦想」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
[原文链接](https://blog.csdn.net/qq_33569137/article/details/110954574)