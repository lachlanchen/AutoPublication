[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> Dokumentations-First-Scaffold für KI-gestützte Workflows zur Videopublikation.

## 🗂️ README-Schnellnavigation<a id="readme-quick-navigation"></a>

| Abschnitt | Link |
|---|---|
| Überblick | [Übersicht](#at-a-glance) |
| Funktionen | [Funktionen](#features) |
| Projektstruktur | [Projektstruktur](#project-structure) |
| Voraussetzungen | [Voraussetzungen](#prerequisites) |
| Installation | [Installation](#installation) |
| Nutzung | [Nutzung](#usage) |
| Konfiguration | [Konfiguration](#configuration) |
| Beispiele | [Beispiele](#examples) |
| Entwicklungsnotizen | [Entwicklungsnotizen](#development-notes) |
| Fehlerbehebung | [Fehlerbehebung](#troubleshooting) |
| Roadmap | [Roadmap](#roadmap) |
| Mitwirken | [Mitwirken](#contributing) |
| Support | [Support](#support) |
| Kontakt | [Kontakt](#contact) |
| Lizenz | [Lizenz](#license) |

## 🧭 Übersicht<a id="at-a-glance"></a>

| Bereich | Details |
| --- | --- |
| Rolle | Kanonische englische Dokumentationsquelle für einen KI-Video-Publikations-Workspace |
| Sprachen | Englisch + 10 lokalisierte README-Spiegel |
| Generierte Artefakte | Snapshot-Metadaten und Pipeline-Spuren in `.auto-readme-work/*` |
| Aktueller Umsetzungsstand | Dokumentations-only-Snapshot (noch kein ausführbarer Anwendungscode committed) |
| Aktuellster Snapshot | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🧭 Projektüberblick<a id="overview"></a>

`AutoPublication` ist ein dokumentationsorientiertes Repository-Scaffold, das dafür vorbereitet wurde, ein größeres KI-Videopublikations-System zu unterstützen.
Es nutzt das englische `README.md` als Hauptquelle und gleicht Übersetzungen in `i18n/README.*.md` über Pipeline-Snapshots ab.

### Was dieses Repository ist

- Eine kanonische Quelle für Projektdokumentation und Beitragsleitfäden.
- Ein mehrsprachiger Dokumentationssatz als Beispiel für synchronisierte README-Entwicklung.
- Ein historischer Evidenzspeicher unter `.auto-readme-work/*`, der jeden Pipeline-Lauf dokumentiert.

### Was dieses Repository (noch) nicht ist

- Noch keine ausführbare Publikations-App.
- Noch kein Paket mit Installationsskripten oder Abhängigkeitsmanifesten.
- Noch kein Runtime-Konfigurationsmodell (`.env`, YAML, CLI-Schema) in diesem Branch.

## ✨ Features<a id="features"></a>

### Aktuelle Fähigkeiten

- Kanonische englische Dokumentation in einer Quell-Datei (`README.md`).
- Sprachwahlschalter-Block mit Links zu allen lokalisieren READMEs.
- Zeitgestempelte Auto-README-Artefakte (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- Dokumentationszentrierte Projektkarte zur Unterstützung inkrementeller Umsetzung.
- Standardisierter Support-Block zur Sichtbarkeit von Spenden/Unterstützung.

### Geplante Fähigkeiten

- KI-gestützte Orchestrierung von Publikationsworkflows.
- Metadaten-Generierung und -Validierung für mehrere Plattformen.
- Konfigurierbare Veröffentlichungsziele und Verwaltung von Berechtigungsnachweisen.
- Reproduzierbarer lokaler Entwicklungsweg mit Tests und CI-Prüfungen.

## 🗂️ Projektstruktur<a id="project-structure"></a>

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

### Wichtige Pfade<a id="notable-paths"></a>

| Pfad | Zweck |
|---|---|
| `i18n/README.*.md` | Lokalisierte READMEs für nutzerorientierte Dokumentation |
| `.auto-readme-work/*/pipeline-context.md` | Lauf-Constraints und Metadaten für jeden Pipeline-Durchlauf |
| `.auto-readme-work/*/language-nav-*.md` | Kanonische und i18n-Sprachzuordnungsdateien |
| `.auto-readme-work/*/repo-structure-analysis.md` | Historische Struktur-Snapshots |
| `.auto-readme-work/*/translation-plan.txt` | Umfang und Ziel der Übersetzung |
| `.auto-readme-work/*/translated-files.txt` | Listen der Ausgabedateien aus früheren Übersetzungsläufen |

## 🧰 Voraussetzungen<a id="prerequisites"></a>

Da dieser Snapshot dokumentations-only ist, gibt es keine Laufzeitabhängigkeiten für die Ausführung der Anwendung.

Für Wartung, Review und Übersetzungsabgleich brauchst du:

- `git`
- Eine POSIX-kompatible Shell (Beispiele verwenden `bash`)
- Einen Markdown-fähigen Editor
- Optional: einen Diff-Viewer (zum Prüfen lokalisierter Branches)

## 🛠️ Installation<a id="installation"></a>

In diesem Snapshot existiert kein installierbares Paket.

Um lokal zu arbeiten:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Nutzung<a id="usage"></a>

Aktuelle Nutzung ist dokumentations- und pipeline-orientiert.

```bash
# Sprachumschalter-Mapping prüfen
head -n 5 README.md

# aktuellen Pipeline-Kontext prüfen
cat .auto-readme-work/20260301_070712/pipeline-context.md

# jüngste Struktur-Analyse des letzten verfügbaren Snapshots ansehen
cat .auto-readme-work/20260301_070712/../20260301_065907/repo-structure-analysis.md

# lokalierte Dokumente für Paritätsprüfungen prüfen
sed -n '1,90p' i18n/README.fr.md
```

### Empfohlener Wartungsablauf

1. Aktualisiere `README.md` bei strukturellen oder verhaltensrelevanten Änderungen.
2. Erzeuge Übersetzungs-Updates bei Bedarf neu.
3. Prüfe, dass Schlüsselabschnitte über `i18n/`-Dateien synchron bleiben.
4. Halte `.auto-readme-work` Snapshots konsistent mit dem aktuellen Workflow.

## 🧩 Konfiguration<a id="configuration"></a>

Es sind noch keine formalen Runtime-Konfigurationsdateien committed (`.env`, `config.yml`, CLI-Schema usw. fehlen noch).

Falls du eine zukünftige Runtime implementierst, sind diese Defaults empfohlen:

- Füge eine Beispielkonfigurationsdatei wie `config.sample.yml` hinzu.
- Speichere Geheimnisse über `.env` (vom Repo ausgeschlossen) oder über den Secret Manager des Hostings.
- Halte Dokumentation und CLI-Referenzen synchron, wenn neue Schlüssel hinzugefügt werden.

## 🧪 Beispiele<a id="examples"></a>

### Aktuelle Beispiele (bestehendes Scaffold)

```bash
# vollständige englische Dokumentation öffnen
cat README.md

# lokalisierten Stand vergleichen
sed -n '1,90p' i18n/README.de.md
```

### Zukünftige Beispiele (erwartete Umsetzung)

```bash
# konzeptionelles Beispiel; kann fehlen, bis Runtime eingeführt wird
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Entwicklungsnotizen<a id="development-notes"></a>

- Behandle Änderungen als inkrementell: priorisiere additive Verbesserungen und vermeide destruktive Neuschreibungen.
- Bewahre das Englische als autoritative Dokumentationsgrundlage.
- Nutze die Sprachdateien in `i18n/` als explizite Synchronisationsziele.
- Behalte Pipeline-Artefakte (`.auto-readme-work/`) als historische Evidenz, nicht als handgeschriebenen Produktionscode.
- Überversprich keine ausführbare Funktionalität in Befehlen; dokumentiere nur, was aktuell vorhanden ist.

### Annahmen in diesem README

- Das Repository bleibt dokumentations-first, bis Runtime-Module eingecheckt werden.
- Übersetzungen bleiben mit sinnvollen strukturellen Änderungen synchron.
- `.auto-readme-work/` enthält append-only, laufbezogene Historie und ist nicht die kanonische Arbeitskopie.

## 🔧 Fehlerbehebung<a id="troubleshooting"></a>

### Ich kann keinen `auto-publication`-Befehl ausführen

**Ursache:** In diesem Snapshot existiert keine Runtime-Anwendung.

**Lösung:** Verwende dieses Repository für Dokumentations-Workflows und warte auf die Implementierungsdateien.

### Eine lokalisierte README wirkt nicht synchronisiert

**Ursache:** Übersetzungen wurden unabhängig von der englischen Quelle aktualisiert.

**Lösung:** Wende die gleichen strukturellen Änderungen auf alle `i18n/README.*.md`-Dateien an und gleiche anschließend Wortlaut und Beispiele ab.

### Ein README-Link verweist auf nicht vorhandene Funktionalität

**Ursache:** Die Dokumentation enthält geplantes Verhalten.

**Lösung:** Halte den Abschnitt als geplant markiert oder ersetze ihn durch aktuell validierte Befehle.

## 🗺️ Roadmap<a id="roadmap"></a>

- [ ] Quellpaket und Runtime-Entrypoint hinzufügen.
- [ ] Abhängigkeitsmanifest und Installationsweg hinzufügen.
- [ ] Plattform-spezifische Veröffentlichungsintegrationen hinzufügen.
- [ ] Konfigurationsvalidierung und Secrets-Handling ergänzen.
- [ ] Ausführbare Beispiele und CI-Smoke-Checks ergänzen.
- [ ] Automatisierte Paritätsprüfungen zwischen lokalisierte READMEs ergänzen.
- [ ] Eine `LICENSE`-Datei und klare Lizenzbedingungen hinzufügen.

## 🤝 Mitwirken<a id="contributing"></a>

Beiträge sind willkommen, während dieses Doku-Scaffold in die Umsetzung übergeht.

```bash
# 1. Branch erstellen
git checkout -b docs/<short-description>

# 2. Änderungen committen
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push und PR öffnen
git push -u origin docs/<short-description>
```

Vorgeschlagene PR-Checkliste:

- Halte `README.md` als Quelle der Wahrheit.
- Aktualisiere alle betroffenen lokalisierten READMEs in `i18n/`.
- Bewahre bestehende Abschnitte und füge inkrementellen Mehrwert hinzu.
- Halte `.auto-readme-work/*`-Metadaten mit dem aktuellen Lauf aligned.

## Kontakt<a id="contact"></a>

Verwende die Repository-Issues für Fragen, Korrekturen der Dokumentation und die Koordination von Beiträgen.

## 📄 Lizenz<a id="license"></a>

In diesem Snapshot ist derzeit keine `LICENSE`-Datei vorhanden.

Empfohlener nächster Schritt:

- Ergänze eine `LICENSE`-Datei und aktualisiere diesen Abschnitt mit der gewählten Lizenzkennung.


## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Submodules

This repository includes these root-level git submodules:

- `AutoPubMonitor` → https://github.com/lachlanchen/AutoPubMonitor
- `LazyEdit` → https://github.com/lachlanchen/LazyEdit
- `AutoPublish` → https://github.com/lachlanchen/AutoPublish
