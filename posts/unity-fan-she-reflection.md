---
id: UgbxbR
title: Unity 反射（Reflection）
createdAt: "2023-03-06 19:30:57"
updated: "2026-06-16 17:26:22"
tags:
    - UnityEngine
    - C#
tag_ids:
    - UNR80K
    - fOiXzM
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

## 参考
[参考视频](https://www.bilibili.com/video/BV1UP4y1T7jE/?spm_id_from=333.999.0.0&vd_source=6f81433b8f1dda2a8d9fd1f770a72ef3)
## 基本使用
```
//step 1 获取对象的描述对象实例
Type t = System.Type.GetType("ReflectionTest");

//step 2 根据描述对象实例，构建一个对象实例
var instance = Activator.CreateInstance(t);

//step 3 对成员变量进行设值
//获取所有成员变量
FieldInfo[] fields = t.GetFields();
//获取单个 fieldInfo
FieldInfo intValue = t.GetField("IntValue");
//设值对象实例的 IntValue 值
intValue.SetValue(instance, 100);

//debug
ReflectionTest reflectionTest = instance as ReflectionTest;
Debug.Log(reflectionTest.IntValue);

//调用成员函数
MethodInfo methodInfo = t.GetMethod("Add");
object[] par = new object[2] { 1, 3 };
object value = methodInfo.Invoke(instance, par);
if(null != value)
{
    Debug.Log((int)value);
}
```
## 注意项
### 补充于2023年3月14日17:59:10
获取成员函数时，如果有重载同名方法，需要传方法参数，否则会获取不到成员函数
```
 MethodInfo methodInfo = T.GetMethod("Awake",
     BindingFlags.Instance | BindingFlags.Public, null, new Type[] { typeof(GameObject), typeof(UIWindowConfigBindingAttribute) }, null);
 object[] par = new object[] { windowObj, attribute };
 methodInfo.Invoke(instance, par);
```