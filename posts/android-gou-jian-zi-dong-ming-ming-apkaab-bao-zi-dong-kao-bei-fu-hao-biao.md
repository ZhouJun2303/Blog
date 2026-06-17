---
id: YPMpbs
title: Android 构建自动命名APK、AAB包，自动拷贝符号表
createdAt: "2023-07-20 15:48:25"
updated: "2026-06-17 10:11:00"
tags:
    - Android
    - 构建发布
tag_ids:
    - SWem6w
    - xn5J0z
categories:
    - Android / iOS
category_ids:
    - DjJyPP
published: true
hideInList: false
feature: ""
isTop: false
---

## APK、AAB的自动化命名
## 示例
```
 defaultConfig {
        minSdkVersion 19
        targetSdkVersion 33
        multiDexEnabled true
        applicationId 'com.xx.xxx'
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
        versionCode 178
        versionName '1.7.8'
        consumerProguardFiles 'proguard-unity.txt'
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        setProperty("archivesBaseName", "${getAppName()}_haiwai_v${versionCode}_${releaseTime()}")
    }
```
## 获取时间
```
//获取时间，添加到发布版本中
static def releaseTime() {
    return new Date().format("yyyy_MM_dd_HH_mm", TimeZone.getTimeZone("GMT+08:00"))
}
```
## 获取APPName
```
// 获取AppName
def getAppName() {
    def stringsFile = android.sourceSets.main.res.sourceFiles.find { it.name.equals 'strings.xml' }
    String s = new XmlParser().parse(stringsFile).string.find { it.@name.equals 'app_name' }.text();
    return s.replaceAll("\"", "");
}
```
## 自动拷贝符号表
```
 applicationVariants.all { variant ->
        variant.outputs.all { output ->
            def currentVersion = defaultConfig.versionCode;
                //
            if (output.outputFile != null && output.outputFile.name.endsWith('.apk')) {
                output.assemble.doLast {
                    println "Root path of the project is: " + rootDir
                    copy {
                        from "$rootDir/unityLibrary/symbols"
                        into "$rootDir/TempSymbols/${currentVersion}_${releaseTime()}"
//                        include output.outputFile.name
                    }
                }
            }
        }
    }
```