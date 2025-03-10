---
title: 'Unity Task'
date: 2025-03-10 11:36:29
tags: [UnityEngine]
published: true
hideInList: false
feature: 
isTop: false
---

# 原生Task
## 使用
```
await Test3();
private async Task Test3()
{
    Debug.Log($"TimeNow3_1 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow3_2 {DateTime.Now.ToString()}");
}
```
- 使用关键字 async 和 await 
## 编译之后源码 
```
[AsyncStateMachine(typeof(<Test3>d__8))]
private Task Test3()
{
	<Test3>d__8 stateMachine = default(<Test3>d__8);
	stateMachine.<>t__builder = AsyncTaskMethodBuilder.Create();
	stateMachine.<>1__state = -1;
	AsyncTaskMethodBuilder <>t__builder = stateMachine.<>t__builder;
	<>t__builder.Start(ref stateMachine);
	return stateMachine.<>t__builder.Task;
}
```
- 方法编译源码
- 由 AsyncTaskMethodBuilder 生成了一个新的状态机继承IAsyncStateMachine
```
private struct <Test3>d__8 : IAsyncStateMachine
{
	public int <>1__state;

	public AsyncTaskMethodBuilder <>t__builder;

	private object <>u__1;

	private void MoveNext()
	{
		int num = <>1__state;
		try
		{
			IEnumeratorAwaitExtensions.SimpleCoroutineAwaiter awaiter;
			if (num != 0)
			{
				UnityEngine.Debug.Log("TimeNow3_1 " + DateTime.Now.ToString());
				awaiter = IEnumeratorAwaitExtensions.GetAwaiter(new WaitForSeconds(3f));
				if (!awaiter.IsCompleted)
				{
					num = (<>1__state = 0);
					<>u__1 = awaiter;
					<>t__builder.AwaitOnCompleted(ref awaiter, ref this);
					return;
				}
			}
			else
			{
				awaiter = (IEnumeratorAwaitExtensions.SimpleCoroutineAwaiter)<>u__1;
				<>u__1 = null;
				num = (<>1__state = -1);
			}
			awaiter.GetResult();
			UnityEngine.Debug.Log("TimeNow3_2 " + DateTime.Now.ToString());
		}
		catch (Exception exception)
		{
			<>1__state = -2;
			<>t__builder.SetException(exception);
			return;
		}
		<>1__state = -2;
		<>t__builder.SetResult();
	}

	void IAsyncStateMachine.MoveNext()
	{
		//ILSpy generated this explicit interface implementation from .override directive in MoveNext
		this.MoveNext();
	}

	[DebuggerHidden]
	private void SetStateMachine(IAsyncStateMachine stateMachine)
	{
		<>t__builder.SetStateMachine(stateMachine);
	}

	void IAsyncStateMachine.SetStateMachine(IAsyncStateMachine stateMachine)
	{
		//ILSpy generated this explicit interface implementation from .override directive in SetStateMachine
		this.SetStateMachine(stateMachine);
	}
}
```
以 await 为分隔符，分成不同的State

