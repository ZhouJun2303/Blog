---
id: g0LTEg
title: Unity 游戏逆向分析与防逆向加固工具教程
createdAt: "2026-06-10 16:30:00"
updated: "2026-06-16 17:26:22"
tags:
    - Unity
    - 安全
    - 逆向
    - IL2CPP
tag_ids:
    - FjODty
    - W6Rjr9
    - UEWN8u
    - IL2CPP
categories: []
published: true
hideInList: false
feature: ""
isTop: false
---

> 本文只用于自有项目、公司授权项目、比赛靶场或教学样本的安全研究。不要用这些方法破解商业游戏、绕过付费、绕过反作弊、修改线上数据或传播他人资源。

这篇文章参考逆向论坛常见的写法：环境、工具、样本、步骤、截图位置、结论。内容重点不是“怎么改游戏”，而是学会用工具看清 Unity 包里暴露了什么，再反过来做防护。

![Unity 授权逆向分析流程](/post-images/unity-authorized-reverse-workflow.svg)

## 1. 准备环境

### 1.1 基础工具

建议准备一个专门的分析目录，例如：

```bash
mkdir -p ~/UnitySecurityLab/{samples,tools,outputs,reports}
```

常用工具如下：

| 工具 | 用途 | 下载建议 |
| --- | --- | --- |
| Unity Hub / Unity Editor | 构建自己的测试样本 | Unity 官方 |
| 7-Zip / Keka / unzip | 解压 APK、AAB、ZIP 包 | 官方或系统包管理器 |
| ILSpy | 查看 Mono 下的 C# 程序集 | https://github.com/icsharpcode/ILSpy |
| dnSpyEx | 查看 .NET 程序集、搜索引用 | https://github.com/dnSpyEx/dnSpy |
| AssetStudio | 查看 Unity 资源、TextAsset、贴图、音频 | https://github.com/Perfare/AssetStudio |
| AssetRipper | 对自有项目做资源结构恢复分析 | https://github.com/AssetRipper/AssetRipper |
| Il2CppDumper | 分析 IL2CPP 元数据与本地符号关系 | https://github.com/Perfare/Il2CppDumper |
| Cpp2IL | IL2CPP 结构分析的可选替代工具 | https://github.com/SamboyCoding/Cpp2IL |
| Ghidra | 查看 IL2CPP 生成的本地代码 | https://github.com/NationalSecurityAgency/ghidra |
| jadx-gui | 查看 Android Java/Kotlin 层代码 | https://github.com/skylot/jadx |
| apktool | 解包 AndroidManifest、资源表 | https://apktool.org/ |
| Android Studio / adb | 安装包、抓日志、看设备状态 | Android 官方 |
| mitmproxy / Charles | 检查自己 App 的网络请求 | 官方网站 |

### 1.2 推荐样本

不要直接拿商业游戏练手。最好自己创建一个 Unity 工程，命名为 `SecurityLabGame`，放几个常见模块：

- `LoginService.cs`：模拟登录、接口地址、测试账号。
- `InventoryService.cs`：金币、钻石、背包。
- `SaveManager.cs`：本地存档。
- `NetworkClient.cs`：请求签名和错误日志。
- `DebugPanel.cs`：仅开发环境使用的调试面板。

然后分别打两个包：

- Mono 包：用于学习 `Assembly-CSharp.dll` 结构。
- IL2CPP 包：用于学习正式包的常见形态。

Unity 设置路径：

```text
File > Build Profiles 或 File > Build Settings
Edit > Project Settings > Player > Other Settings
```

Mono 样本：

```text
Scripting Backend: Mono
Development Build: 可以先打开，便于学习
Script Debugging: 可以先打开，便于学习
```

IL2CPP 样本：

```text
Scripting Backend: IL2CPP
Development Build: 关闭
Script Debugging: 关闭
Managed Stripping Level: Medium
```

Unity 官方说明：脚本后端决定 C# 脚本如何被编译和执行；IL2CPP 会把 IL 转为 C++ 再编译成本地代码。参考 Unity Manual：`https://docs.unity3d.com/Manual/scripting-backends.html`。

