---
title: 'Unity 编辑拓展(UI拖拽师失业)'
date: 2022-08-18 09:54:56
tags: [UnityEditor,Unity]
published: true
hideInList: false
feature: 
isTop: false
---

<!-- more -->
## **先来看看效果**
<!-- more -->

![](https://zhoujun2303.github.io/post-images/1660790489890.gif)

<!-- more -->

## **设计思路**
- 找到子gameObject身上的组件
- 找到父gameObject的位置
- 生成父类
- 写入内存

## **CreateMember.cs**
```
using UnityEngine;
using UnityEditor;
using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;

namespace MLSpace.Editor
{
    public class CreateMember
    {
        private const string BR = "\n";
        private const string YH = "\"";
        private const string publicMember = "_b";
        private const string privateMember = "_i";
        private const string protectedMember = "_o";

        private static List<string> _memberNames = new List<string>();
        private static readonly string[] regularName = new string[] { "Image" };
        private const string TempTextPath = "CreateMember/Editor/MemberTemp.txt";
        private static bool _getChildByChild = false;

        [MenuItem("GameObject/CreateChildMember", priority = 0)]
        private static void CreateChildMember()
        {
            _getChildByChild = false;
            //找组件
            GameObject gameObject = (GameObject)Selection.activeObject;
            if (!gameObject)
            {
                Debug.LogWarning("Selection activeObject is empty!");
                return;
            }
            Component[] comps = gameObject.GetComponents<MonoBehaviour>();
            if (comps.Length == 0)
            {
                Debug.LogWarning(gameObject.name + " no component expand MonoBehaviour!");
                return;
            }
            GenerateCode(gameObject);
        }

        [MenuItem("GameObject/CreateChildByChildMember", priority = 0)]
        private static void CreateChildByChildMember()
        {
            _getChildByChild = true;
            //找组件
            GameObject gameObject = (GameObject)Selection.activeObject;
            if (!gameObject)
            {
                Debug.LogWarning("Selection activeObject is empty!");
                return;
            }
            Component[] comps = gameObject.GetComponents<MonoBehaviour>();
            if (comps.Length == 0)
            {
                Debug.LogWarning(gameObject.name + " no component expand MonoBehaviour!");
                return;
            }
            GenerateCode(gameObject);
        }

        private static void GenerateCode(GameObject gameObject)
        {
            //脚本位置
            string CodePath = GetPath(GetBriefComponentName(gameObject));
            if (CodePath == "")
            {
                Debug.Log("找不到脚本位置");
                return;
            }
            Debug.Log(CodePath);
            if (CodePath.IndexOf("Packages/com") != -1)
            {
                Debug.LogWarning(CodePath + " is system folder");
                return;
            }
            //生成分类
            string newCodePath = CodePath.Remove(CodePath.Length - 2) + "Member.cs";
            string templatePath = Path.Combine(Application.dataPath, TempTextPath);
            string codePath = newCodePath;
            string templateContents = File.ReadAllText(templatePath);
            string result = "";
            using (TextReader reader = new StringReader(templateContents))
            {
                while (reader.Peek() != -1)
                {
                    string line = reader.ReadLine();
                    if (line.Contains("__DATA_TABLE_CREATE_TIME__"))
                    {
                        line = line.Replace("__DATA_TABLE_CREATE_TIME__", DateTime.UtcNow.ToLocalTime().ToString("yyyy-MM-dd HH:mm:ss.fff"));
                    }
                    if (line.Contains("__CLASSNAME__"))
                    {
                        line = line.Replace("__CLASSNAME__", GetBriefComponentName(gameObject));
                    }
                    if (line.Trim().Equals("__MEMBERNAME__"))
                    {
                        result += GetMemberNameStr(gameObject);
                        continue;
                    }
                    if (line.Trim().Equals("__GETCOMPONENT__"))
                    {
                        result += GetGetComponentStr(gameObject);
                        continue;
                    }
                    result += line + "\n";
                }
                reader.Close();
            }
            File.WriteAllText(codePath, result);
            AssetDatabase.SaveAssets();
            AssetDatabase.Refresh();
            Debug.Log(newCodePath + "create success");
        }

        /// <summary>
        /// 获取成员str
        /// </summary>
        /// <param name="go"></param>
        /// <returns></returns>
        private static string GetMemberNameStr(GameObject go)
        {
            string str = "";
            _memberNames.Clear();
            Transform[] childs = _getChildByChild ? GetChildsByChild(go) : GetChilds(go);
            for (int i = 0; i < childs.Length; i++)
            {
                if (childs[i].name.StartsWith(publicMember))
                {
                    string memberName = InitialsCapitalize(childs[i].name);
                    _memberNames.Add(memberName);
                    str += "" +
                        "        public " + GetBriefComponentName(childs[i].gameObject) + " " + memberName + ";" + BR;
                }
                if (childs[i].name.StartsWith(privateMember))
                {
                    string memberName = InitialsLowercase(childs[i].name);
                    _memberNames.Add(memberName);
                    str += "" +
                        "        private " + GetBriefComponentName(childs[i].gameObject) + " " + memberName + "; " + BR;
                }
                if (childs[i].name.StartsWith(protectedMember))
                {
                    string memberName = InitialsCapitalize(childs[i].name);
                    _memberNames.Add(memberName);
                    str += "" +
                        "        protected " + GetBriefComponentName(childs[i].gameObject) + " " + memberName + "; " + BR;
                }
            }
            return str;
        }

        /// <summary>
        /// 方法体内
        /// </summary>
        /// <param name="go"></param>
        /// <returns></returns>
        private static string GetGetComponentStr(GameObject go)
        {
            string str = "";
            int index = 0;
            Transform[] childs = _getChildByChild ? GetChildsByChild(go) : GetChilds(go);
            for (int i = 0; i < childs.Length; i++)
            {
                if (childs[i].name.StartsWith(publicMember)
                    || childs[i].name.StartsWith(privateMember)
                    || childs[i].name.StartsWith(protectedMember))
                {
                    str += "" +
                        "            " + _memberNames[index] + " = " +
                        "transform.FindChildByChild(" + YH + childs[i].name + YH + ")." +
                        "GetComponent<" + GetBriefComponentName(childs[i].gameObject) + ">();" + BR;
                    index++;
                }
            }
            return str;
        }

        private static Transform[] GetChilds(GameObject go)
        {
            Transform[] ts = new Transform[go.transform.childCount];
            for (int i = 0; i < ts.Length; i++)
            {
                ts[i] = go.transform.GetChild(i);
            }
            return ts;
        }

        private static Transform[] GetChildsByChild(GameObject go)
        {
            Transform[] ts = go.transform.GetComponentsInChildren<Transform>();
            return ts;
        }

        #region Tools
        //大写
        private static string InitialsCapitalize(string str)
        {
            string newStr = CropCharTwo(str);
            return newStr.First().ToString().ToUpper() + newStr.Substring(1);
        }
        //小写
        private static string InitialsLowercase(string str)
        {
            string newStr = CropCharTwo(str);
            return "_" + newStr.First().ToString().ToLower() + newStr.Substring(1);
        }
        //裁剪
        private static string CropCharTwo(string str)
        {
            return str.Remove(0, 2);
        }
        /// <summary>
        /// 获取组件名字(包含命名空间)
        /// </summary>
        /// <param name="go"></param>
        /// <returns></returns>
        private static string GetComponentName(GameObject go)
        {
            Component[] comps = go.GetComponents<MonoBehaviour>();
            if (comps.Length == 0)
            {
                Debug.LogWarning(go.name + " no component expand MonoBehaviour!");
                return "Transform";
            }
            return comps[comps.Length - 1].GetType().ToString();
        }

        /// <summary>
        /// 获取组件简单名字
        /// </summary>
        /// <param name="go"></param>
        /// <returns></returns>
        private static string GetBriefComponentName(GameObject go)
        {
            string name = GetComponentName(go);
            string[] newNames = name.Split('.');
            string BriefName = newNames[newNames.Length - 1];
            return BriefName;
        }

        /// <summary>
        /// 获取脚本路径
        /// </summary>
        /// <param name="_scriptName"></param>
        /// <returns></returns>
        static string GetPath(string _scriptName)
        {
            Debug.Log("scriptName " + _scriptName);
            for (int i = 0; i < regularName.Length; i++)
            {
                if (regularName[i] == _scriptName) return "";
            }
            string[] newPath = _scriptName.Split('.');
            string[] path = UnityEditor.AssetDatabase.FindAssets(newPath[newPath.Length - 1]);
            for (int i = 0; i < path.Length; i++)
            {
                string _path = AssetDatabase.GUIDToAssetPath(path[i]);
                string[] names = _path.Split('/');
                if (names[names.Length - 1].Equals(string.Format("{0}.cs", _scriptName)))
                {
                    if (File.Exists(_path) && _path.EndsWith(".cs"))
                    {
                        return _path;
                    }
                }
            }
            return "";
        }
        #endregion
    }
}
```

## **MemberTemp.txt**
```

using System;
using TMPro;
using UnityEngine;
using UnityEngine.UI;
using UnityGameFramework.Runtime;
//------------------------------------------------------------
// 此文件由工具自动生成，请勿直接修改。
// 生成时间：__DATA_TABLE_CREATE_TIME__
//------------------------------------------------------------
namespace MLSpace
{
    public partial class __CLASSNAME__
    {

        __MEMBERNAME__

        protected virtual void InitMember()
        {
            __GETCOMPONENT__
        }
    }
}
```

编辑器拓展真有意思！🤡