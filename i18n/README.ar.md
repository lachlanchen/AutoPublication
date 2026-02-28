[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo%20Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> Auto Publish Videos with AI tools.

## 🧭 نظرة عامة

`AutoPublication` هو بنية أولية قائمة على التوثيق (documentation-first) تهدف إلى تعريف سيرات عمل نشر الفيديو باستخدام أدوات مدعومة بالذكاء الاصطناعي.

في المرحلة الحالية للمستودع، هذا المشروع هو بنية أولية تضم توثيقًا ومخرجات خطّة آلية لإنشاء README، لكن لم يتم بعد تضمين أي شفرة مصدرية للتطبيق أو نقطة دخول تشغيل فعلية.

هذا الـREADME هو المصدر الإنجليزي الرسمي للتوثيق، ومُنظّم لدعم توسّع التنفيذ مستقبلاً دون فقدان نية المشروع الحالية.

## ✨ الميزات

### ✅ القدرات الحالية

- README أساسي موحد في الجذر لتعريف المشروع.
- أهداف README متعددة اللغات محددة مسبقًا ضمن `i18n/`.
- سياق بنية خط أنابيب الـREADME ومخرجاته ضمن `.auto-readme-work/`.
- سطر تنقّل اللغات مركّز في الأعلى لتحقيق اتساق متعدد اللغات.

### القدرات المخططة (مستندة إلى اسم المشروع والوصف الحالي)

- تنسيق تلقائي لسير نشر الفيديو.
- إعداد البيانات الوصفية والمحتوى بمساعدة الذكاء الاصطناعي.
- وجهات نشر قابلة للتكوين وتكاملات مع منصّات متعددة.

## 🗂️ بنية المشروع

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

## 🔎 المسارات المهمة

| المسار | الغرض |
|---|---|
| `i18n/` | مجلد الهدف لملفات README المترجمة. |
| `.auto-readme-work/20260301_064412/pipeline-context.md` | سياق قيود وتشغيل Auto-README الأحدث. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | خطة سابقة لأهداف اللغات في نسخ README. |
| `.auto-readme-work/20260301_064412/translation-plan.txt` | أحدث خطة أولويات وأهداف لغوية. |
| `.gitignore` | قالب تجاهل موجّه إلى بايثون (إرشادي فقط؛ لا توجد حالياً ملفات تطبيق بايثون). |

## المتطلبات المسبقة

نظرًا لعدم وجود ملفات تنفيذية حتى الآن، فمتطلبات التشغيل هي افتراضات مستندة إلى محتوى المستودع.

| النوع | المتطلب |
|---|---|
| الأدوات | `git` |
| الصدفة | صدفة متوافقة مع POSIX (تستخدم الأمثلة `bash`). |

الإشارات المتوقعة للمكدس المستقبلي (من `.gitignore`):

- سلسلة أدوات Python وتغليف الحزم المرتبط بها.

## 🚀 التثبيت

في هذه المرحلة لا توجد حزمة قابلة للتثبيت أو قائمة تبعيات أو نقطة دخول.

استنساخ المستودع والدخول إليه:

```bash
# استنساخ المستودع والدخول إليه
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## ▶️ الاستخدام

لا يوجد حتى الآن أمر تشغيل قابل للتنفيذ.

الاستخدام العملي الحالي هو إعداد المستودع والتوثيق:

```bash
# فحص بنية المستودع
ls -la

# عرض أهداف اللغات
ls -la i18n

# عرض سياق أنبوب README النشط
cat .auto-readme-work/20260301_064412/pipeline-context.md
```

بعد إضافة التنفيذ، استبدل هذه الأوامر بسير عمل تشغيلية ونشر فعلية.

## ⚙️ الإعداد

لا توجد حتى الآن ملفات إعداد رسمية (مثل `.env.example` أو `config.yaml` أو خيارات CLI).

الاقتراحات المستقبلية:

- قالب بيئة لإعداد بيانات اعتماد API ووجهات النشر.
- مخطط تكوين `YAML/JSON` للبيانات الوصفية الافتراضية وتهيئة سير العمل لكل منصة.
- توثيق إعدادات CLI وسلوك التحقق منها.

## 🧪 أمثلة

### مثال الحالي (البنية الأولية)

استخدم المستودع كأساس توثيقي:

```bash
# قراءة مقصود المشروع الرسمي
cat README.md
```

### مثال مستقبلي (عنصر نائب)

```bash
# مثال استدعاء متوقع مستقبلًا
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## 🛠️ ملاحظات التطوير

- لا يحتوي المستودع حاليًا على أي شفرة مصدرية قابلة للتنفيذ.
- يبدو أن إنشاء الـREADME يتم عبر خط أنابيب باستخدام الملفات داخل `.auto-readme-work/`.
- تم تجهيز سير العمل متعدد اللغات عبر ملفات `i18n/` وخطط الترجمة.

المهام المقترحة للتنفيذ التالي:

1. إضافة مجلد المصدر (مثلاً `src/` أو `autopublication/`).
2. إضافة ملف تعريف التبعيات (`pyproject.toml` أو ما يعادله).
3. إضافة نقطة دخول تنفيذية وتغطية اختبارية أولية.
4. إضافة CI للتحقق من lint/test/docs.

## 🩺 استكشاف الأخطاء

### "لا أستطيع تشغيل المشروع"

السبب:

- لا توجد ملفات تنفيذية أو نقطة دخول تشغيلية ضمن الالتزامات الحالية.

الحل:

- تعامل مع المستودع كبنية أولية/توضيحية للتوثيق حتى تتم إضافة التنفيذ.

### "روابط README اللغوية موجودة لكن الملفات غير موجودة"

السبب:

- المجلد `i18n/` موجود، لكن ملفات README المترجمة غير مضافة في هذه اللقطة.

الحل:

- أنشئ وأضف الملفات المدرجة ضمن `i18n/README.*.md` وخطط الترجمة.

## 🧭 خارطة الطريق

- [ ] إضافة أول تنفيذ قابل للتشغيل للنشر الآلي.
- [ ] تعريف تكاملات المزوّديين ومخطط الإعداد.
- [ ] إضافة تعليمات إعداد محلي قابلة لإعادة الإنتاج.
- [ ] إضافة اختبارات وأنبوب CI.
- [ ] نشر مجموعة README كاملة متعددة اللغات ضمن `i18n/`.

## 🤝 المساهمة

المساهمات مرحب بها بينما ينتقل المشروع من البنية الأولية إلى التنفيذ.

تدفق المساهمة المقترح:

```bash
# 1) إنشاء فرع جديد
git checkout -b feat/<short-description>

# 2) تثبيت التغييرات
git add .
git commit -m "feat: <describe change>"

# 3) الدفع وفتح طلب سحب
git push -u origin feat/<short-description>
```

يرجى تضمين:

- وصف واضح للمشكلة ونطاقها.
- خطوات قابلة لإعادة التنفيذ لأي تغييرات سلوكية.
- تحديثات للتوثيق عند إضافة أوامر/إعدادات جديدة.

## ❤️ Support

| Donate | PayPal | Stripe |
|---|---|---|
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=ko-fi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 📫 التواصل

للاستفسارات الحالية وتصحيحات التوثيق، افتح issue في المستودع.

## 📄 الترخيص

لا يوجد ملف ترخيص حاليًا في لقطة هذا المستودع.

الفرضية:

- لم يتم تحديد الترخيص بعد.

الخطوة التالية المقترحة:

- أضف ملف `LICENSE` وقم بتحديث هذا القسم للإشارة إليه صراحةً.
