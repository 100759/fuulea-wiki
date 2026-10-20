# fuulea-wiki 部署配置方案

> 辅立码课（智慧教学云）知识库 —— VitePress + GitHub + Cloudflare Pages 全链路配置
>
> 文档版本：2026-10-19 ｜ 维护人：付恒 ｜ 站点：<https://fuulea.fuheng.vip>

---

## 1. 架构总览

```text
本地编辑 Markdown
      │  git push
      ▼
┌─────────────────────┐     push 触发构建      ┌──────────────────────┐
│  GitHub 仓库         │ ────────────────────▶ │  Cloudflare Pages    │
│  100759/fuulea-wiki  │   npm run docs:build  │  项目：fuulea-wiki   │
│  (public, main)      │                       │  自动部署            │
└─────────────────────┘                       └──────────┬───────────┘
                                                          │ CNAME
                                                          ▼
                                               fuulea.fuheng.vip
                                               （fuheng.vip zone 内自动解析）
```

| 环节 | 服务 | 配置要点 |
| --- | --- | --- |
| 代码托管 | GitHub `100759/fuulea-wiki` | 公开仓库，默认分支 `main` |
| 自动构建 | Cloudflare Pages | 构建命令 `npm run docs:build`，输出目录 `docs/.vitepress/dist` |
| 域名 | `fuulea.fuheng.vip` | zone `fuheng.vip`（ID `cbd62ce95577789e84efa713160d67f2`）内 CNAME 指向 Pages |
| 回滚 | Cloudflare Pages 控制台 | 一键回滚到任意历史部署 |

---

## 2. 项目配置（本地 / 仓库内）

### 2.1 package.json

```json
{
  "name": "fuulea-wiki",
  "version": "1.0.0",
  "private": true,
  "type": "module",
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  },
  "devDependencies": {
    "vitepress": "^1.6.4"
  },
  "engines": {
    "node": ">=18"
  }
}
```

### 2.2 Node 版本固定

仓库根目录 `.nvmrc` 内容为 `22`。Cloudflare Pages 构建环境读取 `.nvmrc` 自动选择 Node 22；同时在 Pages 项目环境变量中设置 `NODE_VERSION=22` 双保险（VitePress 1.6 要求 Node ≥ 18）。

### 2.3 目录结构

```text
fuulea-wiki/
├── package.json            # 依赖与脚本
├── .nvmrc                  # Node 22
├── .gitignore              # 忽略 node_modules / dist / cache
├── README.md
├── DEPLOYMENT.md           # 本文档
└── docs/                   # VitePress 根目录
    ├── index.md            # 首页（hero + features）
    ├── teacher/            # 教师端操作手册（全站唯一内容区）
    │   ├── index.md            # 手册总览（含快速入口表）
    │   ├── task-publish.md     # 一、任务发布
    │   ├── teaching-scenes.md  # 二、教学场景应用
    │   └── advanced.md         # 三、细化使用
    ├── public/             # 静态资源（原样拷贝到站点根）
    │   ├── favicon.svg
    │   └── images/manual/  # 手册截图 99 张
    └── .vitepress/
        ├── config.mjs      # 站点配置（导航/侧边栏/搜索/sitemap）
        └── theme/          # 自定义主题（品牌色）
```

### 2.4 VitePress 关键配置（docs/.vitepress/config.mjs）

| 配置项 | 值 | 说明 |
| --- | --- | --- |
| `base` | `'/'` | 部署在域名根路径 |
| `cleanUrls` | `true` | 链接不带 `.html`；Cloudflare Pages 会自动把 `/teacher/advanced` 匹配到 `teacher/advanced.html` |
| `lang` | `'zh-CN'` | 中文界面 |
| `lastUpdated` | `true` | 页脚显示 git 最后提交时间（Cloudflare 构建环境带 git） |
| `sitemap.hostname` | `https://fuulea.fuheng.vip` | 生成 sitemap.xml |
| `search.provider` | `'local'` | minisearch 本地搜索，零外部依赖 |
| `editLink.pattern` | GitHub 编辑链接 | 每页「在 GitHub 上编辑此页」 |
| `themeConfig.sidebar` | 6 个分组 | 新增页面只需在对应分组加一行 |

---

## 3. GitHub 仓库配置

| 项 | 值 |
| --- | --- |
| 仓库 | `https://github.com/100759/fuulea-wiki` |
| 可见性 | Public |
| 默认分支 | `main` |
| 提交身份 | 付恒 `<63717495+100759@users.noreply.github.com>` |

推送方式（任选其一）：

```bash
# HTTPS + PAT（推荐，本次采用）
git remote add origin https://github.com/100759/fuulea-wiki.git
git push -u origin main
# 提示输入用户名时填 100759，密码处粘贴 PAT

# 或一次性配置（避免重复输入）
git remote set-url origin https://100759:<PAT>@github.com/100759/fuulea-wiki.git
```

---

## 4. Cloudflare Pages 部署配置

### 4.1 账号信息