## 2. 识别 Unity 包结构

### 2.1 Windows 包

典型 Mono 包：

```text
SecurityLabGame.exe
SecurityLabGame_Data/
  Managed/
    Assembly-CSharp.dll
    UnityEngine.CoreModule.dll
  Resources/
  StreamingAssets/
```

典型 IL2CPP 包：

```text
SecurityLabGame.exe
GameAssembly.dll
UnityPlayer.dll
SecurityLabGame_Data/
  Managed/
    Metadata/
      global-metadata.dat
  il2cpp_data/
```

检查命令：

```bash
find ./SecurityLabGame -maxdepth 4 -type f | sort
```

快速判断：

```bash
find ./SecurityLabGame -name "Assembly-CSharp.dll" -o -name "GameAssembly.dll" -o -name "global-metadata.dat"
```

看到 `Assembly-CSharp.dll`，大概率有 Mono 托管程序集可看。看到 `GameAssembly.dll` 和 `global-metadata.dat`，大概率是 IL2CPP。

### 2.2 Android APK

APK 本质是 ZIP，可以先列文件：

```bash
unzip -l SecurityLabGame.apk | rg "Assembly-CSharp|libil2cpp|global-metadata|resources.assets|AndroidManifest"
```

Mono 常见位置：

```text
assets/bin/Data/Managed/Assembly-CSharp.dll
```

IL2CPP 常见位置：

```text
lib/arm64-v8a/libil2cpp.so
assets/bin/Data/Managed/Metadata/global-metadata.dat
```

解压到分析目录：

```bash
mkdir -p outputs/SecurityLabGame_apk
unzip SecurityLabGame.apk -d outputs/SecurityLabGame_apk
```

查看基本信息：

```bash
file outputs/SecurityLabGame_apk/lib/arm64-v8a/libil2cpp.so
shasum -a 256 SecurityLabGame.apk
```

### 2.3 AAB 包

如果是 Android App Bundle：

```bash
unzip -l SecurityLabGame.aab | rg "base|libil2cpp|global-metadata|manifest"
```

本地生成通用 APK 方便测试：

```bash
java -jar bundletool.jar build-apks \
  --bundle=SecurityLabGame.aab \
  --output=SecurityLabGame.apks \
  --mode=universal
```

解出 APK：

```bash
unzip SecurityLabGame.apks -d outputs/SecurityLabGame_apks
```

## 3. Mono 项目分析：ILSpy 和 dnSpyEx

### 3.1 找到程序集

Windows：

```text
SecurityLabGame_Data/Managed/Assembly-CSharp.dll
```

Android：

```text
assets/bin/Data/Managed/Assembly-CSharp.dll
```

把文件复制到：

```text
~/UnitySecurityLab/outputs/mono/Assembly-CSharp.dll
```

### 3.2 使用 ILSpy

操作步骤：

1. 打开 ILSpy。
2. `File > Open`，选择 `Assembly-CSharp.dll`。
3. 左侧展开程序集。
4. 优先看自己写的命名空间，例如 `Game`, `Hotfix`, `Services`, `Managers`。
5. 使用搜索框搜索关键词。

推荐搜索：

```text
http
https
token
secret
password
debug
gm
cheat
coin
diamond
iap
purchase
sign
```

重点观察：

- 类名是否暴露真实业务，例如 `AddDiamondService`。
- 方法名是否暴露敏感能力，例如 `UnlockAllSkins`。
- 字符串是否包含测试域名、后台接口、临时 token。
- 逻辑是否完全由客户端决定，例如金币增加、抽卡结果、支付成功。
- `Debug.Log` 是否打印用户 ID、token、订单号。

右键常用功能：

```text
Analyze
```

可以查看：

- `Used By`：谁调用了这个方法。
- `Uses`：这个方法调用了谁。
- 字段在哪里被读写。

### 3.3 使用 dnSpyEx

操作步骤：

