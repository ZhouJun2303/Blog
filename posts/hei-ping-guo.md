---
id: QS4dzx
title: 黑苹果
createdAt: "2021-03-27 13:47:29"
updated: "2026-06-17 10:11:00"
tags:
    - 黑苹果
tag_ids:
    - poK2r9
categories:
    - 工具链
category_ids:
    - VFyF1L
published: true
hideInList: false
feature: ""
isTop: false
---

[黑苹果长期维护机型](https://blog.daliansky.net/Hackintosh-long-term-maintenance-model-checklist.html)

[OpenCore下载](https://github.com/acidanthera/OpenCorePkg/releases)

[macOS镜像下载](https://blog.daliansky.net/)

[安装盘制作工具etcher下载](https://etcher.balena.io/)

[OpenCore安装指南、驱动与SSDT下载](https://dortania.github.io/OpenCore-Install-Guide/)

[SSDTTime下载](https://github.com/corpnewt/SSDTTime)

[Config编辑器](https://github.com/ic005k/OCAuxiliaryTools)

[OpenCore排错](https://opencore.slowgeek.com/)

[DiskGenius下载](https://www.diskgenius.cn/)

[视频](https://www.bilibili.com/video/BV18V41187JZ)

## VMware16安装macOS Big Sur 11.0.1

（黑苹果）VMware16安装macOS Big Sur 11.0.1

目录  隐藏

1 下载 macOS Big Sur 11.0.1

2 下载并安装VMware16

3 安装unlocker

4 创建虚拟机

4.1 选择macOS11.0

4.2 选择处理器数量

4.3 设置虚拟机内存

4.4 选择网络类型

4.5 选择I/O控制器类型

4.6 选择磁盘类型

4.7 指定磁盘容量

5 配置虚拟机

6 挂载安装镜像

7 安装 macOS

7.1 选择安装语言

7.2 选择磁盘工具

7.3 磁盘初始化

7.4 选择安装位置

7.5 开始安装

8 配置macOS

8.1 选择国家和地区

8.2 选择网络连接方式

8.3 迁移助理

8.4 设置apple ID

8.5 创建账户

9 安装 VMware Tools

10 安装Xcode

文章目录 收缩

下载 macOS Big Sur 11.0.1

私我

提取码 crsw

下载并安装VMware16

下载地址：https://download3.vmware.com/software/wkst/file/VMware-workstation-full-16.0.0-16894299.exe

序列号：

安装unlocker

默认安装好的VMware16没有MacOS选项，需要先安装unlocker，下载地址：

https://github.com/paolo-projects/auto-unlocker/releases

安装后：

![](/post-images/youdao-hei-ping-guo-01.png)

创建虚拟机

打开 VMware Workstation 16 ，选择 “创建新的虚拟机”

![](/post-images/youdao-hei-ping-guo-02.png)

![](/post-images/youdao-hei-ping-guo-03.png)

![](/post-images/youdao-hei-ping-guo-04.png)

选择macOS11.0

![](/post-images/youdao-hei-ping-guo-05.png)

选择处理器数量

![](/post-images/youdao-hei-ping-guo-06.png)

设置虚拟机内存

![](/post-images/youdao-hei-ping-guo-07.png)

选择网络类型

![](/post-images/youdao-hei-ping-guo-08.png)

选择I/O控制器类型

![](/post-images/youdao-hei-ping-guo-09.png)

选择磁盘类型

![](/post-images/youdao-hei-ping-guo-10.png)

![](/post-images/youdao-hei-ping-guo-11.png)

指定磁盘容量

![](/post-images/youdao-hei-ping-guo-12.png)

配置虚拟机

创建完虚拟机后，找到虚拟机文件位置，编辑macOS 11.0.vmx文件，在末尾添加：

挂载安装镜像

点击“编辑虚拟机设置”，选择“CD/DVD”选项。

![](/post-images/youdao-hei-ping-guo-13.png)

保存以后点击“开启虚拟机”

安装 macOS

![](/post-images/youdao-hei-ping-guo-14.png)

选择安装语言

![](/post-images/youdao-hei-ping-guo-15.png)

选择磁盘工具

![](/post-images/youdao-hei-ping-guo-16.png)

磁盘初始化

找到名称为 VMware Virtual SATA Hard Drive Media 的磁盘，选中该磁盘，点击抹掉，格式选择 APFS

![](/post-images/youdao-hei-ping-guo-17.png)

退出磁盘工具，选择 安装 macOS 并继续

![](/post-images/youdao-hei-ping-guo-18.png)

![](/post-images/youdao-hei-ping-guo-19.png)

选择安装位置

![](/post-images/youdao-hei-ping-guo-20.png)

开始安装

![](/post-images/youdao-hei-ping-guo-21.png)

配置macOS

选择国家和地区

![](/post-images/youdao-hei-ping-guo-22.png)

选择网络连接方式

![](/post-images/youdao-hei-ping-guo-23.png)

![](/post-images/youdao-hei-ping-guo-24.png)

提示网络连接失败的解决办法：

1、回到windows，控制面板-网络连接-右键属性-VMware Network Adapter VMnet1–IPV4设置–自动获取ip地址–自动获得dns服务器；

2、打开windows服务，打开服务：VMware DHCP Sevice和VMware NAT Service;

![](/post-images/youdao-hei-ping-guo-25.png)

迁移助理

选择以后

![](/post-images/youdao-hei-ping-guo-26.png)

设置apple ID

选择稍后设置

![](/post-images/youdao-hei-ping-guo-27.png)

创建账户

![](/post-images/youdao-hei-ping-guo-28.png)

安装 VMware Tools

在 VMware 的 虚拟机(M) 菜单栏中选择 安装 VMware Tools(T)… 选项。

![](/post-images/youdao-hei-ping-guo-29.png)

![](/post-images/youdao-hei-ping-guo-30.png)

安装过程会触发多个安全限制，请按照提示转到设置里的安全设置里解锁，最后完成安装。

![](/post-images/youdao-hei-ping-guo-31.png)

完成安装后必须重启系统，然后点击虚拟机上的进入全屏模式，macOS即可全屏显示。

安装Xcode

![](/post-images/youdao-hei-ping-guo-32.png)

控制台中显示效果：

![](/post-images/youdao-hei-ping-guo-33.png)