| 项 | 值 |
| --- | --- |
| 账号 | `2827162018@qq.com's Account` |
| Account ID | `47843e1d05e3cb3056fee2c26f0de2be` |
| zone（域名） | `fuheng.vip`，ID `cbd62ce95577789e84efa713160d67f2`，Free 计划，NS 为 `benedict/clara.ns.cloudflare.com` |

### 4.2 创建 Pages 项目并关联 GitHub

**方式 A：Cloudflare API（本次采用）**

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/47843e1d05e3cb3056fee2c26f0de2be/pages/projects" \
  -H "Authorization: Bearer <CLOUDFLARE_API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "fuulea-wiki",
    "production_branch": "main",
    "source": {
      "type": "github",
      "config": {
        "owner": "100759",
        "repo_name": "fuulea-wiki",
        "production_branch": "main",
        "deployments_enabled": true,
        "pr_comments_enabled": true
      }
    },
    "build_config": {
      "build_command": "npm run docs:build",
      "destination_dir": "docs/.vitepress/dist",
      "root_dir": ""
    },
    "deployment_configs": {
      "production": {
        "env_vars": {
          "NODE_VERSION": { "value": "22" }
        }
      },
      "preview": {
        "env_vars": {
          "NODE_VERSION": { "value": "22" }
        }
      }
    }
  }'
```

> 前提：Cloudflare 的 GitHub App 已安装且授权访问 `100759/fuulea-wiki`。
> 若 API 报「GitHub connection」相关错误，到 Dashboard 完成一次授权即可：
> <https://dashboard.cloudflare.com/?to=/:47843e1d05e3cb3056fee2c26f0de2be/pages/view/fuulea-wiki>
> →「Connect to Git」→ 安装 Cloudflare GitHub App → 勾选 `fuulea-wiki` 仓库。

**方式 B：Dashboard 图形界面（等价）**

Pages →「创建项目」→「连接到 Git」→ 选 `100759/fuulea-wiki` → 构建设置：

| 设置项 | 值 |
| --- | --- |
| 框架预设 | 无（None） |
| 构建命令 | `npm run docs:build` |
| 构建输出目录 | `docs/.vitepress/dist` |
| 根目录 | （留空） |
| 环境变量 | `NODE_VERSION = 22` |

**执行结果**（2026-10-19 00:16 UTC，方式 A）：项目创建成功，返回确认——

- `source.type = github`，`owner = 100759`，`repo_name = fuulea-wiki`，`repo_id = 1424926920`
- `deployments_enabled = true`、`production_deployments_enabled = true`
- 生产域名 `fuulea-wiki.pages.dev` 已分配
- 推送空提交触发首次构建，**production 部署成功**（deploy success）

### 4.3 自动部署触发规则

- 推送（push）到 `main` → 自动构建并发布为 **production** 部署
- 非 main 分支推送 / PR → 生成 **preview** 部署（`<hash>.fuulea-wiki.pages.dev`）
- 每次部署可在 Pages 控制台查看日志、回滚

### 4.4 备选方案：GitHub Actions + wrangler（不依赖 Cloudflare Git 集成）

如果暂不想授权 Cloudflare 访问 GitHub，可在仓库加 `.github/workflows/deploy.yml`：

```yaml
name: Deploy to Cloudflare Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run docs:build
      - uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          command: pages deploy docs/.vitepress/dist --project-name=fuulea-wiki
```

需在仓库 Settings → Secrets 添加 `CLOUDFLARE_API_TOKEN`（权限：Account → Cloudflare Pages → Edit）。

---

## 5. 域名解析配置

### 5.1 目标

`https://fuulea.fuheng.vip` → Cloudflare Pages 项目 `fuulea-wiki`

### 5.2 DNS 记录

| 类型 | 名称 | 内容 | 代理状态 |
| --- | --- | --- | --- |
| CNAME | `fuulea` | `fuulea-wiki.pages.dev` | 已代理（橙色云） |

因为 `fuheng.vip` 的 NS 已指向 Cloudflare，把域名加到 Pages 项目后，Cloudflare 会自动写入（或自动扁平化为代理记录）该 CNAME。

> ✅ **最终状态（2026-10-19 复核）**：`fuulea.fuheng.vip` 在 Pages 项目中状态为 **active**，`verification_data.status = active`；
> `dig +short fuulea.fuheng.vip` 返回 Cloudflare 代理 IP `172.67.217.214` / `104.21.86.103`；
> `https://fuulea.fuheng.vip/` 返回 200，标题、章节页、截图资源均正常。
>
> 📌 **过程备注**：刚通过 API 添加时是 `pending` 并报 `CNAME record not set`，此后无需人工干预即自行转为 active（记录已由 Cloudflare 侧补齐）。
> 若再次遇到长时间 pending，再走 5.3 的手动兜底。

**API 添加域名：**

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/47843e1d05e3cb3056fee2c26f0de2be/pages/projects/fuulea-wiki/domains" \
  -H "Authorization: Bearer <CLOUDFLARE_API_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{ "name": "fuulea.fuheng.vip" }'
