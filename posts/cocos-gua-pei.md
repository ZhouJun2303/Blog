---
title: 'Cocos适配'
date: 2019-08-08 10:40:57
tags: [Cocos]
published: true
hideInList: false
feature: 
isTop: false
---
```
cc.Canvas.prototype.applySettings = function () {
    var width = this.designResolution.width;
    var height = this.designResolution.height;
    if (CC_EDITOR) {
        cc.engine.setDesignResolutionSize(width, height);
    } else {
        if ((cc.sys.isNative && cc.sys.isMobile) || CC_PREVIEW) {
            // 横屏 FIXED_HEIGHT
            // 竖屏 FIXED_WIDTH
            // 强制拉伸 EXACT_FIT
            // 当前屏幕尺寸 > 设计分辨率的时候,  将强制拉伸修改为按宽适配
            var frameSize = cc.view.getFrameSize();
            var resolutionPolicy = frameSize.width > frameSize.height ? cc.ResolutionPolicy.FIXED_HEIGHT : cc.ResolutionPolicy.FIXED_WIDTH;
            var designSize = cc.view.getDesignResolutionSize();
            var isFullScreen = frameSize.width / frameSize.height > designSize.width / designSize.height;
            // resolutionPolicy = isFullScreen ? cc.ResolutionPolicy.EXACT_FIT : resolutionPolicy;
            frameSize.width <= 640 && frameSize.height <= 960 && (resolutionPolicy = cc.ResolutionPolicy.EXACT_FIT);
            cc.log(cc.director.getScene().name, frameSize.width, frameSize.height, designSize.width, designSize.height, isFullScreen, resolutionPolicy);
            cc.view.setDesignResolutionSize(width, height, resolutionPolicy);
        } else {
            cc.view.setDesignResolutionSize(width, height, cc.ResolutionPolicy.SHOW_ALL);
        }
    }
};
```