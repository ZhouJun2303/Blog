---
id: necwsC
title: Mac强制将硬盘恢复出厂设置
createdAt: "2022-01-05 14:28:58"
updated: "2026-06-16 17:26:22"
tags:
    - Mac
tag_ids:
    - 1dgFIU
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

在 CMD 命令中输入 diskpart
```
list disk
select disk 1
clean
```