1. 打开 dnSpyEx。
2. `File > Open`，选择 `Assembly-CSharp.dll`。
3. `Ctrl + Shift + K` 全局搜索类型、方法、字符串。
4. 点到方法后，看右侧反编译结果。
5. 右键方法选择 `Analyze`，看调用链。

本文只建议把 dnSpyEx 当只读分析工具使用，不写补丁、不改第三方程序、不绕过授权。

### 3.4 命令行辅助搜索

先用 `strings` 提取明显字符串：

```bash
strings -a Assembly-CSharp.dll | rg -i "http|token|secret|password|debug|gm|cheat|coin|diamond|purchase"
```

把结果保存为证据：

```bash
strings -a Assembly-CSharp.dll \
  | rg -i "http|token|secret|password|debug|gm|cheat|coin|diamond|purchase" \
  > reports/mono-sensitive-strings.txt
```

报告写法：

```text
发现：Assembly-CSharp.dll 中包含 https://test-api.example.local
风险：测试接口地址被正式包携带，可能暴露内部环境。
证据：reports/mono-sensitive-strings.txt 第 12 行。
建议：正式构建使用环境配置注入，不在客户端硬编码测试域名。
```

## 4. IL2CPP 项目分析：Il2CppDumper、Cpp2IL、Ghidra

IL2CPP 比 Mono 更难直接阅读，但它不是安全边界。类名、方法名、字符串、metadata 仍可能泄露信息。

### 4.1 找到关键文件

Windows：

```text
GameAssembly.dll
SecurityLabGame_Data/Managed/Metadata/global-metadata.dat
```

Android：

```text
lib/arm64-v8a/libil2cpp.so
assets/bin/Data/Managed/Metadata/global-metadata.dat
```

复制到工作目录：

```bash
mkdir -p outputs/il2cpp
cp GameAssembly.dll outputs/il2cpp/
cp SecurityLabGame_Data/Managed/Metadata/global-metadata.dat outputs/il2cpp/
```

Android 示例：

```bash
mkdir -p outputs/il2cpp
cp outputs/SecurityLabGame_apk/lib/arm64-v8a/libil2cpp.so outputs/il2cpp/
cp outputs/SecurityLabGame_apk/assets/bin/Data/Managed/Metadata/global-metadata.dat outputs/il2cpp/
```

### 4.2 使用 Il2CppDumper

Windows 示例：

```bash
Il2CppDumper GameAssembly.dll global-metadata.dat outputs/il2cpp/dumper
```

Android 示例：

```bash
Il2CppDumper libil2cpp.so global-metadata.dat outputs/il2cpp/dumper
```

常见输出：

```text
DummyDll/
il2cpp.h
script.json
stringliteral.json
ghidra.py 或 ida.py
```

怎么看：

- `DummyDll`：用 ILSpy 打开，查看类、方法、字段轮廓。
- `stringliteral.json`：搜索接口、敏感词、配置名。
- `il2cpp.h`：给 Ghidra/IDA 辅助理解结构。
- `ghidra.py`：部分版本会生成导入符号的脚本。

搜索字符串：

```bash
rg -i "http|token|secret|debug|gm|coin|diamond|purchase" outputs/il2cpp/dumper
```

### 4.3 使用 Cpp2IL

Cpp2IL 是另一种 IL2CPP 分析工具。不同版本参数可能略有变化，先看帮助：

```bash
Cpp2IL --help
```

常见思路：

```bash
Cpp2IL --game-path ./SecurityLabGame --output-to outputs/cpp2il
```

输出后重点看：

- 还原出的类型名和方法名。
- 字符串引用。
- 是否有调试类、测试入口、后台接口常量。

如果 Cpp2IL 和 Il2CppDumper 结果不一致，以“能稳定复现的证据”为准，不要只凭一个工具下结论。

### 4.4 使用 Ghidra

Ghidra 适合看 IL2CPP 生成的本地代码结构。

操作步骤：

