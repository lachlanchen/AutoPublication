[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# AutoPublication

![Status](https://img.shields.io/badge/status-documentation_first-0f172a?style=for-the-badge&logo=markdown&logoColor=white)
![Scope](https://img.shields.io/badge/scope-readme_generation-0ea5e9?style=for-the-badge&logo=github&logoColor=white)
![i18n](https://img.shields.io/badge/i18n-10%20locales-16a34a?style=for-the-badge&logo=googletranslate&logoColor=white)
![Focus](https://img.shields.io/badge/focus-AI%20Video%20Publishing-9333ea?style=for-the-badge&logo=video&logoColor=white)
![Lifecycle](https://img.shields.io/badge/lifecycle-documentation--first-6b7280?style=for-the-badge&logo=github&logoColor=white)
![Pipelines](https://img.shields.io/badge/pipeline%20artifacts-.auto--readme--work-0f766e?style=for-the-badge&logo=githubactions&logoColor=white)

> Khung tài liệu theo hướng documentation-first cho quy trình xuất bản video có hỗ trợ AI.

## 📌 Tóm tắt nhanh

| Khu vực | Chi tiết |
| --- | --- |
| Vai trò | Nguồn tài liệu tiếng Anh chuẩn cho workspace xuất bản video AI |
| Ngôn ngữ | Tiếng Anh + 10 bản mirror README bản địa hóa |
| Tài liệu tạo ra | Siêu dữ liệu snapshot và dấu vết pipeline trong `.auto-readme-work/*` |
| Triển khai hiện tại | Snapshot chỉ chứa tài liệu (chưa commit mã ứng dụng runtime) |
| Snapshot mới nhất | `.auto-readme-work/20260301_070712/` |

![Docs](https://img.shields.io/badge/docs%20state-documentation--first-0ea5e9?style=for-the-badge&logo=readme&logoColor=white)
![Locale sync](https://img.shields.io/badge/locale%20sync-English%20source%20%2F%20i18n-22c55e?style=for-the-badge&logo=googletranslate&logoColor=white)

## 🗂️ Điều hướng nhanh README

| Mục | Liên kết |
|---|---|
| Tổng quan | [Tổng quan](#%E2%98%9B-overview) |
| Tính năng | [Tính năng](#%E2%9C%A8-features) |
| Cấu trúc dự án | [Cấu trúc dự án](#%F0%9F%97%82%EF%B8%8F-project-structure) |
| Điều kiện tiên quyết | [Điều kiện tiên quyết](#%F0%9F%A7%B0-prerequisites) |
| Cài đặt | [Cài đặt](#%F0%9F%9B%A0%EF%B8%8F-installation) |
| Sử dụng | [Sử dụng](#%E2%96%B6%EF%B8%8F-usage) |
| Cấu hình | [Cấu hình](#%F0%9F%A7%A9-configuration) |
| Ví dụ | [Ví dụ](#%F0%9F%A7%AA-examples) |
| Ghi chú phát triển | [Ghi chú phát triển](#%F0%9F%99%82-development-notes) |
| Khắc phục sự cố | [Khắc phục sự cố](#%F0%9F%94%A7-troubleshooting) |
| Lộ trình | [Lộ trình](#%F0%9F%97%BA-roadmap) |
| Đóng góp | [Đóng góp](#%F0%9F%A4%9D-contributing) |
| Hỗ trợ | [Support](#%E2%9D%A4%EF%B8%8F-support) |
| Contact | [Contact](#contact) |
| License | [License](#%F0%9F%93%84-license) |

## 🧭 Tổng quan

`AutoPublication` là một khung tài liệu cấp repository, được chuẩn bị để hỗ trợ hệ thống xuất bản video AI lớn hơn.
Nó giữ `README.md` tiếng Anh làm nguồn dữ liệu chuẩn và đồng bộ bản dịch trong `i18n/README.*.md` thông qua snapshot pipeline.

### Kho này là gì

- Nguồn tài liệu chuẩn cho tài liệu dự án và hướng dẫn cho người đóng góp.
- Một bộ tài liệu đa ngôn ngữ được dùng làm ví dụ về tiến trình phát triển README đồng bộ.
- Kho lưu trữ dữ liệu bằng chứng lịch sử trong `.auto-readme-work/*` ghi lại từng lần chạy pipeline.

### Kho này chưa phải là gì (chưa)

- Chưa phải là ứng dụng xuất bản có thể chạy.
- Chưa phải một gói có script cài đặt hoặc manifest phụ thuộc.
- Chưa triển khai mô hình cấu hình runtime (`.env`, YAML, schema CLI) trong nhánh này.

## ✨ Tính năng

### Khả năng hiện tại

- Tài liệu tiếng Anh chuẩn trong một tệp nguồn duy nhất (`README.md`).
- Khối chọn ngôn ngữ liên kết đến toàn bộ các README bản địa hóa.
- Các artefact auto-README có dấu thời gian (`pipeline-context`, `language-nav-*`, `translation-plan`, `repo-structure-analysis`).
- Bản đồ dự án theo hướng tài liệu để hỗ trợ triển khai theo từng bước.
- Bảng hỗ trợ chuẩn hóa để hiển thị rõ thông tin gây quỹ/đóng góp.

### Khả năng dự kiến

- Điều phối quy trình xuất bản có hỗ trợ AI.
- Tạo và xác thực metadata đa nền tảng.
- Mục tiêu xuất bản có thể cấu hình và quản lý credentials.
- Quy trình phát triển local tái lập được với tests và kiểm tra CI.

## 🗂️ Cấu trúc dự án

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

### Các đường dẫn đáng chú ý

| Đường dẫn | Mục đích |
|---|---|
| `i18n/README.*.md` | README bản địa hóa cho tài liệu hướng người dùng |
| `.auto-readme-work/*/pipeline-context.md` | Ràng buộc chạy và siêu dữ liệu cho mỗi lượt pipeline |
| `.auto-readme-work/*/language-nav-*.md` | Bản đồ ánh xạ ngôn ngữ chuẩn và i18n |
| `.auto-readme-work/*/repo-structure-analysis.md` | Snapshot cấu trúc lịch sử |
| `.auto-readme-work/*/translation-plan.txt` | Phạm vi locale và kế hoạch dịch |
| `.auto-readme-work/*/translated-files.txt` | Danh sách tệp đầu ra từ các lần dịch trước |

## 🧰 Điều kiện tiên quyết

Vì snapshot này là tài liệu-only, không có phụ thuộc runtime nào cho việc chạy ứng dụng.

Để bảo trì, review và đồng bộ bản dịch bạn cần:

- `git`
- Một shell tương thích POSIX (các ví dụ dùng `bash`)
- Một trình chỉnh sửa Markdown
- Tùy chọn: trình xem diff (để rà soát các nhánh bản địa hóa)

## 🛠️ Cài đặt

Trong snapshot này chưa có package có thể cài đặt.

Để làm việc local:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
sed -n '1,140p' README.md
```

## ▶️ Sử dụng

Hiện tại mục đích sử dụng chủ yếu là tài liệu và theo dõi pipeline trace.

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

### Luồng bảo trì được khuyến nghị

1. Cập nhật `README.md` cho các thay đổi cấu trúc hoặc hành vi.
2. Tạo lại bản cập nhật bản dịch khi cần.
3. Kiểm tra các section quan trọng vẫn đồng bộ giữa các file `i18n/`.
4. Giữ các snapshot `.auto-readme-work` nhất quán với luồng làm việc hiện tại.

## 🧩 Cấu hình

Hiện chưa có file cấu hình runtime chính thức nào được commit (`.env`, `config.yml`, schema CLI, v.v. hiện vẫn vắng mặt).

Nếu bạn đang triển khai runtime trong tương lai, nên dùng các mặc định sau:

- Thêm file mẫu cấu hình như `config.sample.yml`.
- Lưu trữ secrets qua `.env` (được loại khỏi repo) hoặc secret manager của hosting.
- Giữ tài liệu và tham chiếu CLI đồng bộ khi thêm key mới.

## 🧪 Ví dụ

### Ví dụ hiện tại (khung scaffold đang có)

```bash
# open full English documentation
cat README.md

# compare localized versions
sed -n '1,90p' i18n/README.de.md
```

### Ví dụ tương lai (dự kiến triển khai)

```bash
# conceptual example; may not exist until runtime is introduced
auto-publication publish \
  --video ./assets/sample.mp4 \
  --config ./config.sample.yml \
  --platform youtube,tiktok
```

## 🛠️ Ghi chú phát triển

- Xử lý thay đổi theo hướng incremental: ưu tiên cải tiến cộng thêm và tránh viết lại phá hủy.
- Giữ `README.md` tiếng Anh làm nền tảng tài liệu chuẩn.
- Dùng các file ngôn ngữ trong `i18n/` làm target đồng bộ rõ ràng.
- Giữ artefacts pipeline (`.auto-readme-work/`) như bằng chứng lịch sử, không chỉnh sửa thủ công như mã production.
- Tránh cam kết hành vi thực thi chưa có sẵn; chỉ mô tả đúng thứ đã tồn tại hiện tại.

### Giả định được nêu trong README này

- Repository vẫn theo hướng documentation-first cho tới khi các module runtime được commit.
- Bản dịch giữ nguyên đồng bộ với các thay đổi cấu trúc có ý nghĩa.
- `.auto-readme-work/` chứa lịch sử append-only theo lượt chạy và không phải bản làm việc chuẩn.

## 🔧 Khắc phục sự cố

### Tôi không thể chạy lệnh `auto-publication`

**Nguyên nhân:** Không có ứng dụng runtime trong snapshot này.

**Cách xử lý:** Dùng repo này cho quy trình tài liệu và chờ khi file triển khai được thêm vào.

### Một README bản địa hóa có vẻ không đồng bộ

**Nguyên nhân:** Bản dịch được cập nhật độc lập với nguồn tiếng Anh.

**Cách xử lý:** Áp dụng cùng thay đổi cấu trúc cho tất cả các file `i18n/README.*.md`, sau đó căn chỉnh lại cách diễn đạt và ví dụ.

### Liên kết trong README trỏ tới chức năng không tồn tại

**Nguyên nhân:** Tài liệu có chứa hành vi đã lên kế hoạch.

**Cách xử lý:** Giữ phần được đánh dấu là dự kiến hoặc thay thế bằng lệnh đã được xác nhận hiện tại.

## 🗺️ Lộ trình

- [ ] Thêm source package và entrypoint runtime.
- [ ] Thêm manifest phụ thuộc và đường dẫn cài đặt.
- [ ] Thêm tích hợp phát hành theo từng nền tảng.
- [ ] Thêm xác thực cấu hình và xử lý secrets.
- [ ] Thêm ví dụ thực thi được và kiểm tra smoke CI.
- [ ] Thêm kiểm tra tự động đối chiếu các README bản địa hóa.
- [ ] Thêm file `LICENSE` và điều khoản cấp phép rõ ràng.

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón khi khung tài liệu này chuyển dần sang giai đoạn triển khai.

```bash
# 1. create a branch
git checkout -b docs/<short-description>


# 2. commit changes
git add README.md i18n/README.fr.md
git commit -m "docs: update English README scaffold"

# 3. push and open PR
git push -u origin docs/<short-description>
```

Danh sách kiểm tra PR đề xuất:

- Giữ `README.md` làm nguồn dữ liệu chuẩn.
- Cập nhật mọi README bản địa hóa đã chỉnh sửa trong `i18n/`.
- Giữ nguyên các section có sẵn khi thêm giá trị mới theo từng bước.
- Keep `.auto-readme-work/*` metadata aligned with the current pass.

## ❤️ Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://camo.githubusercontent.com/24a4914f0b42c6f435f9e101621f1e52535b02c225764b2f6cc99416926004b7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4c617a79696e674172742d3045413545393f7374796c653d666f722d7468652d6261646765266c6f676f3d6b6f2d6669266c6f676f436f6c6f723d7768697465)](https://chat.lazying.art/donate) | [![PayPal](https://camo.githubusercontent.com/d0f57e8b016517a4b06961b24d0ca87d62fdba16e18bbdb6aba28e978dc0ea21/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f50617950616c2d526f6e677a686f754368656e2d3030343537433f7374796c653d666f722d7468652d6261646765266c6f676f3d70617970616c266c6f676f436f6c6f723d7768697465)](https://paypal.me/RongzhouChen) | [![Stripe](https://camo.githubusercontent.com/1152dfe04b6943afe3a8d2953676749603fb9f95e24088c92c97a01a897b4942/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374726970652d446f6e6174652d3633354246463f7374796c653d666f722d7468652d6261646765266c6f676f3d737472697065266c6f676f436f6c6f723d7768697465)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Contact

Dùng mục issue của repository cho các câu hỏi, chỉnh sửa tài liệu và phối hợp đóng góp.

## 📄 License

Hiện chưa có file `LICENSE` trong snapshot này.

Bước tiếp theo đề xuất:

- Thêm file `LICENSE` và cập nhật phần này với mã giấy phép đã chọn.
