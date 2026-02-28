[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> AI 도구를 사용해 비디오를 자동 게시합니다.

## 개요

`AutoPublication`은 AI 보조 도구를 활용해 비디오 게시 워크플로를 자동화하는 것을 목표로 합니다.

현재 저장소 단계에서 이 프로젝트는 문서와 README 생성 파이프라인 산출물로 구성된 스캐폴드이며, 애플리케이션 소스 코드나 런타임 엔트리포인트는 아직 커밋되지 않았습니다.

이 README는 정식 영어 기준 문서(canonical base)로서, 현재 프로젝트 의도를 유지하면서 향후 구현 확장을 지원하도록 구성되어 있습니다.

| 영역 | 현재 상태 |
|---|---|
| 구현 | 스캐폴드 단계(커밋된 런타임 앱 없음) |
| 문서화 | 기준 루트 README 존재 |
| 다국어 문서 | `i18n/` 아래 언어 대상 정의됨 |
| 파이프라인 산출물 | `.auto-readme-work/` 아래 존재 |

## 기능

### 현재 제공 항목

- 프로젝트 정의를 위한 기준 루트 README.
- `i18n/` 아래 사전 정의된 다국어 README 대상.
- 반복 가능한 문서 생성을 위한 README 파이프라인 컨텍스트.

### 계획된 기능(프로젝트 이름 및 현재 설명을 바탕으로 추론)

- 비디오 자동 게시 오케스트레이션.
- AI 보조 메타데이터/콘텐츠 준비.
- 게시 대상별로 구성 가능한 통합.

## 프로젝트 구조

```text
AutoPublication/
├── README.md
├── .gitignore
├── i18n/
└── .auto-readme-work/
    └── 20260228_230008/
        ├── pipeline-context.md
        ├── language-nav-root.md
        ├── language-nav-i18n.md
        ├── translation-plan.txt
        └── repo-structure-analysis.md
```

### 주요 경로

| 경로 | 용도 |
|---|---|
| `README.md` | 영어 기준 프로젝트 정의 문서. |
| `i18n/` | 번역된 README 파일의 대상 폴더. |
| `.auto-readme-work/20260228_230008/pipeline-context.md` | Auto-README 실행 컨텍스트 및 제약 사항. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | 언어 매핑 및 파일 대상. |
| `.gitignore` | Python 중심 ignore 템플릿(참고용; 현재 Python 앱 파일은 없음). |

## 사전 요구 사항

아직 구현 파일이 없으므로, 런타임 요구 사항은 현재 가정 수준입니다.

### 문서화된 기준

- `git`
- POSIX 호환 셸(예시는 `bash` 사용)

### 향후 스택 신호(`.gitignore` 기준)

- 나중에 Python 툴체인이 필요할 수 있습니다.

## 설치

현재 단계에서는 설치 가능한 패키지나 의존성 매니페스트가 없습니다.

저장소를 클론하고 진입하세요:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## 사용법

아직 실행 가능한 애플리케이션 명령은 없습니다.

현재 실질적인 사용 방식은 문서 워크플로와 저장소 준비입니다:

```bash
# Inspect repository structure
ls -la

# Inspect i18n targets
ls -la i18n
```

구현이 추가되면, 이 섹션은 구체적인 실행 명령과 실제 엔드투엔드 예제로 확장되어야 합니다.

## 구성

아직 정식 구성 파일(`.env.example`, `config.yaml`, CLI 플래그 등)이 없습니다.

향후 권장 추가 항목:
- 문서화된 환경 템플릿(API 키/토큰용).
- 플랫폼별 게시 구성.
- AI 제공자/모델 선택 설정.

## 예제

### 현재(스캐폴드) 예제

저장소를 문서 기준선으로 사용합니다:

```bash
# Read canonical project intent
cat README.md
```

### 향후(목표) 예제

가정된 향후 워크플로(플레이스홀더 전용):

```bash
# Placeholder example for future implementation
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## 개발 노트

- 현재 저장소에는 실행 가능한 소스 코드가 없습니다.
- README 생성은 `.auto-readme-work/` 내 파일을 사용하는 파이프라인 기반으로 보입니다.
- 언어 네비게이션 라인은 다국어 일관성을 지원하기 위해 이 README 상단에 의도적으로 중앙 배치되어 있습니다.

권장되는 다음 구현 마일스톤:
1. 소스 디렉터리 추가(예: `src/` 또는 `autopublication/`).
2. 의존성 매니페스트 추가(`pyproject.toml` 또는 동등 항목).
3. 실행 엔트리포인트 및 최소 테스트 커버리지 추가.
4. lint/test/docs 검증용 CI 추가.

## 문제 해결

### "프로젝트를 실행할 수 없습니다"

원인:
- 현재 런타임 애플리케이션 파일 또는 엔트리포인트가 커밋되어 있지 않습니다.

해결:
- 소스 코드가 추가될 때까지 저장소를 스캐폴드/문서로 취급하세요.

### "언어 README 링크는 있는데 파일이 없습니다"

원인:
- `i18n/`은 존재하지만, 이 스냅샷에서는 로컬라이즈된 README 파일이 생성되지 않았습니다.

해결:
- `.auto-readme-work/20260228_230008/translation-plan.txt`에 나열된 대상 파일을 생성/추가하세요.

## 로드맵

- [ ] 자동 게시를 위한 첫 실행 가능한 구현 추가.
- [ ] 제공자 통합 및 구성 스키마 정의.
- [ ] 재현 가능한 로컬 설정 지침 추가.
- [ ] 테스트 및 CI 파이프라인 추가.
- [ ] `i18n/`에 완전한 다국어 README 세트 게시.

## 기여

프로젝트가 스캐폴드에서 구현 단계로 전환되는 동안 기여를 환영합니다.

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
- 명확한 문제 정의와 범위.
- 동작 변경 사항에 대한 재현 가능한 단계.
- 새 명령/구성에 대한 문서 업데이트.

## 지원

현재 이 저장소에는 후원/스폰서 채널이 선언되어 있지 않습니다.

향후 지원 링크가 추가되면, 이곳에 기재하고 i18n 변형 전반에 동일하게 반영해야 합니다.

## 라이선스

현재 저장소 스냅샷에는 라이선스 파일이 없습니다.

가정:
- 라이선스가 아직 선언되지 않았습니다.

권장 다음 단계:
- `LICENSE` 파일을 추가하고 이 섹션에서 해당 파일을 명시적으로 참조하도록 업데이트하세요.