1. 打开 Ghidra。
2. `File > New Project`，创建非共享项目。
3. `File > Import File`。
4. Windows 选 `GameAssembly.dll`；Android 选 `libil2cpp.so`。
5. 双击导入的程序。
6. 弹出分析提示时选择 `Yes`，保留默认分析项。
7. 等待 Auto Analysis 完成。
8. 如果 Il2CppDumper 生成了 `ghidra.py`，在 `Window > Script Manager` 中添加脚本目录并运行。

常用视图：

```text
Symbol Tree
Defined Strings
Decompile
Listing
Function Graph
```

常用搜索：

```text
Search > For Strings
Search > Program Text
Search > Memory
```

建议搜索：

```text
Login
Save
Purchase
Diamond
Coin
Debug
GM
http
```

分析目标：

- 确认敏感字符串是否进入二进制。
- 确认类名、方法名是否暴露核心业务。
- 确认 Release 包是否仍有调试分支。
- 确认 native 插件是否包含密钥或测试接口。

不要在本文范围内做二进制补丁、授权绕过、反作弊规避或线上作弊。

## 5. Unity 资源分析：AssetStudio 和 AssetRipper

### 5.1 资源位置

Windows：

```text
SecurityLabGame_Data/resources.assets
SecurityLabGame_Data/sharedassets*.assets
SecurityLabGame_Data/StreamingAssets/
```

Android：

```text
assets/bin/Data/resources.assets
assets/bin/Data/sharedassets*.assets
assets/bin/Data/StreamingAssets/
```

Addressables / AssetBundle 常见位置：

```text
StreamingAssets/aa/
AssetBundles/
remote catalog
```

### 5.2 使用 AssetStudio

操作步骤：

1. 打开 AssetStudio。
2. `File > Load Folder`，选择整个 `*_Data` 目录，Android 选择 `assets/bin/Data`。
3. 等待索引完成。
4. 切到 `Asset List`。
5. 用 `Type` 过滤资源类型。

常看类型：

```text
TextAsset
Texture2D
Sprite
AudioClip
Mesh
MonoBehaviour
AnimationClip
```

检查点：

- `TextAsset` 是否包含配置表、概率、活动数据、测试域名。
- `Texture2D` 是否包含未上线角色、活动图、运营素材。
- `AudioClip` 是否包含未上线剧情。
- `MonoBehaviour` 序列化字段是否暴露调试开关。
- AssetBundle 名称是否暴露未上线内容。

导出证据：

```text
右键资源 > Export selected assets
```

报告写法：

```text
发现：正式包包含 TextAsset activity_2026_summer_boss_config。
风险：未上线活动和 Boss 名称提前暴露。
建议：活动资源改为远程分包，并在活动开启前下发。
```

### 5.3 使用 AssetRipper

AssetRipper 对自有项目很适合做“包体内容盘点”。

操作步骤：

1. 打开 AssetRipper。
2. 选择 `Open Folder`。
3. 选择 `SecurityLabGame_Data` 或 Android 的 `assets/bin/Data`。
4. 加载完成后选择导出目录，例如 `outputs/assetripper-export`。
5. 导出后用编辑器搜索。

命令行搜索：

```bash
rg -i "http|token|debug|gm|coin|diamond|purchase|test" outputs/assetripper-export
```

注意：AssetRipper 恢复出的工程不是原工程，结论应写成“资源暴露风险”，不要把导出结果当作源码原貌。

## 6. Android 层分析：jadx、apktool、adb

Unity 游戏也有 Android 壳层，里面可能有 SDK、权限、深链、广告、支付、推送配置。

### 6.1 使用 jadx-gui

操作步骤：

1. 打开 `jadx-gui`。
2. 拖入 `SecurityLabGame.apk`。
3. 等待反编译完成。
4. 左侧查看 `AndroidManifest.xml`、`resources.arsc`、`com.xxx` 包名。
5. 全局搜索关键词。

推荐搜索：

```text
api
secret
token
appkey
appid
channel
debug
payment
purchase
```

重点检查：

- SDK 初始化参数是否硬编码。
- AndroidManifest 是否有多余权限。
- `android:debuggable` 是否为 `true`。
- 是否暴露不该导出的 Activity、Service、Provider、Receiver。
- 渠道包配置是否混入测试环境。

