[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo%20Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> AI 도구로 비디오를 자동 게시합니다.

## 🧭 개요

`AutoPublication`은 AI 지원 비디오 게시 워크플로를 정의하기 위한 문서 우선형 스캐폴드입니다.

현재 저장소 단계에서 이 프로젝트는 문서와 README 생성 파이프라인 산출물로 구성된 스캐폴드이며, 아직 애플리케이션 소스 코드나 런타임 진입점이 커밋되지 않았습니다.

이 README는 현재 프로젝트 의도를 잃지 않으면서 향후 구현 확대를 지원할 수 있도록 구조화된 표준 영어 문서 원본입니다.

## ✨ 기능

### ✅ 현재 제공 기능

- 프로젝트 정의를 위한 기준 루트 README.
- `i18n/` 하위의 사전 정의된 다국어 README 대상.
- `.auto-readme-work/` 하위의 README 파이프라인 컨텍스트 및 구조 산출물.
- 다국어 일관성을 위해 상단에 언어 네비게이션 라인 중앙 배치.

### 계획된 기능(프로젝트 이름과 현재 설명에서 추론)

- 비디오 자동 게시 오케스트레이션.
- AI 보조 메타데이터 및 콘텐츠 준비.
- 구성 가능한 게시 대상 및 플랫폼 통합.

## 🗂️ 프로젝트 구조

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

## 🔎 중요 경로

| 경로 | 용도 |
|---|---|
| `i18n/` | 번역된 README 파일 대상 폴더. |
| `.auto-readme-work/20260301_064412/pipeline-context.md` | 최신 자동 README 실행 컨텍스트 및 제약 조건. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | README 변형 언어 대상에 대한 이전 계획. |
| `.auto-readme-work/20260301_064412/translation-plan.txt` | 최신 언어 대상 계획 및 우선순위. |
| `.gitignore` | Python 중심 무시 규칙 템플릿(현재는 Python 앱 파일이 실제로 없음). |

## 전제 조건

구현 파일이 아직 존재하지 않으므로, 런타임 전제 조건은 저장소 내용으로부터 추론된 가정입니다.

| 유형 | 요구 사항 |
|---|---|
| 도구 | `git` |
| 쉘 | POSIX 호환 쉘(예시: `bash`) |

향후 스택 신호 ( `.gitignore` 기준):

- Python 도구 체인과 관련 패키징 도구

## 🚀 설치

현재 시점에는 설치 가능한 패키지, 의존성 매니페스트, 또는 진입점이 없습니다.

저장소를 클론하고 진입합니다:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## ▶️ 사용법

아직 실행 가능한 애플리케이션 명령이 없습니다.

현재 실질적인 사용은 저장소 문서화 및 워크플로 준비입니다:

```bash
# Inspect repository structure
ls -la

# Inspect language targets
ls -la i18n

# Inspect active README pipeline context
cat .auto-readme-work/20260301_064412/pipeline-context.md
```

구현이 추가되면 이 명령들 대신 구체적인 런타임 및 게시 워크플로 명령으로 교체해야 합니다.

## ⚙️ 구성

아직 정식 구성 파일(`.env.example`, `config.yaml`, CLI 플래그 등)이 없습니다.

권장되는 향후 추가 항목:

- API 자격 증명 및 게시 대상용 환경 템플릿.
- 플랫폼별 메타데이터와 워크플로 기본값을 위한 YAML/JSON 구성 스키마.
- CLI 구성 문서화 및 유효성 검사 동작.

## 🧪 예시

### 현재(스캐폴드) 예시

저장소를 문서 기준선으로 사용합니다:

```bash
# Read canonical project intent
cat README.md
```

### 향후(목표) 예시 (플레이스홀더)

```bash
# Example intended future invocation
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## 🛠️ 개발 노트

- 저장소에는 현재 실행 가능한 소스 코드가 없습니다.
- README 생성은 `.auto-readme-work/`의 파일을 이용한 파이프라인 방식으로 보입니다.
- 다국어 워크플로는 `i18n/` 파일과 번역 계획으로 구성됩니다.

권장 다음 구현 마일스톤:

1. 소스 디렉터리 추가(예: `src/` 또는 `autopublication/`).
2. 의존성 매니페스트 추가(`pyproject.toml` 또는 동등 항목).
3. 실행 진입점 추가 및 최소 테스트 범위 확보.
4. 린트/테스트/문서 검증 CI 추가.

## 🩺 문제 해결

### "프로젝트를 실행할 수 없습니다"

원인:

- 현재 런타임 애플리케이션 파일 또는 엔트리포인트가 커밋되지 않았습니다.

해결:

- 구현이 추가될 때까지 저장소를 스캐폴드/문서 기반으로 취급하십시오.

### "언어 README 링크는 있으나 파일이 없습니다"

원인:

- `i18n/`는 존재하지만, 이 스냅샷에서는 해당 언어 README 파일이 모두 생성되지 않았습니다.

해결:

- `i18n/README.*.md` 매핑에 따라 파일을 생성하고 번역 계획 산출물을 반영하십시오.

## 🧭 로드맵

- [ ] 자동 게시를 위한 첫 실행 가능한 구현 추가.
- [ ] 제공자 통합 및 구성 스키마 정의.
- [ ] 재현 가능한 로컬 환경 설정 가이드 추가.
- [ ] 테스트와 CI 파이프라인 추가.
- [ ] `i18n/`에 완전한 다국어 README 세트를 게시.

## 🤝 기여

프로젝트가 스캐폴드에서 구현 단계로 이동할 때 기여를 환영합니다.

권장 기여 흐름:

```bash
# 1) Create a branch
git checkout -b feat/<short-description>

# 2) Commit your changes
git add .
git commit -m "feat: <describe change>"

# 3) Push and open a PR
git push -u origin feat/<short-description>
```

다음 내용을 포함해 주세요:

- 명확한 문제 진술 및 범위.
- 동작 변경에 대한 재현 가능한 단계.
- 신규 명령/구성에 대한 문서 업데이트.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📫 Contact

현재 사용법 관련 질문과 문서 수정 요청은 저장소에서 이슈를 열어주세요.

## 📄 License

현재 이 저장소 스냅샷에는 라이선스 파일이 없습니다.

가정:

- 라이선스가 아직 명시되지 않았습니다.

권장 다음 단계:

- `LICENSE` 파일을 추가하고 이 섹션에서 이를 명시적으로 참조하도록 업데이트하세요.
