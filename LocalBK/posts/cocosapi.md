---
title: 'CocosAPI'
date: 2019-12-28 10:54:57
tags: [Cocos]
published: true
hideInList: false
feature: 
isTop: false
---
- 其他组件
```    
    cc.Motionstreak 拖尾
    cc.Animation 动画组件  cc.AnimationClip 动画剪辑
```
- 资源类型
```
    cc.AudioClip 音频资源
    cc.SpriteFrame 图片资源
   cc.SpriteFrameAtlas 图集资源
   cc.AnimathonClip 动画剪辑资源
   cc.Prefab  预制件
```
- 单例模式
```
cc.director 
    preloadScene() 预加载创景
    loadScene()切换场景
    pause()暂停游戏逻辑，不会禁用触摸事件
    
cc.loader
    loadRes()  动态加载本地资源  resources 文件下面
    load()  远程加载资源
cc.audioEngine 
    play()
    playMusic()
    playEffect()//音效  
 cc.Button()按钮组件
     过度类型：颜色，图片，缩放
     四种状态：normal,hover,pressed,cancel
     回调函数的绑定
     禁用  interactable
 cc.ProgressBar
     progress 进度
 cc.SrollView滚动视图
     isAutoScrolling()是否在移动
     this.scrollNode.stopAutoScroll();
 cc.Layout  布局
 cc.Widget 对其组件（做适配）
 cc.Canvas 画布 屏幕适配方案    
 cc.ToggleContainer 单选按钮
 ```
 
- 渲染组件
```
 cc.Sprite 精灵
     九宫格精灵的使用
     填充精灵的使用
     混合模式的使用
     动态切换精灵的图片
 cc.Label 文本的使用
     内容的设置 .string、
     文本的适配与对其
     字体的使用
     富文本的使用
 cc.ParticalSystem 粒子系统
```
                                               
- 碰撞组件
```
  cc.Collider 
      boxCollider
      circleCollider
      PolygonCollider
      分组设置
      组别配对
      碰撞回调
      碰撞管理器  
```

add 2020.01.03
```
director
获取视图打下
cc.director.getWinSize()
=> cc.winSize
获取屏幕的物理分辨率
cc.view.getFrameSize()
获取当前场景
cc.director.getScene() ==>return this._scene;
控制游戏帧率
cc.game.setFrameRate();
暂停动画
cc.director.stopAnimation();
game
切入后台，切入前台
cc.game.EVENT_HIDE
cc.game.EVENT_SHOW
常驻节点的添加
cc.game.addPersistRootNode();
cc.game.removePersistRootNode();
cc.game.isPersistRootNode();
systemEvent
cc.systemEvent.KEY_DOWN;
cc.systemEvent.KEY_UP;
cc.systemEvent.DEVICEMOTION;//重力感应
view
cc.view.resizeWithBrowserSize()//自适应浏览器尺寸
cc.view.setOrientation()//设置屏幕朝向
cc.view.enableAutoFullScreen()//移动端全屏
cc.view.setCanvasSize(width,height)//web端设置尺寸

关闭FPS显示
cc.debug.setDisplayStats(false);
```
