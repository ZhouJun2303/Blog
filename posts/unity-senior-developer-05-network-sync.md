---
id: kFUH0c
title: Unity 开发高级/资深 05：网络通信与多人同步
createdAt: "2026-06-10 21:55:00"
updated: "2026-06-17 10:10:59"
tags:
    - Unity
    - 开发高级/资深
    - 网络
tag_ids:
    - FjODty
    - P46nOZ
    - hKdl9N
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: true
feature: ""
isTop: false
---

[返回总览](https://zhoujun2303.github.io/post/unity-senior-developer-skills/)

![Unity 开发高级/资深工具链地图](/post-images/unity-senior-developer-toolchain-map.svg)

<a id="network"></a>
## 网络通信

- 协议选择：HTTP、WebSocket、TCP、UDP、KCP、可靠 UDP 的适用场景。
- 连接状态：未连接、连接中、已连接、重连中、断开、后台、恢复。
- 心跳机制：客户端心跳、服务器超时、时间同步、网络延迟估算。
- 消息结构：包头、长度、协议号、序列号、压缩、加密、签名。
- 序列化：Protobuf、FlatBuffers、MessagePack、JSON 的成本和调试便利性。
- 请求回调：请求 ID、超时、取消、重试、错误码、重复请求。
- 消息分发：按模块订阅、弱引用、生命周期解绑、主线程派发。
- 弱网处理：延迟、丢包、断网、网络切换、切后台、锁屏。
- 调试工具：网络日志、抓包、协议回放、模拟延迟、模拟断线。

### 需要掌握的工具

- Protobuf、FlatBuffers、MessagePack：协议序列化和版本兼容。
- Postman、Apifox：调试 HTTP 接口、登录、活动和运营后台接口。
- Wireshark、Charles、tcpdump：抓包、分析连接、延迟、重传和数据内容。
- Network Link Conditioner、Clumsy、tc：模拟弱网、延迟、丢包和断线。
- Logcat、Xcode Console：查看移动端网络错误和系统状态变化。
- 自研协议日志工具：按协议号、请求 ID、玩家 ID、耗时和错误码追踪。
- 协议回放工具：复现线上请求序列，验证兼容和错误处理。

### 可继续细分方向

- 连接状态机、心跳和重连。
- 协议结构、序列化和版本兼容。
- 弱网模拟、超时和重试。
- 网络日志、抓包和协议回放。

<a id="multiplayer-aoi"></a>
## 多人同步与 AOI

- AOI 策略：距离、格子、区域、房间、兴趣列表、服务器分线。
- 实体生命周期：进入视野、离开视野、创建、销毁、换线、下线。
- 移动同步：位置、朝向、速度、动作、时间戳、插值、纠偏。
- 外观同步：角色、时装、武器、坐骑、宠物、称号、挂件、特效。
- 行为同步：表情、互动、技能展示、采集、坐下、跳舞、社交动作。
- 优先级：近处高频、远处低频、屏外降频、关键动作即时同步。
- 客户端预测：输入预测、表现预测、服务器校验、回滚或平滑修正。
- 分线机制：自动分线、手动换线、好友跟随、活动线、拥挤保护。
- 断线重连：位置恢复、队伍恢复、战斗恢复、面板恢复、临时对象清理。

### 需要掌握的工具

- Unity Multiplayer Tools：参考网络性能统计、消息量和延迟观察方式。
- Netcode for GameObjects、Mirror、Photon 文档：理解常见同步模型和取舍。
- Scene Gizmos：可视化 AOI 范围、同步格子、兴趣列表和实体状态。
- 网络模拟器：模拟高延迟、抖动、丢包、断线和分线切换。
- Replay/录像工具：回放移动、动作、外观和同步纠偏过程。
- 性能面板：统计同屏人数、实体数量、消息频率、带宽和实例化耗时。

### 可继续细分方向

- AOI 和兴趣管理。
- 移动同步、插值和纠偏。
- 外观、动作和社交同步。
- 分线、断线重连和状态恢复。

## 网络层接口建议

- Connect、Disconnect、Reconnect、Send、Request、Subscribe、Unsubscribe。
- Request 支持超时、取消、错误码、重试策略。
- Subscribe 绑定生命周期，避免关闭面板后仍收到消息。
- 网络层只处理通信，不直接改业务 UI。
- 协议解析失败必须记录协议号、版本、玩家 ID、服务器、原始长度。

## 开发高级/资深关注点

- 弱网下用户是否能恢复，而不是只能重启游戏。
- 协议版本不一致时是否有明确提示和升级路径。
- 断线重连后客户端状态和服务器状态是否一致。
- 多人同屏是否有带宽、CPU、实例数量、动画和 UI 降级策略。
- 网络日志是否足够定位“客户端没发、服务器没回、客户端没处理”。