---
id: q4CQUm
title: Unity(UI Horizontal Layout Group)
createdAt: "2023-03-19 14:24:12"
updated: "2026-06-17 10:11:00"
tags:
    - UnityEngine
    - User  Interface
tag_ids:
    - UNR80K
    - Bpnrqu
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

宽屏横向适配问题
适配 左-中-右，中间大小不变，左右自动拉升
## 方案1
中间居中
左：锚点设置最左边
右：锚点设置最右边
```
float width = ui.HpNode.rectTransform.rect.width;
float nodeItemLength = (width - 166) / 2;
ui.LeftNode.rectTransform.sizeDelta = new Vector2(nodeItemLength, 52);
ui.RightNode.rectTransform.sizeDelta = new Vector2(nodeItemLength, 52);
```

## 方案2
Horizontal Layout Group 设置控制子节点大小
![](/post-images/1679208119320.jpeg)
中间节点设置固定大小
![](/post-images/1679208147076.jpg)
左右节点设置按比例自动分配大小
![](/post-images/1679208171158.jpg)