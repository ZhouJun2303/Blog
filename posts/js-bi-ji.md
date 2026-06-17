---
id: pKBd5t
title: JS笔记
createdAt: "2019-05-17 09:57:55"
updated: "2026-06-16 17:26:23"
tags:
    - JavaScript
tag_ids:
    - Q353xo
categories:
    - 编程基础
published: true
hideInList: false
feature: ""
isTop: false
---

- function 中的this指向问题
```
JS 中this指向问题
//undefined
var user = {
    count:1,
    getCount:function(){
      return this.count;   
    }
}
console.log(user.getCount()); //1
var otherGetCount = user.getCount;
console.log(otherGetCount());  //undefined;

//count为全局时的，this可以访问到var中的this
var count = 2;
var user = {
    count:1,
    getCount:function(){
      return this.count;   
    }
}
console.log(user.getCount()); //1
var otherGetCount = user.getCount;
console.log(otherGetCount());  //2;
```