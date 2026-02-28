[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo%20Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> Publica vídeos automáticamente con herramientas de IA.

## 🧭 Descripción general

`AutoPublication` es un andamiaje centrado en la documentación concebido para definir flujos de publicación de vídeo asistidos por IA.

En el estado actual del repositorio, este proyecto es un andamiaje con documentación y artefactos de la canalización de generación de README, pero aún no se han incorporado código fuente de aplicación ni punto de entrada de ejecución.

Este README es la fuente canónica de documentación en inglés y está estructurado para soportar un crecimiento futuro de implementación sin perder la intención actual del proyecto.

## ✨ Características

### ✅ Capacidades actuales

- README raíz canónico para la definición del proyecto.
- Objetivos de README multilingües predefinidos en `i18n/`.
- Artefactos de contexto y estructura de pipeline de README en `.auto-readme-work/`.
- Línea de navegación de idioma centralizada en la parte superior para mantener paridad multilingüe.

### Capacidades planificadas (inferidas del nombre del proyecto y la descripción actual)

- Orquestación automatizada de publicación de vídeos.
- Preparación de metadatos y contenido asistida por IA.
- Destinos de publicación configurables e integraciones con plataformas.

## 🗂️ Estructura del proyecto

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

## 🔎 Rutas destacadas

| Ruta | Propósito |
|---|---|
| `i18n/` | Carpeta destino de los README traducidos. |
| `.auto-readme-work/20260301_064412/pipeline-context.md` | Último contexto de ejecución y restricciones de auto-README. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | Plan de objetivos de idioma y precedencias anterior. |
| `.auto-readme-work/20260301_064412/translation-plan.txt` | Último plan de objetivos de idioma y prioridades. |
| `.gitignore` | Plantilla de exclusión orientada a Python (solo indicativa; actualmente no hay archivos de app Python). |

## Requisitos previos

Dado que aún no existen archivos de implementación, los prerrequisitos de ejecución son suposiciones derivadas del contenido del repositorio.

| Tipo | Requisito |
|---|---|
| Herramientas | `git` |
| Shell | Shell compatible con POSIX (los ejemplos usan `bash`) |

Señales de stack futuro probable (según `.gitignore`):

- Cadena de herramientas de Python y utilidades de empaquetado relacionadas

## 🚀 Instalación

En esta fase no hay paquete instalable, manifiesto de dependencias ni punto de entrada.

Clona y entra en el repositorio:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## ▶️ Uso

Aún no existe un comando de aplicación ejecutable.

El uso práctico actual es la documentación del repositorio y la preparación del flujo de trabajo:

```bash
# Inspeccionar la estructura del repositorio
ls -la

# Inspeccionar objetivos de idioma
ls -la i18n

# Ver el contexto activo de la canalización de README
cat .auto-readme-work/20260301_064412/pipeline-context.md
```

Cuando se agregue la implementación, reemplaza estos comandos con flujos de publicación y ejecución concretos.

## ⚙️ Configuración

Aún no existen archivos de configuración formales (como `.env.example`, `config.yaml` o opciones de CLI).

Añadidos recomendados para el futuro:

- Plantilla de entorno para credenciales de API y destinos de publicación.
- Esquema de configuración YAML/JSON para metadatos específicos de plataforma y valores predeterminados de flujo.
- Documentación de configuración de CLI y comportamiento de validación.

## 🧪 Ejemplos

### Ejemplo actual (andamiaje)

Usa el repositorio como línea base de documentación:

```bash
# Leer la intención canónica del proyecto
cat README.md
```

### Ejemplo objetivo futuro (marcador de posición)

```bash
# Ejemplo de invocación futura prevista
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## 🛠️ Notas de desarrollo

- Actualmente el repositorio no contiene código fuente ejecutable.
- La generación de README parece estar guiada por canalización con archivos en `.auto-readme-work/`.
- El flujo multilingüe está esqueletonado por los archivos de `i18n/` y los planes de traducción.

Hitos recomendados de implementación siguientes:

1. Agregar directorio de código fuente (por ejemplo, `src/` o `autopublication/`).
2. Agregar manifiesto de dependencias (`pyproject.toml` o equivalente).
3. Agregar punto de entrada ejecutable y cobertura inicial de pruebas.
4. Agregar CI para validar lint/test/docs.

## 🩺 Solución de problemas

### "No puedo ejecutar el proyecto"

Causa:

- No hay archivos de aplicación en tiempo de ejecución ni punto de entrada comprometidos actualmente.

Resolución:

- Tratar el repositorio como un andamiaje/documentación base hasta que se agregue la implementación.

### "Los enlaces de README por idioma existen, pero faltan archivos"

Causa:

- `i18n/` existe, pero los README localizados no se han generado en esta instantánea.

Resolución:

- Genera y agrega los archivos listados en `i18n/README.*.md` y los artefactos del plan de traducción.

## 🧭 Hoja de ruta

- [ ] Añadir la primera implementación ejecutable para publicación automatizada.
- [ ] Definir integraciones de proveedores y esquema de configuración.
- [ ] Añadir instrucciones reproducibles de configuración local.
- [ ] Añadir pruebas y pipeline de CI.
- [ ] Publicar el conjunto completo de README multilingües en `i18n/`.

## 🤝 Contribución

Las contribuciones son bienvenidas a medida que el proyecto avance de un andamiaje a una implementación.

Flujo de contribución sugerido:

```bash
# 1) Crear una rama
git checkout -b feat/<short-description>

# 2) Confirmar cambios
git add .
git commit -m "feat: <describe change>"

# 3) Enviar y abrir un PR
git push -u origin feat/<short-description>
```

Por favor incluye:

- Declaración clara del problema y alcance.
- Pasos reproducibles para cualquier cambio de comportamiento.
- Actualizaciones de documentación para nuevos comandos/configuración.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📫 Contacto

Para preguntas de uso actuales y correcciones de documentación, abre un issue en el repositorio.

## 📄 Licencia

No hay archivo de licencia presente actualmente en esta instantánea del repositorio.

Suposición:

- La licencia aún no está declarada.

Siguiente paso recomendado:

- Añade un archivo `LICENSE` y actualiza esta sección para referenciarlo explícitamente.
