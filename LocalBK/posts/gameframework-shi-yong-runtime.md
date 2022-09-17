---
title: 'GameFramework使用(Runtime)'
date: 2022-09-17 12:23:54
tags: [Unity,GameFramework]
published: true
hideInList: false
feature: /post-images/gameframework-shi-yong-runtime.png
isTop: false
---
# GameEntry
整个框架的启动入口
## Builtin:内置组件
### config
 Config 配置表位于Assets/GameMain/Configs/DefaultConfig
 ```
 //int类型值获取
 int c1 = GameEntry.Config.GetInt("configName");
 //float
 float c2 = GameEntry.Config.GetFloat("configName");
 //string
 string c3 = GameEntry.Config.GetString("configName");
 //bool
 bool c4 = GameEntry.Config.GetBool("configName");
```
### DataNode TODO
### DataTable 配置表位于Assets/GameMain/DataTables
```
//获取实体表
IDataTable<DREntity> table = GameEntry.DataTable.GetDataTable<DREntity>();
//获取单行数据 请确认ID存在 
int id = 1001;
DREntity dataRow = table.GetDataRow(id);
if (null == dataRow) UnityGameFramework.Runtime.Log.Error("实体表 编号{0} 不存在", id);
//获取所有表行数据
DREntity[] dREntities = table.GetAllDataRows();
//获取单行中数据
var tableRowData1 = dataRow.AssetName;
```
### Debugger 调试组件
```
//在开发阶段用于真机调试查看日志
GameEntry.Debugger.ActiveWindow = true;
```
### Download TODO
### Entity 实体模块
```
//显示实体  为异步操作 这里做了一层封装
string entityGroup = "Default";
GameEntry.Entity.ShowDefaultEntity<PlayerEntity>(new PlayerEntityData(dataRow.Id), entityGroup);
//"Player"为一个实体分组 增加或删除分组见Entity Inspector面板设置
/*
 * 如Default分组
 * Name 分组名称
 * Auto Release Interval 自动销毁时间
 * Capaclity 最大缓存数量
 * Expire Time 失效时间
 * */
//销毁实体
int childEntityID = 0;
int parentEntityID = 1;
GameEntry.Entity.HideEntity(childEntityID);
//附加实体
GameEntry.Entity.AttachEntity(childEntityID, parentEntityID);
//移除附加实体
GameEntry.Entity.DetachChildEntities(parentEntityID);
GameEntry.Entity.DetachEntity(childEntityID);
//隐藏莫个分组所有实体
GameEntry.Entity.HideAllLoadedEntities("entityGroup");
//隐藏全部实体
GameEntry.Entity.HideAllLoadedEntities();
GameEntry.Entity.HideAllLoadingEntities();
```
### Event
```
//订阅事件
//先定义事件类
GameEntry.Event.Subscribe(TempEvent.EventId, OnTempEvent);
//发送事件
GameEntry.Event.Fire(this, new TempEvent());//下一帧
GameEntry.Event.FireNow(this, new TempEvent());//立即
//取消订阅
GameEntry.Event.Unsubscribe(TempEvent.EventId, OnTempEvent);
```
```
protected virtual void OnTempEvent(object sender, GameEventArgs e)
{
        TempEvent tempEvent = (TempEvent)e;
        //如果传了参数可以拿到
}
public class TempEvent : GameEventArgs
{
    public static readonly int EventId = typeof(TempEvent).GetHashCode();
    public override int Id { get { return EventId; } }
    public TempEvent() { }
    public TempEvent(int param1) { }
    public TempEvent(string parem1) { }
    public override void Clear() { }
}
```
### FileSystem TODO
### Fsm TODO
### Localization 本地化
```
//全局配置位于Assets/GameMain/Configs/DefaultDictionary
//一份语言对应一份 xml配置文件(Assets/GameMain/Localization)
//增加一种语种 需要在 Recourse Editor中增加一个变体目录
GameEntry.Localization.GetString("languageKey");
//TODO 封装支持动态切换语言
```
### Network TODO
### ObjectPool
```
//创建引用池
var tempTestObjectPoolItem = new TestItem();
IObjectPool<TestObjectPoolItem> _itemObjectPool = GameEntry.ObjectPoolCreateSingleSpawnObjectPool<TestObjectPoolItem>("Test", 16);
//创建对象
TestObjectPoolItem itemObject = _itemObjectPool.Spawn();
if (itemObject != null)
{
    itemObject = (TestObjectPoolItem)itemObject.Target;
}
else
{
    itemObject = UnityEngine.Object.Instantiate(tempTestObjectPoolItem);
    _itemObjectPool.Register(TestObjectPoolItem.Create(itemObject), true);
}
//回收对象
_itemObjectPool.Unspawn(itemObject);
```
```
public class TestObjectPoolItem : ObjectBase
{
    public static TestObjectPoolItem Create(object target)
    {
        TestObjectPoolItem itemObject = ReferencePool.Acquire<TestObjectPoolItem>();
        itemObject.Initialize(target);
        return itemObject;
    }
    protected override void Release(bool isShutdown)
    {
        TestItem item = (TestItem)Target;
        if (item == null)
        {
            return;
        }
        Object.Destroy(item.gameObject);
    }
}
public class TestItem : MonoBehaviour
{
}
```
### Procedure 流程模块 TODO
### Resource 资源模块 加载图片为例
```
string path = "TestPath";
Image obj = new GameObject().AddComponent<Image>();
GameEntry.Resource.LoadAsset(path, Constant.AssetPriority.SpriteAsset, newLoadAssetCallbacks(LoadSuccessWhithNativeSize), obj);
```
### Scene 
```
//加载场景
GameEntry.Scene.LoadScene("Path");
//卸载场景
GameEntry.Scene.UnloadScene("Path");
/**
 *  UnityGameFramework.Runtime.LoadSceneSuccessEventArgs.EventId    加载成功
    UnityGameFramework.Runtime.LoadSceneFailureEventArgs.EventId    加载失败
    UnityGameFramework.Runtime.UnloadSceneFailureEventArgs.EventId  卸载成功
    UnityGameFramework.Runtime.UnloadSceneSuccessEventArgs.EventId  卸载失败
    UnityGameFramework.Runtime.LoadSceneUpdateEventArgs.EventId     加载进度
    具体 监听参考 Event 模块
 * */
```
### Setting 存储模块
```
//存储 Key + Object
GameEntry.Setting.SetObject("UserData", null);
/*
 *  GameEntry.Setting.SetBool();
 *  GameEntry.Setting.SetFloat();
 *  GameEntry.Setting.SetInt();
 *  GameEntry.Setting.SetString();
 *  建议不同的数据存储类型不一样，方便于数据清理
 * **/
//获取同上Get
```
### Sound 声音模块 配置表位于Assets/GameMain/DataTables
```
//播放音效 封装过
GameEntry.Sound.PlaySound(1001);
//TODO 封装音效循环 封装相同音效只允许存在单个
```
### UI UI模块 配置表位于Assets/GameMain/DataTables
```
//打开
int gameFormId = (int)GameEntry.UI.OpenUIForm(UIFormId.GameForm);
//关闭
GameEntry.UI.CloseUIForm(gameFormId);
//关闭所有
GameEntry.UI.CloseAllLoadedUIForms();
GameEntry.UI.CloseAllLoadingUIForms();
```
### WebRequest TODO

## Customs:自定义组件
### 如Native 
```
脚本  NativeComponent : GameFrameworkComponent 并挂载于GF节点下
//GameEntry获取
NativeComponent Native = UnityGameFramework.Runtime.GameEntryGetComponent<NativeComponent>();
//全局使用
GameEntry.Native.Vibrate(50);
//其他同
```
# 传送门
### [GameFramework官网](https://gameframework.cn/)
### [GameFramework仓库](https://github.com/EllanJiang/GameFramework)