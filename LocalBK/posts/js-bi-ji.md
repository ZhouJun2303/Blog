---
title: 'JS笔记'
date: 2019-05-17 09:57:55
tags: [JavaScript]
published: true
hideInList: false
feature: /post-images/js-bi-ji.png
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