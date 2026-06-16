---
id: eL81LM
title: C# 学习
createdAt: "2021-04-10 13:51:18"
updated: "2026-06-16 17:26:22"
tags:
    - C#
tag_ids:
    - fOiXzM
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

- 修饰符
```
public 
公共的

private
私有，类内部才能访问

protected
只修饰成员，类内部及子类内部可以访问

static 
修饰类为静态类，不能实例化类
static修饰构造函数时，构造函数不能含有任何参数及修饰符
构造函数：名字和类名相同（实例，静态，私有）

internal
默认修饰符，同一个程序集内成员可以访问

abstract
abstract可以修饰类，方法，属性
抽象类不能被实例化
抽象不能用sealed修饰，sealed修饰不能被继承
抽象方法只能定义在抽象类，抽象方法只声明，不提供实现
抽象方法声明不能用virtual或者static修饰
不能在静态属性上用abstract修饰
抽象属性在非抽象派生类覆盖重写，须使用override修饰符

partial
只能修饰类，可以将一个分成部分写在不同文件，这些文件只能在同一个程序集

sealed
修饰类不能被继承，修饰方法不能被重写

virtual
修饰方法，父类可以有该方法的实现，子类可以重写改方法(注意和abstract区别)

override
表示该方法覆盖了父类的方法

readonly
修饰字段，运行时只读，修改无需编译

const
只读，编译前确定值

operator
在类或结构声明中声明运算符

base
调用构造函数，或者基类被重写的方法
```
- 注释
```
// 不会被编译
/// 会被编译（影响编译速度，不影响执行速度）在调用代码时调用感知
/// <summary>
///
/// </summary>
```
- 协程
```
https://blog.csdn.net/qq_36684665/article/details/80829049
https://www.bilibili.com/video/BV1f5411G7bp?p=14

StartCoroutine("BezierToTargetPosIenum",0.1f);//way1 
StartCoroutine(BezierToTargetPosIenum(0.1f));//way2
 /// <summary>
/// 协程测试
        /// </summary>
        /// <param name="dt"></param>
        /// <returns></returns>
        IEnumerator   BezierToTargetPosIenum(float dt)
        {
            Debug.Log("协程测试 开始");
            while (Count<10)
            {
                Count++;
                yield return null;
            }
            Debug.Log("计数 结束");
            yield return new WaitForSeconds(0.5f);
            Debug.Log("协程测试 结束");
        }
```
- 委托
```
 //委托
        delegate int  Multidelegate(int a,int b);
        Multidelegate myMultidelegate;

        public void TestMultidelegate()
        {
            myMultidelegate = AddNumber;
            myMultidelegate += AddNumber;
            myMultidelegate -= AddNumber;
            // 没有进行任何操作是 为null
            if (myMultidelegate == null) return;
          Debug.Log(  myMultidelegate(3, 5));
        }
```
- 接口
```
 //接口
    public interface TestInterFace1
    {
        void Test1();
    }

    public interface TestInterFace2<T>
    {
        void Test2(T s);
    }

//使用接口
 public partial class GameEntry : MonoBehaviour,TestInterFace1,TestInterFace2<int>
 
  //接口实现
        public void Test1()
        {
            Debug.Log("Test1");
        }

        public void Test2(int num)
        {
            Debug.Log("Test2"+num);
        }
```
- 泛型
```
//泛型 
        public List<string> StrList = new List<string>();

        //class struct new  mono
        public T GenericTest<T, U, V>(T t, U u, V v) where T :class
        {
            return t;
        }

        public void GenericTestS()
        {
            var test1 = GenericTest<TestSerializable, int, float>(new TestSerializable(), 10, 10f);
            var tets2 = GenericTest(new TestSerializable(), 10, 10f);
        }
```