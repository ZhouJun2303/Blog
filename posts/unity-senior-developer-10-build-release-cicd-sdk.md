---
id: rrSZLc
title: Unity 开发高级/资深 10：构建发布、CI/CD 与 SDK
createdAt: "2026-06-10 22:00:00"
updated: "2026-06-29 15:42:42"
tags:
    - Unity
    - 开发高级/资深
    - 构建发布
    - SDK
tag_ids:
    - FjODty
    - P46nOZ
    - xn5J0z
    - 0lhPed
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: true
feature: ""
isTop: false
---

[返回总览](/post/unity-senior-developer-skills/)

相关图示：[交付闭环图](/post/unity-senior-developer-skills/#delivery-loop)

<a id="build-release"></a>
## 构建发布与 CI/CD

- Build Pipeline：Player Settings、Build Settings、Scripting Define Symbols、平台参数。
- 自动化构建：Jenkins、GitHub Actions、GitLab CI、TeamCity、命令行 Unity。
- 资源构建：AssetBundle/Addressables 构建、清单、hash、版本号、上传。
- 多环境：开发、测试、预发布、正式服务器配置隔离。
- 多渠道：包名、图标、SDK、权限、渠道参数、资源差异。
- 版本管理：客户端版本、资源版本、配置版本、协议版本、构建号。
- 符号管理：dSYM、mapping、so 符号、IL2CPP 符号、产物归档。
- 发版流程：提测、冻结、回归、灰度、上线、回滚、补丁。
- 构建稳定性：失败重试、缓存清理、依赖锁定、构建日志归档。

### 需要掌握的工具

- Unity Batchmode：命令行构建、资源构建、测试和导出工程。
- Jenkins、GitHub Actions、GitLab CI、TeamCity：自动化构建和流水线。
- Fastlane：iOS/Android 打包、签名、上传和元数据管理。
- Gradle：Android 依赖、渠道参数、AAR、Manifest 合并和构建日志。
- xcodebuild、Xcode Organizer：iOS 构建、归档、导出和上传。
- 符号上传工具：dSYM、mapping、so、IL2CPP 符号归档和上传。
- Build Report、构建日志分析脚本：定位构建失败、包体变化和资源异常。

### 可继续细分方向

- Unity 命令行构建。
- 资源构建、版本清单和产物归档。
- 多渠道、多环境和多平台发布。
- 符号、灰度、上线和回滚流程。

<a id="platform-sdk"></a>
## 平台与 SDK 接入

- Android 桥接：AAR、Jar、Gradle、AndroidManifest、Activity、权限。
- iOS 桥接：Framework、Info.plist、Entitlements、Objective-C/Swift、隐私清单。
- 登录：游客、账号、渠道、第三方、Token、过期、切换账号。
- 支付：下单、支付回调、验签、补单、重复发货、异常订单。
- 广告：激励视频、插屏、失败回调、冷却、广告位、收益上报。
- 统计：启动、登录、付费、关卡、留存、崩溃、性能埋点。
- 推送：权限、Token、前后台行为、厂商推送、点击跳转。
- 合规：隐私弹窗、实名、防沉迷、权限说明、数据删除。
- 线程与回调：SDK 回调不一定在 Unity 主线程，必须统一派发。

### 需要掌握的工具

- Android Studio：调试 Java/Kotlin、Gradle、Manifest、AAR 和 Logcat。
- Xcode：调试 Objective-C/Swift、Framework、Info.plist、Entitlements 和签名。
- ADB、Logcat：查看 Android 设备日志、安装包、权限、崩溃和 ANR。
- CocoaPods、Swift Package Manager：管理 iOS 第三方依赖。
- SDK Demo 和渠道后台：验证登录、支付、广告、推送、统计和回调。
- Charles/Wireshark：排查 SDK 网络请求和支付链路。
- 隐私检测工具：检查权限、隐私清单、数据采集和合规提示。

### 可继续细分方向

- Android 原生桥接。
- iOS 原生桥接。
- 登录、支付、广告、统计、推送。
- 隐私合规、权限和应用商店审核。

## 开发高级/资深关注点

- 构建产物是否可追溯到代码提交、资源版本、配置版本。
- 构建失败是否能快速定位是 Unity、Gradle、Xcode、资源还是 SDK。
- 渠道差异是否集中管理，而不是散落在业务代码里。
- 支付链路是否有服务器校验、补单和重复发货保护。
- 上线前是否准备好回滚包、热更包、符号文件和监控看板。
