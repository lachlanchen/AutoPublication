[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> Documentation-first pour une architecture de publication vidéo assistée par IA.

## 📌 En bref

| Domaine | Détails |
| --- | --- |
| Rôle | Source de documentation canonique pour un espace de travail de publication vidéo IA |
| Langues | Anglais + 10 traductions localisées de `README` |
| Artefacts générés | Métadonnées d'instantané et traces du pipeline dans `.auto-readme-work/*` |
| Implémentation actuelle | Scaffold uniquement documentaire (aucun code applicatif exécutable commité pour l'instant) |
| Dernier instantané | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ Navigation rapide du README

| Section | Lien |
|---|---|
| Aperçu | [Aperçu](#%E2%98%9B-overview) |
| Fonctionnalités | [Fonctionnalités](#%E2%9C%A8-features) |
| Structure du projet | [Structure du projet](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| Prérequis | [Prérequis](#%F0%9F%A7%B0-prerequisites) |
| Installation | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| Utilisation | [Utilisation](#%E2%96%B6%EF%B8%8F-usage) |
| Configuration | [Configuration](#%F0%9F%A7%A9-configuration) |
| Exemples | [Exemples](#%F0%9F%A7%AA-examples) |
| Notes de développement | [Notes de développement](#%F0%9F%99%82-development-notes) |
| Dépannage | [Dépannage](#%F0%9F%94%A7-troubleshooting) |
| Feuille de route | [Feuille de route](#%F0%9F%97%BA-roadmap) |
| Contribution | [Contribution](#%F0%9F%A4%9D-contributing) |
| Support | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| Contact | [Contact](#contact) |
| License | [License](#%F0%9F%93%84-license) |

## 🧭 Aperçu

`AutoPublication` est un scaffold documentaire au niveau du dépôt conçu pour prendre en charge un système plus large de publication vidéo assisté par IA.  
Il maintient le `README.md` en anglais comme source de vérité et aligne les traductions dans `i18n/README.*.md` via les snapshots de pipeline.

### Ce qu'est ce dépôt

- Une source canonique de documentation et de guidance pour les contributeurs.
- Un ensemble de documentation multilingue utilisé comme exemple d'évolution synchronisée des README.
- Un historique de preuve dans `.auto-readme-work/*` qui conserve chaque exécution de pipeline.

### Ce que ce dépôt n'est pas (encore)

- Pas encore d'application de publication exécutable.
- Pas encore un package avec scripts d'installation ou manifeste de dépendances.
- Pas encore de modèle de configuration runtime (`.env`, YAML, schéma CLI) dans cette branche.

## ✨ Fonctionnalités

### Capacités actuelles

- Documentation anglaise canonique dans un seul fichier source (`README.md`).
- Bloc de sélection de langue renvoyant vers tous les `README` localisés.
- Artefacts auto-README horodatés (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- Carte de projet centrée sur la documentation pour soutenir la mise en œuvre incrémentielle.
- Panneau de support standardisé pour la visibilité des dons et sponsorings.

### Capacités prévues

- Orchestration de workflows de publication assistée par IA.
- Génération et validation de métadonnées multi-plateforme.
- Cibles de publication configurables et gestion des identifiants.
- Parcours reproductible de développement local avec tests et vérifications CI.

## 🗂️ Structure du projet

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

### Chemins notables

| Chemin | Objectif |
|---|---|
| `i18n/README.*.md` | README localisés pour la documentation destinée aux utilisateurs |
| `.auto-readme-work/*/pipeline-context.md` | Contraintes d'exécution et métadonnées pour chaque passage du pipeline |
| `.auto-readme-work/*/language-nav-*.md` | Fichiers de correspondance langue-canonique |
| `.auto-readme-work/*/repo-structure-analysis.md` | Snapshots historiques de la structure |
| `.auto-readme-work/*/translation-plan.txt` | Portée et plan de traduction |
| `.auto-readme-work/*/translated-files.txt` | Listes de fichiers générés par les traductions précédentes |

## 🧰 Prérequis

Étant donné que cet instantané est exclusivement documentaire, il n'existe pas de dépendances d'exécution runtime pour faire tourner une application.

Pour la maintenance, la revue et la synchronisation des traductions, vous avez besoin de :

- `git`
- Un shell compatible POSIX (les exemples utilisent `bash`)
- Un éditeur compatible Markdown
- Optionnel : un outil de diff (pour examiner les branches localisées)

## 🛠️ Installation

Aucun package installable n'existe dans cet instantané.

Pour travailler localement :

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Utilisation

L'utilisation actuelle est orientée documentation et traces de pipeline.

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

### Flux de maintenance recommandé

1. Mettez à jour `README.md` pour les changements structurels ou comportementaux.
2. Régénérez les traductions quand nécessaire.
3. Vérifiez que les sections clés restent synchronisées dans les fichiers `i18n/`.
4. Conservez les snapshots `.auto-readme-work` cohérents avec le workflow actuel.

## 🧩 Configuration

Aucun fichier de configuration runtime formel n'est encore commité (`.env`, `config.yml`, schéma CLI, etc. sont absents).

Si vous implémentez un runtime futur, recommandations :

- Ajoutez un fichier d'exemple tel que `config.sample.yml`.
- Stockez les secrets via `.env` (exclu du dépôt) ou le gestionnaire de secrets de la plateforme d'hébergement.
- Gardez docs et références CLI en phase lorsque vous ajoutez de nouvelles clés.

## 🧪 Exemples

### Exemples actuels (scaffold existant)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### Exemples futurs (implémentation attendue)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Notes de développement

- Traitez les changements de manière incrémentale : privilégiez les améliorations additives et évitez les réécritures destructrices.
- Conservez l'anglais de `README.md` comme base documentaire de référence.
- Utilisez les fichiers de `i18n/` comme cibles de synchronisation explicites.
- Gardez les artefacts de pipeline (`.auto-readme-work/`) comme preuve historique, pas comme code de production édité à la main.
- Évitez de promettre un comportement exécutable dans les commandes ; documentez uniquement ce qui existe réellement.

### Hypothèses de ce README

- Le dépôt reste documentation-first tant que les modules runtime ne sont pas ajoutés.
- Les traductions restent alignées avec les modifications structurelles pertinentes.
- `.auto-readme-work/` contient un historique append-only dépendant d'une exécution et n'est pas la copie de travail canonique.

## 🔧 Dépannage

### Je ne peux pas exécuter une commande `auto-publication`

**Cause :** Aucun runtime applicatif n'existe dans cet instantané.

**Solution :** Utilisez ce dépôt pour les flux de travail de documentation et attendez l'ajout de fichiers d'implémentation.

### Un README localisé semble désynchronisé

**Cause :** Les traductions ont été mises à jour indépendamment de la source anglaise.

**Solution :** Appliquez les mêmes changements structurels à tous les `i18n/README.*.md`, puis alignez la formulation et les exemples.

### Un lien de README pointe vers une fonctionnalité inexistante

**Cause :** La documentation comporte un comportement planifié.

**Solution :** Conservez cette section comme planifiée ou remplacez-la par des commandes validées actuellement.

## 🗺️ Feuille de route

- [ ] Ajouter le package source et un point d'entrée runtime.
- [ ] Ajouter le manifeste de dépendances et le parcours d'installation.
- [ ] Ajouter des intégrations de publication spécifiques aux plateformes.
- [ ] Ajouter la validation de configuration et la gestion des secrets.
- [ ] Ajouter des exemples exécutables et des vérifications de smoke CI.
- [ ] Ajouter des vérifications automatisées de parité entre les README localisés.
- [ ] Ajouter un fichier `LICENSE` et des conditions de licence explicites.

## 🤝 Contribution

Les contributions sont les bienvenues alors que ce scaffold documentaire évolue vers une implémentation.

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

Checklist PR suggérée :

- Gardez `README.md` comme source de vérité.
- Mettez à jour chaque README localisé touché dans `i18n/`.
- Conservez les sections existantes tout en ajoutant une valeur incrémentielle.
- Conservez les métadonnées `.auto-readme-work/*` alignées avec le passage courant.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

Utilisez les issues du dépôt pour les questions, corrections de documentation et coordination des contributions.

## 📄 License

Aucun fichier `LICENSE` n'est présent actuellement dans cet instantané.

Étape suivante suggérée :

- Ajouter un fichier `LICENSE` et mettre à jour cette section avec l'identifiant de licence choisi.

## Submodules

This repository includes these root-level git submodules:

- `AutoPubMonitor` → https://github.com/lachlanchen/AutoPubMonitor
- `LazyEdit` → https://github.com/lachlanchen/LazyEdit
- `AutoPublish` → https://github.com/lachlanchen/AutoPublish
