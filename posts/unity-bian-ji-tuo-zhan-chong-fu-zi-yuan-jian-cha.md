---
id: ety3Zc
title: Unity 编辑拓展(重复资源检查)
createdAt: "2022-08-18 09:28:28"
updated: "2026-06-17 10:11:00"
tags:
    - UnityEditor
    - Unity
tag_ids:
    - J7VXMO
    - FjODty
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

**用于解决项目中重复的资源**
## Code
```
using System.Collections;
using UnityEngine;
using UnityEditor;
using System.Security.Cryptography;
using System;
using System.IO;
using System.Collections.Generic;

namespace MLSpace.Editor
{
    //纯原生写法 不基于Ordin
    public sealed class DuplicateResourceWindows : EditorWindow
    {
        [MenuItem("Tools/Report/DuplicateResourceWindows", false, 12)]
        public static void DuplicateWindows()
        {
            DuplicateResourceWindows window = GetWindow<DuplicateResourceWindows>("Duplicate Resource", true);
#if UNITY_2019_3_OR_NEWER
            window.minSize = new Vector2(800f, 640f);
#else
            window.minSize = new Vector2(800f, 600f);
#endif
        }

        public static bool NeedRefresh = false;
        private Dictionary<string, List<string>> Duplicates = new Dictionary<string, List<string>>();

        private void OnGUI()
        {
            //GetDuplicateResource();
            EditorGUILayout.BeginVertical(GUILayout.Width(position.width), GUILayout.Height(position.height));
            {
                GUILayout.Space(5f);
                EditorGUILayout.LabelField("重复资源列表", EditorStyles.boldLabel);
                foreach (var key in Duplicates.Keys)
                {
                    EditorGUILayout.BeginVertical("box");
                    {
                        EditorGUILayout.BeginHorizontal();
                        {
                            EditorGUILayout.LabelField(key, GUILayout.Width(position.width - 200f));
                            if (GUILayout.Button("Select", GUILayout.Width(80f)))
                            {
                                SelectFile(key);
                            }
                            GUILayout.Space(5f);
                            if (GUILayout.Button("Delete", GUILayout.Width(80f)))
                            {
                                DeleteFile(key);
                            }
                        }
                        EditorGUILayout.EndHorizontal();
                        foreach (var vkey in Duplicates[key])
                        {
                            EditorGUILayout.BeginHorizontal();
                            {
                                EditorGUILayout.LabelField(vkey, GUILayout.Width(position.width - 200f));
                                if (GUILayout.Button("Select", GUILayout.Width(80f)))
                                {
                                    SelectFile(key);
                                }
                                GUILayout.Space(5f);
                                if (GUILayout.Button("Delete", GUILayout.Width(80)))
                                {
                                    DeleteFile(vkey);
                                }
                            }
                            EditorGUILayout.EndHorizontal();
                        }
                    }
                    EditorGUILayout.EndVertical();
                    GUILayout.Space(10f);
                }

            }
        }

        private void SelectFile(string path)
        {
            Selection.activeObject = AssetDatabase.LoadAssetAtPath<UnityEngine.Object>(path);
        }

        private void DeleteFile(string path)
        {
            if (File.Exists(path))
            {
                File.Delete(path);
                AssetDatabase.SaveAssets();
                AssetDatabase.Refresh();
            }
        }

        private void OnEnable()
        {
            GetDuplicateResource();
        }

        private void Update()
        {
            if (NeedRefresh)
            {
                NeedRefresh = false;
                GetDuplicateResource();
            }
        }

        private void GetDuplicateResource()
        {
            Duplicates.Clear();
            Dictionary<string, string> md5dic = new Dictionary<string, string>();
            string[] paths = AssetDatabase.FindAssets(
                "t:Scene t:Prefab t:Shader t:Model t:Material t:Texture t:AudioClip t:AnimationClip t:AnimatorController t:Font t:TextAsset t:ScriptableObject",
                new string[] { "Assets" });

            foreach (var prefabGuid in paths)
            {
                string prefabAssetPath = AssetDatabase.GUIDToAssetPath(prefabGuid);
                string[] depend = AssetDatabase.GetDependencies(prefabAssetPath, true);
                for (int i = 0; i < depend.Length; i++)
                {
                    string assetPath = depend[i];
                    AssetImporter importer = AssetImporter.GetAtPath(assetPath);
                    //满足贴图和模型资源
                    if (importer is TextureImporter || importer is ModelImporter || importer is AudioImporter)
                    {
                        string md5 = DuplicateResourceTools.GetMD5Hash(Path.Combine(Directory.GetCurrentDirectory(), assetPath));
                        string path;
                        if (!md5dic.TryGetValue(md5, out path))
                        {
                            md5dic[md5] = assetPath;
                        }
                        else
                        {
                            if (path != assetPath)
                            {
                                InitDuplcates(path);
                                Duplicates[path].Add(assetPath);
                            }
                        }
                    }
                }
            }
            //Debug.Log(Duplicates);
        }

        private void InitDuplcates(string path)
        {
            if (path == null) return;
            if (!Duplicates.ContainsKey(path))
            {
                Duplicates[path] = new List<string>();
            }
        }
    }
}
```
## 测试一下
![](/post-images/1660787596237.jpg)
## 在需要打包之前或者上传Git之前可以加上自动检测，有重复资源自动打开页面