---
id: 5ZPdEc
title: WebSocket
createdAt: "2021-12-02 14:21:34"
updated: "2026-06-17 10:11:00"
tags:
    - WebSocket
tag_ids:
    - uf8pXo
categories:
    - 编程基础
category_ids:
    - kthGs4
published: true
hideInList: false
feature: ""
isTop: false
---

[自行百度](https://www.cnblogs.com/upze/p/10630713.html)
- 引入websocket模块
```
npm i nodejs-websocket  --sava
```
```
npm install socket.io --save
```
- 服务器端
```
npm install -g ws //全局安装WS  npm指令自行学习
```
目录如下
![](/post-images/1659767199779.jpg)
constValue.js
```
exports.config = {
    "host":"192.168.5.178",//服务器端口 此为我的电脑IP cmd -》 ipconfig
    "port":3000,
},

exports.protocol={
    login:101,
    hallLogin:201,
}
```
app.js
```
var constValue = require("./hall/constValue");

var ws = require("ws").Server;
const connect = new ws({
    port:constValue.config.port
});

connect.on("listening",function(){
    console.log("服务器开启监听！！！");
})

connect.on("connection",function(ws,req){
    console.log(ws);
    console.log("有刺客——————>"+ req.connection.remoteAddress);
    ws.on("message",function(packet){
        let msg = JSON.parse(packet);
        if(msg.cmd == constValue.protocol.login){
            login(msg)
        }else if(msg.cmd == constValue.protocol.hallLogin){
            hallLogin(msg)
        }
    });

    ws.on("close",function(msg){
        console.log("有玩家关闭了连接");
        console.log(msg);
    });

    ws.on("ping",function(msg){
        console.log("ping",msg);
    });

    ws.on("error",function(msg){
        console.log("error",msg);
    })

    login = function(msg){
        console.log(msg);
        ws.send("来了老弟！");
    };

    hallLogin = function(msg){
        console.log(msg);
        ws.send('进入大厅');
    };
    
});

connect.on("headers",function(msg,data){
    console.log(msg);
    console.log(data);
})


console.log(constValue.config);
```
- 项目初始化
```
npm init
```
package.json配置
![](/post-images/1659767215597.jpg)
```
//test:"node app.js"
//启用包配置之后
启动服务器可以为 
    1-> node app.js
    2-> npm test
```
服务器启动
![](/post-images/1659767226470.jpg)
![](/post-images/1659767244493.jpg)
```
Ctrl + c 关闭服务器
```
在html中使用
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <script>
    let ws = new WebSocket('ws://192.168.5.178:3000');
    ws.onopen = function (params) {
      console.log('客户端连接成功')
      // 向服务器发送消息
      let data ={
          cmd:101,
          msg:"haha"
      }
      ws.send(JSON.stringify(data))
    };

    ws.onmessage = function (e) {
      console.log('收到服务器响应', e.data)
    };

    </script>
</body>
</html>
```
在cocos creator中使用同理
```
let ws = new WebSocket('ws://192.168.5.178:3000');
    ws.onopen = function (params) {
      console.log('客户端连接成功')
      // 向服务器发送消息
      let data ={
          cmd:101,
          msg:"haha"
      }
      ws.send(JSON.stringify(data))
    };

    ws.onmessage = function (e) {
      console.log('收到服务器响应', e.data)
    };
```
![](/post-images/1659767263042.jpg)