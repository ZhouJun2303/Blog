---
id: ewCQJm
title: 关于UnityBuild 模板使用
createdAt: "2022-08-06 14:46:53"
updated: "2026-06-17 10:11:00"
tags:
    - Unity
    - Android
tag_ids:
    - FjODty
    - SWem6w
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-01.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板1 对应UnityLibrary中的Manifest清单文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-02.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板2 对应Launcher中的Manifest清单文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-03.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板3 对应unityLibrary的.gradle文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-04.png)

    **当勾选使用了模板3的时候，如果项目中使用了Google的安卓依赖包管理器，那么此时管理器会失效

    建议

        项目未使用androidx 时，取消使用此模板，依赖google包管理器进行依赖包管理，系统会自动剔除不同sdk的重复引用包

        项目使用androidx时，建议使用此模板，SDK(GA 为例)大部分会与androidx冲突

***使用google依赖包不使用此模板

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-05.png)

***使用此模板google依赖包无效

导出之后采用模板配置

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-06.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板4 对应Launch的.gradle文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-07.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板5 对应Project 的.gradle文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-08.png)

--------------------------------------------------------分割线-----------------------------------------------------------

```javascript
模板6 对应 gradle.properties 文件
```

![](/post-images/youdao-guan-yu-unitybuild-mo-ban-shi-yong-09.png)

--------------------------------------------------------分割线-----------------------------------------------------------

unity-jar-resolver
