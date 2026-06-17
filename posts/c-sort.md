---
id: xYgAy9
title: C# Sort
createdAt: "2023-03-14 20:40:56"
updated: "2026-06-17 10:11:00"
tags:
    - C#
tag_ids:
    - fOiXzM
categories:
    - 编程基础
category_ids:
    - kthGs4
published: true
hideInList: false
feature: ""
isTop: false
---

```
using System.Collections.Generic;
using UIFramework;
using UnityEngine;


public class SingleDebug : MonoBehaviour
{
#if UNITY_EDITOR
    // Start is called before the first frame update
    void Start() { }

    // Update is called once per frame
    void Update() { }

    private static SingleDebug Instance;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
    public static void Init()
    {
        if (Instance == null)
        {
            GameObject go = new GameObject("SingleDebug");
            Instance = go.GetOrAddComponent<SingleDebug>();
            DontDestroyOnLoad(go);
        }


        List<SortTest> sortTests = new List<SortTest>();
        //随机假数据
        for (int i = 0; i < 10; i++)
        {
            bool isGet = UnityEngine.Random.Range(0f, 1f) > 0.5f ? true : false;
            float progress = isGet ? 1 : Random.Range(0, 1f);
            SortTest sortTest = new SortTest(i,progress, isGet);
            sortTests.Add(sortTest);
        }

        /*
         * 排序
         * isGet == true 放在最后
         * progress 由大到小
         * **/
        sortTests.Sort((right, left) =>
        {
            int result = 0;// 0 不交换 1 
            if (right.IsGet)
            {
                if (left.IsGet)
                {
                    //都已领取
                    result = 0;
                }
                else
                {
                    //right > left 
                    result = 1;
                }
            }
            else
            {
                if (left.IsGet)
                {
                    //left>right
                    result = -1;
                }
                else
                {
                    if (right.Progress > left.Progress)
                    {
                        //right > left 
                        result = 1;
                    }
                    else
                    {
                        //left > right 
                        result = -1;
                    }
                }
            }

            return result;
        });

        //sortTests.Sort((right, left) =>
        //{
        //    int result = 0;// 0 不交换 1 
        //    if (right.IsGet)
        //    {
        //        if (left.IsGet)
        //        {
        //            //都已领取
        //            result = 0;
        //        }
        //        else
        //        {
        //            //right > left 
        //            result = -1;
        //        }
        //    }
        //    else
        //    {
        //        if (left.IsGet)
        //        {
        //            //left>right
        //            result = 1;
        //        }
        //        else
        //        {
        //            if (right.Progress > left.Progress)
        //            {
        //                //right > left 
        //                result = -1;
        //            }
        //            else
        //            {
        //                //left > right 
        //                result = 1;
        //            }
        //        }
        //    }

        //    return result;
        //});

        for (int i = 0; i < sortTests.Count; i++)
        {
            Debug.Log(sortTests[i].IsGet);
        }
        for (int i = 0; i < sortTests.Count; i++)
        {
            Debug.Log(sortTests[i].Progress);
        }
    }

    private void FixedUpdate()
    {
        if (Input.GetKeyDown(KeyCode.A))
        {
            //UICtrl.OpenWindow<UITreasureConveyor>();
        }
    }

    public class SortTest
    {
        public int Index = 0;
        public float Progress;//进度
        public bool IsGet;//是否已经领取
        public SortTest(int index,float progress, bool isGet)
        {
            Index = index;
            Progress = progress;
            IsGet = isGet;
        }
    }
#endif
}
```