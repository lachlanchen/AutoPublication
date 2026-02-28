[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> AI 기반 비디오 발행 워크플로우를 위한 문서 우선형 스캐폴드입니다.

## 📌 한눈에 보기

| 영역 | 세부 사항 |
| --- | --- |
| 역할 | AI 비디오 발행 워크스페이스의 정본(영문) 문서 출처 |
| 언어 | 영어 + 지역화된 README 10개 |
| 생성 산출물 | `.auto-readme-work/*`의 스냅샷 메타데이터 및 파이프라인 추적 |
| 현재 구현 | 문서 전용 스냅샷 (런타임 실행 애플리케이션 코드는 아직 커밋되지 않음) |
| 최신 스냅샷 | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ README 빠른 탐색

| 섹션 | 링크 |
|---|---|
| 개요 | [Overview](#%E2%98%9B-overview) |
| 기능 | [Features](#%E2%9C%A8-features) |
| 프로젝트 구조 | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| 사전 조건 | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| 설치 | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| 사용법 | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| 구성 | [Configuration](#%F0%9F%A7%A9-configuration) |
| 예시 | [Examples](#%F0%9F%A7%AA-examples) |
| 개발 노트 | [Development notes](#%F0%9F%99%82-development-notes) |
| 문제 해결 | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| 로드맵 | [Roadmap](#%F0%9F%97%BA-roadmap) |
| 기여 | [Contributing](#%F0%9F%A4%9D-contributing) |
| 지원 | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| 문의 | [Contact](#contact) |
| 라이선스 | [License](#%F0%9F%93%84-license) |

## 🧭 개요

`AutoPublication`은 더 큰 AI 비디오 게시 시스템을 지원하도록 준비된 저장소 단위의 문서형 스캐폴드입니다.
영문 정본 `README.md`를 진실의 출처로 유지하고, 파이프라인 스냅샷을 통해 `i18n/README.*.md`의 번역을 정합합니다.

### 이 저장소의 현재 정의

- 프로젝트 문서와 기여자 가이드를 담은 정본 소스.
- README 동기화 진화를 보여주는 지역화 문서 모음.
- 파이프라인 실행마다 기록이 쌓이는 `.auto-readme-work/*`의 이력 저장소.

### 이 저장소가 아직 아닌 것

- 실행 가능한 게시 애플리케이션이 아직 없음.
- 설치 스크립트나 의존성 매니페스트가 포함된 패키지가 아님.
- 현재 브랜치에는 런타임 설정 모델(`.env`, YAML, CLI 스키마)이 아직 없음.

## ✨ 기능

### 현재 기능

- 단일 정본 파일(`README.md`)에 정식 영문 문서 보관.
- 모든 로컬라이즈 README로 이어지는 언어 선택 블록.
- 타임스탬프 기반 자동 README 산출물(`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- 구현을 점진적으로 확장할 수 있도록 지원하는 문서 중심 프로젝트 지도.
- 후원/기부 노출을 위한 표준 지원 패널.

### 예정 기능

- AI 기반 게시 워크플로우 오케스트레이션.
- 다중 플랫폼 메타데이터 생성 및 검증.
- 사용자 정의 가능한 게시 대상과 자격 증명 관리.
- 테스트와 CI 검증을 포함한 재현 가능한 로컬 개발 경로.

## 🗂️ 프로젝트 구조

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

### 핵심 경로

| 경로 | 목적 |
|---|---|
| `i18n/README.*.md` | 사용자 대상 문서로 사용되는 지역화 README |
| `.auto-readme-work/*/pipeline-context.md` | 각 파이프라인 실행의 제약 조건 및 메타데이터 |
| `.auto-readme-work/*/language-nav-*.md` | 정본과 i18n 간 언어 매핑 |
| `.auto-readme-work/*/repo-structure-analysis.md` | 저장소 구조의 이력 스냅샷 |
| `.auto-readme-work/*/translation-plan.txt` | 로캘 및 번역 범위 |
| `.auto-readme-work/*/translated-files.txt` | 이전 번역 실행에서 출력된 파일 목록 |

## 🧰 사전 조건

이 스냅샷은 문서 전용이므로 애플리케이션 실행을 위한 런타임 의존성이 없습니다.

문서 정비, 검토, 번역 동기화 작업을 위해 필요한 항목:

- `git`
- POSIX 호환 셸(예: `bash`)
- Markdown 편집기
- 선택 사항: 차이 비교 도구(지역화 브랜치 검토용)

## 🛠️ 설치

이 스냅샷에는 설치 가능한 패키지가 없습니다.

로컬에서 작업하려면:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ 사용법

현재 사용은 문서 열람과 파이프라인 추적 확인에 초점이 맞춰져 있습니다.

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

### 권장 유지보수 흐름

1. 구조 또는 동작 변경이 있으면 `README.md`를 먼저 업데이트합니다.
2. 필요 시 번역 갱신을 재생성합니다.
3. `i18n/` 전역에서 핵심 섹션 동기화 상태를 확인합니다.
4. `.auto-readme-work` 스냅샷을 현재 워크플로우와 정합되게 유지합니다.

## 🧩 구성

현재 공식 런타임 구성 파일은 커밋되어 있지 않습니다(`.env`, `config.yml`, CLI 스키마 등은 미포함).

향후 런타임을 구현할 경우 권장 기본값:

- `config.sample.yml` 같은 샘플 구성 파일을 추가합니다.
- 비밀 값은 `.env`(레포지토리 외부) 또는 호스팅 비밀 관리자에서 저장합니다.
- 새 키를 추가할 때 문서와 CLI 참조를 동기화 상태로 함께 유지합니다.

## 🧪 예시

### 현재 예시(기존 스캐폴드)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### 향후 예시(예정 구현)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ 개발 노트

- 변경은 점진적으로 처리하고, 추가 개선을 우선하며 파괴적 재작성은 피하세요.
- 영문 정본인 `README.md`를 권위 있는 기준 문서로 유지하세요.
- `i18n/` 파일들을 명시적 동기화 대상으로 다루세요.
- 파이프라인 산출물(`.auto-readme-work/`)은 운영 코드가 아니라 이력 증거로 보존하세요.
- 실행 동작을 과장하지 말고, 현재 실제로 존재하는 내용만 문서화하세요.

### 이 README에서의 가정

- 저장소는 런타임 모듈이 커밋될 때까지 문서 우선 상태를 유지합니다.
- 의미 있는 구조 변경마다 번역이 정렬됩니다.
- `.auto-readme-work/`는 추가 전용 실행 이력이며, 정작 작업 기준본은 아닙니다.

## 🔧 문제 해결

### `auto-publication` 명령을 실행할 수 없습니다

**원인:** 이 스냅샷에는 런타임 애플리케이션이 구현되어 있지 않습니다.

**해결:** 이 저장소를 문서 워크플로우용으로 사용하고, 구현 파일이 추가될 때까지 기다리세요.

### 지역화 README가 동기화되지 않은 것으로 보입니다

**원인:** 번역이 영문 소스와 독립적으로 변경되어 동기화가 깨졌습니다.

**해결:** 동일한 구조 변경을 모든 `i18n/README.*.md`에 적용한 뒤 문구와 예시를 정렬합니다.

### README 링크가 존재하지 않는 기능을 가리킵니다

**원인:** 문서에 예정된 동작이 포함되어 있습니다.

**해결:** 해당 섹션을 계획 항목으로 표시하거나, 현재 검증된 명령으로 교체합니다.

## 🗺️ 로드맵

- [ ] 소스 패키지와 런타임 진입점을 추가.
- [ ] 의존성 매니페스트와 설치 경로를 추가.
- [ ] 플랫폼별 게시 통합을 추가.
- [ ] 구성 검증 및 비밀 관리 처리 추가.
- [ ] 실행 가능한 예시와 CI 스모크 점검 추가.
- [ ] 지역화 README 간 자동 정합성 검사 추가.
- [ ] `LICENSE` 파일과 명시적 라이선스 조건 추가.

## 🤝 기여

이 문서 스캐폴드가 구현 단계로 전환되는 과정에서 기여를 환영합니다.

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

권장 PR 체크리스트:

- `README.md`를 정본으로 유지하세요.
- 변경이 있는 모든 `i18n/` README를 함께 업데이트하세요.
- 기존 섹션은 유지하고 증분 개선을 추가하세요.
- `.auto-readme-work/*` 메타데이터를 현재 실행 흐름과 정합되게 유지하세요.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

질문, 문서 수정, 기여 조율은 저장소 이슈를 사용하세요.

## 📄 License

이 스냅샷에는 현재 `LICENSE` 파일이 없습니다.

Suggested next step:

- `LICENSE` 파일을 추가하고 선택한 라이선스 식별자로 이 섹션을 업데이트하세요.
