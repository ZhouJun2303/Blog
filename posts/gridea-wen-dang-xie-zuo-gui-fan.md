---
id: hKNOLQ
title: Gridea 文档写作规范
createdAt: "2026-06-10 22:10:00"
updated: "2026-06-17 10:35:00"
tags:
    - 写作规范
    - 文档规范
tag_ids:
    - V2lHuS
    - qtVIaK
categories:
    - 阅读与资料
category_ids:
    - czdc35
published: true
hideInList: false
feature: /post-images/unity-senior-developer-toolchain-map.svg
isTop: false
---

> 本规范用于当前 Gridea Pro 站点后续新增和维护文章。只要文章最终要发布到本站，就按这里的目录、元数据、图片、链接和渲染规则处理。

![](/post-images/unity-senior-developer-toolchain-map.svg)

## 目录规则

- 站点根目录是当前 Gridea Pro 项目目录，也就是本仓库根目录。
- 文章 Markdown 放在 `posts/`。
- 文章图片放在 `post-images/`。
- 通用静态资源放在 `static/`，不要混进文章图片目录。
- Gridea Pro 文章仍按扁平结构管理，`posts/` 下不要再建子目录。
- 长文档采用“一篇主文档 + N 篇分文档”的方式拆分，每篇文档都有独立 slug。
- 主文档 `hideInList: false`，分文档建议 `hideInList: true`，通过主文档目录跳转。
- `output/` 是 Gridea Pro 渲染后的产物，不要手动编辑。
- 新增、修改、发布和渲染优先通过 Gridea Pro 客户端或 Gridea Pro MCP 完成。

## 文件命名

- 文件名使用稳定 slug，例如 `unity-senior-developer-08-performance-memory-package.md`。
- 只使用小写英文、数字和连字符。
- 不使用中文文件名、空格、特殊符号。
- slug 一旦发布不要随意改，否则旧链接会失效。

## Frontmatter 模板

```yaml
---
id: AbCd12
title: 文章标题
createdAt: "2026-06-17 10:30:00"
updated: "2026-06-17 10:30:00"
tags:
    - Unity
    - 性能优化
tag_ids:
    - WOSAx0
    - 584J9D
categories:
    - Unity
category_ids:
    - h3GlEL
published: true
hideInList: false
feature: /post-images/example.svg
isTop: false
---
```

字段要求：

- `id`：Gridea Pro 的文章 ID。新文章优先让 Gridea Pro 生成；迁移旧文时保持稳定。
- `title`：文章标题，使用中文即可。
- `createdAt`：首次创建时间，格式固定为 `YYYY-MM-DD HH:mm:ss`。
- `updated`：最近更新时间，内容变更后同步更新。
- `tags`：使用 YAML 列表，标签不要过多。
- `tag_ids`：与 `tags` 一一对应，使用 Gridea Pro 已有标签 ID。
- `categories`：通常只放一个分类。
- `category_ids`：与 `categories` 一一对应，使用 Gridea Pro 已有分类 ID。
- `published`：正式文章为 `true`。
- `hideInList`：主文档为 `false`，分文档可设为 `true`。
- `feature`：有封面图时使用站点根路径 `/post-images/...`，没有则留空。
- `isTop`：默认 `false`。

> 手动写 frontmatter 时，优先复用 `config/tags.json` 和 `config/categories.json` 里的名称与 ID。更推荐的做法是用 Gridea Pro 创建文章，再补正文。

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

- 图片文件放在 `post-images/`。
- 图片命名使用文章 slug 前缀，例如 `unity-senior-developer-toolchain-map.svg`。
- Markdown 中使用站点根路径：

```markdown
![](/post-images/unity-senior-developer-toolchain-map.svg)
```

- 不使用 `../`、`./images/`、本地绝对路径或仓库相对路径引用图片。
- 能说明内容的图片要写 alt 文本，例如 `![Unity 开发技能地图](/post-images/unity-senior-developer-skill-map.svg)`。
- 封面图路径写在 `feature` 字段里，正文里是否再次展示按文章需要决定。

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
- 当前项目发布路径由 Gridea Pro 配置决定：文章路径是 `/post/<slug>/`，标签路径是 `/tag/<slug>/`。

## Gridea Pro 元数据规则

- `config/posts.json`、`config/tags.json`、`config/categories.json` 是 Gridea Pro 的站点数据，不再当作文档写作的手工主入口。
- 通过 Gridea Pro 客户端或 Gridea Pro MCP 创建、更新文章时，让工具维护这些 JSON。
- 如果直接修改 `posts/*.md`，要确认对应文章在 `config/posts.json` 中的 `content`、标题、标签、分类、发布时间也已同步，否则渲染结果可能仍是旧内容。
- 不要手动改 `output/post/.../index.html`，它会在渲染时被覆盖。
- 不要随意删除或重建已有文章 `id`、`tag_ids`、`category_ids`，这些字段会影响 Gridea Pro 识别和分类。

## 发布与渲染规则

- 内容修改完成后，用 Gridea Pro 渲染站点。
- 渲染后检查 `output/post/<slug>/index.html` 是否更新。
- 发布前确认页面里没有本地路径、源码相对链接、失效图片和旧域名。
- RSS、站点地图、首页列表、标签页和分类页都属于渲染产物，异常时重新渲染，不手动改输出文件。

## 长文档拆分规范

长文档按这个方式拆：

- 主文档：总览、导航、能力地图、工具总览、交付物索引。
- 分文档：每个方向一个专题，必要时继续按小节细分。
- 图片：主文档至少一张总览图，分文档按需要引用流程图或工具图。
- 链接：主文档跳分文档，分文档返回主文档。
- 首页：只让主文档进入列表，分文档隐藏在列表中但保留访问链接。

## 新增文档检查清单

- 文件是否在 `posts/`。
- 是否有完整 Gridea Pro frontmatter。
- slug 是否稳定、可读、无中文和空格。
- `createdAt` 和 `updated` 是否是 `YYYY-MM-DD HH:mm:ss`。
- 标签、分类名称是否存在，对应 ID 是否同步。
- 图片是否在 `post-images/`。
- 图片是否使用 `/post-images/...`。
- 内部链接是否使用 `https://zhoujun2303.github.io/post/<slug>/`。
- 被跳转的小节是否有稳定 `<a id="..."></a>`。
- 如手动改 Markdown，是否同步或确认了 `config/posts.json`。
- 是否完成 Gridea Pro 渲染并检查输出页。
- 是否避免空泛表达，写清工具、流程、交付物和验收方式。
