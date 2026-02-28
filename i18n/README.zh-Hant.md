[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo%20Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> 使用 AI 工具自動發布影片。

## 🧭 概覽

`AutoPublication` 是一個以文件優先為核心、用於定義 AI 輔助影片發布流程的腳手架。

在目前的倉庫階段，這個專案仍是腳手架：目前只提交了文件與 README 生成流程產物，但尚未提交應用原始碼或可執行進入點。

此 README 是英文標準來源文件，結構上能支援未來實作擴展，同時保留目前專案目標與邊界。

## ✨ 特性

### ✅ 目前能力

- 專案定義用的英文根 README。
- 在 `i18n/` 下預先定義的多語系 README 目標。
- 在 `.auto-readme-work/` 下提供 README 流程上下文與結構化產物。
- 將語言導覽列集中在頂部以維持多語一致性。

### 規劃能力（依專案名稱與當前描述推斷）

- 自動化影片發布編排。
- AI 輔助的中繼資料與內容準備。
- 可設定的發布目標平台與平台整合能力。

## 🗂️ 專案結構

```text
AutoPublication/
├── README.md
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
    │   ├── pipeline-context.md
    │   ├── language-nav-root.md
    │   ├── language-nav-i18n.md
    │   ├── translation-plan.txt
    │   └── repo-structure-analysis.md
    ├── 20260301_064342/
    │   ├── pipeline-context.md
    │   ├── language-nav-root.md
    │   ├── language-nav-i18n.md
    │   ├── translation-plan.txt
    │   └── repo-structure-analysis.md
    └── 20260301_064412/
        ├── pipeline-context.md
        ├── language-nav-root.md
        ├── language-nav-i18n.md
        └── translation-plan.txt
```

## 🔎 重要路徑

| 路徑 | 用途 |
|---|---|
| `i18n/` | 翻譯版本檔案的目標目錄。 |
| `.auto-readme-work/20260301_064412/pipeline-context.md` | 最新 README 自動化執行的上下文與限制。 |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | 較早的語言目標與執行計畫。 |
| `.auto-readme-work/20260301_064412/translation-plan.txt` | 最新語言目標與優先順序規劃。 |
| `.gitignore` | Python 風格的忽略模板（目前僅為參考；尚未包含 Python 應用檔案）。 |

## 前置條件

由於尚未提交實作檔案，執行前置條件目前根據倉庫內容進行假設。

| 類型 | 要求 |
|---|---|
| 工具 | `git` |
| Shell | POSIX 相容的 Shell（範例使用 `bash`） |

可能的未來技術棧訊號（來自 `.gitignore`）：

- Python 工具鏈與相關打包工具

## 🚀 安裝

此階段尚無可安裝套件、依賴清單或進入點。

克隆並進入倉庫：

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## ▶️ 使用

目前沒有可執行的應用程式指令。

當前可實際使用的是倉庫文件與流程準備：

```bash
# 檢視倉庫結構
ls -la

# 檢視語言目標
ls -la i18n

# 檢視目前 README 流程上下文
cat .auto-readme-work/20260301_064412/pipeline-context.md
```

實作補齊後，請將這些命令替換為具體可執行的發布流程與執行指令。

## ⚙️ 設定

目前尚未提供正式設定檔（例如 `.env.example`、`config.yaml` 或 CLI 旗標）。

建議的未來補充：

- 提供用於 API 憑證與發布目標的環境變數範本。
- 提供 YAML/JSON 設定 schema，用於平台特定中繼資料與流程預設值。
- 補充 CLI 設定檔與參數驗證行為說明。

## 🧪 範例

### 目前（腳手架）範例

將本倉庫作為文件基準使用：

```bash
# 檢視標準化專案定義
cat README.md
```

### 未來（目標）範例（佔位）

```bash
# 預期未來可執行的指令範例
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## 🛠️ 開發說明

- 倉庫目前不包含可執行原始碼。
- README 生成看起來由 `.auto-readme-work/` 的流程檔驅動。
- 多語流程已透過 `i18n/` 檔案與翻譯計畫進行腳手架搭建。

建議的下一步實作里程碑：

1. 新增原始碼目錄（例如 `src/` 或 `autopublication/`）。
2. 新增依賴清單（`pyproject.toml` 或同類型檔案）。
3. 新增可執行進入點並補齊基本測試覆蓋。
4. 新增 CI 以校驗 lint/test/docs。

## 🩺 疑難排解

### 「我無法執行專案」

原因：

- 目前尚未提交執行期應用檔案或進入點。

解決方式：

- 將此倉庫視為腳手架與文件基線，待實作補齊後再驗證執行。

### 「語言 README 連結存在但檔案缺失」

原因：

- `i18n/` 已存在，但此快照中的本地化 README 尚未全部生成。

解決方式：

- 依 `i18n/README.*.md` 對應清單與翻譯規劃生成並補齊所列檔案。

## 🧭 路線圖

- [ ] 新增第一個可執行的自動發布實作。
- [ ] 定義平台整合與設定 schema。
- [ ] 新增可重複的本地環境建置說明。
- [ ] 增加測試與 CI 流程。
- [ ] 在 `i18n/` 完成完整多語 README 發布。

## 🤝 貢獻

專案由腳手架走向實作的過程歡迎提交貢獻。

建議的貢獻流程：

```bash
# 1) Create a branch
git checkout -b feat/<short-description>

# 2) Commit your changes
git add .
git commit -m "feat: <describe change>"

# 3) Push and open a PR
git push -u origin feat/<short-description>
```

請包含：

- 清楚的問題敘述與範圍。
- 對任何行為變更提供可重現步驟。
- 為新增命令/設定同步更新文件。

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📫 聯絡方式

若有當前使用問題或文件修正，請在倉庫提出 issue。

## 📄 授權

此倉庫快照中尚未提供授權文件。

假設：

- 授權尚未宣告。
