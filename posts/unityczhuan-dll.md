---
id: B2dqbo
title: UnityC#转dll
createdAt: "2022-08-06 14:45:13"
updated: "2026-06-17 10:11:00"
tags:
    - Unity
    - Dll
tag_ids:
    - FjODty
    - hQfCCb
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

本节讲解怎样将Unity中我们写的代码，做成dll文件。

从.cs生成的dll文件，是没有加密的，可被随意破解。因此后面我们还会讲解怎样对该dll文件进行加密。

一、配置VS

首先，要确保你的VS安装了“.NET桌面开发”。若没有，则先安装一下。

否则，在用VS创建类库时，会发现没有类库选项（找不到完全匹配项）。

![](/post-images/youdao-unityczhuan-dll-01.png)

![](/post-images/youdao-unityczhuan-dll-02.png)

二、创建类库

Q：我们能不能直接从Unity双击脚本，打开VS，不像下面这样还要创建一个新VS项目啊？

A：我们不能从Unity打开VS项目来生成dll文件，因为Unity打开的VS项目并不是类库项目，我们仍需要像下面这样来做。

1、创建新项目

启动VS2019，创建新项目

![](/post-images/youdao-unityczhuan-dll-03.png)

2、选择类库

选择C#、库，创建类库（.NET Framework）

![](/post-images/youdao-unityczhuan-dll-04.png)

3、配置新项目

项目名称，即为你的代码命名空间

框架选择3.5即可（若你选了其他选项，也可在后面“四”进行更改）

![](/post-images/youdao-unityczhuan-dll-05.png)

4、将VS的解决方案显示出来

你的VS可能是这样的，VS中并没有解决方案。

![](/post-images/youdao-unityczhuan-dll-06.png)

![](/post-images/youdao-unityczhuan-dll-07.png)

三、添加代码

注意：

所有我们需要通过 dll 调用的函数，都需要设为 公有（public static）

如果想要调用 Unity的API ，就需要导入 Unity 中的2个 DLL 到库中（否则不用）。

1、导入 Unity 中的2个 DLL 到库中

1、找到这两个dll文件的位置

![](/post-images/youdao-unityczhuan-dll-08.png)

2、给库添加引用

给我们创建的库，添加这两个dll文件的引用。方法是：

按住ctrl可同时选择这两个dll文件–>添加–>确定

2、添加我们的代码

三个类：

继承MonoBehaviour的类：可在dll文件下显示出该类，可将该类挂载到物体上

不继承MonoBehaviour：dll文件下不显示

```csharp
using UnityEngine;

namespace SARF
{
    public class Skode_00 : MonoBehaviour
    {
        /// <summary>
        /// 对两个整数相加
        /// </summary>
        public static int Addition(int parameter1, int parameter2)
        {
            return parameter1 + parameter2;
        }

        /// <summary>
        /// 字符串拼接
        /// </summary>
        public string Splice(string parameter1, string parameter2)
        {
            return parameter1 + parameter2;
        }

        /// <summary>
        /// 输出文本 —— 颜色：绿色
        /// </summary>
        /// <param name="parameter">字符串</param>
        public static void Print(string parameter)
        {
            Debug.Log($"<b><color=lime><size={12}>{parameter}</size></color></b>");
        }
    }

    public class Skode_01 : MonoBehaviour
    {

    }

    public class Skode_02
    {

    }
}
```

一个脚本，可以写多个类。若类继承了MonoBehaviour，则该dll文件导入Unity后，dll文件下会出现该类，可将该类挂载到物体上。

没继承MonoBehaviour的类，不会出现在dll下（不继承的可以写静态的类）。

![](/post-images/youdao-unityczhuan-dll-09.png)

类Skode_00、Skode_01继承了MonoBehaviour

![](/post-images/youdao-unityczhuan-dll-10.png)

没有类继承MonoBehaviour

四、生成dll文件

1、确定你的dll版本

若你上方选的是3.5版本，则继续第二步即可。

![](/post-images/youdao-unityczhuan-dll-11.png)

若不是，则需要改成Unity适用的3.5版本。

方法是：

右键"项目"–>属性–>目标框架：.3.5

2、生成dll文件

右键解决方案–>生成解决方案

3、找到dll文件

直接右键你的脚本，打开所在文件夹

bin/Debug：该文件夹中，就能找到你的dll文件。dll文件名称为你的命名空间名称。

![](/post-images/youdao-unityczhuan-dll-12.png)

![](/post-images/youdao-unityczhuan-dll-13.png)

五、使用dll文件

1、将该dll文件导入Unity

将Skode_00挂载到物体上，第2步我们会用到它。

2、写一个测试脚本，试试看！

该脚本挂载到Skode_00物体上。

```csharp
using UnityEngine;
using SARF;

public class NewBehaviourScript : MonoBehaviour
{
    void Start()
    {
        Skode_00.Print("Hello");
        print(Skode_00.Addition(1, 1));

        //因为dll文件中该方法不是静态的，但继承了Mono，因此我们也可这样来调用不是静态的方法
        GetComponent<Skode_00>().Splice("字符串1", "----字符串2");
    }
}
```

![](/post-images/youdao-unityczhuan-dll-14.png)

好啦，本届到此结束，再理一下思路：

创建类库

添加引用

添加代码

配置.Net框架版本

生成解决方案输出dll

导入Untiy使用~
