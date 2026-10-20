import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: '辅立码课WiKi',
  description: '辅立码课教师端操作手册 —— 任务发布、教学场景应用、细化使用',
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
      { text: '手册总览', link: '/teacher/' },
      { text: '任务发布', link: '/teacher/task-publish' },
      { text: '教学场景应用', link: '/teacher/teaching-scenes' },
      { text: '细化使用', link: '/teacher/advanced' }
    ],

    // 全站统一侧边栏：只有教师端手册，各章常驻，方便随时切换
    sidebar: [
      {
        text: '教师端操作手册',
        collapsed: false,
        items: [
          { text: '手册总览', link: '/teacher/' },
          { text: '一、任务发布', link: '/teacher/task-publish' },
          { text: '二、教学场景应用', link: '/teacher/teaching-scenes' },
          { text: '三、细化使用', link: '/teacher/advanced' },
          { text: '如何导入成绩', link: '/teacher/import-scores' }
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

    editLink: undefined,

    footer: {
      message: '内容维护：辅立码课-华东POD：付恒',
      copyright: 'Copyright © 2026 辅立码课WiKi'
    }
  }
})
