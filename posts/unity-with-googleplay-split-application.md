---
id: vA4srT
title: Unity With GooglePlay Split Application
createdAt: "2023-09-28 10:46:50"
updated: "2026-06-16 17:26:22"
tags:
    - Android
    - Unity
tag_ids:
    - SWem6w
    - FjODty
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

### Google [官方文档](https://developer.android.google.cn/guide/playcore/asset-delivery/integrate-native?hl=zh-cn)
### 原理
#### U3D
开启分包之后 Unity的部分资源文件在android中独立成一个资源package模块
##### 设置 
```
// 切换Split Application Binary状态
PlayerSettings.Android.useAPKExpansionFiles = BuildProjectWindows.GetShouldEnableSplitAPK();
EditorUserBuildSettings.buildAppBundle = BuildProjectWindows.GetShouldEnableSplitAPK();
```
#### android 
##### launcher/build.gradle
```
old 
@@ -53,8 +53,10 @@ android {
        doNotStrip '*/armeabi-v7a/*.so'
        doNotStrip '*/arm64-v8a/*.so'
    }



    bundle {
        language {
            enableSplit = false
        }

new
@@ -53,8 +53,10 @@ android {
        doNotStrip '*/armeabi-v7a/*.so'
        doNotStrip '*/arm64-v8a/*.so'
    }

    assetPacks = [":UnityDataAssetPack"]

    bundle {
        language {
            enableSplit = false
        }

```
##### gradle.properties
```
old 
@@ -1,4 +1,5 @@
org.gradle.jvmargs=-Xmx2048M
org.gradle.parallel=true
android.enableR8=false
unityStreamingAssets=.unity3d, UnityServicesProjectConfiguration.json

new
@@ -1,4 +1,5 @@
org.gradle.jvmargs=-Xmx2048M
org.gradle.parallel=true
android.enableR8=false
unityStreamingAssets=.unity3d
android.bundle.enableUncompressedNativeLibs=false
No newline at end of file
```
##### settings.gradle
```
old
@@ -1,1 +1,2 @@
include ':launcher', ':unityLibrary'
No newline at end of file

new
@@ -1,1 +1,2 @@
include ':launcher', ':unityLibrary'
include ':UnityDataAssetPack'
No newline at end of file

```