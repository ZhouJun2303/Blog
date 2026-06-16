---
id: hKNOLQ
title: Gridea 文档写作规范
createdAt: "2026-06-10 22:10:00"
updated: "2026-06-16 17:26:21"
tags:
    - 写作规范
    - 文档规范
tag_ids:
    - V2lHuS
    - qtVIaK
categories: []
published: true
hideInList: false
feature: /post-images/unity-senior-developer-toolchain-map.svg
isTop: false
---

> 本规范用于本仓库后续新增文章。只要是要发布到 Gridea 的文档，都要按这里的结构、路径、图片和链接规则处理。

![](/post-images/unity-senior-developer-toolchain-map.svg)

## 目录规则

- 文章 Markdown 必须放在 `LocalBK/posts/`。
- 图片必须放在 `LocalBK/post-images/`。
- Gridea 文章是扁平结构，`LocalBK/posts/` 下不要再建子目录。
- 长文档采用“一篇主文档 + N 篇分文档”的方式拆分。
- 主文档 `hideInList: false`，分文档建议 `hideInList: true`，通过主文档目录跳转。
- 新增或修改文章后，同步更新 `LocalBK/config/posts.json`，否则 Gridea 客户端可能识别不到。

## 文件命名

- 文件名使用稳定 slug，例如 `unity-senior-developer-08-performance-memory-package.md`。
- 只使用小写英文、数字和连字符。
- 不使用中文文件名、空格、特殊符号。
- slug 一旦发布不要随意改，否则旧链接会失效。

## Frontmatter 模板

```yaml
---
title: '文章标题'
date: 2026-06-10 21:00:00
tags: [Unity,开发高级/资深,性能优化]
published: true
hideInList: false
feature: /post-images/example.svg
isTop: false
---
```

字段要求：

- `title`：文章标题，使用中文即可。
- `date`：格式固定为 `YYYY-MM-DD HH:mm:ss`。
- `tags`：使用方括号数组，标签不要过多。
- `published`：正式文章为 `true`。
- `hideInList`：主文档为 `false`，分文档可设为 `true`。
- `feature`：有封面图时使用站点根路径 `/post-images/...`，没有则留空。
- `isTop`：默认 `false`。

## 正文结构

- 正文不要再写一级标题，标题交给 frontmatter 和主题渲染。
- 正文从简介、图片或 `##` 二级标题开始。
- 长文档必须有目录或导航表。
- 每个被主文档跳转的段落，前面加稳定锚点：

```html
<a id="performance"></a>
## 性能优化
```

- 内容不能只写方向词，要写具体交付物、工具、排查流程、验收标准。
- 涉及代码时使用带语言的代码块，例如 `csharp`、`json`、`bash`。

## 图片规则

- 图片文件放在 `LocalBK/post-images/`。
- 图片命名使用文章 slug 前缀，例如 `unity-senior-developer-toolchain-map.svg`。
- Markdown 中使用站点根路径：

```markdown
![](/post-images/unity-senior-developer-toolchain-map.svg)
```

- 不使用 `../`、`./images/`、本地绝对路径或仓库相对路径引用图片。

## 内部跳转规则

- 文章之间跳转使用发布后的完整路径：

```markdown
[性能、内存与包体](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/)
```

- 跳到文章内小节时使用锚点：

```markdown
[性能优化](https://zhoujun2303.github.io/post/unity-senior-developer-08-performance-memory-package/#performance)
```

- 不使用 `../xxx.md` 这种源码相对链接。Gridea 发布后，源码路径不会直接存在。

## posts.json 同步规则

每篇文章都要在 `LocalBK/config/posts.json` 中有一条记录：

- `fileName`：不带 `.md` 的 slug。
- `content`：正文内容，不包含 frontmatter。
- `data`：与 frontmatter 保持一致。
- `isEmpty`：有正文时为 `false`。
- `excerpt` 和 `abstract`：默认空字符串。

## 长文档拆分规范

长文档按这个方式拆：

- 主文档：总览、导航、能力地图、工具总览、交付物索引。
- 分文档：每个方向一个专题，必要时继续按小节细分。
- 图片：主文档至少一张总览图，分文档按需要引用流程图或工具图。
- 链接：主文档跳分文档，分文档返回主文档。
- 首页：只让主文档进入列表，分文档隐藏在列表中但保留访问链接。

## 新增文档检查清单

- 文件是否在 `LocalBK/posts/`。
- 是否有完整 frontmatter。
- slug 是否稳定、可读、无中文和空格。
- 图片是否在 `LocalBK/post-images/`。
- 图片是否使用 `/post-images/...`。
- 内部链接是否使用 `https://zhoujun2303.github.io/post/<slug>/`。
- 被跳转的小节是否有稳定 `<a id="..."></a>`。
- 是否同步更新 `LocalBK/config/posts.json`。
- 是否避免空泛表达，写清工具、流程、交付物和验收方式。