### 6.2 使用 apktool

解包：

```bash
apktool d SecurityLabGame.apk -o outputs/apktool-SecurityLabGame
```

查看 Manifest：

```bash
sed -n '1,220p' outputs/apktool-SecurityLabGame/AndroidManifest.xml
```

搜索配置：

```bash
rg -i "debuggable|exported|permission|http|secret|token|appkey" outputs/apktool-SecurityLabGame
```

本文只讲解包检查，不讲重打包、绕签名、绕支付或绕反作弊。

### 6.3 使用 adb 看日志

安装自有测试包：

```bash
adb install -r SecurityLabGame.apk
```

清空日志：

```bash
adb logcat -c
```

只看 Unity 日志：

```bash
adb logcat Unity:D '*:S'
```

把日志保存下来：

```bash
adb logcat Unity:D '*:S' > reports/unity-logcat.txt
```

检查敏感日志：

```bash
rg -i "token|secret|password|order|purchase|uid|debug|gm" reports/unity-logcat.txt
```

报告写法：

```text
发现：登录成功后日志输出 accessToken。
风险：测试机、崩溃平台或第三方日志 SDK 可能收集敏感凭证。
建议：Release 包删除该日志，日志系统默认脱敏。
```

## 7. 网络检查：mitmproxy 或 Charles

只对自己的 App 和自己的服务器做抓包检查。不要讲或做证书锁定绕过。

### 7.1 mitmproxy 基本流程

电脑启动代理：

```bash
mitmweb --listen-host 0.0.0.0 --listen-port 8080
```

手机设置 Wi-Fi 代理：

```text
代理主机：电脑 IP
代理端口：8080
```

测试目标：

- 请求是否全部走 HTTPS。
- URL 是否带 token、手机号、邮箱等敏感参数。
- 是否有时间戳、nonce、签名。
- 重放同一个请求是否会被服务端拒绝。
- 客户端传来的金币、道具、价格是否被服务端重新校验。

### 7.2 Charles 基本流程

操作步骤：

1. `Proxy > Proxy Settings`，确认 HTTP Proxy 端口。
2. 手机连接同一 Wi-Fi。
3. 手机 Wi-Fi 代理指向电脑 IP 和 Charles 端口。
4. `Proxy > SSL Proxying Settings`，只添加自己的测试域名。
5. 运行自有测试包，观察请求。

报告写法：

```text
发现：领取奖励接口只接收客户端上传 rewardCount。
风险：客户端参数可被篡改，服务端没有按配置重新计算奖励。
建议：客户端只上报事件，服务端根据关卡、任务、账号状态计算奖励。
```

## 8. 输出逆向分析报告

推荐目录：

```text
reports/
  01-package-structure.md
  02-mono-analysis.md
  03-il2cpp-analysis.md
  04-assets-analysis.md
  05-android-analysis.md
  06-network-analysis.md
  99-summary.md
```

单条问题模板：

```text
编号：U-SEC-001
标题：正式包包含测试接口地址
等级：中
影响范围：Android 1.0.0 Release
证据：
- Assembly-CSharp.dll strings 结果包含 https://test-api.example.local
- jadx 搜索结果显示 TestConfig.TEST_API
风险：
- 暴露内部服务命名和测试环境
- 可能被误连或被扫描
建议：
- 正式包构建时从 CI 注入环境配置
- 客户端不携带测试环境地址
- 服务端限制测试环境访问来源
复测：
- 重新构建后 strings / jadx / AssetStudio 均未检出测试域名
```

## 9. 防逆向与防篡改总原则

![Unity 防逆向分层加固](/post-images/unity-defense-layers.svg)

客户端防护只能提高成本，不能保证绝对安全。真正重要的判断必须由服务端完成。

不要把这些东西交给客户端最终决定：

- 支付是否成功。
- 金币、钻石、体力、道具数量。
- 抽卡结果和掉落结果。
- 排行榜成绩。
- PVP 结算。
- 活动资格。
- 封禁和解封。

客户端可以做：

