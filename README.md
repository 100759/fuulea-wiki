# fuulea-wiki

**辅立码课（智慧教学云）产品知识库** —— 基于 [VitePress](https://vitepress.dev/) 构建，部署于 Cloudflare Pages。

🌐 在线访问：<https://fuulea.fuheng.vip>

## 内容

- **教师端操作手册**：任务发布、教学场景应用、细化使用（含全部操作截图）
- **产品介绍**：辅立码课是什么、六大任务类型、产品矩阵
- **FAQ / 学生端 / 后台管理**：内容整理中（来源：飞书《产品使用手册 && FAQ》）

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

## 目录结构

```text
docs/
├── index.md               # 首页
├── product/               # 产品介绍
├── teacher/               # 教师端操作手册
│   ├── task-publish.md    # 一、任务发布
│   ├── teaching-scenes.md # 二、教学场景应用
│   └── advanced.md        # 三、细化使用
├── student/               # 学生端（整理中）
├── faq/                   # FAQ（整理中）
├── admin/                 # 后台管理（整理中）
├── about.md               # 关于与贡献指南
├── public/images/manual/  # 手册截图
└── .vitepress/            # 站点配置
```

新增页面流程见 [关于本站 - 如何添加新内容](https://fuulea.fuheng.vip/about)。
