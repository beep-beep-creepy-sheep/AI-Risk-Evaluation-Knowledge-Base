import { defineConfig } from 'vitepress'

const enSidebar = [
  {
    text: 'Handbook',
    items: [
      { text: 'Introduction', link: '/introduction' },
      { text: 'Safe-Use Principles', link: '/safe-use-principles' },
      { text: 'Prompt Patterns', link: '/prompt-patterns' },
      { text: 'Risk Taxonomy', link: '/risk-taxonomy' },
      { text: 'Evaluation Design', link: '/evaluation-design' },
      { text: 'Harness Workflow', link: '/harness-workflow' },
      { text: 'Test Case Library', link: '/test-case-library' },
      { text: 'Error Analysis', link: '/error-analysis-playbook' },
      { text: 'Templates & Checklists', link: '/templates-checklists' }
    ]
  }
]

const zhSidebar = [
  {
    text: '手册',
    items: [
      { text: '导读', link: '/zh/introduction' },
      { text: '安全使用原则', link: '/zh/safe-use-principles' },
      { text: '提示词模式', link: '/zh/prompt-patterns' },
      { text: '风险分类', link: '/zh/risk-taxonomy' },
      { text: '评估设计', link: '/zh/evaluation-design' },
      { text: '评估闭环', link: '/zh/harness-workflow' },
      { text: '测试用例库', link: '/zh/test-case-library' },
      { text: '错误分析', link: '/zh/error-analysis-playbook' },
      { text: '模板与清单', link: '/zh/templates-checklists' }
    ]
  }
]

export default defineConfig({
  title: 'AI Risk & Evaluation Knowledge Base',
  description: 'A bilingual handbook for safe AI use, prompt engineering, and evaluation design in analyst workflows.',
  cleanUrls: true,
  ignoreDeadLinks: false,
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'AI Risk & Evaluation Knowledge Base',
      description: 'A practical handbook for safe analyst AI workflows.',
      themeConfig: {
        nav: [
          { text: 'Guide', link: '/introduction' },
          { text: '中文', link: '/zh/' },
          { text: 'GitHub', link: 'https://github.com/beep-beep-creepy-sheep/AI-Risk-Evaluation-Knowledge-Base' }
        ],
        sidebar: enSidebar
      }
    },
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'AI 风险与评估知识库',
      description: '面向分析师工作流的 AI 安全使用、提示词工程与评估设计手册。',
      themeConfig: {
        nav: [
          { text: '指南', link: '/zh/introduction' },
          { text: 'English', link: '/' },
          { text: 'GitHub', link: 'https://github.com/beep-beep-creepy-sheep/AI-Risk-Evaluation-Knowledge-Base' }
        ],
        sidebar: zhSidebar
      }
    }
  },
  themeConfig: {
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Educational mock-data handbook. Not financial advice.',
      copyright: 'Released as a personal learning project.'
    }
  }
})
