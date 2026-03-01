[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> 面向 AI 辅助视频发布工作流的文档优先脚手架。

## 📌 一览

| 区域 | 详情 |
| --- | --- |
| 角色 | AI 视频发布工作空间的英文权威文档来源 |
| 语言 | 英文 + 10 种本地化 README 镜像 |
| 生成产物 | `.auto-readme-work/*` 中的快照元数据与流水线追踪 |
| 当前实现 | 仅文档快照（尚未提交可运行的应用代码） |
| 最新快照 | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ README 快速导航

| 章节 | 链接 |
|---|---|
| 概览 | [Overview](#%E2%98%9B-overview) |
| 特性 | [Features](#%E2%9C%A8-features) |
| 项目结构 | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| 前置条件 | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| 安装 | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| 使用方法 | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| 配置 | [Configuration](#%F0%9F%A7%A9-configuration) |
| 示例 | [Examples](#%F0%9F%A7%AA-examples) |
| 开发说明 | [Development notes](#%F0%9F%99%82-development-notes) |
| 故障排查 | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| 路线图 | [Roadmap](#%F0%9F%97%BA-roadmap) |
| 参与贡献 | [Contributing](#%F0%9F%A4%9D-contributing) |
| 支持 | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| 联系方式 | [Contact](#contact) |
| 许可证 | [License](#%F0%9F%93%84-license) |

## 🧭 概述

`AutoPublication` 是一个为更大规模的 AI 视频发布系统提供支撑的仓库级文档脚手架。
它将英文 `README.md` 作为真值源，并通过流水线快照将 `i18n/README.*.md` 中的翻译与之对齐。

### 本仓库是什么

- 一个项目文档和贡献者指南的权威来源。
- 一个多语言文档集，作为 README 持续同步演进的示例。
- 一个位于 `.auto-readme-work/*` 下的历史证据库，记录每次流水线运行。

### 本仓库目前不是什么

- 尚未成为可运行的发布应用。
- 尚未成为包含安装脚本或依赖清单的包。
- 尚未在当前分支提供运行时配置模型（如 `.env`、YAML、CLI schema）。

## ✨ 特性

### 当前能力

- 一个单一源文件中的英文权威文档（`README.md`）。
- 链接所有本地化 README 的语言选择器区块。
- 带时间戳的 auto-README 产物（`pipeline-context`、`language-nav-*`、`translation-plan`、`repo-structure-analysis`）。
- 文档优先的项目映射，用于支持渐进式实现。
- 标准化的支持面板，用于捐赠/赞助展示。

### 计划能力

- AI 辅助的发布流程编排。
- 多平台元数据生成与校验。
- 可配置的发布目标和凭据管理。
- 可复现的本地开发路径，包含测试与 CI 检查。

## 🗂️ 项目结构

```text
AutoPublication/
├── README.md
├── README.md.auto-readme-support
├── README.md.auto-readme-support.filtered
├── .gitignore
├── i18n/
│   ├── README.ar.md
│   ├── README.de.md
│   ├── README.es.md
│   ├── README.fr.md
│   ├── README.ja.md
│   ├── README.ko.md
│   ├── README.ru.md
│   ├── README.vi.md
│   ├── README.zh-Hans.md
│   └── README.zh-Hant.md
└── .auto-readme-work/
    ├── 20260228_230008/
    ├── 20260301_064342/
    ├── 20260301_064412/
    ├── 20260301_064745/
    ├── 20260301_065035/
    ├── 20260301_065907/
    └── 20260301_070712/
        ├── pipeline-context.md
        ├── language-nav-root.md
        ├── language-nav-i18n.md
        └── translation-plan.txt
```

### 关键路径

| 路径 | 用途 |
|---|---|
| `i18n/README.*.md` | 面向用户的本地化 README |
| `.auto-readme-work/*/pipeline-context.md` | 每次流水线运行的约束与元数据 |
| `.auto-readme-work/*/language-nav-*.md` | 官方语言与本地语言映射文件 |
| `.auto-readme-work/*/repo-structure-analysis.md` | 历史结构快照 |
| `.auto-readme-work/*/translation-plan.txt` | 各次运行的语言与翻译范围 |
| `.auto-readme-work/*/translated-files.txt` | 历史运行中输出文件列表 |

## 🧰 前置条件

由于本快照为仅文档内容，运行应用不需要额外运行时依赖。

在维护、复核和同步翻译时，你需要：

- `git`
- 一个兼容 POSIX 的 shell（示例使用 `bash`）
- 一个支持 Markdown 的编辑器
- 可选：用于复核本地化分支的差异查看工具

## 🛠️ 安装

本快照中没有可安装的软件包。

在本地使用：

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ 使用方法

当前主要用于文档和流水线追踪。

```bash
# 检查语言选择器映射
head -n 5 README.md

# 查看最新流水线上下文
cat .auto-readme-work/20260301_070712/pipeline-context.md

# 查看最近一次可用快照中的仓库结构分析
cat .auto-readme-work/20260301_070712/../20260301_065907/repo-structure-analysis.md

# 检查本地化文档的一致性
sed -n '1,90p' i18n/README.fr.md
```

### 推荐的维护流程

1. 更新 `README.md` 的结构或行为相关内容。
2. 按需重新生成翻译更新。
3. 校验关键章节在 `i18n/` 文件中的同步。
4. 保持 `.auto-readme-work` 快照与当前工作流一致。

## 🧩 配置

当前尚未提交正式的运行时配置文件（例如 `.env`、`config.yml`、CLI schema 等）。

如果未来实现运行时，建议采用以下默认实践：

- 新增示例配置文件，如 `config.sample.yml`。
- 通过 `.env`（仓库外部）或托管方密钥管理器保存密钥。
- 在新增配置项时，确保文档与 CLI 引用保持同步。

## 🧪 示例

### 当前示例（已有脚手架）

```bash
# 打开完整英文文档
cat README.md

# 对比本地化版本
sed -n '1,90p' i18n/README.de.md
```

### 未来示例（预计实现）

```bash
# 概念示例；在引入运行时前可能尚未可用
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ 开发说明

- 以增量方式处理更改：优先采用增量增强并避免破坏性重写。
- 将英文源保持为权威文档基线。
- 使用 `i18n/` 目录中的语言文件作为明确同步目标。
- 保持 `.auto-readme-work/` 流水线产物作为历史依据，而非手工编辑的生产代码。
- 避免过度承诺可执行行为；仅记录当前已存在的内容。

### 本 README 中的假设

- 在运行时模块提交前，仓库仍以文档优先为主。
- 翻译应与有意义的结构性修改保持一致。
- `.auto-readme-work/` 包含追加式、按运行场景的历史记录，不是权威工作副本。

## 🔧 故障排查

### 我无法运行 `auto-publication` 命令

**原因：** 本快照中没有运行时应用。

**解决方案：** 将本仓库当作文档工作区使用，等待实现文件的后续补充。

### 本地化 README 与源出现不同步

**原因：** 翻译内容独立于英文源更新。

**解决方案：** 将同样的结构变更应用到所有 `i18n/README.*.md`，然后对齐措辞和示例。

### README 链接指向不存在的功能

**原因：** 文档中包含了计划中的行为。

**解决方案：** 保持该段标注为计划内容，或用当前可验证的命令替换。

## 🗺️ 路线图

- [ ] 增加源码包与运行时入口。
- [ ] 增加依赖清单和安装路径。
- [ ] 增加平台化发布集成。
- [ ] 增加配置校验与密钥处理。
- [ ] 增加可执行示例与 CI 冒烟检测。
- [ ] 增加本地化 README 的自动一致性检查。
- [ ] 增加 `LICENSE` 文件并明确许可条款。

## 🤝 贡献

随着该文档脚手架向实现阶段过渡，欢迎提交贡献。

```bash
# 1. 创建分支
git checkout -b docs/<short-description>

# 2. 提交更改
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. 推送并发起 PR
git push -u origin docs/<short-description>
```

建议的 PR 检查清单：

- 保持 `README.md` 为真值源。
- 更新所有受影响的 `i18n/` 本地化 README。
- 在增量变更时保留现有章节内容。
- 保持 `.auto-readme-work/*` 元数据与当前运行一致。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

如有疑问、文档修正或协作协调，请使用仓库 Issue。

## 📄 License

当前快照中尚未提供 `LICENSE` 文件。

建议下一步：

- 添加 `LICENSE` 文件，并使用目标许可证标识更新本节。

## Submodules

This repository includes these root-level git submodules:

- `AutoPubMonitor` → https://github.com/lachlanchen/AutoPubMonitor
- `LazyEdit` → https://github.com/lachlanchen/LazyEdit
- `AutoPublish` → https://github.com/lachlanchen/AutoPublish
