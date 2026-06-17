---
id: lDOZzB
title: Unity JAR 包制作
createdAt: "2021-08-12 14:06:43"
updated: "2026-06-17 10:11:00"
tags:
    - Unity
    - Jar
tag_ids:
    - FjODty
    - Qh55SV
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

- 1,创建一个新的模块
![](/post-images/1659766098389.jpg)
- 2,拷贝unity 自带jar包到模块下的lib
![](/post-images/1659766112757.jpg)
- 3,添加lib到模块
- 4,java 调用 C# 代码
![](/post-images/1659766121750.jpg)
![](/post-images/1659766125549.jpg)
```
package com.miaole.mlunityplugins_v1_1;

import android.app.Activity;
import android.content.Context;
import android.os.Vibrator;
import android.util.Log;
import android.widget.Toast;

import com.unity3d.player.UnityPlayer;

public class MLSDK {
    public static final String TAG = "MLSDK";
    public static Activity activity = null;
    public static Vibrator ChacheVb = null;

    public static Activity getActivity() {
        if (activity == null) {
            activity = UnityPlayer.currentActivity;
        }
        return activity;
    }

    //震动
    public static void Vibrator(long patter, int repeat) {
        if (ChacheVb != null) {
            ChacheVb.vibrate(patter);
            return;
        }
        ChacheVb = (Vibrator) getActivity().getSystemService(Context.VIBRATOR_SERVICE);
        if (ChacheVb != null) {
            ChacheVb.vibrate(patter);
        }
    }

    public static void ShowToast(String msg, int length) {
        Toast.makeText(getActivity(), "msg", length).show();
    }

    //Java 调用 C# 方法
    public static void SetName(String name) {
        UnityPlayer.UnitySendMessage("","","");
    }
}
```