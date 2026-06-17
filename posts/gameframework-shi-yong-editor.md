---
id: vQ01xf
title: GameFramework使用(Editor)
createdAt: "2022-09-17 15:48:10"
updated: "2026-06-16 17:26:22"
tags:
    - Unity
    - GameFramework
tag_ids:
    - FjODty
    - VNguF1
categories:
    - Unity
published: true
hideInList: false
feature: ""
isTop: false
---

## 工具栏Game Framework
### OpenFolder 
- 目录相关路径
### ResourceTools ***
#### Resource Builder ***
#### Resource Editor *** 
#### Resource Analyzer
#### Resource Pack Builder
#### Resource Sync Tools
### Scenes in Build Settings
- 一键构建打包Scene
### LogScripting Define Symbols
- 日志打印
### Documentation
### API Reference

## 构建流程
### Resource Editor 构建ResourceCollection.xml
![](/post-images/1663402232621.jpg)
- 保存之后可在ResourceCollection.xml 查看
- 优化点 同一时间需要用到的资源放入同一个包可以优化加载时间
- 优化点 游戏启动时需要的资源在同一个包可以优化启动时间
### Resource Builder 构建资源文件
![](/post-images/1663402597440.jpg)
- 构建完成之后可通过取消勾选Builtin Insperctor 面板Editor Resource Mode 模拟真机测试
- 注意 部分Android studio 版本可能会忽略 Assetbundle文件大小写

## 传送门
### [GameFramework官网](http://gameframework.cn/)
### [GameFramework仓库](https://github.com/EllanJiang/GameFramework)