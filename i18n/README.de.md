[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> Videos automatisch mit KI-Tools veröffentlichen.

## Überblick

`AutoPublication` soll Video-Veröffentlichungs-Workflows mit KI-gestützten Tools automatisieren.

Im aktuellen Repository-Stand ist dieses Projekt ein Gerüst mit Dokumentation und Artefakten einer README-Generierungs-Pipeline, aber es wurde noch kein Anwendungsquellcode oder Runtime-Entrypoint eingecheckt.

Diese README dient als kanonische englische Basis und ist so strukturiert, dass zukünftige Implementierungsfortschritte unterstützt werden, ohne die aktuelle Projektabsicht zu verlieren.

| Bereich | Aktueller Status |
|---|---|
| Implementierung | Scaffold-Phase (keine Runtime-App eingecheckt) |
| Dokumentation | Kanonische Root-README vorhanden |
| Mehrsprachige Doku | Sprachziele unter `i18n/` definiert |
| Pipeline-Artefakte | Unter `.auto-readme-work/` vorhanden |

## Funktionen

### Aktuelle Fähigkeiten

- Kanonische Root-README zur Projektdefinition.
- Vordefinierte mehrsprachige README-Ziele unter `i18n/`.
- README-Pipeline-Kontext für reproduzierbare Dokumentationsgenerierung.

### Geplante Fähigkeiten (aus Projektname und aktueller Beschreibung abgeleitet)

- Orchestrierung der automatisierten Videoveröffentlichung.
- KI-gestützte Vorbereitung von Metadaten/Inhalten.
- Konfigurierbare Integrationen für Veröffentlichungsziele.

## Projektstruktur

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

### Wichtige Pfade

| Pfad | Zweck |
|---|---|
| `README.md` | Kanonische Projektdefinition auf Englisch. |
| `i18n/` | Zielordner für übersetzte README-Dateien. |
| `.auto-readme-work/20260228_230008/pipeline-context.md` | Kontext und Einschränkungen des Auto-README-Laufs. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | Sprachzuordnung und Dateiziele. |
| `.gitignore` | Python-orientierte Ignore-Vorlage (nur indikativ; derzeit keine Python-App-Dateien vorhanden). |

## Voraussetzungen

Da Implementierungsdateien noch nicht vorhanden sind, sind Runtime-Voraussetzungen derzeit Annahmen.

### Dokumentierte Basis

- `git`
- Eine POSIX-kompatible Shell (Beispiele verwenden `bash`)

### Wahrscheinliches Signal für zukünftigen Stack (nur aus `.gitignore`)

- Eine Python-Toolchain könnte später erforderlich sein.

## Installation

In diesem Stadium gibt es kein installierbares Paket und kein Dependency-Manifest.

Repository klonen und wechseln:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## Nutzung

Es gibt noch keinen ausführbaren Anwendungsbefehl.

Aktuell besteht die praktische Nutzung im Dokumentations-Workflow und in der Repository-Vorbereitung:

```bash
# Inspect repository structure
ls -la

# Inspect i18n targets
ls -la i18n
```

Sobald eine Implementierung hinzugefügt wurde, sollte dieser Abschnitt um konkrete Ausführungsbefehle und echte End-to-End-Beispiele erweitert werden.

## Konfiguration

Derzeit sind noch keine formalen Konfigurationsdateien vorhanden (z. B. `.env.example`, `config.yaml` oder CLI-Flags).

Empfohlene zukünftige Ergänzungen:
- Eine dokumentierte Umgebungs-Vorlage (für API-Keys/Tokens).
- Plattformspezifische Veröffentlichungskonfiguration.
- Einstellungen zur Auswahl von KI-Anbieter/Modell.

## Beispiele

### Aktuelles (Scaffold-)Beispiel

Repository als Dokumentations-Basis verwenden:

```bash
# Read canonical project intent
cat README.md
```

### Zukünftiges (Ziel-)Beispiel

Angenommener zukünftiger Workflow (nur Platzhalter):

```bash
# Placeholder example for future implementation
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## Hinweise zur Entwicklung

- Das Repository enthält derzeit keinen ausführbaren Quellcode.
- Die README-Generierung scheint Pipeline-gesteuert zu sein und Dateien in `.auto-readme-work/` zu verwenden.
- Die Sprach-Navigationszeile ist absichtlich am Anfang dieser README zentralisiert, um mehrsprachige Parität zu unterstützen.

Vorgeschlagene nächste Implementierungs-Meilensteine:
1. Quellcodeverzeichnis hinzufügen (zum Beispiel `src/` oder `autopublication/`).
2. Dependency-Manifest hinzufügen (`pyproject.toml` oder Äquivalent).
3. Ausführbaren Entrypoint und minimale Testabdeckung hinzufügen.
4. CI hinzufügen, um Lint/Test/Doku zu validieren.

## Fehlerbehebung

### "Ich kann das Projekt nicht ausführen"

Ursache:
- Es sind derzeit keine Runtime-Anwendungsdateien oder kein Entrypoint eingecheckt.

Lösung:
- Das Repository als Scaffold/Dokumentation behandeln, bis Quellcode hinzugefügt wird.

### "Links zu Sprach-READMEs existieren, aber Dateien fehlen"

Ursache:
- `i18n/` existiert, aber lokalisierte README-Dateien wurden in diesem Snapshot nicht generiert.

Lösung:
- Die in `.auto-readme-work/20260228_230008/translation-plan.txt` aufgeführten Zieldateien generieren/hinzufügen.

## Roadmap

- [ ] Erste lauffähige Implementierung für automatisierte Veröffentlichung hinzufügen.
- [ ] Anbieterintegrationen und Konfigurationsschema definieren.
- [ ] Reproduzierbare lokale Setup-Anleitungen hinzufügen.
- [ ] Tests und CI-Pipeline hinzufügen.
- [ ] Vollständigen mehrsprachigen README-Satz in `i18n/` veröffentlichen.

## Mitwirken

Beiträge sind willkommen, während sich das Projekt vom Scaffold zur Implementierung entwickelt.

Vorgeschlagener Beitragsablauf:

```bash
# 1) Create a branch
git checkout -b feat/<short-description>

# 2) Commit your changes
git add .
git commit -m "feat: <describe change>"

# 3) Push and open a PR
git push -u origin feat/<short-description>
```

Bitte einfügen:
- Klare Problembeschreibung und Umfang.
- Reproduzierbare Schritte für Verhaltensänderungen.
- Dokumentations-Updates für neue Befehle/Konfiguration.

## Support

In diesem Repository sind derzeit keine Spenden-/Sponsoring-Kanäle angegeben.

Falls später Support-Links hinzugefügt werden, sollten sie hier aufgeführt und über alle i18n-Varianten hinweg gespiegelt werden.

## Lizenz

Im aktuellen Snapshot dieses Repositorys ist derzeit keine Lizenzdatei vorhanden.

Annahme:
- Die Lizenzierung ist noch nicht festgelegt.

Empfohlener nächster Schritt:
- Eine `LICENSE`-Datei hinzufügen und diesen Abschnitt so aktualisieren, dass explizit darauf verwiesen wird.
