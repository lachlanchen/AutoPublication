[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> Documentación base orientada a documentación primero para flujos de publicación de vídeo asistidos por IA.

## 📌 A simple vista

| Área | Detalles |
| --- | --- |
| Rol | Fuente de documentación canónica para un espacio de trabajo de publicación de vídeo con IA |
| Idiomas | Inglés + 10 versiones localizadas de README |
| Artefactos generados | Metadatos de instantánea y trazas del pipeline en `.auto-readme-work/*` |
| Implementación actual | Solo documentación; no hay código de app en ejecución en este commit |
| Instantánea más reciente | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ Navegación rápida del README

| Sección | Enlace |
|---|---|
| Visión general | [Visión general](#%E2%98%9B-overview) |
| Funcionalidades | [Funcionalidades](#%E2%9C%A8-features) |
| Estructura del proyecto | [Estructura del proyecto](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| Prerrequisitos | [Prerrequisitos](#%F0%9F%A7%B0-prerequisites) |
| Instalación | [Instalación](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| Uso | [Uso](#%E2%96%B6%EF%B8%8F-usage) |
| Configuración | [Configuración](#%F0%9F%A7%A9-configuration) |
| Ejemplos | [Ejemplos](#%F0%9F%A7%AA-examples) |
| Notas de desarrollo | [Notas de desarrollo](#%F0%9F%99%82-development-notes) |
| Solución de problemas | [Solución de problemas](#%F0%9F%94%A7-troubleshooting) |
| Hoja de ruta | [Hoja de ruta](#%F0%9F%97%BA-roadmap) |
| Contribuciones | [Contribuciones](#%F0%9F%A4%9D-contributing) |
| Soporte | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| Contacto | [Contacto](#contact) |
| Licencia | [Licencia](#%F0%9F%93%84-license) |

## 🧭 Visión general

`AutoPublication` es un andamiaje de documentación a nivel de repositorio preparado para soportar un sistema más amplio de publicación de vídeo con IA.  
Mantiene el `README.md` en inglés como fuente de verdad y alinea las traducciones en `i18n/README.*.md` mediante snapshots de pipeline.

### Qué es este repositorio

- Una fuente canónica de documentación y guía para contribuyentes.
- Un conjunto de documentación multilingüe usado como ejemplo de evolución sincronizada de README.
- Un historial de evidencia en `.auto-readme-work/*` que captura cada ejecución de pipeline.

### Qué no es este repositorio (todavía)

- Aún no es una aplicación publicadora ejecutable.
- Aún no es un paquete con scripts de instalación o manifiesto de dependencias.
- Aún no incluye un modelo de configuración en ejecución (`.env`, YAML, esquema de CLI) en esta rama.

## ✨ Características

### Capacidades actuales

- Documentación canónica en inglés en un único archivo fuente (`README.md`).
- Bloque selector de idioma que enlaza a todos los READMEs localizados.
- Artefactos de auto-README con marca temporal (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- Mapa del proyecto centrado en documentación para soportar implementación incremental.
- Panel de soporte estandarizado para visibilidad de donaciones/patrocinio.

### Capacidades previstas

- Orquestación de flujo de publicación asistido por IA.
- Generación y validación de metadatos multiplataforma.
- Objetivos de publicación configurables y gestión de credenciales.
- Ruta reproducible de desarrollo local con pruebas y chequeos de CI.

## 🗂️ Estructura del proyecto

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

### Rutas destacadas

| Ruta | Propósito |
|---|---|
| `i18n/README.*.md` | READMEs localizados para documentación de cara al usuario |
| `.auto-readme-work/*/pipeline-context.md` | Restricciones de ejecución y metadatos para cada pasada de pipeline |
| `.auto-readme-work/*/language-nav-*.md` | Mapas canónicos e i18n de enlaces de idioma |
| `.auto-readme-work/*/repo-structure-analysis.md` | Snapshot histórico de la estructura del repositorio |
| `.auto-readme-work/*/translation-plan.txt` | Alcance y estrategia de traducción por ejecución |
| `.auto-readme-work/*/translated-files.txt` | Listas de archivos traducidos en pasadas anteriores |

## 🧰 Prerrequisitos

Como esta instantánea es solo de documentación, no hay dependencias de tiempo de ejecución para ejecutar una aplicación.

Para tareas de mantenimiento, revisión y sincronización de traducción necesitas:

- `git`
- Una shell compatible con POSIX (los ejemplos usan `bash`)
- Un editor con soporte para Markdown
- Opcional: un visor de diffs (para revisar ramas localizadas)

## 🛠️ Instalación

No existe paquete instalable en esta instantánea.

Para trabajar localmente:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Uso

El uso actual está orientado a documentación y trazas de pipeline.

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

### Flujo recomendado de mantenimiento

1. Actualiza `README.md` para cambios estructurales o de comportamiento.
2. Regenera actualizaciones de traducción cuando sea necesario.
3. Verifica que las secciones clave se mantengan sincronizadas en los archivos `i18n/`.
4. Mantén los snapshots de `.auto-readme-work` consistentes con el flujo de trabajo actual.

## 🧩 Configuración

Todavía no existen archivos formales de configuración en tiempo de ejecución (`.env`, `config.yml`, esquema de CLI, etc.).

Si estás implementando un runtime en el futuro, se recomienda:

- Añadir un archivo de ejemplo como `config.sample.yml`.
- Guardar secretos vía `.env` (excluido del repositorio) o el gestor de secretos de la plataforma de despliegue.
- Mantener la documentación y referencias de CLI en sincronía al añadir nuevas claves.

## 🧪 Ejemplos

### Ejemplos actuales (scaffold existente)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### Ejemplos futuros (implementación esperada)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Notas de desarrollo

- Aplica cambios de forma incremental: prioriza mejoras aditivas y evita reescrituras destructivas.
- Conserva el inglés de `README.md` como documentación base de referencia.
- Usa los archivos del directorio `i18n/` como objetivos explícitos de sincronización.
- Mantén los artefactos del pipeline (`.auto-readme-work/`) como evidencia histórica, no como código productivo editado a mano.
- Evita prometer funcionalidades ejecutables en comandos; documenta solo lo que existe hoy.

### Supuestos incluidos en este README

- El repositorio seguirá siendo documentation-first hasta que se incorporen módulos de ejecución.
- Las traducciones permanecen alineadas con ediciones estructurales significativas.
- `.auto-readme-work/` contiene historial por ejecución solo agregativo y no es la copia de trabajo canónica.

## 🔧 Solución de problemas

### No puedo ejecutar un comando `auto-publication`

**Causa:** No hay una aplicación en ejecución en esta instantánea.

**Solución:** Usa este repositorio para flujos de trabajo de documentación y espera a que se añadan archivos de implementación.

### Un README localizado parece desincronizado

**Causa:** Las traducciones se actualizaron de forma independiente al origen en inglés.

**Solución:** Aplica los mismos cambios estructurales a todos los `i18n/README.*.md` y luego alinea el texto y los ejemplos.

### Un enlace de README apunta a una funcionalidad no existente

**Causa:** La documentación incluye comportamiento previsto.

**Solución:** Mantén esa sección marcada como planificada o sustitúyela por comandos validados actualmente.

## 🗺️ Hoja de ruta

- [ ] Añadir paquete fuente y punto de entrada en ejecución.
- [ ] Añadir manifiesto de dependencias y ruta de instalación.
- [ ] Añadir integraciones de publicación específicas por plataforma.
- [ ] Añadir validación de configuración y gestión de secretos.
- [ ] Añadir ejemplos ejecutables y checks de humo en CI.
- [ ] Añadir verificaciones automáticas de paridad entre READMEs localizados.
- [ ] Añadir archivo `LICENSE` y términos de licencia explícitos.

## 🤝 Contribuciones

Las contribuciones son bienvenidas a medida que este scaffold de documentación se transforma en implementación.

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

Lista recomendada para PR:

- Mantén `README.md` preciso y conciso.
- Actualiza los READMEs de `i18n/` ante cualquier cambio visible al usuario.
- Conserva la estructura existente al añadir secciones útiles de forma incremental.
- Asegura que los artefactos de pipeline sigan alineados con el estado actual del documento.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contacto

Usa los issues del repositorio para preguntas, correcciones de documentación y coordinación de contribuciones.

## 📄 Licencia

Actualmente no existe un archivo `LICENSE` en esta instantánea.
