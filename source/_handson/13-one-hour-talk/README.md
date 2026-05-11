# 一小时分享 · 配套讲稿与幻灯片

本目录是 Part 0（`source/chapters/00-presentation/`）的配套 hands-on 材料。
Part 0 本身是 **讲稿腹稿**；这里的 `SLIDES.md` 是可以直接投影或
导出的 **幻灯片版本**，带 speaker notes。附录 F 现在是工程师落地手册。

## 文件

- `SLIDES.md` —— 双轨幻灯片（Marp 兼容，也可直接当 Markdown 阅读）
  - 每一页正文是投影内容
  - `<!-- ... -->` 注释块是 **讲者备注**（不会出现在投影上）
  - 页面样式用 `<!-- _class: ... -->` 切换（`title` 首尾、`whiteboard`
    白板页、`pitfall` 陷阱页）
- `README.md` —— 本文件

## 用法

### 方式 1 · 直接阅读

把 `SLIDES.md` 当普通 Markdown 读就行；每一节之间用 `---` 分页，
讲者备注在注释里清晰可见。适合在会议前 10 分钟对一遍流程。

### 方式 2 · 用 Marp 渲染

[Marp](https://marp.app/) 是把 Markdown 直出幻灯片的工具。安装后：

```bash
# 导出为 HTML（浏览器直接放映）
npx @marp-team/marp-cli SLIDES.md -o talk.html

# 导出为 PDF
npx @marp-team/marp-cli SLIDES.md --pdf -o talk.pdf

# 导出为 PowerPoint（保留 speaker notes）
npx @marp-team/marp-cli SLIDES.md --pptx -o talk.pptx
```

如果装了 VS Code 的 **Marp for VS Code** 插件，打开 `SLIDES.md` 就能
右侧预览。

### 方式 3 · 贴进 Keynote / PowerPoint / Google Slides

打开 `SLIDES.md`，按 `---` 分割每一页：

- 把每一页的正文贴进幻灯片的主区域
- 把每一页 `<!-- ... -->` 里的 "讲者备注" 贴进 speaker notes 栏

## 时长

- 标准版（F.0–F.8 主线页）：**约 60 分钟**
- 压缩版（见附录幻灯的 "30 分钟压缩版"）：**约 30 分钟**
- 工作坊版（见附录幻灯的 "90 分钟工作坊版"）：**约 90 分钟**，包含
  现场动手填一张 HarnessCard

## 与 Part 0 讲稿的对应关系

`SLIDES.md` 的每一节标题都与 Part 0 讲稿的小节一一对应（F.0 / F.1 /
… / F.8）。想查某一页背后的详细论证、回书锚、以及避免哪些 pitfall，
翻 `source/chapters/00-presentation/index.md` 的对应小节即可。

## 许可证

同宿主仓库：**CC-BY-NC-ND-4.0**（正文 / 幻灯内容）· **MIT**（若你把某
一页当代码样例引用）。
