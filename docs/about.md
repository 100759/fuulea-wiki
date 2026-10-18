# 关于本站

## 站点简介

本站是**辅立码课（智慧教学云）**的产品知识库，使用 [VitePress](https://vitepress.dev/) 构建，部署于 Cloudflare Pages，自定义域名 **fuulea.fuheng.vip**。

- 项目仓库：<https://github.com/100759/fuulea-wiki>
- 部署平台：Cloudflare Pages（GitHub 推送自动部署）
- 内容维护：河北习知软件科技有限公司

## 内容来源

| 内容 | 来源 | 状态 |
| --- | --- | --- |
| 教师端操作手册（任务发布 / 教学场景应用 / 细化使用） | 《辅立码课教师操作手册》PDF（北京辅立教育科技研究院，2025 年 6 月） | ✅ 已整理，含全部截图 |
| 学生端使用手册 | 飞书《辅立码课学生端 - 使用手册》 | ⏳ 待导出补充 |
| FAQ（通用 / 考试系统） | 飞书《辅立码课FAQ（通用）》《考试系统FAQ》 | ⏳ 待导出补充 |
| 后台管理 & 录入站 FAQ | 飞书《后台管理&录入站_FAQ（员工版）》 | ⏳ 待导出补充 |

::: info 关于飞书文档
上述飞书文档位于《产品使用手册 && FAQ》wiki 节点下（<https://dcnfinl5rn4u.feishu.cn/wiki/Z0k2wEGNOipHMMkzXAEcKThlnfh>），需要登录后才能读取全文。请在各飞书文档右上角「…」→「导出」为 Markdown/Word 后，按下方流程放入本站。
:::

## 如何添加新内容

本站结构专为持续扩充设计，新增一个页面只需两步：

**第一步**：在 `docs/` 对应目录下新建 Markdown 文件，例如新增一篇教师端章节：

```text
docs/teacher/new-feature.md
```

```markdown
# 新功能名称

正文内容……
```

**第二步**：在 `docs/.vitepress/config.mjs` 的 `sidebar` 对应分组中加一行：

```js
{ text: '新功能名称', link: '/teacher/new-feature' }
```

推送后 Cloudflare Pages 会自动重新部署，约 1-2 分钟后生效。

### 图片放置

截图等静态资源放在 `docs/public/images/` 下，页面中用绝对路径引用：

```markdown
![截图说明](/images/manual/xxx.png)
```

### 本地预览

```bash
npm install
npm run docs:dev      # 本地开发，默认 http://localhost:5173
npm run docs:build    # 生产构建，输出 docs/.vitepress/dist
```

## 技术栈

| 组件 | 选型 | 说明 |
| --- | --- | --- |
| 框架 | VitePress 1.6 | Vue 驱动静态站点生成器 |
| 搜索 | 本地搜索（minisearch） | 无需外部服务 |
| 部署 | Cloudflare Pages | GitHub 集成，推送自动构建 |
| 域名 | fuulea.fuheng.vip | Cloudflare DNS CNAME |
| Node | ≥ 18（.nvmrc 固定 22） | Cloudflare 构建环境同步 |