# 参考ETTask实现一个最基本的 [ET文档](https://et-framework.cn/)
## 实现
### 使用System.Runtime.CompilerServices.AsyncMethodBuilder(typeof(MyAsyncTaskMethodBuilder)
```
  [System.Runtime.CompilerServices.AsyncMethodBuilder(typeof(MyAsyncTaskMethodBuilder))]
  public class MyTask : ICriticalNotifyCompletion, INotifyCompletion
  {
      ...other code
```
### 实现 MyAsyncTaskMethodBuilder
```
 public struct MyAsyncTaskMethodBuilder
 {
     public MyTask _tsc;
     public MyTask Task
     {
         get
         {
             return _tsc;
         }
     }

     public static MyAsyncTaskMethodBuilder Create()
     {
         MyAsyncTaskMethodBuilder builder = new MyAsyncTaskMethodBuilder() { _tsc = MyTask.Create() };
         return builder;
     }
     ...other code
```
## 使用
```
/// <summary>
/// My Task
/// </summary>
/// <returns></returns>
private async MyTask Test1()
{
    Debug.Log($"TimeNow1_1 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow2_1 {DateTime.Now.ToString()}");
}


/// <summary>
/// My Task
/// </summary>
/// <returns></returns>
private async MyTask Test2()
{
    Debug.Log($"TimeNow2_1 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow2_2 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow2_3 {DateTime.Now.ToString()}");
}

private async Task Test3()
{
    Debug.Log($"TimeNow3_1 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow3_2 {DateTime.Now.ToString()}");
}

private async Task Test4()
{
    Debug.Log($"TimeNow4_1 {DateTime.Now.ToString()}");
    await new WaitForSeconds(3);
    Debug.Log($"TimeNow4_2 {DateTime.Now.ToString()}");
}

private async MyTask Test5()
{
    await Test1();
    await Test2();
    await Test3();
    await Test4();
    await new WaitForSeconds(5);
    Test6();
}


private void Test6()
{
    Test1();
    Test2();
    Test3();
    Test4();
}
```
## 查看编译之后的代码
- 重点查看 Test5 编译之后
```
private struct <Test5>d__10 : IAsyncStateMachine
	{
		public int <>1__state;

		public MyAsyncTaskMethodBuilder <>t__builder;

		public launchGame <>4__this;

		private object <>u__1;

		private TaskAwaiter <>u__2;

		private void MoveNext()
		{
			int num = <>1__state;
			launchGame launchGame2 = <>4__this;
			try
			{
				MyTask awaiter3;
				TaskAwaiter awaiter2;
				IEnumeratorAwaitExtensions.SimpleCoroutineAwaiter awaiter;
				switch (num)
				{
				default:
					awaiter3 = launchGame2.Test1().GetAwaiter();
					if (!awaiter3.IsCompleted)
					{
						num = (<>1__state = 0);
						<>u__1 = awaiter3;
						<>t__builder.AwaitUnsafeOnCompleted(ref awaiter3, ref this);
						return;
					}
					goto IL_007b;
				case 0:
					awaiter3 = (MyTask)<>u__1;
					<>u__1 = null;
					num = (<>1__state = -1);
					goto IL_007b;
				case 1:
					awaiter3 = (MyTask)<>u__1;
					<>u__1 = null;
					num = (<>1__state = -1);
					goto IL_00d4;
				case 2:
					awaiter2 = <>u__2;
					<>u__2 = default(TaskAwaiter);
					num = (<>1__state = -1);
					goto IL_012e;
				case 3:
					awaiter2 = <>u__2;
					<>u__2 = default(TaskAwaiter);
					num = (<>1__state = -1);
					goto IL_0189;
				case 4:
					{
						awaiter = (IEnumeratorAwaitExtensions.SimpleCoroutineAwaiter)<>u__1;
						<>u__1 = null;
						num = (<>1__state = -1);
						break;
					}
					IL_0189:
					awaiter2.GetResult();
					awaiter = IEnumeratorAwaitExtensions.GetAwaiter(new WaitForSeconds(5f));
					if (!awaiter.IsCompleted)
					{
						num = (<>1__state = 4);
						<>u__1 = awaiter;
						<>t__builder.AwaitOnCompleted(ref awaiter, ref this);
						return;
					}
					break;
					IL_007b:
					awaiter3.GetResult();
					awaiter3 = launchGame2.Test2().GetAwaiter();
					if (!awaiter3.IsCompleted)
					{
						num = (<>1__state = 1);
						<>u__1 = awaiter3;
						<>t__builder.AwaitUnsafeOnCompleted(ref awaiter3, ref this);
						return;
					}
					goto IL_00d4;
					IL_012e:
					awaiter2.GetResult();
					awaiter2 = launchGame2.Test4().GetAwaiter();
					if (!awaiter2.IsCompleted)
					{
						num = (<>1__state = 3);
						<>u__2 = awaiter2;
						<>t__builder.AwaitUnsafeOnCompleted(ref awaiter2, ref this);
						return;
					}
					goto IL_0189;
					IL_00d4:
					awaiter3.GetResult();
					awaiter2 = launchGame2.Test3().GetAwaiter();
					if (!awaiter2.IsCompleted)
					{
						num = (<>1__state = 2);
						<>u__2 = awaiter2;
						<>t__builder.AwaitUnsafeOnCompleted(ref awaiter2, ref this);
						return;
					}
					goto IL_012e;
				}
				awaiter.GetResult();
				launchGame2.Test6();
			}
			catch (Exception exception)
			{
				<>1__state = -2;
				<>t__builder.SetException(exception);
				return;
			}
			<>1__state = -2;
			<>t__builder.SetResult();
		}

        ...other code
```
- Unity 的Task 异步是伪异步，本质是状态机进行状态控制
# 其他异步
## 协程
```
	...other code
    StartCoroutine(Custom1Enumerator());
}

IEnumerator Custom1Enumerator()
{
    CustomLog("CustomEnumerator log1");
    yield return new WaitForSeconds(1);
    CustomLog("CustomEnumerator log2");
    yield return new WaitForFixedUpdate();
    CustomLog("CustomEnumerator log3");
    yield return new WaitForFixedUpdate();
    Invoke("InvokTest", 1);
}
```
- 编译成了 IEnumerator 迭代器 
```
private bool MoveNext()
	{
		int num = <>1__state;
		launchGame launchGame2 = <>4__this;
		switch (num)
		{
		default:
			return false;
		case 0:
			<>1__state = -1;
			launchGame2.CustomLog("CustomEnumerator log1");
			<>2__current = new WaitForSeconds(1f);
			<>1__state = 1;
			return true;
		case 1:
			<>1__state = -1;
			launchGame2.CustomLog("CustomEnumerator log2");
			<>2__current = new WaitForFixedUpdate();
			<>1__state = 2;
			return true;
		case 2:
			<>1__state = -1;
			launchGame2.CustomLog("CustomEnumerator log3");
			<>2__current = new WaitForFixedUpdate();
			<>1__state = 3;
			return true;
		case 3:
			<>1__state = -1;
			launchGame2.Invoke("InvokTest", 1f);
			return false;
		}
	}
```
## Invoke
```
Invoke("DelayedMethod", 3f); // 延迟 3 秒后调用 DelayedMethod 方法
```
- Invoke 不能取消，一个简单的延迟调用
