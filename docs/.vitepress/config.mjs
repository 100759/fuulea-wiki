import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: '辅立码课知识库',
  description: '辅立码课（智慧教学云）产品使用手册与 FAQ 知识库 —— 任务发布、教学场景、考试系统、学情诊断全流程指南',
  lang: 'zh-CN',
  base: '/',
  cleanUrls: true,
  lastUpdated: true,
  // 站点地图，便于搜索引擎收录（域名需与最终部署域名一致）
  sitemap: {
    hostname: 'https://fuulea.fuheng.vip'
  },
  head: [
    ['link', { rel: 'icon', href: '/favicon.svg', type: 'image/svg+xml' }],
    ['meta', { name: 'theme-color', content: '#2563eb' }]
  ],
  markdown: {
    // 代码块行号
    lineNumbers: true
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    logo: '/favicon.svg',

    nav: [
      { text: '首页', link: '/' },
      {
        text: '使用手册',
        items: [
          { text: '教师端操作手册', link: '/teacher/' },
          { text: '学生端使用手册', link: '/student/' }
        ]
      },
      { text: 'FAQ', link: '/faq/' },
      { text: '后台管理', link: '/admin/' },
      { text: '关于', link: '/about' }
    ],

    sidebar: [
      {
        text: '产品介绍',
        collapsed: false,
        items: [
          { text: '辅立码课是什么', link: '/product/intro' }
        ]
      },
      {
        text: '教师端操作手册',
        collapsed: false,
        items: [
          { text: '总览', link: '/teacher/' },
          { text: '一、任务发布', link: '/teacher/task-publish' },
          { text: '二、教学场景应用', link: '/teacher/teaching-scenes' },
          { text: '三、细化使用', link: '/teacher/advanced' }
        ]
      },
      {
        text: '学生端',
        collapsed: true,
        items: [
          { text: '使用手册（整理中）', link: '/student/' }
        ]
      },
      {
        text: 'FAQ 常见问题',
        collapsed: true,
        items: [
          { text: '常见问题（整理中）', link: '/faq/' }
        ]
      },
      {
        text: '后台管理 & 录入站',
        collapsed: true,
        items: [
          { text: '员工版 FAQ（整理中）', link: '/admin/' }
        ]
      },
      {
        text: '关于本站',
        collapsed: true,
        items: [
          { text: '关于与贡献指南', link: '/about' }
        ]
      }
    ],

    outline: {
      level: [2, 3],
      label: '页面目录'
    },

    lastUpdated: {
      text: '最后更新于',
      formatOptions: {
        dateStyle: 'full',
        timeStyle: 'medium'
      }
    },

    docFooter: {
      prev: '上一页',
      next: '下一页'
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '搜索文档',
            buttonAriaLabel: '搜索文档'
          },
          modal: {
            noResultsText: '没有找到相关结果',
            resetButtonTitle: '清除搜索条件',
            footer: {
              selectText: '选择',
              navigateText: '切换',
              closeText: '关闭'
            }
          }
        }
      }
    },

    editLink: {
      pattern: 'https://github.com/100759/fuulea-wiki/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/100759/fuulea-wiki' }
    ],

    footer: {
      message: '辅立码课（智慧教学云）产品知识库',
      copyright: 'Copyright © 2026 河北习知软件科技有限公司'
    }
  }
})