```

### 5.3 手动添加 DNS（备选兜底）

Dashboard → `fuheng.vip` → DNS → 添加记录（直达链接：<https://dash.cloudflare.com/cbd62ce95577789e84efa713160d67f2/fuheng.vip/dns>）：

- 类型：`CNAME`
- 名称：`fuulea`
- 目标：`fuulea-wiki.pages.dev`
- 代理状态：**开启**（橙色云，走 Cloudflare CDN）
- TTL：自动

添加完成后，返回 Pages → `fuulea-wiki` → 域名设置，状态会从 pending 变为 active（约 1-2 分钟），SSL 证书自动签发。

### 5.4 生效与验证

```bash
# 1. DNS 解析验证（应返回 Cloudflare 任播 IP，如 104.21.x.x / 172.67.x.x）
dig fuulea.fuheng.vip +short

# 2. HTTPS 访问验证（证书由 Cloudflare 自动签发，通常几分钟内）
curl -I https://fuulea.fuheng.vip

# 3. 页面抽查
curl -s https://fuulea.fuheng.vip/teacher/task-publish | grep -o "<title>[^<]*</title>"
```

### 5.5 注意事项

- Pages 自动为该域名签发 Universal SSL 证书，无需手动配置
- 如果域名长时间 pending，检查 zone 是否已激活（`fuheng.vip` 当前状态 active）
- 修改 DNS 后全球生效通常几分钟；本地 DNS 缓存可 `sudo dscacheutil -flushcache` 刷新

---

## 6. 日常运维

### 6.1 更新内容

```bash
# 1. 本地改 docs/ 下的 Markdown
# 2. 本地预览（可选）
npm run docs:dev
# 3. 提交推送
git add -A && git commit -m "docs: 更新 xxx" && git push
# 4. 等 1-2 分钟，Cloudflare Pages 自动部署完成
```

### 6.2 新增一个页面

1. `docs/` 对应目录新建 `xxx.md`
2. `docs/.vitepress/config.mjs` 的 sidebar 对应分组加 `{ text: '页面标题', link: '/路径/xxx' }`
3. 提交推送

### 6.3 回滚

Cloudflare Dashboard → Pages → `fuulea-wiki` → 部署记录 → 选历史部署 →「回滚到此部署」。

### 6.4 本地构建验证（推送前自检）

```bash
npm run docs:build   # 失败则先修复再推送，避免污染部署记录
```

---

## 7. 故障排查

| 现象 | 排查 |
| --- | --- |
| 推送后没有触发部署 | 检查 Pages 项目是否显示 GitHub 已连接；重新执行「Connect to Git」 |
| 构建失败 `spawn git ENOENT` | 构建环境缺少 git 或 PATH 问题；确认 `NODE_VERSION=22` 且未改动默认构建镜像 |
| 页面 404（不带 .html 的链接） | Pages 默认支持无扩展名匹配；若用自建服务器需配 try_files |
| 图片不显示 | 确认图片在 `docs/public/` 下且引用以 `/` 开头 |
| 域名 pending | 确认 zone NS 为 Cloudflare；CNAME 目标为 `<项目名>.pages.dev` |
| 搜索无结果 | 本地搜索为构建期索引，重新构建后生效 |

---

## 8. 本次交付清单（已完成）

| # | 事项 | 状态 |
| --- | --- | --- |
| 1 | VitePress 项目 `fuulea-wiki` 本地构建通过 | ✅ |
| 2 | 教师端操作手册全文 + 99 张截图 | ✅ |
| 3 | GitHub 仓库 `100759/fuulea-wiki`（public，main） | ✅ <https://github.com/100759/fuulea-wiki> |
| 4 | 代码推送（134 个跟踪文件） | ✅ |
| 5 | Cloudflare Pages 项目 `fuulea-wiki` + GitHub 关联 | ✅ 推送自动触发构建 |
| 6 | 生产域名 `fuulea-wiki.pages.dev` 上线 | ✅ 已验证 200 |
| 7 | 自定义域名 `fuulea.fuheng.vip` | ✅ 已 active，HTTPS 200 |
| 8 | 推送 → 自动部署全链路验证 | ✅ 多轮 deploy success |
| 9 | 站内去除所有 GitHub 外链（导航图标 /「编辑此页」/ 首页「在 GitHub 上查看」） | ✅ 线上已验证无残留 |

> **关于第 7 项**：域名经 Pages API 添加后曾短暂处于 `pending`（报 "CNAME record not set"），随后由 Cloudflare 侧自行补齐记录转为 `active`，
> 无需人工干预。复核结果：`dig +short fuulea.fuheng.vip` → `172.67.217.214` / `104.21.86.103`（代理开启）；
> `https://fuulea.fuheng.vip/`、`/teacher/task-publish`、`/images/manual/*.png` 全部 200。若日后重建项目遇到同类 pending，按 5.3 手动兜底即可。
>
> **关于第 9 项**：站点面向学校老师，仓库入口属误操作风险点，故已全部移除——`themeConfig.editLink` 置空、删除导航栏 GitHub 社交图标、
> 首页 hero 区改为仅保留「教师端操作手册」与「FAQ常见问题」两个按钮。仓库内的 `README.md` / 本文件仍保留 GitHub 地址，
> 但它们不参与站点构建（不在 `docs/` 下），仅作开发侧文档。
