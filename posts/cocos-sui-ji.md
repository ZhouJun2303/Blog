---
id: uXwkG8
title: Cocos随记
createdAt: "2019-06-29 10:03:13"
updated: "2026-06-17 10:11:00"
tags:
    - Cocos
tag_ids:
    - Zuqsnn
categories:
    - Cocos / Laya
category_ids:
    - Lwedfg
published: true
hideInList: false
feature: ""
isTop: false
---

- 富文本使用
```
this.win.string='<color=#00ff00>'+'游戏'+'</c><color=#0fffff>'+'完结</c>';
```
- 取两位字符
```
substring
```

```
前后补字符
padStart  //   padEnd
Js判断转boolean类型为false的6种情况
Boolean(0);
Boolean('');
Boolean(false);
Boolean(NaN);
Boolean(undefined);
Boolean(null)
```
```
prompt("");接受外部的数据
var age= parseInt(prompt("请输入年龄"))；
instanceof()//判断莫一个对象那个是否属于一个对象
```
- 数据类型
```
Array
String
Number
Object
JSON
Date
Math
```
```
hasOwnProperty
var str="sad9a9d90sa9578fa922f9a";
console.log(str.match(/\d+/g).length);//正则表达式
console.log(str.match(/\d+/g));//求数字的长度和个数

Math.ceil();//向上取整
Math.floor();//向下取整
Math.round();//四舍五入取整
parseInt();//向下取整
```
```
换行：<br>  \n
取整：parseInt
输入： prompt
输出： console.log()   document.write()  alert("弹窗")
内置函数：
```
	parseInt():转整形
	parseFloat():转浮点型
	isNaN():
	isFinite():判断一个数值是否有限
	eval():求字符串中表达式的值
```
空格:&nbsp
函数体内定义全局变量，如果不使用var关键字，就是定义的全局变量
```
- API
```
To:绝对动作(坐标)，相对于最开始的状态所做的动作；
By:相对动作(坐标)，相对于当前的状态所做的动作;


移动
moveTo(time,x,y)
moveBy(time,cc.P(x,y))


缩放
图片对象.scale=0.3：缩小三倍

旋转
rotateTo(时间，绕x轴旋转坐标，绕y轴旋转坐标)
rotateBy

倾斜
skewTo(时间，绕x轴旋转度数，绕y轴旋转度数)
skewBy

跳跃
jumpTo
//以坐标原点为原点，移动到目标坐标
//参数: (时间duration，目标坐标point(x, y)， 每次跳跃高度height， 跳跃次数count)
var jumpTo = cc.jumpTo(duration, cc.p(size.width / 2, size.height / 2), 50, 10);
sprite.runAction(jumpTo);


透明度
对象.opacity=200(最大值为255)


淡入淡出
fadeTo
//第二个参数为透明度,透明区间(0, 1)
var fadeTo = cc.fadeTo(duration, 0.5);
sprite.runAction(fadeTo);

fadeIn同上
fadeOut


闪烁效果
blink
//闪烁效果
//第二个参数为duration时间内闪烁次数
var blink = cc.blink(duration, 5);
sprite.runAction(blink);


色调的改变
tintTo
//改变色调效果
var tintTo = cc.tintTo(duration, 255, 127.5, 0);
sprite.runAction(tintTo);



延迟执行
delay Time
var delaytime=cc.delayTime(时间)
用于组合动作中


顺序执行
sequence
//顺序执行当前添加的所有动作
var sequence = cc.sequence(moveby, moveto, scaleTo, scaleBy, fadeTo, 
fadeOut, fadeIn, blink, tintTo,rotateTo, rotateBy, skewBy, skewTo, 
jumpBy, jumpTo, bezierTo, bezierBy);

sprite.runAction(sequence);



重复执行
repeat/repeatforever
//重复执行
//参数: (action，执行次数)
var repeat = cc.repeat(sequence, 3);
sprite.runAction(repeat);


//无限重复
var repeatForever = cc.repeatForever(sequence);
sprite.runAction(repeatForever);



同时执行
spawn
//spawn 同时执行
var spawn = cc.spawn(moveby, scaleTo, blink, tintTo);
sprite.runAction(spawn);


反向执行 reverse


//坐标转换
pos=this.convertToNodeSpace(pos);
```