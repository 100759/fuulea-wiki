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
│   ├── task-publish.md    # 任务发布
│   ├── teaching-scenes.md # 教学场景应用
│   ├── advanced.md        # 细化使用
│   └── import-scores.md   # 如何导入成绩（含操作录屏）
├── public/
│   ├── images/manual/     # 手册截图
│   └── videos/            # 操作录屏（mp4）
└── .vitepress/            # 站点配置
```

### 放视频

录屏统一放 `docs/public/videos/`，页面里用全局组件 `VideoPlayer`：

```html
<VideoPlayer
  src="/videos/xxx.mp4"
  poster="/images/manual/xxx.png"
  caption="视频说明"
/>
```

`preload="none"`、`playsinline` 已在组件里设好，直接写 src 即可。
**单个 mp4 不要超过 25 MiB**（Cloudflare Pages 单文件上限）。录屏一般是 60fps 的高分辨率大文件，
上传前先压一遍，例如：

```bash
ffmpeg -i 原始.mov -vf "scale=1470:-1,fps=30" \
  -c:v libx264 -preset medium -crf 30 -pix_fmt yuv420p \
  -c:a aac -b:a 48k -ac 1 -movflags +faststart \
  docs/public/videos/xxx.mp4
```

实测一段 2 分 38 秒、2940×1912@60fps 的原始录屏（154 MB）压完是 5.9 MB。

## 如何添加新内容

新增一章（推荐，保持导航一级平铺）：

1. 新建 `docs/teacher/xxx.md`，一级标题直接写章名（不带「一、二、三」序号，导航栏只放纯章名）
2. 在 `docs/.vitepress/config.mjs` 的 `nav` 和 `sidebar` 里各加一行：
   `{ text: 'xxx', link: '/teacher/xxx' }`
3. 提交推送，Cloudflare Pages 自动部署，1-2 分钟后生效

> 导航项超过 6 个时建议改成下拉菜单（`nav` 项里用 `items: [...]` 嵌套），避免顶部挤压。

章内小节直接用 `##` 标题，会自动出现在页面右侧「页面目录」里，无需额外配置。

### 编号约定（已按此执行）

| 位置 | 编号 |
| --- | --- |
| 顶部导航栏 | **无序号**，只放章名 |
| 左侧边栏 | `一、` `二、` `三、` + 章名 |
| 右侧「页面目录」一级标题（`##`） | `1`、`2`、`3`…（页内递增） |
| 右侧「页面目录」二级标题（`###`） | `1.1`、`1.2`…（在所属 `##` 下重新从 1 开始） |

示例：

```markdown
## 4 答题卡任务
### 4.1 添加题目
### 4.2 答案与解析
### 4.3 切题
## 5 背诵任务
```

右侧目录会自动带上序号（它由标题文本生成，不是配置出来的）。
**注意**：标题一旦以数字开头，锚点 id 会变成 `_4-答题卡任务` 这种带下划线前缀的形式，
所以改序号后必须同步修正所有指向旧锚点的链接——`python3 _work/fix_anchors.py` 会按构建产物里的
真实 id 自动改，然后再跑 `python3 _work/check_links.py` 校验（同页 `#anchor` 与跨页 `/path#anchor` 都查）。
