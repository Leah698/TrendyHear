# Reusable OctoScript navigation experiments

This directory preserves the reusable runtime work reviewed for the
TrendyHear v0.9.1 submission. These patches are **optional failed experiments**
and are not a runtime dependency of the submitted application.

## NavigationDrawer experiment

- `0001-octoscript-navigation-drawer.patch` adds a reusable OctoScript widget
  with open/close/toggle state, native animation, left/right placement, scrim
  dismissal, Escape/Back handling, selected index and navigation callbacks.
- `0002-app-hub-register-navigation-drawer.patch` registers that widget in the
  App Hub/card host render path used for local experiments.
- The component and its registration passed the OctoScript node, render,
  Makepad and widget release tests in the recorded development checkout.

The drawer was then tested in TrendyHear on a narrow Android presentation.
That run exposed a platform/layout mismatch: the application remained in its
desktop split layout and compressed both columns into the phone width. The
failure is recorded in the v0.9.1 submission failure-state document. The
original development screenshot was not retained in the frozen source package.

TrendyHear therefore uses a fixed four-item bottom navigation in its release
bundle. The drawer remains here as a separately reviewable contribution and
future upstream candidate. Installing or running TrendyHear does not require
these two patches.

# 可复用 OctoScript 导航实验

本目录保存 TrendyHear v0.9.1 复赛材料中仍有复盘价值的通用运行时成果。
这些补丁是**未采用的可选实验**，参赛应用正式运行不依赖它们。

## NavigationDrawer 实验组件

- `0001-octoscript-navigation-drawer.patch` 增加可复用 OctoScript 组件，
  包含展开/关闭/切换状态、原生动画、左右侧位置、遮罩关闭、Escape/Back
  处理、选中索引和导航回调。
- `0002-app-hub-register-navigation-drawer.patch` 将组件注册到本地实验使用的
  App Hub/card host 渲染路径。
- 组件及注册修改已通过对应开发基线的 OctoScript node、render、Makepad
  和 widget release 测试。

随后在 TrendyHear 的窄屏 Android 演示中发现平台/布局判断不一致：应用仍
进入桌面双栏，将两栏压缩进手机宽度。失败现象已写入 v0.9.1 提交材料的
失败状态记录；旧开发截图没有继续放入冻结源码包。

因此 TrendyHear 正式 bundle 改用固定四项底部导航。抽屉组件继续作为独立、
可审核、可上游化的技术贡献候选保留；安装和运行 TrendyHear 不需要应用这两
个补丁。
