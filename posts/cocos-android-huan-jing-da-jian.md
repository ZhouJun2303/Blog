---
id: KCPTaG
title: Cocos Android环境搭建
createdAt: "2020-01-30 11:15:12"
updated: "2026-06-17 10:11:00"
tags:
    - Cocos
    - Android
tag_ids:
    - Zuqsnn
    - SWem6w
categories:
    - Cocos / Laya
category_ids:
    - Lwedfg
published: true
hideInList: false
feature: ""
isTop: false
---

## 安卓环境搭建
JDK：1.8 个人qq群里有jdk1.8版本
下载AS
*1，下载NKDR16版本
2，下载SDK主流版本，22-29
3，配置好NDK和SDK的环境变量
4，cocos Creator中配置
## 使用cocos creator构建项目*
并使用cocos creator导入构建好的项目
可能出现的问题
![](/post-images/1659755923050.jpg)
```
Manifest merger failed : uses-sdk:minSdkVersion 16 cannot be smaller than version 22 declared in library [:libcocos2dx] D:\tmyclient\build\jsb-default\frameworks\cocos2d-x\cocos\platform\android\libcocos2dx\build\intermediates\merged_manifests\debug\processDebugManifest\merged\AndroidManifest.xml as the library might be using APIs not available in 16
	Suggestion: use a compatible library with a minSdk of at most 16,
		or increase this project's minSdk version to at least 22,
		or use tools:overrideLibrary="org.cocos2dx.lib" to force usage (may lead to runtime failures)
```
sdk版本不一致导致的问题
解决办法 更改为最低需要的SDK版本

## 导入依赖的资源包
showInExport:打开资源路径
libs包引入成功
![](/post-images/1659755991694.jpg)
打开build.gradle，将所需的libs包引入
![](/post-images/1659756019666.jpg)
点击sync now：立即改变
打开appActivity
将需要用到的方法声明写入
![](/post-images/1659756064938.jpg)
![](/post-images/1659756078819.jpg)

打包成功之后就是原生反射调用JAVA中的函数