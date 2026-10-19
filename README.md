# fuulea-wiki

**辅立码课WiKi** —— 使用手册与 FAQ，基于 [VitePress](https://vitepress.dev/) 构建，部署于 Cloudflare Pages。

🌐 在线访问：<https://fuulea.fuheng.vip>（<https://fuulea-wiki.pages.dev>）

内容维护：辅立码课-华东POD：付恒

## 内容

- **教师端操作手册**：任务发布、教学场景应用、细化使用（含全部操作截图）
- **学生端操作手册**：整理中（来源：飞书《辅立码课学生端 - 使用手册》）
- **FAQ常见问题**：整理中（来源：飞书《辅立码课FAQ（通用）》《考试系统FAQ》）

## 本地开发

```bash
npm install
npm run docs:dev      # 本地预览 http://localhost:5173
npm run docs:build    # 构建输出 docs/.vitepress/dist
```

## 部署

推送至 GitHub `main` 分支 → Cloudflare Pages 自动构建部署 → <https://fuulea.fuheng.vip>

- 构建命令：`npm run docs:build`
- 输出目录：`docs/.vitepress/dist`
- Node 版本：22（见 `.nvmrc`）
- 完整配置方案见 [DEPLOYMENT.md](DEPLOYMENT.md)

## 目录结构

```text
docs/
├── index.md               # 首页
├── teacher/               # 教师端操作手册
│   ├── index.md
│   ├── task-publish.md    # 一、任务发布
│   ├── teaching-scenes.md # 二、教学场景应用
│   └── advanced.md        # 三、细化使用
├── student/               # 学生端操作手册（整理中）
├── faq/                   # FAQ常见问题（整理中）
├── public/images/manual/  # 手册截图
└── .vitepress/            # 站点配置
```

## 如何添加新内容

1. 在 `docs/` 对应目录新建 Markdown 文件，如 `docs/teacher/new-feature.md`
2. 在 `docs/.vitepress/config.mjs` 的 sidebar 对应分组加一行：
   `{ text: '页面标题', link: '/teacher/new-feature' }`
3. 提交推送，Cloudflare Pages 自动部署，1-2 分钟后生效
