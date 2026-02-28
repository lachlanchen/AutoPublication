[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

🌐 **Language links**


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> Documentation-first scaffold for AI-assisted video publishing workflows.

## 📌 At a glance

| Area | Details |
| --- | --- |
| Generated artifacts | Snapshot metadata and pipeline traces in `.auto-readme-work/*` |
| Current implementation | Documentation-only snapshot (no runtime app code committed yet) |
| Latest snapshot | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ README quick navigation

| Section | Link |
|---|---|
| Overview | [Overview](#%E2%98%9B-overview) |
| Features | [Features](#%E2%9C%A8-features) |
| Project structure | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| Prerequisites | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| Installation | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| Usage | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| Configuration | [Configuration](#%F0%9F%A7%A9-configuration) |
| Examples | [Examples](#%F0%9F%A7%AA-examples) |
| Development notes | [Development notes](#%F0%9F%99%82-development-notes) |
| Troubleshooting | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| Roadmap | [Roadmap](#%F0%9F%97%BA-roadmap) |
| Contributing | [Contributing](#%F0%9F%A4%9D-contributing) |
| Support | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| Contact | [Contact](#contact) |
| License | [License](#%F0%9F%93%84-license) |

## 🧭 Overview

`AutoPublication` is a repository-level documentation scaffold prepared to support a larger AI video publication system.  

### What this repository is

- A canonical source for project documentation and contributor guidance.
- A multilingual documentation set used as an example of synchronized README evolution.
- A historical evidence store under `.auto-readme-work/*` capturing each pipeline run.

### What this repository is not (yet)

- Not yet a runnable publication app.
- Not yet a package with install scripts or dependency manifests.
- Not yet shipping a runtime config model (`.env`, YAML, CLI schema) in this branch.

## ✨ Features

### Current capabilities

- Language selector block linking to all localized READMEs.
- Timestamped auto-README artifacts (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- Document-first project map to support incremental implementation.
- Standardized support panel for donation/sponsorship visibility.

### Planned capabilities

- AI-assisted publication workflow orchestration.
- Multi-platform metadata generation and validation.
- Configurable publishing targets and credentials management.
- Reproducible local development path with tests and CI checks.

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
| `i18n/README.*.md` | Localized READMEs for user-facing documentation |
| `.auto-readme-work/*/pipeline-context.md` | Run constraints and metadata for each pipeline pass |
| `.auto-readme-work/*/language-nav-*.md` | Canonical and i18n language mapping files |
| `.auto-readme-work/*/repo-structure-analysis.md` | Historical structure snapshots |
| `.auto-readme-work/*/translation-plan.txt` | Locale and translation scope |
| `.auto-readme-work/*/translated-files.txt` | Output file lists from previous translation runs |

## 🧰 Prerequisites

Because this snapshot is documentation-only, there are no runtime dependencies for application execution.

For maintenance, review, and translation sync work you need:

- `git`
- A POSIX-compatible shell (examples use `bash`)
- A markdown-capable editor
- Optional: a diff viewer (for reviewing localized branches)

## 🛠️ Installation

No installable package exists in this snapshot.

To work locally:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Usage

Current usage is documentation and pipeline-trace oriented.

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

1. Update `README.md` for structural or behavioral changes.
2. Regenerate translation updates when required.
3. Verify key sections remain synchronized across `i18n/` files.
4. Keep `.auto-readme-work` snapshots consistent with the current workflow.

## 🧩 Configuration

No formal runtime configuration files are committed yet (`.env`, `config.yml`, CLI schema, etc. are absent).

If you are implementing a future runtime, recommended defaults:

- Add a sample configuration file such as `config.sample.yml`.
- Store secrets via `.env` (excluded from repo) or the hosting secret manager.
- Keep docs and CLI references in lockstep when adding new keys.

## 🧪 Examples

### Current examples (existing scaffold)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### Future examples (expected implementation)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Development notes

- Treat changes as incremental: prioritize additive improvements and avoid destructive rewrites.
- Preserve the English source as the authoritative documentation baseline.
- Use the language files in `i18n/` as explicit sync targets.
- Keep pipeline artifacts (`.auto-readme-work/`) as historical evidence, not hand-edited production code.
- Avoid overpromising executable behavior in commands; only document what is currently present.

### Assumptions made in this README

- The repository remains documentation-first until runtime modules are committed.
- Translations stay aligned with meaningful structural edits.
- `.auto-readme-work/` contains append-only, run-scoped history and is not the canonical working copy.

## 🔧 Troubleshooting

### I cannot run an `auto-publication` command

**Cause:** No runtime application exists in this snapshot.

**Fix:** Use this repository for documentation workflows and wait for implementation files to be added.

### A localized README seems out of sync

**Cause:** Translations were updated independently of the English source.

**Fix:** Apply the same structural changes to all `i18n/README.*.md` files, then align wording and examples.

### A README link points to non-existent functionality

**Cause:** The documentation includes planned behavior.

**Fix:** Keep the section marked as planned or replace it with currently validated commands.

## 🗺️ Roadmap

- [ ] Add source package and runtime entrypoint.
- [ ] Add dependency manifest and installation path.
- [ ] Add platform-specific publication integrations.
- [ ] Add config validation and secrets handling.
- [ ] Add executable examples and CI smoke checks.
- [ ] Add automated parity checks across localized READMEs.
- [ ] Add a `LICENSE` file and explicit licensing terms.

## 🤝 Contributing

Contributions are welcome as this docs scaffold transitions into implementation.

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

Suggested PR checklist:

- Keep `README.md` as the source of truth.
- Update every touched localized README in `i18n/`.
- Keep existing sections while adding incremental value.
- Keep `.auto-readme-work/*` metadata aligned with the current pass.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

Use repository issues for questions, documentation corrections, and contribution coordination.

## 📄 License

No `LICENSE` file is currently present in this snapshot.

Suggested next step:

- Add a `LICENSE` file and update this section with the chosen license identifier.
