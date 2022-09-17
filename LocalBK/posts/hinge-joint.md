---
title: 'hinge joint'
date: 2021-04-29 13:58:01
tags: [Unity,Physics]
published: true
hideInList: false
feature: 
isTop: false
---
[文档](https://docs.unity.cn/cn/2019.4/Manual/class-HingeJoint.html)
- hinge joint 须配合 rigidbody 使用
- 属性中的 spring  和 motor 不能同时使用，会导致意想不到的问题
- 配合rigidbody 中的mass 属性需要和主角的重量考虑
    - 在 rockCrawling中
    - car mass 500 hinge joint 25
- car body
- car wheel
![](https://zhoujun2303.github.io/post-images/1659765712852.jpg)
- hingejoint rigidbofy
![](https://zhoujun2303.github.io/post-images/1659765716689.jpg)
- hinge joint
![](https://zhoujun2303.github.io/post-images/1659765720978.jpg)
