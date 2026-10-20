# fuulea-wiki

**辅立码课WiKi** —— 教师端操作手册，基于 [VitePress](https://vitepress.dev/) 构建，部署于 Cloudflare Pages。

🌐 在线访问：<https://fuulea.fuheng.vip>（<https://fuulea-wiki.pages.dev>）

内容维护：辅立码课-华东POD：付恒

## 内容

**教师端操作手册**，分三章：

1. 任务发布 —— 课程/资料/答题卡/背诵/题库选题/选卷/学科网选题、选题篮、发布设置
2. 教学场景应用 —— 大屏讲题、批改阅卷、完成统计、错题反扫
3. 细化使用 —— 举一反三、催交作业、靶向教学、信息修改、考试系统、学情诊断、创建课程、知识点关联

三章在导航栏一级平铺，方便老师一眼定位；页面右侧「页面目录」可直达章内小节。

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
├── teacher/               # 教师端操作手册（全站唯一内容区）
│   ├── index.md           # 手册总览（含快速入口表）
│   ├── task-publish.md    # 一、任务发布
│   ├── teaching-scenes.md # 二、教学场景应用
│   └── advanced.md        # 三、细化使用
├── public/images/manual/  # 手册截图
└── .vitepress/            # 站点配置
```

## 如何添加新内容

新增一章（推荐，保持导航一级平铺）：

1. 新建 `docs/teacher/xxx.md`，一级标题写成「四、xxx」
2. 在 `docs/.vitepress/config.mjs` 的 `nav` 和 `sidebar` 里各加一行：
   `{ text: '四、xxx', link: '/teacher/xxx' }`
3. 提交推送，Cloudflare Pages 自动部署，1-2 分钟后生效

章内小节直接用 `##` 标题，会自动出现在页面右侧「页面目录」里，无需额外配置。
