---
title: 'Odin Inspector'
date: 2022-09-25 14:02:55
tags: [Unity,UnityEditor]
published: true
hideInList: false
feature: 
isTop: false
---
- 记录一下Odin一些常用功能
## 标题类型
```
[Title("Name")]
//标题，类似于Unity 原生Header
```
## 限制数值
```
[Range(0,100)]
[MinValue(0)]
[MaxValue(0)]
[ProgressBar(0,100)]
```
## 颜色
```
[GUIColor(0,1,0)]//可以为字段，按钮添加颜色
```
## 提示信息
```
[ReadOnly]
[Title("")]
[Space]
[InfoBox("info")]
[Required("xx is Empty)]//空的时候会提示
```
## 显示在面板
```
[ShowInInspector]//私有成员,List,Map,类都可以显示
[HideInInspector]//隐藏在面板
[LabelText("描述")]//非常好用，直接显示描述
[InlineEditor(InlineEditorObjectFieldModes.Boxed)]//可以直接将.assets 文件显示在面板
[ShowIf("bool值")]//常用，通过bool决定是否显示在面板
```
## 分组
```
[TabGroup("GroupA")]
[TabGroup("GroupB")]
[TabGroup("GroupC")]
//可显示三个Group
```
## 按钮
```
[Button(60, Name = "Generate")]
[ButtonGroup("MybuttonGroup")]
```
## 路径
```
[FilePath]//文件路径
[FolderPath]//文件夹路径
```
## 窗口
```
//DG.Tweening TMPro
public class ABTestCreator : OdinEditorWindow
{
    [MenuItem("Tools/ABTest/Created  Prefab", false, 1)]
    private static void CreateABTestPrefab()
    {
        if (UnityEngine.Object.FindObjectOfType(typeof(ABTestHelper)) == null)
        {
            GameObject go = PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath(DebugEditor.WhereIs("ABTest.prefab", "Prefab"), typeof(GameObject))) as GameObject;
            go.name = "ABTest";
            Selection.activeObject = go;
            Undo.RegisterCreatedObjectUndo(go, "Created ABTest Object");
        }
        else
        {
            Debug.LogWarning("A ABTest object already exists in this scene - you should never have more than one per scene!");
        }
    }
    [MenuItem("Tools/ABTest/ Creator", false, 2)]
    private static void OpenWindow()
    {
        GetWindow<ABTestCreator>().Show();
    }
}
```
