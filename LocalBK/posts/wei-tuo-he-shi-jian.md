---
title: '委托和事件'
date: 2023-03-25 14:38:25
tags: [UnityEngine,C#]
published: true
hideInList: false
feature: 
isTop: false
---
## 委托
+ 使用``delegate``关键字来声明
+ 委托是一个函数指针数组，运行时保存一个或多个方式引用，可以为null
+ 委托是独立的，不依赖于事件
+ 包含``Combine()``和``Remove()``方法，用于将方法添加到调用类表
+ 可以作为方法参数传递
+ =用于分配单个方法，+=分配多个方法
多播委托
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Main : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //create Game
        MainGame mainGame = new MainGame();
        //create Player
        List<Player> cachedPlayers = new List<Player>();
        for (int i = 0; i < 10; i++)
        {
            //Player player = new Player(mainGame.OnGameOverDelegate);
            Player player = new Player();
            cachedPlayers.Add(player);
        }
        //call MainGame GameOver
        mainGame.GameOver();
        //log

        //relesePlayer
        for (int i = 0; i < cachedPlayers.Count; i++)
        {
            cachedPlayers[i]?.Dispose();
            cachedPlayers[i] = null;
        }
        cachedPlayers.Clear();

        //call MainGame GameOver
        mainGame.GameOver();

        //可以直接赋值置空
        MainGame.OnGameOverDelegate = null;
    }

    // Update is called once per frame
    void Update()
    {

    }


}

public delegate void OnGameOverDelegate();
public class MainGame
{
    public static OnGameOverDelegate OnGameOverDelegate = null;

    public void GameOver()
    {
        OnGameOverDelegate?.Invoke();
    }
}

public class Player
{
    public static int PlayerIndex = 0;

    private int _playerIndex;
    public Player()
    {
        ++PlayerIndex;
        _playerIndex = PlayerIndex;
        MainGame.OnGameOverDelegate += OnGameOver;
    }

    public void Dispose()
    {
        MainGame.OnGameOverDelegate -= OnGameOver;
    }

    ~Player()
    {

    }

    private void OnGameOver()
    {
        Debug.Log($"player {_playerIndex} game over");
    }
}

```
## 事件
+ 使用``event``关键字来声明
+ 依赖于委托的通知机制
+ 依赖于委托，没有委托就无法创建，只允许添加或者移除目标
+ 通过``AddEventHandler()``和``RemoveEventHandler()``向调用类表添加或者移除方法
+ 事件被引发，不能作为方法参数传递
+ =运算符不能应用于事件
```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainEvent : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        //create Game
        MainGame1 mainGame = new MainGame1();
        //create Player
        List<Player> cachedPlayers = new List<Player>();
        for (int i = 0; i < 10; i++)
        {
            //Player player = new Player(mainGame.OnGameOverDelegate);
            Player player = new Player();
            cachedPlayers.Add(player);
        }
        //call MainGame GameOver
        mainGame.GameOver();
        //log

        //relesePlayer
        for (int i = 0; i < cachedPlayers.Count; i++)
        {
            cachedPlayers[i]?.Dispose();
            cachedPlayers[i] = null;
        }
        cachedPlayers.Clear();

        //call MainGame GameOver
        mainGame.GameOver();

        //不能直接赋值
        MainGame1.OnGameOverDelegateEvent = null;
    }

    // Update is called once per frame
    void Update()
    {

    }


}

public class MainGame1
{
    public static event OnGameOverDelegate OnGameOverDelegateEvent;
    public void GameOver()
    {
        OnGameOverDelegateEvent?.Invoke();
    }
}

public class Player1
{
    public static int PlayerIndex = 0;

    private int _playerIndex;
    public Player1()
    {
        ++PlayerIndex;
        _playerIndex = PlayerIndex;
        MainGame1.OnGameOverDelegateEvent += OnGameOver;

    }

    public void Dispose()
    {
        MainGame1.OnGameOverDelegateEvent -= OnGameOver;
    }

    ~Player1()
    {

    }

    private void OnGameOver()
    {
        Debug.Log($"player {_playerIndex} game over");
    }
}

```