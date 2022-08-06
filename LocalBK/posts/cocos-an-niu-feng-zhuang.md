---
title: 'Cocos按钮封装'
date: 2019-08-12 10:43:24
tags: [Cocos]
published: true
hideInList: false
feature: /post-images/cocos-an-niu-feng-zhuang.png
isTop: false
---
- 动态添加按钮组件：函数的封装
```
cc.vv.addButton = function (data) {
    for (let i in data) {
        if (data[i] === null) {
            cc.warn([i] + '不存在');
            return false;
        }
    }
    const transition = cc.Button.Transition.SCALE;
    const duration = 0.1;
    const zoomScale = 1.2;

    var target = data.target;
    var btn = data.btn;
    var component = data.component;
    var handler = data.handler;
    var customEventData = data.customEventData;
    var enableAutoGrayEffect = data.enableAutoGrayEffect;
    var interactable = data.interactable;

    var clickEventHandler = new cc.Component.EventHandler();
    clickEventHandler.target = target;
    clickEventHandler.component = component;
    clickEventHandler.handler = handler;
    clickEventHandler.customEventData = customEventData;
    btn.clickEvents.push(clickEventHandler);

    btn.transition = transition;
    btn.duration = duration;
    btn.zoomScale = zoomScale;
    btn.enableAutoGrayEffect = enableAutoGrayEffect;
    btn.interactable = interactable;
};
```
- 函数的调用
```
addButton() {
    for (let i = 0, pNode = this.mapPar.children, len = pNode.length; i < len; i += 1) {
        let node = pNode[i];
        let btn = node.addComponent(cc.Button);
        cc.vv.addButton({
            'target': this.node, 'btn': btn, 'component': 'Map', 'handler': 'chooseChapter',
            'customEventData': i + 1, 'enableAutoGrayEffect': true, 'interactable': i + 1 <= 1
        });
    }
},
```
