---
title: 'AAB 转 APKS本地测试(bundletool)'
date: 2021-11-08 14:16:20
tags: [Java,Bundletool]
published: true
hideInList: false
feature: /post-images/aab-zhuan-apks-ben-di-ce-shi-bundletool.png
isTop: false
---
# bundletool
![](https://zhoujun2303.github.io/post-images/1659766786590.jpg)
[官方文档](https://developer.android.google.cn/studio/command-line/bundletool?hl=zh_cn)
# AAB  转 APKS 
```
java -jar bundletool-all-1.8.0.jar build-apks --bundle=launcher.aab --output=release.apks --ks=E:/gitGogs/CarCraftRaceIO/CarCraftRace.keystore --ks-pass=pass:password --ks-key-alias=normalKey --key-pass=pass:password
```

*目录结构，同级目录打开命令行*
![](https://zhoujun2303.github.io/post-images/1659766793471.jpg)
[bundletool](https://github.com/google/bundletool)
![](https://zhoujun2303.github.io/post-images/1659766799713.jpg)
# 命令行安装APKS （一次安装到多个USB 设备自行百度）
```
java -jar bundletool-all-1.8.0.jar install-apks --apks=release.apks
```