- 展示 UI。
- 收集玩家输入。
- 播放动画。
- 本地预测。
- 缓存非关键数据。
- 做基础完整性检查。

服务端必须做：

- 重新计算奖励。
- 校验订单。
- 校验签名。
- 校验 nonce 和时间戳。
- 校验用户状态。
- 校验排行榜数据合理性。
- 记录异常行为。

## 10. Unity 构建层防护

### 10.1 Player Settings

路径：

```text
Edit > Project Settings > Player
```

正式包建议：

```text
Development Build: 关闭
Script Debugging: 关闭
Wait For Managed Debugger: 关闭
Scripting Backend: IL2CPP
Managed Stripping Level: Medium 或 High
Strip Engine Code: 开启，先完整回归测试
Stack Trace: Release 下尽量降低详细程度
```

Unity 官方说明：Managed Code Stripping 会在构建过程中移除未使用或不可达的托管代码，可在 Editor 中配置裁剪级别，也可以通过注解或 `link.xml` 保留必要代码。参考 Unity Manual：`https://docs.unity3d.com/Manual/managed-code-stripping.html`。

### 10.2 检查构建产物

构建完成后做一次“自查逆向”：

```bash
strings -a GameAssembly.dll | rg -i "secret|token|password|gm|cheat|debug|http://|test-api"
```

Android：

```bash
unzip -l app-release.apk | rg "Assembly-CSharp|libil2cpp|global-metadata"
strings -a outputs/SecurityLabGame_apk/lib/arm64-v8a/libil2cpp.so | rg -i "secret|token|password|gm|debug|test-api"
strings -a outputs/SecurityLabGame_apk/assets/bin/Data/Managed/Metadata/global-metadata.dat | rg -i "AddDiamond|UnlockAll|DebugPanel|GM"
```

如果还能搜到非常直白的业务词，说明命名、日志、配置或裁剪策略还需要处理。

## 11. 代码层防护

### 11.1 移除 Release 调试入口

错误写法：

```csharp
public class DebugPanel : MonoBehaviour
{
    public void AddDiamond()
    {
        PlayerData.Diamond += 9999;
    }
}
```

推荐写法：

```csharp
#if UNITY_EDITOR || DEVELOPMENT_BUILD
public class DebugPanel : MonoBehaviour
{
    public void Open()
    {
        gameObject.SetActive(true);
    }
}
#endif
```

再用命令检查：

```bash
rg -n "DebugPanel|AddDiamond|GM|Cheat|TestAccount" Assets
```

### 11.2 日志脱敏

错误写法：

```csharp
Debug.Log($"login success uid={uid}, token={token}");
```

推荐写法：

```csharp
SafeLog.Info("login success uid={0}", MaskUserId(uid));
```

示例：

```csharp
public static class SafeLog
{
    [System.Diagnostics.Conditional("UNITY_EDITOR")]
    [System.Diagnostics.Conditional("DEVELOPMENT_BUILD")]
    public static void Info(string format, params object[] args)
    {
        UnityEngine.Debug.LogFormat(format, args);
    }
}
```

检查：

```bash
rg -n "Debug\\.Log|Debug\\.LogWarning|Debug\\.LogError|print\\(" Assets
```

不是所有 `Debug.LogError` 都必须删除，但要确认不会输出 token、订单号、手机号、邮箱、身份证、后台地址。

### 11.3 混淆工具

可选工具：

- BeeByte Obfuscator：Unity 生态常见商业混淆工具。
- Eazfuscator.NET：.NET 混淆工具，适用性需要按 Unity 版本验证。
- 自研命名混淆：对业务层类名、方法名、字段名做构建期映射。

混淆前先列白名单：

- Unity 序列化字段。
- 反射调用的类和方法。
- JSON 序列化字段。
- Lua/JS/热更新入口。
- SDK 回调方法。
- `SendMessage` 调用的方法。

混淆后必测：

- 登录。
- 支付。
- 新手引导。
- 背包。
- 战斗。
- 热更新。
- Addressables 加载。
- 崩溃上报。

混淆不是为了隐藏密钥。密钥一旦放在客户端，就应该默认会被拿到。

