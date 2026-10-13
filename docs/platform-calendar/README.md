# TrendyHear → OctoSense Calendar：最小平台补丁与验证结果

日期：2026-10-12。范围：供审核的本地补丁；尚未提交官方仓库、发布或重新安装。

## 交付文件

| 文件 | 修改范围 | 目的 |
| --- | --- | --- |
| `01-app-hub-calendar-offer.patch` | 4 个文件，新增 19 行 | 允许应用明确申请两个内置 Calendar 工具，附权限测试与双语说明 |
| `02-octosense-calendar-receipts.patch` | 4 个文件，新增 113 行、删除 5 行 | 将真实工具执行结果返回给调用应用，附回执单元测试、隔离集成测试与双语说明 |
| `验证记录.txt` | 测试命令、基线和原始结果摘要 | 区分代码验证与正式环境验收 |

### App Hub 补丁

只增加 `calendar.events`、`calendar.add_event` 两个可申请工具。申请后仍受应用准入、清单声明、用户同意与宿主跨应用路由约束。新增测试确认：未申请不会自动获得权限，修改、删除及设备日历工具仍被拒绝。

### OctoSense 补丁

在本轮 Agent 返回中增加 `calendar_receipts`。回执来自宿主的成功工具响应，要求 owner 为 `os.calendar`、工具属于上述两个名称、上下文有效且属于当前轮次。每轮最多 8 条，每条最多 32,000 字节；错误响应和其他工具不进入回执。不会把模型回答中的“已创建”文字当作执行证据。

隔离集成测试使用现有 Calendar 服务与宿主工具路由，覆盖未授权、未确认、确认后保存、相同请求重试去重、按日期读回、磁盘持久化及应用撤回。测试中的事件只写入临时测试目录，未访问本机 Calendar。

## 验证结果

| 验证 | 结果 | 边界 |
| --- | --- | --- |
| 当前官方 App Hub 基线上 contract + policy 回归 | 157 项通过，0 失败 | 包括文档测试；不是全部平台测试 |
| Calendar 权限范围专项测试 | 1 项通过 | 已包含于上面的回归数量，不重复计数 |
| 本地 OctoSense app-peers 回归 | 99 项通过 | 另外 15 个可选真实内核测试虽显示通过，但可能无凭据提前返回，不作为真实 Agent 证据 |
| 内置 Calendar 服务 | 7 项通过 | 临时测试数据 |
| 已有 Mail → Calendar 冷启动路由测试 | 1 项通过 | 宿主代码测试 |
| 新增 contained-app Calendar 隔离集成测试 | 1 项通过 | 模拟应用准入与用户同意，真实服务保存/读回；未测试签名安装或真实模型 |
| 两份补丁空白检查 | 通过 | `git diff --check` |
| OctoSense 补丁应用于当前官方 main | 通过 | 最新基线仅验证补丁兼容性，未重新构建和运行宿主测试 |

## 精确基线与应用方式

App Hub 补丁基线：`386359153ed6377b5f047bd9ed2767a6a2ac2bc7`。

OctoSense 补丁基线：`37eb1e23a54cfdea6a88ccf14e2e4c325468226b`。

在各自干净的审核分支中执行，替换补丁路径为本文件夹实际路径：

```sh
# App Hub 仓库
git apply --check /path/to/01-app-hub-calendar-offer.patch
git apply /path/to/01-app-hub-calendar-offer.patch
cargo test -p octosense-app-contract -p octosense-app-policy

# OctoSense 仓库；先按其官方流程准备固定版本依赖
git apply --check /path/to/02-octosense-calendar-receipts.patch
git apply /path/to/02-octosense-calendar-receipts.patch
cargo test -p octosense-app-peers calendar_receipts_only_accept_bounded_host_success
cargo test -p octosense-shell --features app-hub host_tools::tests::contained_calendar_action_requires_consent_and_survives_exact_retry --lib
```

宿主必须实际链接包含 App Hub 工具许可修改的依赖版本。仅修改 App Hub main 而宿主仍固定旧版，不能完成接入。交付补丁不包含本机路径、Cargo 依赖替换、签名密钥、目录信任修改或无关 UI 改动。

## 后续正式验收条件

1. 平台维护者审核并合入两份补丁，发布兼容版本；在最新基线重新执行宿主测试。
2. TrendyHear 发布流程固定到包含支持的工具版本，通过正式证明与可信目录安装。当前旧测试包不能代表新的源代码。
3. 用户在机会卡片中确认后，宿主执行内置 Calendar 写入，再按日期和事件 ID 读回。只打开 Calendar 不等于保存成功。
4. 在 OctoSense 内置 Calendar 看到同一标题、日期和事件，重启后仍存在；重复点击不产生第二条。
5. 保留调用方 TrendyHear、工具 owner `os.calendar`、请求 ID、事件 ID 和读回结果；再录制连续操作证据。

**当前结论：最小补丁与代码验证材料已完成；正式安装及 TrendyHear → 内置 Calendar 全链路尚未验收。**

## 0.8.0 附加保存的应用端代码

`app-calendar-experiment.splash.txt` 保存0.7.3的应用侧授权后调用与读回验证片段，来自本地版本备份。它依赖原版本的状态和辅助函数，不能单独运行，0.8.0不会加载它。平台权限、兼容宿主和可信安装恢复后仍需重新审查、接入与端到端验收；当前正式路径只有听见日程。
