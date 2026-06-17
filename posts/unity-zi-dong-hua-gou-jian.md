---
id: ChbiBE
title: Unity自动化构建
createdAt: "2024-02-01 15:08:08"
updated: "2026-06-16 17:26:22"
tags:
    - UnityEditor
    - NodeJS
tag_ids:
    - J7VXMO
    - NodeJS
categories:
    - Unity
published: true
hideInList: false
feature: ""
isTop: false
---

## 配置

* 下载本仓库
* 在DB文件夹中手动创建DB  //FIXME
* 在项目文件夹中手动创建Record  //FIXME
* 在 ``config\projectConfig.js``中配置打包机IP地址
* 在 ``Web\main.js``中配置打包机IP地址
* 在 ``config\Web\main.js``中配置打包机IP地址
* 终端执行 ``npm install`` 安装所有依赖库
* 项目依赖pm2 进程管理，pm2安装及使用自行查询
* 项目依赖Visual Studio
* 启动项目双击 .\FirstStartup.bat

## 说明

* 目前仅支持局域网访问 //FIXME 内网穿透
* 同时仅支持一个项目构建
* 四小时无任何操作缓存APK将被清理
* 请确保分支对应
## 界面说明

  ### 构建控制台
  -  构建控制台地址 `http://本机ip:9998`
  -  增加自动构建项目请点击 ``项目配置``
  ### 项目配置界面
  - 名称（主Key）
  - Unity 工程路径 
  - Android 工程路径
  - 飞书机器人链接
  - .....
  - Unity 静态打包方法(构建完毕之Unity不会自动关闭，请在Unity 中执行完所有操作关闭Unity,否则将卡住整个构建流程)(适配协程或自定义异步构建设计)
  - 添加值数据库
  ### APK下载/日志
    - APK 构建缓存路径
    - Unity 构建输出日志路径

## 参数说明

* 项目名称
* Unity 打包静态方法 （Unity构建静态方法）
* 构建类型
* Unity分支名称 （本地已经缓存的分支，请确保origin上有相同分支）
* Android分支名称
* 版本号
* 导出Unity 工程 （Unity工程未修改可不勾选，减少打包耗时）
* 同步最新Unity 分支代码:
  * 丢弃本地缓存
  * 切换至指定分支
  * 拉取最新代码
* 同步最新Android 分支代码 （同上）
* 构建AAB
* 推送日志消息（不勾选仅屏蔽不重要日志）
* 清理Android 缓存 （Unity项目更改不大，同一天连续打包，可不勾选，极大提升构建速度 30分钟缩减至5分钟）

## 流程说明（全部选项勾选为例）

1. 写入操作记录到数据库
2. 丢弃Unity 本地缓存
3. 切换到指定Unity分支
4. 拉取最新代码
5. 执行Unity 的静态方法
6. Android git 操作同上
7. 设置Launcher.gradle 版本号，构建APK名称
8. 清理android 缓存
9. 同步最新更改
10. 打包APK，拷贝至下载路径
11. 打包AAB，拷贝至下载路径

## 重要提示

* projectPath + "/launcher/build.gradle" 配置签名路径

    ```Java
    示例
    signingConfigs {
    ​    ​release {
    ​        ​storeFile file('xxxxxng_cn.keystore')
            storePassword 'xxx'
            keyAlias 'xxxxx'
            keyPassword 'xxx'
        }
    ​    ​debug {
    ​        ​storeFile file('xxxxxxng_cn.keystore')
            storePassword 'xxx'
            keyAlias 'xxx'
            keyPassword 'xxx'
        }
    }

    //buildTypes 必须在 signingConfigs 之后
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt')
            signingConfig signingConfigs.release
            ndk {
                debugSymbolLevel = 'FULL'
            }
        }
        debug {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android.txt')
            signingConfig signingConfigs.debug
            jniDebuggable true
        }
    }
    ```

* 本地的 aar 包请手动引用
```
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation(name: 'common', ext: 'aar')
```


* 请在 gradle.properties 指定 JDK路径
```
 org.gradle.java.home=C\:/Program Files/Android/Android Studio/jbr
```