### 11.4 link.xml 和 Preserve

裁剪级别升高后，反射和热更新容易出问题。可以用 `Preserve` 或 `link.xml` 保留必要类型。

代码：

```csharp
using UnityEngine.Scripting;

[Preserve]
public class HotfixEntry
{
    [Preserve]
    public void Run()
    {
    }
}
```

`Assets/link.xml`：

```xml
<linker>
  <assembly fullname="Assembly-CSharp">
    <type fullname="Game.HotfixEntry" preserve="all" />
  </assembly>
</linker>
```

检查思路：

```text
提高 Managed Stripping Level
打包
跑自动化和核心流程
如果反射入口丢失，再用 Preserve 或 link.xml 精确保留
```

## 12. 资源层防护

### 12.1 不提前下发未上线资源

最有效的资源防泄露方法不是加密，而是不把资源放进包里。

建议：

- 未上线角色不进当前包。
- 活动资源按活动时间远程下发。
- 剧情文本和语音分版本控制。
- 测试图、废弃图、运营草稿不进正式包。
- AssetBundle 名称不要暴露真实活动名。

检查：

```bash
rg -i "summer|boss|secret|test|debug|gm|activity" outputs/assetripper-export
```

### 12.2 AssetBundle 完整性

建议保存：

```text
bundleName
version
crc
hash
size
downloadUrl
```

客户端加载前检查：

- 下载大小是否正确。
- Hash 是否匹配。
- 版本是否匹配。
- Catalog 是否来自可信服务端。

注意：CRC/Hash 是完整性校验，不是保密。资源只要到了客户端，就有被提取的可能。

## 13. 存档和本地数据防护

### 13.1 本地存档最低要求

存档建议包含：

```json
{
  "userId": "10001",
  "level": 12,
  "inventory": [],
  "timestamp": 1781080200,
  "version": 3
}
```

再加签名：

```text
signature = HMAC(sessionKey, canonicalJson(payload))
```

客户端发送给服务端时：

```text
payload + signature + nonce + timestamp
```

服务端验证：

- 签名是否正确。
- 时间戳是否过期。
- nonce 是否用过。
- userId 是否匹配当前会话。
- 数据变化是否合理。

### 13.2 C# HMAC 示例

这个示例用于说明格式。正式项目的关键密钥应由服务端生成和校验，不要把长期密钥硬编码在客户端。

```csharp
using System;
using System.Security.Cryptography;
using System.Text;

public static class RequestSigner
{
    public static string HmacSha256(string message, string sessionKey)
    {
        byte[] keyBytes = Encoding.UTF8.GetBytes(sessionKey);
        byte[] messageBytes = Encoding.UTF8.GetBytes(message);

        using var hmac = new HMACSHA256(keyBytes);
        byte[] hash = hmac.ComputeHash(messageBytes);
        return Convert.ToBase64String(hash);
    }
}
```

规范化字符串示例：

```text
POST
/api/reward/claim
nonce=8f2b...
timestamp=1781080200
bodyHash=...
```

服务端不要相信客户端传来的 `rewardCount`、`price`、`diamond`，这些值必须重新计算。

## 14. 通信和平台完整性

### 14.1 请求签名

推荐字段：

```text
timestamp
nonce
bodyHash
sessionId
signature
```

服务端策略：

- `timestamp` 超过窗口直接拒绝。
- `nonce` 已使用直接拒绝。
- `bodyHash` 不匹配直接拒绝。
- `sessionId` 失效直接拒绝。
- 账号状态异常进入风控队列。

### 14.2 Android Play Integrity

Android 可以接入 Google Play Integrity API。基本思路：

```text
客户端请求 integrity token
客户端把 token 发给服务端
服务端调用 Google API 验证
服务端根据 verdict 参与风控决策
```

不要只在客户端判断，也不要把完整性结果当成唯一封禁依据。官方文档：`https://developer.android.com/google/play/integrity`。

### 14.3 iOS App Attest / DeviceCheck

iOS 可以考虑 App Attest 或 DeviceCheck。基本思路同样是：

