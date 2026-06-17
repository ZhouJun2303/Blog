---
id: 3GjgPK
title: 安卓常见问题
createdAt: "2021-06-16 14:48:34"
updated: "2026-06-17 10:11:00"
tags:
    - Android
tag_ids:
    - SWem6w
categories:
    - Android / iOS
category_ids:
    - DjJyPP
published: true
hideInList: false
feature: ""
isTop: false
---

- 1，google国内镜像（安卓依赖包下载慢问题）
```
  url'http://maven.aliyun.com/nexus/content/groups/public/'
```
- 2，解决Failure [INSTALL_FAILED_TEST_ONLY]
![](/post-images/1659768635872.jpg)
```
android:testOnly="true" 
改成 android:testOnly="false"
// 升级之后BUG 
android.injected.testOnly=false 
```
- 3，测试打出来的是不是签名包
    - a,打出来的签名release包安装至手机（签名release包）
    - b,连接至Androidstudio
    - c,查看logcat（能查看包名的release包不能上架市场，不能查看即为正常）
    - d,检查 androidManifest.xml 文件中是否存在 isDebugger = true的标签，如果存在该标签,即使使用签名文件发布正式包，打出来的apk或者aab 也是debug包
![](/post-images/1659768662006.jpg)

- 4，存在重复引用库问题
[log.txt](https://note.youdao.com/s/GLwOleTm)
检查.dragle文件 dependencies标签内是否存在重复引用
切换到project视角，差看Lib 里面是否在存重复引用库
- 5，编译不通过问题
尝试升级 gradle版本