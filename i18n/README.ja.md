[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> AI支援の動画公開ワークフロー向けに、ドキュメント優先で整えたスキャフォールド。

## 📌 一覧

| 領域 | 詳細 |
| --- | --- |
| 役割 | AI動画公開ワークスペースの正式なドキュメントソース |
| 言語 | 英語 + 10言語のローカライズ済みREADME |
| 生成アーティファクト | `.auto-readme-work/*` に保存されるスナップショットメタデータとパイプライン履歴 |
| 現在の実装 | ドキュメントのみのスナップショット（実行時アプリコードはまだコミットされていません） |
| 最新スナップショット | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ READMEクイックナビゲーション

| セクション | リンク |
|---|---|
| 概要 | [Overview](#%E2%98%9B-overview) |
| 機能 | [Features](#%E2%9C%A8-features) |
| プロジェクト構成 | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| 前提条件 | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| インストール | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| 使用方法 | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| 設定 | [Configuration](#%F0%9F%A7%A9-configuration) |
| 例 | [Examples](#%F0%9F%A7%AA-examples) |
| 開発ノート | [Development notes](#%F0%9F%99%82-development-notes) |
| トラブルシューティング | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| ロードマップ | [Roadmap](#%F0%9F%97%BA-roadmap) |
| 貢献 | [Contributing](#%F0%9F%A4%9D-contributing) |
| サポート | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| お問い合わせ | [Contact](#contact) |
| ライセンス | [License](#%F0%9F%93%84-license) |

## 🧭 Overview

`AutoPublication` は、AI動画公開システム全体を支えるためのリポジトリレベルのドキュメント・スキャフォールドです。
英語版 `README.md` を真実の情報源として保持し、パイプラインスナップショットを通じて `i18n/README.*.md` の翻訳を同期します。

### What this repository is

- プロジェクトのドキュメントとコントリビュータ向けガイダンスの正規ソース。
- 同期されたREADME更新の例として使われる、ドキュメントの多言語セット。
- `.auto-readme-work/*` 配下に各パイプライン実行を記録する履歴の保存領域。

### What this repository is not (yet)

- まだ実行可能な公開アプリではありません。
- まだインストールスクリプトや依存関係定義を持つパッケージではありません。
- このブランチではランタイム設定モデル（`.env`, YAML, CLIスキーマ）をまだ提供していません。

## ✨ Features

### Current capabilities

- 単一ソースの英語ドキュメントを `README.md` に保持する構成。
- すべてのローカライズ版READMEへ接続する言語セレクターブロック。
- タイムスタンプ付きの自動README成果物（`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`）。
- 実装を段階的に進めるためのドキュメント先行型プロジェクトマップ。
- 寄付/サポート表示のために標準化されたサポートパネル。

### Planned capabilities

- AI支援の公開ワークフロー統合。
- マルチプラットフォーム向けメタデータ生成と検証。
- 公開先と資格情報を設定可能な管理。
- テストとCIを含む再現可能なローカル開発導線の追加。

## 🗂️ Project structure

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

### Notable paths

| Path | Purpose |
|---|---|
| `i18n/README.*.md` | 利用者向けドキュメントのローカライズ版 |
| `.auto-readme-work/*/pipeline-context.md` | 各パイプライン実行での制約とメタ情報 |
| `.auto-readme-work/*/language-nav-*.md` | 正式版とi18nの言語マップ |
| `.auto-readme-work/*/repo-structure-analysis.md` | リポジトリ構成の履歴スナップショット |
| `.auto-readme-work/*/translation-plan.txt` | ロケールと翻訳対象の方針 |
| `.auto-readme-work/*/translated-files.txt` | これまでの翻訳対象ファイルの一覧 |

## 🧰 Prerequisites

このスナップショットはドキュメントのみのため、アプリケーション実行用のランタイム依存は必要ありません。

ドキュメント整備、レビュー、翻訳同期を行うには、以下が必要です。

- `git`
- POSIX互換シェル（例: `bash`）
- Markdown対応エディタ
- 任意: 差分ビューア（ローカライズ版の確認に有用）

## 🛠️ Installation

このスナップショット内にインストール可能なパッケージはありません。

ローカルで作業するには:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Usage

現在の利用用途は、ドキュメントとパイプライン履歴の参照に焦点を当てています。

```bash
# inspect the language selector map
head -n 5 README.md

# inspect the latest pipeline context
cat .auto-readme-work/20260301_070712/pipeline-context.md

# inspect the repository structure analysis from the latest available snapshot
cat .auto-readme-work/20260301_070712/../20260301_065907/repo-structure-analysis.md

# review localized docs for parity checks
sed -n '1,90p' i18n/README.fr.md
```

### Recommended maintenance flow

1. 構造や振る舞いの変更があれば `README.md` を更新します。
2. 必要に応じて翻訳更新を再生成します。
3. `i18n/` 全体で主要セクションの同期を確認します。
4. `.auto-readme-work` のスナップショットを現在のワークフローに沿って整合させます。

## 🧩 Configuration

現在、正式なランタイム設定ファイルはまだコミットされていません（` .env`, `config.yml`, CLIスキーマなどは未導入）。

将来的なランタイム実装時に推奨されるデフォルト:

- `config.sample.yml` のようなサンプル設定ファイルを追加します。
- シークレットは `.env`（リポジトリ外）またはホスティング側のシークレット管理で保管します。
- 新しいキーを追加する場合は、ドキュメントとCLI参照を同じタイミングで更新します。

## 🧪 Examples

### 現在の例（既存スキャフォールド）

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### 将来の例（実装予定）

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Development notes

- 変更は増分的に扱い、追加改善を優先し破壊的な書き換えは避けます。
- 英語版を権威ある情報源として保持します。
- `i18n/` 内の言語ファイルを明示的な同期対象として扱います。
- パイプライン成果物（`.auto-readme-work/`）は歴史的証跡として残し、運用コードを直接編集しないようにします。
- 実装可能な振る舞いを過剰に主張せず、現在存在する内容のみを文書化します。

### Assumptions made in this README

- ランタイムモジュールがコミットされるまでは、リポジトリはドキュメント優先のままです。
- 重要な構造変更があるたびに翻訳を同期します。
- `.auto-readme-work/` は追記専用の実行履歴であり、実作業のカノニカルなソースではありません。

## 🔧 Troubleshooting

### `auto-publication` コマンドを実行できない

**原因:** このスナップショットにはランタイムアプリケーションがまだ存在しません。

**対処:** このリポジトリをドキュメント向けワークフローとして扱い、実装ファイルが追加されるのを待ってください。

### ローカライズ版READMEの内容が同期していない

**原因:** 翻訳が英語ソース更新とは独立して更新されたためです。

**対処:** まず `i18n/README.*.md` 全体に同じ構造変更を適用し、その後文言と例を揃えます。

### README内のリンクが未実装機能を指している

**原因:** 文書内に計画機能が記載されているためです。

**対処:** 該当セクションを「予定」に明示するか、または現在検証済みのコマンドに置き換えます。

## 🗺️ Roadmap

- [ ] ソースパッケージとランタイムエントリーポイントを追加。
- [ ] 依存関係マニフェストとインストール手順を追加。
- [ ] プラットフォーム固有の公開連携を追加。
- [ ] 設定検証とシークレット管理を追加。
- [ ] 実行可能な例とCIのスモークチェックを追加。
- [ ] ローカライズ済みREADME間の自動整合チェックを追加。
- [ ] `LICENSE` ファイルと明示的なライセンス条項を追加。

## 🤝 Contributing

このドキュメントスキャフォールドが実装フェーズへ移行する際の貢献を歓迎します。

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

推奨PRチェックリスト:

- `README.md` を信頼できる情報源として維持します。
- 影響を受ける `i18n/` の各READMEを更新します。
- 既存セクションを保ちながら、価値を追加する改良を行います。
- `.auto-readme-work/*` メタデータを現在の実行パスに合わせて整合させます。

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

質問、ドキュメント修正、コントリビューション調整は、リポジトリのIssueを利用してください。

## 📄 License

このスナップショットでは、現在 `LICENSE` ファイルは存在しません。

Suggested next step:

- `LICENSE` を追加し、選択したライセンス識別子でこのセクションを更新します。
