---
title: 'IIS'
date: 2022-08-05 14:54:18
tags: [Windows]
published: true
hideInList: false
feature: /post-images/iis.jpg
isTop: false
---

![](https://zhoujun2303.github.io/post-images/1659750458057.jpg)
打开计算机管理
compmgmt.msc
![](https://zhoujun2303.github.io/post-images/1659750471290.jpg)
![](https://zhoujun2303.github.io/post-images/1659750476496.jpg)
刷新DNS缓存
ipconfig/flushdns


Hosts
```
# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
127.0.0.1 client.com
127.0.0.2 ws.com
```