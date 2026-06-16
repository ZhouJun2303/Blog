---
id: G3qaRS
title: EditorAttribute
createdAt: "2022-03-02 14:42:08"
updated: "2026-06-16 17:26:22"
tags:
    - Unity
    - UnityEditor
tag_ids:
    - FjODty
    - J7VXMO
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

```
[InitializeOnEnterPlayModeAttribute]
作用于静态方法，使编辑器类方法在进入 Play Mode 时初始化

[MenuItem("WarlGMenu/Item #&g")]
static void WarlGMenuItem()
{
}
作用于静态方法，为主菜单和 Inspector context menu 添加选项
可添加快捷键：%（ctrl 或 command，区别于 Windows 或 MacOS） #（Shift） &（Alt）
#LEFT （左Shift）LEFT, RIGHT, UP, DOWN, F1 .. F12, HOME, END, PGUP, PGDN等
如：WarlGMenu/Item #&g 即 shift-alt-G WarlGMenu/Item _g 即仅适用 G 键

OnOpenAssetAttribute
作用于静态方法，当 Unity 将要打开一个 Asset 时，该方法被调用需满足如下条件：
static bool OnOpenAsset(int instanceID, int line)
static bool OnOpenAsset(int instanceID, int line, int column)
返回 true 表明由方法处理该 Asset，返回 false 表明外部打开

[PostProcessBuildAttribute(1)]
public static void OnPostprocessBuild(BuildTarget target, string pathToBuiltProject) {
  Debug.Log( pathToBuiltProject );
}
作用于静态方法，构建 Player 之后被调用

[PostProcessSceneAttribute]
作用于静态方法，构建 Scene 或 Play Mode 调用 SceneManager.LoadScene 方法后被调用


//Unity build 构建之前回调 可用于设置安卓密码
public interface IPreprocessBuildWithReport : IOrderedCallback{
    void OnPreprocessBuild(BuildReport report);
}
```