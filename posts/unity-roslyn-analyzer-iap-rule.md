---
id: UaR015
title: Unity Roslyn Analyzer 实战：首次接入与二次更新
createdAt: "2026-07-15 12:10:00"
updated: "2026-07-15 14:18:00"
tags:
    - Unity
    - C#
    - 工程规范
tag_ids:
    - FjODty
    - fOiXzM
    - 9dEULI
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: ""
isTop: false
---
## 背景

有些工程规范不适合只靠 Code Review 或提交前脚本兜底。比如支付、登录、资源加载、埋点等关键入口，团队通常会约定只能从统一门面调用。如果业务代码直接调用底层接口，功能可能还能跑，但链路上的打点、弹窗、校验、风控或状态管理就可能被绕开。

这类问题最好的反馈位置是编译期：一写错，IDE 或 Unity 编译马上报错。

这次实战目标是：用 Unity 的 Roslyn Analyzer 写一条规则，把某个禁止直接调用的 API 变成编译错误。示例规则如下：

```csharp
GameEntity.IAP.Buy(...)
```

除统一入口文件外，其它 Hotfix 业务代码里一旦出现该直接调用，就报编译错误。

最终效果类似：

```text
error HLWD001: 禁止在此处直接调用 GameEntity.IAP.Buy(...)；请通过统一入口触发支付
```

## 一、首次接入 Roslyn Analyzer 怎么做

首次接入不要先写一堆规则。先选一个边界清晰、误报低、能稳定复现的工程约束，把整条链路跑通。

推荐流程：

1. 明确规则口径。
2. 建立 Analyzer 源码项目。
3. 实现一条 `DiagnosticAnalyzer`。
4. 构建 Analyzer DLL。
5. 让 Unity 把 DLL 识别为 Roslyn Analyzer。
6. 用违规样例和合法样例验证。
7. 再接入真实项目编译。

本次规则口径是：只允许统一入口文件调用 `GameEntity.IAP.Buy(...)`，其它业务代码都禁止直接调用。

Analyzer 项目建议单独放在工具目录，例如：

```text
Tools/CodeAnalyzer/Analyzer/
```

Unity 侧只放最终产物：

```text
Assets/Analyzers/ProjectRules.Analyzer.dll
```

这样源码和 Unity 加载的 DLL 分开，后续维护更清楚。

## 二、Unity 侧首次接入要点

Unity 2022.3 支持把 Roslyn Analyzer DLL 作为编译期分析器加载。接入时有几个关键点：

1. Analyzer DLL 必须在 `Assets` 目录下，例如：

```text
Assets/Analyzers/ProjectRules.Analyzer.dll
```

2. 这个 DLL 是编译期工具，不是运行时代码，所以插件平台要禁用，避免被打进运行程序集。

3. 给 DLL 的 `.meta` 增加 Unity 识别标签：

```yaml
labels:
- RoslynAnalyzer
```

4. Analyzer 项目建议目标框架使用：

```text
netstandard2.0
```

5. Unity 2022.3 的 Roslyn 兼容性更接近 `Microsoft.CodeAnalysis 3.8`，不要随手引用过新的 4.x 版本，否则 Unity 编译链路可能加载失败。

Unity 官方文档：

```text
https://docs.unity3d.com/2022.3/Documentation/Manual/roslyn-analyzers.html
```

如果 Unity 生成的 `.csproj` 里没有出现 `<Analyzer Include="..." />`，优先检查 DLL 的 `.meta` 是否有 `RoslynAnalyzer` 标签。

## 三、规则的核心设计

规则 ID 要稳定：

```csharp
public const string DiagnosticId = "HLWD001";
```

必须阻断编译的规则使用 Error：

```csharp
DiagnosticSeverity.Error
```

注册检查点：

```csharp
context.RegisterSyntaxNodeAction(AnalyzeInvocation, SyntaxKind.InvocationExpression);
```

为什么检查 `InvocationExpression`？因为目标是函数调用：

```csharp
GameEntity.IAP.Buy(productId);
```

它在语法树里大致是两层成员访问：

```text
Buy
└── IAP
    └── GameEntity
```

因此可以用 `MemberAccessExpressionSyntax` 做结构匹配，而不是用字符串搜索。

## 四、文件范围和白名单

规则不应该扫所有 C# 文件，只扫业务热更新代码目录，例如：

```text
Assets/Scripts_Hotfix/
```

并放行统一入口文件，例如：

```text
Assets/Scripts_Hotfix/Modules/IAP/IAPEventCenter.cs
```

路径判断要统一分隔符：

```csharp
string normalizedPath = filePath.Replace('\\', '/');
```

然后判断：

```csharp
normalizedPath.IndexOf("Assets/Scripts_Hotfix/", StringComparison.OrdinalIgnoreCase) >= 0
```

白名单文件直接 return：

```csharp
normalizedPath.EndsWith(
    "Assets/Scripts_Hotfix/Modules/IAP/IAPEventCenter.cs",
    StringComparison.OrdinalIgnoreCase)
```

这样 Windows 和 macOS/Linux 路径都能兼容。

## 五、核心匹配逻辑

示意代码：

```csharp
private static bool IsDirectIapBuyCall(ExpressionSyntax expression)
{
    if (!(expression is MemberAccessExpressionSyntax buyAccess))
    {
        return false;
    }

    if (buyAccess.Name.Identifier.ValueText != "Buy")
    {
        return false;
    }

    if (!(buyAccess.Expression is MemberAccessExpressionSyntax iapAccess))
    {
        return false;
    }

    if (iapAccess.Name.Identifier.ValueText != "IAP")
    {
        return false;
    }

    return iapAccess.Expression is IdentifierNameSyntax gameEntity
        && gameEntity.Identifier.ValueText == "GameEntity";
}
```