```text
设备生成证明
客户端提交证明
服务端验证证明
服务端把结果纳入风控
```

客户端结果只能作为信号，最终决策在服务端。

## 15. Android 发布层防护

### 15.1 检查 debuggable

用 apktool 解包后：

```bash
rg -n "debuggable" outputs/apktool-SecurityLabGame/AndroidManifest.xml
```

正式包不应出现：

```xml
android:debuggable="true"
```

### 15.2 检查签名

使用 Android SDK 的 `apksigner`：

```bash
apksigner verify --verbose --print-certs app-release.apk
```

检查点：

- 是否已签名。
- 是否使用正确 release 证书。
- 是否意外使用 debug keystore。

### 15.3 R8 / ProGuard

Unity Android 层的 Java/Kotlin 代码可以使用 R8/ProGuard。路径通常在：

```text
Edit > Project Settings > Player > Android > Publishing Settings
```

可开启：

```text
Minify Release
Custom Proguard File
```

自定义规则文件常见位置：

```text
Assets/Plugins/Android/proguard-user.txt
```

注意：

- ProGuard 主要保护 Java/Kotlin 层，不保护 C# IL2CPP 本体。
- 三方 SDK 需要保留规则，否则可能运行时崩溃。
- 开启后必须跑支付、登录、广告、推送、分享等 SDK 流程。

## 16. CI 中加入安全检查

可以在打包流水线后加入自动检查：

```bash
#!/usr/bin/env bash
set -euo pipefail

APK="$1"
OUT="outputs/security-check"

rm -rf "$OUT"
mkdir -p "$OUT"
unzip -q "$APK" -d "$OUT/apk"

echo "[1] check manifest"
if rg -n 'android:debuggable="true"' "$OUT/apk"; then
  echo "Release APK is debuggable"
  exit 1
fi

echo "[2] check sensitive strings"
if strings -a "$OUT/apk/lib/arm64-v8a/libil2cpp.so" | rg -i "test-api|secret|password|gm|cheat"; then
  echo "Sensitive strings found in libil2cpp.so"
  exit 1
fi

echo "[3] done"
```

按项目调整关键词，不要把正常业务词误判为失败。

## 17. 最终检查清单

| 分类 | 检查项 | 工具 |
| --- | --- | --- |
| 构建 | 关闭 Development Build | Unity Editor |
| 构建 | 关闭 Script Debugging | Unity Editor |
| 构建 | 使用 IL2CPP | Unity Editor |
| 构建 | Managed Stripping Level 已测试 | Unity Editor |
| 代码 | Release 无 GM / Cheat / DebugPanel | rg / ILSpy / Il2CppDumper |
| 代码 | 无硬编码长期密钥 | rg / strings |
| 代码 | 日志不输出 token / 订单号 | adb logcat / rg |
| 资源 | 未上线资源不进包 | AssetStudio / AssetRipper |
| 资源 | AssetBundle 有版本和 Hash | 自研工具 / CI |
| Android | `debuggable` 为 false | apktool |
| Android | 使用 release 签名 | apksigner |
| Android | Java 层开启合适混淆 | R8 / ProGuard |
| 网络 | HTTPS + nonce + timestamp | mitmproxy / Charles |
| 服务端 | 支付走平台回调 | 服务端日志 |
| 服务端 | 货币、道具、排行榜服务端校验 | 服务端测试 |
| 风控 | Play Integrity / App Attest 只作为信号 | 服务端风控 |

## 18. 总结

逆向教程的价值不是学会破解，而是看清自己的包在别人眼里是什么样子。Mono 包最容易暴露 C# 逻辑，IL2CPP 能提高分析成本但不能保密，资源包只要到达客户端就可能被提取。

防护的正确顺序：

```text
服务端权威 > 不下发敏感内容 > Release 构建配置 > 日志清理 > 混淆裁剪 > 完整性检查 > 风控
```

做完防护以后，再用本文前半部分的工具重新分析一遍自己的正式包。能被工具轻易搜到的东西，线上用户也有机会看到。