---
title: 'Mac强制将硬盘恢复出厂设置'
date: 2022-01-05 14:28:58
tags: [Mac]
published: true
hideInList: false
feature: /post-images/mac-qiang-zhi-jiang-ying-pan-hui-fu-chu-han-she-zhi.png
isTop: false
---
在 CMD 命令中输入 diskpart
```
list disk
select disk 1
clean
```