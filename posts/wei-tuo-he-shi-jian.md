---
id: s35UeN
title: 委托和事件
createdAt: "2023-03-25 14:38:25"
updated: "2026-07-01 21:36:05"
tags:
    - UnityEngine
    - C#
tag_ids:
    - UNR80K
    - fOiXzM
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---

## 先说结论

委托和事件最容易混在一起，是因为事件本身就是基于委托做的。

可以先这样记：

+ 委托是一个类型安全的方法引用，可以保存一个或多个方法
+ 多播委托用 `+=` 增加方法，用 `-=` 移除方法，调用时会按注册顺序执行
+ 事件是对委托字段的一层限制，外部只能订阅和取消订阅，不能直接赋值、清空或者主动触发

也就是说，委托解决的是“什么样的方法可以被保存和调用”，事件解决的是“谁有资格触发这个通知”。

## 委托

委托使用 `delegate` 关键字声明。

下面这个委托表示：只要是无参数、无返回值的方法，都可以被保存进来。

```csharp
public delegate void GameOverHandler();
```

比如游戏结束时，通知所有玩家处理结算逻辑：

```csharp
using UnityEngine;

public delegate void GameOverHandler();

public class GameWithDelegate
{
    public GameOverHandler OnGameOver;

    public void GameOver()
    {
        Debug.Log("game over");
        OnGameOver?.Invoke();
    }
}

public class DelegatePlayer
{
    private readonly GameWithDelegate _game;
    private readonly int _id;

    public DelegatePlayer(GameWithDelegate game, int id)
    {
        _game = game;
        _id = id;
        _game.OnGameOver += HandleGameOver;
    }

    public void Dispose()
    {
        _game.OnGameOver -= HandleGameOver;
    }

    private void HandleGameOver()
    {
        Debug.Log($"player {_id} handle game over");
    }
}
```

使用时可以注册多个玩家：

```csharp
public class DelegateExample : MonoBehaviour
{
    private void Start()
    {
        GameWithDelegate game = new GameWithDelegate();

        DelegatePlayer player1 = new DelegatePlayer(game, 1);
        DelegatePlayer player2 = new DelegatePlayer(game, 2);

        game.GameOver();

        player1.Dispose();
        player2.Dispose();
    }
}
```

输出结果大概是：

```text
game over
player 1 handle game over
player 2 handle game over
```

这个例子能跑，但它有一个问题：`OnGameOver` 是公开的委托字段，外部代码权限太大。

```csharp
game.OnGameOver = null;        // 可以清空所有订阅
game.OnGameOver = SomeMethod;  // 可以覆盖之前的订阅
game.OnGameOver?.Invoke();     // 可以在外部主动触发
```

这就是公开委托字段不适合做“事件通知”的原因。游戏结束应该只能由 `GameWithDelegate` 自己触发，而不是任何拿到 `game` 对象的代码都能触发。

## 事件

事件使用 `event` 关键字声明，但它仍然需要一个委托类型。

把上面的例子改成事件，只需要改 `Game` 这一层：

```csharp
using UnityEngine;

public delegate void GameOverHandler();

public class GameWithEvent
{
    public event GameOverHandler OnGameOver;

    public void GameOver()
    {
        Debug.Log("game over");
        OnGameOver?.Invoke();
    }
}
```

玩家订阅事件的方式不变：

```csharp
public class EventPlayer
{
    private readonly GameWithEvent _game;
    private readonly int _id;

    public EventPlayer(GameWithEvent game, int id)
    {
        _game = game;
        _id = id;
        _game.OnGameOver += HandleGameOver;
    }

    public void Dispose()
    {
        _game.OnGameOver -= HandleGameOver;
    }

    private void HandleGameOver()
    {
        Debug.Log($"player {_id} handle game over");
    }
}
```

使用方式也差不多：

```csharp
public class EventExample : MonoBehaviour
{
    private void Start()
    {
        GameWithEvent game = new GameWithEvent();

        EventPlayer player1 = new EventPlayer(game, 1);
        EventPlayer player2 = new EventPlayer(game, 2);

        game.GameOver();

        player1.Dispose();
        player2.Dispose();
    }
}
```

区别在于，外部代码现在只能 `+=` 和 `-=`：

```csharp
game.OnGameOver += SomeMethod;
game.OnGameOver -= SomeMethod;
```

下面这些写法都会编译失败：

```csharp
game.OnGameOver = null;
game.OnGameOver = SomeMethod;
game.OnGameOver?.Invoke();
```

事件的意义就在这里：订阅者可以说“游戏结束时通知我”，但不能反过来控制整个通知列表，更不能替 `GameWithEvent` 假装游戏结束。

## 对比

| 对比项 | 委托字段 | 事件 |
| --- | --- | --- |
| 声明方式 | `public GameOverHandler OnGameOver;` | `public event GameOverHandler OnGameOver;` |
| 外部订阅 | 可以 `+=` | 可以 `+=` |
| 外部取消订阅 | 可以 `-=` | 可以 `-=` |
| 外部直接赋值 | 可以 | 不可以 |
| 外部清空 | 可以 | 不可以 |
| 外部触发 | 可以 | 不可以 |
| 适合场景 | 回调参数、策略传入、临时方法组合 | 对外发布通知 |

## Unity 里怎么用

Unity 里更常见的写法是：在 `OnEnable` 里订阅，在 `OnDisable` 里取消订阅。

```csharp
using UnityEngine;

public class GameController : MonoBehaviour
{
    public event GameOverHandler OnGameOver;

    public void GameOver()
    {
        OnGameOver?.Invoke();
    }
}

public class PlayerView : MonoBehaviour
{
    [SerializeField] private GameController gameController;

    private void OnEnable()
    {
        gameController.OnGameOver += HandleGameOver;
    }

    private void OnDisable()
    {
        gameController.OnGameOver -= HandleGameOver;
    }

    private void HandleGameOver()
    {
        Debug.Log("show game over ui");
    }
}
```

如果只是把一个方法当参数传进去，比如排序规则、按钮回调、异步完成回调，用委托就够了。

如果是一个对象向外发布通知，比如游戏结束、血量变化、网络断开，优先用事件。这样外部只能监听，不能越权修改发布者内部的通知列表。
