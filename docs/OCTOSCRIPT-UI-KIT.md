# TrendyHear OctoScript UI Kit

## 中文

TrendyHear v0.9.1 在应用层整理了一套可复用的 OctoScript 视觉组件，不要求修改 OctoSense Shell。组件直接定义在 `bundle/main.splash`，图标位于 `bundle/assets/icons/`。

- `Primary`：46px 高的主行动按钮，深绿底、白字、12px 圆角。
- `Secondary`：与主按钮等高的次行动按钮，白底、浅绿描边。
- `Quiet`：用于卡片内部反馈、已读等低权重操作。
- `Nav` / `ActiveNav`：共用 24×24 viewBox、2px 圆角线条的底部导航。
- `NewsCard` 规则：优先显示 RSS 原始图片；没有图片时显示统一的主题占位块，不由模型编造配图。

这组组件是应用层技术贡献，可复制到其他 OctoScript 应用。可选的 Shell/运行时实验补丁仍单独位于 `build/runtime-patches/` 与 `build/shell-patches/`，正式应用不依赖它们。

## English

TrendyHear v0.9.1 includes a reusable, app-local OctoScript visual kit. It requires no OctoSense Shell modification. Components live in `bundle/main.splash`; icons live in `bundle/assets/icons/`.

- `Primary`: 46px primary action, deep green fill, white label, 12px radius.
- `Secondary`: matching secondary action with a white surface and pale green border.
- `Quiet`: low-emphasis actions inside content cards.
- `Nav` / `ActiveNav`: a shared 24×24 viewBox and 2px rounded-line icon language.
- `NewsCard`: uses the image supplied by the RSS source. When none is available, it renders a consistent topic placeholder instead of generating an unrelated image.

The kit can be copied into other OctoScript apps. Optional Shell/runtime experiments remain isolated under `build/runtime-patches/` and `build/shell-patches/`; the release app does not depend on them.
