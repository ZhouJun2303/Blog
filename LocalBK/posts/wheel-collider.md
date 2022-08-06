---
title: 'wheel collider'
date: 2021-04-29 14:02:46
tags: [Physics,Unity]
published: true
hideInList: false
feature: /post-images/wheel-collider.png
isTop: false
---
- mass 质量
- radius 半径
- wheelDampingRate 车轮阻尼率
- suspension distance 悬挂距离
- forceAppPointDistance   着力点距离
- suspension spring 
    - Spring  越大到达目标位置约快
    - Damper 越大弹簧移动越慢
    - targetPosition 1max延伸悬挂 0 max压缩悬挂
- forwardFriction 向前的摩擦力
    - extremum slip 什么情况达到起步
    - extremum value 起步摩擦力生效程度
    - asymptote slip 什么时候达到匀速
    - asymptote value 匀速时摩擦生效程度
    - stiffness 0 打滑，越大越强 （有限制性）
- sidewatsFriction 同上参考
    - up
    - .
    - .
    - .
    - .
![](https://zhoujun2303.github.io/post-images/1659765876893.jpg)
