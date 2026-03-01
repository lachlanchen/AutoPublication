[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> 面向 AI 輔助影片發佈工作流程的文件優先腳手架。

## 📌 一覽

| 區域 | 詳情 |
| --- | --- |
| 角色 | AI 影片發布工作空間的英文權威文件來源 |
| 語言 | 英文 + 10 種在地化 README 鏡像 |
| 產生產物 | `.auto-readme-work/*` 中的快照中繼資料與流程追蹤 |
| 目前實作 | 僅有文件快照（目前尚未提交可執行應用程式程式碼） |
| 最新快照 | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ README 快速導覽

| 章節 | 連結 |
|---|---|
| 概覽 | [Overview](#%E2%98%9B-overview) |
| 特性 | [Features](#%E2%9C%A8-features) |
| 專案結構 | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| 前置需求 | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| 安裝 | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| 使用方式 | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| 設定 | [Configuration](#%F0%9F%A7%A9-configuration) |
| 範例 | [Examples](#%F0%9F%A7%AA-examples) |
| 開發備註 | [Development notes](#%F0%9F%99%82-development-notes) |
| 疑難排解 | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| 路線圖 | [Roadmap](#%F0%9F%97%BA-roadmap) |
| 參與貢獻 | [Contributing](#%F0%9F%A4%9D-contributing) |
| 支援 | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| 聯絡方式 | [Contact](#contact) |
| 授權 | [License](#%F0%9F%93%84-license) |

## 🧭 概述

`AutoPublication` 是一個用來支援更大規模 AI 影片發布系統的儲存庫層級文件腳手架。它保留英文版 `README.md` 作為真實來源，並透過流程快照對齊 `i18n/README.*.md` 中的翻譯。

### 這個儲存庫是什麼

- 一個專案文件與貢獻者指引的權威來源。
- 一套多語系文件，用作 README 持續同步演進的範本。
- `.auto-readme-work/*` 底下的歷史證據庫，保存每次流程執行的紀錄。

### 這個儲存庫目前還不是

- 尚未成為可執行的發布應用。
- 尚未成為包含安裝腳本或相依套件清單的套件。
- 在目前分支中尚未提供運行時設定模型（如 `.env`、YAML、CLI schema）。

## ✨ 特性

### 目前能力

- 權威英文文件集中在單一來源檔案（`README.md`）。
- 具備連結所有在地化 README 的語言選擇器區塊。
- 具時間戳記的 auto-README 產物（`pipeline-context`、`language-nav-*`、`translation-plan`、`repo-structure-analysis`）。
- 文件優先的專案地圖，支援漸進式實作。
- 標準化的贊助展示面板，讓捐款/贊助資訊可見。

### 規劃中能力

- AI 輔助發布流程編排。
- 多平台中繼資料生成與驗證。
- 可設定的發布目標與憑證管理。
- 可重現的本機開發路徑，逐步加入測試與 CI 檢查。

## 🗂️ 專案結構

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

### 關鍵路徑

| 路徑 | 用途 |
|---|---|
| `i18n/README.*.md` | 使用者可見文件的在地化 README |
| `.auto-readme-work/*/pipeline-context.md` | 每次流程執行的約束條件與中繼資料 |
| `.auto-readme-work/*/language-nav-*.md` | 官方語系與在地化對應檔 |
| `.auto-readme-work/*/repo-structure-analysis.md` | 專案結構快照歷史 |
| `.auto-readme-work/*/translation-plan.txt` | 語言與翻譯範圍 |
| `.auto-readme-work/*/translated-files.txt` | 歷次翻譯輸出的檔案清單 |

## 🧰 前置需求

因為此快照僅為文件，故不需要執行時依賴。

在維護、審閱與翻譯同步工作中，你需要：

- `git`
- 相容 POSIX 的 shell（範例使用 `bash`）
- 可編輯 Markdown 的編輯器
- 可選：差異比對工具（用於審查本地化分支）

## 🛠️ 安裝

本快照中沒有可安裝的套件。

在本機使用：

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ 使用方式

目前使用方向以文件與流程追蹤為主。

```bash
# 檢查語言選擇器對應
head -n 5 README.md

# 檢查最新流程上下文
cat .auto-readme-work/20260301_070712/pipeline-context.md

# 檢查最近可用快照中的儲存庫結構分析
cat .auto-readme-work/20260301_070712/../20260301_065907/repo-structure-analysis.md

# 檢視在地化文件以進行一致性比對
sed -n '1,90p' i18n/README.fr.md
```

### 推薦維護流程

1. 更新 `README.md` 的結構或行為變更。
2. 按需求重新產生翻譯更新。
3. 驗證關鍵章節在 `i18n/` 檔案間仍保持同步。
4. 讓 `.auto-readme-work` 快照與目前工作流保持一致。

## 🧩 設定

目前尚未提交正式的運行時設定檔（例如 `.env`、`config.yml`、CLI schema 等）。

若未來要實作運行時，建議預設如下：

- 新增範例設定檔，例如 `config.sample.yml`。
- 透過 `.env`（排除於版本庫）或託管端憑證管理保存金鑰。
- 新增新設定鍵時，務必保持文件與 CLI 參考同步。

## 🧪 範例

### 目前範例（現有腳手架）

```bash
# 開啟完整英文文件
cat README.md

# 比對本地化版本
sed -n '1,90p' i18n/README.de.md
```

### 未來範例（預計實作）

```bash
# 概念範例；在引入執行時前可能尚未存在
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ 開發備註

- 採取增量式變更：優先採用加法式改進，避免破壞性重寫。
- 將 `README.md` 視為權威文件基礎。
- 將 `i18n/` 下的語言檔作為明確的同步目標。
- 將 `.auto-readme-work/` 流程檔案視為歷史證據，非手工編輯的生產程式碼。
- 避免過度承諾可執行行為；僅記錄目前實際存在的內容。

### 本 README 的假設

- 在提交執行時模組前，本儲存庫仍維持文件優先。
- 翻譯與有意義的結構性更新保持同步。
- `.auto-readme-work/` 是按執行建立、可追加的歷史資料，不是權威工作副本。

## 🔧 疑難排解

### 我無法執行 `auto-publication` 指令

**原因：** 本快照尚未有運行時應用。

**解法：** 將此儲存庫視為文件工作區，等待實作檔案補齊。

### 本地化 README 與原始版本不同步

**原因：** 翻譯內容先於英文來源更新。

**解法：** 將相同結構變更套用到所有 `i18n/README.*.md`，再對齊措辭與範例。

### README 連結指向不存在的功能

**原因：** 文件中包含了計畫中的行為。

**解法：** 將該段保留為「規劃中」，或改為目前可驗證的指令。

## 🗺️ 路線圖

- [ ] 新增原始碼套件與執行時入口。
- [ ] 新增相依套件清單與安裝路徑。
- [ ] 新增特定平台發布整合。
- [ ] 新增設定驗證與密鑰管理。
- [ ] 新增可執行範例與 CI 冒煙檢查。
- [ ] 加入本地化 README 之間的自動一致性檢查。
- [ ] 加入 `LICENSE` 檔案並明確授權條款。

## 🤝 參與貢獻

當這個文件腳手架轉向實作階段時，歡迎提交貢獻。

```bash
# 1. 建立分支
git checkout -b docs/<short-description>

# 2. 提交變更
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. 推送並發起 PR
git push -u origin docs/<short-description>
```

建議的 PR 檢查清單：

- 保持 `README.md` 為權威文件來源。
- 更新 `i18n/` 中所有受影響的本地化 README。
- 在新增內容時保留既有段落，遵循增量原則。
- 讓 `.auto-readme-work/*` 中繼資料與目前流程保持一致。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

以本儲存庫 `issues` 提出問題、文件修正與協作排程。

## 📄 License

目前快照中尚未提供 `LICENSE` 檔案。

建議的下一步：

- 新增 `LICENSE` 檔案，並使用目標授權識別碼更新本節。

## Submodules

This repository includes these root-level git submodules:

- `AutoPubMonitor` → https://github.com/lachlanchen/AutoPubMonitor
- `LazyEdit` → https://github.com/lachlanchen/LazyEdit
- `AutoPublish` → https://github.com/lachlanchen/AutoPublish
