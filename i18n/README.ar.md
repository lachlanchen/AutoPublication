[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> هيكل توثيق أولي مخصص لسير عمل نشر فيديو مدعوم بالذكاء الاصطناعي.

## 📌 لمحة سريعة

| المجال | التفاصيل |
| --- | --- |
| الدور | المصدر الرسمي للوثائق باللغة الإنجليزية لمساحة عمل نشر الفيديو بالذكاء الاصطناعي |
| اللغات | الإنجليزية + 10 نسخ README مترجمة |
| المخرجات المولدة | بيانات تعريف اللقطة وسجلات خط الأنابيب في `.auto-readme-work/*` |
| التنفيذ الحالي | هيكل توثيقي فقط (لا يوجد كود تشغيل فعلي ملتزم بعد) |
| أحدث لقطة | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ تنقل سريع للـ README

| القسم | الرابط |
|---|---|
| نظرة عامة | [Overview](#%E2%98%9B-overview) |
| الميزات | [Features](#%E2%9C%A8-features) |
| بنية المشروع | [Project structure](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| المتطلبات المسبقة | [Prerequisites](#%F0%9F%A7%B0-prerequisites) |
| التثبيت | [Installation](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| الاستخدام | [Usage](#%E2%96%B6%EF%B8%8F-usage) |
| الإعداد | [Configuration](#%F0%9F%A7%A9-configuration) |
| أمثلة | [Examples](#%F0%9F%A7%AA-examples) |
| ملاحظات التطوير | [Development notes](#%F0%9F%99%82-development-notes) |
| استكشاف الأخطاء | [Troubleshooting](#%F0%9F%94%A7-troubleshooting) |
| خارطة الطريق | [Roadmap](#%F0%9F%97%BA-roadmap) |
| المساهمة | [Contributing](#%F0%9F%A4%9D-contributing) |
| الدعم | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| التواصل | [Contact](#contact) |
| الترخيص | [License](#%F0%9F%93%84-license) |

## 🧭 نظرة عامة

`AutoPublication` هو هيكل توثيق على مستوى المستودع مُعد لدعم نظام أوسع لنشر الفيديو بالذكاء الاصطناعي.
يُبقي ملف الـ `README.md` الإنجليزي كمصدر الحقيقة الأساسي، ويُزامن الترجمات في `i18n/README.*.md` عبر لقطات خط الأنابيب.

### ما الذي يمثله هذا المستودع

- مصدر رسمي لتوثيق المشروع وإرشادات المساهمين.
- مجموعة وثائق متعددة اللغات تُستخدم كمرجع متزامن لتطور README.
- مخزن أدلة تاريخية تحت `.auto-readme-work/*` يلتقط كل تشغيل من خط الأنابيب.

### ما الذي لا يمثله هذا المستودع (حتى الآن)

- لا يوجد تطبيق نشر قابل للتنفيذ بعد.
- لا يوجد حزمة ذات نصوص تثبيت أو سجلات اعتماد.
- لا يوجد نموذج تكوين تشغيل (`.env`، YAML، مخطط CLI) في هذا الفرع.

## ✨ الميزات

### القدرات الحالية

- توثيق إنجليزي أساسي في ملف مصدر واحد (`README.md`).
- كتلة اختيار لغة تربط جميع ملفات README المترجمة.
- لقطات README مؤتمتة ذات طابع زمني (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- خريطة مشروع قياسية موجهة للتوثيق لدعم التنفيذ التدريجي.
- لوحة دعم قياسية لعرض خيارات التبرع/الرعاية.

### القدرات المخطط لها

- تنسيق سير نشر المحتوى بمساعدة الذكاء الاصطناعي.
- توليد بيانات وصفية متعددة المنصات والتحقق منها.
- أهداف نشر قابلة للتخصيص وإدارة بيانات اعتماد.
- مسار تطوير محلي قابل لإعادة التشغيل مع اختبارات وفحوصات CI.

## 🗂️ بنية المشروع

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

### المسارات المهمة

| المسار | الغرض |
|---|---|
| `i18n/README.*.md` | ملفات README مترجمة لتوثيق واجهات المستخدم |
| `.auto-readme-work/*/pipeline-context.md` | قيود التشغيل والبيانات الوصفية لكل تمريرة خط أنابيب |
| `.auto-readme-work/*/language-nav-*.md` | ملفات رسمية لتثبيت خرائط اللغة (root و i18n) |
| `.auto-readme-work/*/repo-structure-analysis.md` | لقطات هيكلية تاريخية لبنية المستودع |
| `.auto-readme-work/*/translation-plan.txt` | نطاقات الترجمة وخطة الترجمة |
| `.auto-readme-work/*/translated-files.txt` | قوائم ملفات الإخراج من عمليات الترجمة السابقة |

## 🧰 المتطلبات المسبقة

نظرًا لأن هذه اللقطة توثيقية فقط، لا توجد تبعيات تنفيذية لتشغيل التطبيق.

لأعمال الصيانة والمراجعة وتزامن الترجمة تحتاج إلى:

- `git`
- واجهة shell متوافقة مع POSIX (تعتمد الأمثلة على `bash`)
- محرر يدعم Markdown
- اختياري: عرض المقارنات (diff viewer) لمراجعة الفروع المحلية

## 🛠️ التثبيت

لا توجد حزمة قابلة للتثبيت في هذه اللقطة.

للعمل محليًا:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ الاستخدام

الاستخدام الحالي موجه للتوثيق وتتبع مسار خط الأنابيب.

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

### سير صيانة موصى به

1. حدّث `README.md` عند تغييرات بنيوية أو سلوكية.
2. أعد إنشاء تحديثات الترجمة عند الحاجة.
3. تأكد من بقاء الأقسام الرئيسية متزامنة عبر ملفات `i18n/`.
4. احرص على اتساق لقطات `.auto-readme-work` مع سير العمل الحالي.

## 🧩 الإعداد

لا توجد ملفات إعداد تشغيل رسمية بعد (`.env`, `config.yml`, CLI schema، إلخ غير موجودة).

إذا كنت ستنفذ نموذج تشغيل مستقبلاً، فالإعدادات المقترحة:

- أضف ملف نموذج مثل `config.sample.yml`.
- خزّن الأسرار عبر `.env` (مستبعد من المستودع) أو مدير الأسرار في منصة الاستضافة.
- احرص على تزامن الوثائق والـ CLI عند إضافة مفاتيح جديدة.

## 🧪 الأمثلة

### الأمثلة الحالية (المخطط القائم حالياً)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### الأمثلة المستقبلية (المتوقعة)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ ملاحظات التطوير

- عُدّ التغييرات بشكل تدريجي: قدّم تحسينات إضافية وابتعد عن إعادة البناء الجذرية.
- احتفظ بالإنجليزية كمصدر موثوق للتوثيق الأساسي.
- استخدم ملفات `i18n/` كأهداف مزامنة صريحة.
- اعتبر لقطات `.auto-readme-work/` أدلة تاريخية، وليس شفرة إنتاجية.
- لا تعدّي الوعود التشغيلية في الأوامر؛ وثّق فقط ما هو موجود بالفعل.

### الافتراضات المندرجة في هذا الـ README

- يستمر المستودع كتوثيق أولاً حتى تُدمج وحدات التشغيل.
- تبقى الترجمات متماشية مع التعديلات الهيكلية المعقولة.
- يحتوي `.auto-readme-work/` على سجل تاريخي إضافي للعمليات وليس النسخة الأساسية للعمل.

## 🔧 استكشاف الأخطاء

### لا أستطيع تشغيل أمر `auto-publication`

**السبب:** لا يوجد تطبيق وقتي/تشغيلي في هذه اللقطة.

**الإصلاح:** استخدم هذا المستودع لسير عمل التوثيق وانتظر إضافة ملفات التنفيذ.

### يبدو أن نسخة README مترجمة غير متزامنة

**السبب:** تم تحديث الترجمات بشكل منفصل عن المصدر الإنجليزي.

**الإصلاح:** طبّق نفس التغييرات البنيوية على جميع ملفات `i18n/README.*.md`، ثم راجع الصياغة والأمثلة.

### يشير رابط README إلى وظيفة غير موجودة

**السبب:** يحتوي التوثيق على سلوك مخطط في المستقبل.

**الإصلاح:** أبقِ القسم محددًا كوظيفة مستقبلية أو استبدله بوظائف موثقة حاليًا.

## 🗺️ خارطة الطريق

- [ ] إضافة حزمة المصدر ونقطة دخول تشغيلية.
- [ ] إضافة بيان اعتمادات ومسار تثبيت.
- [ ] إضافة تكاملات نشر خاصة بالمنصات.
- [ ] إضافة التحقق من التكوين وإدارة الأسرار.
- [ ] إضافة أمثلة تشغيلية وفحوصات smoke في CI.
- [ ] إضافة فحوصات تطابق آلية بين READMEs المترجمة.
- [ ] إضافة ملف `LICENSE` وصياغة شروط الترخيص.

## 🤝 المساهمة

المساهمات مرحب بها بينما ينتقل هذا الهيكل التوثيقي تدريجيًا نحو تنفيذ فعلي.

```bash
# 1. create a branch
git checkout -b docs/<short-description>

# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

قائمة تحقق مقترحة للـ PR:

- حافظ على `README.md` كمصدر الحقيقة.
- حدّث كل ملف `i18n/README.*.md` تم تعديله.
- احتفظ بالأقسام الحالية مع إضافة قيمة تدريجية.
- حافظ على اتساق بيانات `.auto-readme-work/*` مع هذه الدورة الحالية.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

استخدم قضايا المستودع (Issues) للطرح والاستفسارات وتنسيق الملاحظات البرمجية.

## 📄 License

لا يوجد ملف `LICENSE` حاليًا في هذه اللقطة.

الخطوة المقترحة التالية:

- أضف ملف `LICENSE` وحدث هذا القسم بمعرف الترخيص المختار.