这条规则只处理直接调用：

```csharp
GameEntity.IAP.Buy(productId);
```

如果有人写：

```csharp
var iap = GameEntity.IAP;
iap.Buy(productId);
```

这应该由另一条规则处理：禁止缓存 `GameEntity` / `GameQuery` 模块引用。规则拆开维护更清晰。

## 六、构建 Analyzer DLL

如果能正常 restore，可以用普通 SDK 项目构建。但在一些本地环境里，NuGet 目录权限、缓存锁、离线环境会让 `dotnet restore` 不稳定。

更稳的方案是准备一个构建脚本，直接调用本机 SDK 自带的 Roslyn 编译器：

```powershell
.\Tools\CodeAnalyzer\build-analyzer.ps1
```

脚本大致做这些事：

1. 定位 `csc.dll`。
2. 引用 Unity 兼容的 `Microsoft.CodeAnalysis.dll`。
3. 引用 `Microsoft.CodeAnalysis.CSharp.dll`。
4. 引用 `System.Collections.Immutable.dll`。
5. 使用 `netstandard2.0` reference assemblies。
6. 输出到 Unity 固定 analyzer 路径，例如：

```text
Assets/Analyzers/ProjectRules.Analyzer.dll
```

一个容易踩的坑：不要混用 `netstandard2.1` reference 去编译目标为 `netstandard2.0` 的 analyzer。能编过，但可能出现兼容警告。最好明确使用 `netstandard2.0` 的 reference assemblies。

## 七、首次验证怎么做

不要为了验证去污染真实业务代码。可以临时构造两个样例文件。

违规样例：

```text
.temp-analyzer-check/Assets/Scripts_Hotfix/Game/BadIapCall.cs
```

内容：

```csharp
namespace Demo
{
    public static class GameEntity
    {
        public static readonly IapModule IAP = new IapModule();
    }

    public sealed class IapModule
    {
        public void Buy(int productId) { }
    }

    public sealed class CallSite
    {
        public void Run()
        {
            GameEntity.IAP.Buy(1);
        }
    }
}
```

预期：编译失败，出现 `HLWD001`。

白名单样例：

```text
.temp-analyzer-check/Assets/Scripts_Hotfix/Modules/IAP/IAPEventCenter.cs
```

同样写：

```csharp
GameEntity.IAP.Buy(1);
```

预期：编译通过。

最后清理临时目录，只保留 analyzer 源码、构建脚本和最终 DLL。

## 八、二次更新 Roslyn Analyzer 怎么做

二次更新指的是：已有 Analyzer 已经接入 Unity，后面要新增规则、调整白名单、改错误文案或扩展检测范围。

推荐流程：

1. 先改 Analyzer 源码，不直接改 DLL。
2. 每条新规则分配稳定 ID，例如：

```text
HLWD001
HLWD002
HLWD003
```

3. 根据强度选择级别：

```csharp
DiagnosticSeverity.Error
DiagnosticSeverity.Warning
```

4. 如果只是调整已有规则，也要补对应违规样例和合法样例。
5. 运行构建脚本：

```powershell
.\Tools\CodeAnalyzer\build-analyzer.ps1
```

6. 确认 Unity 加载的是新 DLL。
7. 用临时样例验证：违规必须失败，合法必须通过。
8. 再检查真实项目中是否已有历史违规。
9. 清理临时验证文件。
10. 如有 CI 或本地测试脚本，把新规则的触发口径同步到文档里。

二次更新最容易犯的错有两个：

1. 只改了源码，没有重建 DLL。
2. 只替换了 DLL，没有保留源码和构建脚本，导致下一次没人知道怎么维护。

## 九、本次实战步骤回放

这次实际落地时按下面顺序完成：

1. 从测试约束里提取规则：非白名单文件禁止直接调用 `GameEntity.IAP.Buy(...)`。
2. 检查项目里是否已有 Analyzer DLL。
3. 发现 DLL 存在，但 Unity 工程里没有作为 `<Analyzer>` 引入。
4. 检查 `.meta`，发现缺少 `RoslynAnalyzer` 标签。
5. 新增 Analyzer 源码项目和规则源码。
6. 实现 `HLWD001`，匹配 `GameEntity.IAP.Buy(...)` 的直接调用。
7. 用文件路径过滤 Hotfix 范围，并放行统一入口文件。
8. 编写构建脚本，直接调用 Roslyn `csc.dll` 构建 Analyzer DLL。
9. 替换 Unity 侧 Analyzer DLL。
10. 给 `.meta` 补 `RoslynAnalyzer` 标签。
11. 构造临时违规样例，确认触发 `error HLWD001`。
12. 构造临时白名单样例，确认编译通过。
13. 全仓搜索现有调用，确认只剩统一入口内的合法调用。
14. 清理临时验证目录。

## 十、结论

脚本检测适合兜底，Roslyn Analyzer 适合把规则前移。

对于“只能从统一入口调用”的工程约束，Analyzer 的收益很明显：

1. 反馈更早，写错就报错。
2. 规则更稳定，不依赖人工 Review。
3. 团队新成员不需要记住所有隐性约定。
4. CI 脚本仍然可以保留，作为最后一道兜底。

这类规则不要一开始写得过大。先从一个明确、可验证、误报低的约束开始，例如禁止直接调用某个关键 API。跑通后，再逐步扩展到模块引用、生命周期、事件清理等更复杂的工程规范。
