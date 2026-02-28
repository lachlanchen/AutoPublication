[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)


# AutoPublication

![Status](https://img.shields.io/badge/status-scaffold-1f6feb)
![Docs](https://img.shields.io/badge/docs-readme_in_progress-2ea043)
![i18n](https://img.shields.io/badge/i18n-planned-f59e0b)
![Stage](https://img.shields.io/badge/stage-documentation_first-0ea5e9)
![Repo Focus](https://img.shields.io/badge/focus-AI_video_publishing-8b5cf6)

> Tự động xuất bản video bằng các công cụ AI.

## Tổng quan

`AutoPublication` được định hướng để tự động hóa quy trình xuất bản video bằng các công cụ có hỗ trợ AI.

Ở giai đoạn hiện tại của kho mã, dự án vẫn đang ở mức khung sườn (scaffold) với tài liệu và các tạo tác của pipeline sinh README; chưa có mã nguồn ứng dụng hay điểm vào runtime nào được commit.

README này đóng vai trò là bản tiếng Anh chuẩn (canonical base) và được tổ chức để hỗ trợ mở rộng triển khai trong tương lai mà không làm mất đi mục tiêu hiện tại của dự án.

| Khu vực | Trạng thái hiện tại |
|---|---|
| Triển khai | Giai đoạn scaffold (chưa commit ứng dụng runtime) |
| Tài liệu | Đã có README gốc chuẩn ở thư mục gốc |
| Tài liệu đa ngôn ngữ | Đã định nghĩa các ngôn ngữ mục tiêu trong `i18n/` |
| Tạo tác pipeline | Có trong `.auto-readme-work/` |

## Tính năng

### Khả năng hiện có

- README gốc chuẩn để định nghĩa dự án.
- Các README đa ngôn ngữ mục tiêu được định sẵn trong `i18n/`.
- Ngữ cảnh pipeline README để tạo tài liệu lặp lại một cách nhất quán.

### Khả năng dự kiến (suy ra từ tên dự án và mô tả hiện tại)

- Điều phối tự động quy trình xuất bản video.
- Hỗ trợ AI cho việc chuẩn bị metadata/nội dung.
- Tích hợp có thể cấu hình cho các nền tảng đích xuất bản.

## Cấu trúc dự án

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

### Các đường dẫn đáng chú ý

| Đường dẫn | Mục đích |
|---|---|
| `README.md` | Định nghĩa dự án chuẩn bằng tiếng Anh. |
| `i18n/` | Thư mục đích cho các file README đã dịch. |
| `.auto-readme-work/20260228_230008/pipeline-context.md` | Ngữ cảnh và ràng buộc của lần chạy Auto-README. |
| `.auto-readme-work/20260228_230008/translation-plan.txt` | Ánh xạ ngôn ngữ và file đích. |
| `.gitignore` | Mẫu ignore thiên về Python (chỉ mang tính gợi ý; hiện chưa có file ứng dụng Python). |

## Điều kiện tiên quyết

Vì chưa có file triển khai, các điều kiện tiên quyết cho runtime hiện chỉ là giả định.

### Mốc cơ sở đã được ghi nhận

- `git`
- Shell tương thích POSIX (ví dụ dùng `bash`)

### Tín hiệu stack có khả năng dùng trong tương lai (chỉ từ `.gitignore`)

- Có thể sau này sẽ cần toolchain Python.

## Cài đặt

Ở giai đoạn này, chưa có gói cài đặt hoặc tệp khai báo phụ thuộc.

Clone repo và truy cập thư mục:

```bash
git clone <your-repo-url> AutoPublication
cd AutoPublication
```

## Sử dụng

Hiện chưa có lệnh chạy ứng dụng.

Cách sử dụng thực tế lúc này là phục vụ luồng tài liệu và chuẩn bị repository:

```bash
# Inspect repository structure
ls -la

# Inspect i18n targets
ls -la i18n
```

Khi phần triển khai được bổ sung, phần này nên được mở rộng bằng các lệnh chạy cụ thể và ví dụ end-to-end thực tế.

## Cấu hình

Hiện chưa có file cấu hình chính thức (như `.env.example`, `config.yaml`, hoặc cờ CLI).

Các bổ sung nên có trong tương lai:
- Mẫu môi trường được tài liệu hóa (cho API key/token).
- Cấu hình xuất bản theo từng nền tảng.
- Thiết lập chọn nhà cung cấp/model AI.

## Ví dụ

### Ví dụ hiện tại (Scaffold)

Dùng repository như một đường cơ sở tài liệu:

```bash
# Read canonical project intent
cat README.md
```

### Ví dụ tương lai (Mục tiêu)

Quy trình giả định trong tương lai (chỉ là placeholder):

```bash
# Placeholder example for future implementation
# python -m autopublication run --video ./assets/demo.mp4 --platform youtube
```

## Ghi chú phát triển

- Repository hiện chưa chứa mã nguồn thực thi.
- Việc tạo README có vẻ được điều khiển bằng pipeline thông qua các file trong `.auto-readme-work/`.
- Dòng điều hướng ngôn ngữ được đặt tập trung ở đầu README này để hỗ trợ tính tương đương đa ngôn ngữ.

Các mốc triển khai tiếp theo được đề xuất:
1. Thêm thư mục mã nguồn (ví dụ `src/` hoặc `autopublication/`).
2. Thêm tệp khai báo phụ thuộc (`pyproject.toml` hoặc tương đương).
3. Thêm entrypoint thực thi và bộ test tối thiểu.
4. Thêm CI để xác thực lint/test/docs.

## Khắc phục sự cố

### "Tôi không thể chạy dự án"

Nguyên nhân:
- Hiện chưa commit các file ứng dụng runtime hoặc entrypoint.

Cách xử lý:
- Xem repository như scaffold/tài liệu cho đến khi mã nguồn được thêm vào.

### "Có liên kết README ngôn ngữ nhưng thiếu file"

Nguyên nhân:
- `i18n/` có tồn tại, nhưng các file README bản địa hóa chưa được tạo trong snapshot này.

Cách xử lý:
- Tạo/thêm các file đích được liệt kê trong `.auto-readme-work/20260228_230008/translation-plan.txt`.

## Lộ trình

- [ ] Thêm bản triển khai chạy được đầu tiên cho xuất bản tự động.
- [ ] Định nghĩa tích hợp nhà cung cấp và schema cấu hình.
- [ ] Thêm hướng dẫn thiết lập cục bộ có thể tái lập.
- [ ] Thêm test và pipeline CI.
- [ ] Phát hành bộ README đa ngôn ngữ đầy đủ trong `i18n/`.

## Đóng góp

Hoan nghênh đóng góp khi dự án chuyển từ scaffold sang triển khai.

Quy trình đóng góp được gợi ý:

```bash
# 1) Create a branch
git checkout -b feat/<short-description>

# 2) Commit your changes
git add .
git commit -m "feat: <describe change>"

# 3) Push and open a PR
git push -u origin feat/<short-description>
```

Vui lòng bao gồm:
- Mô tả rõ vấn đề và phạm vi.
- Các bước tái hiện được cho mọi thay đổi hành vi.
- Cập nhật tài liệu cho lệnh/cấu hình mới.

## Hỗ trợ

Hiện repository này chưa công bố kênh quyên góp/tài trợ.

Nếu các liên kết hỗ trợ được thêm sau này, chúng nên được liệt kê tại đây và đồng bộ trên các biến thể i18n.

## Giấy phép

Hiện chưa có file giấy phép trong snapshot repository này.

Giả định:
- Chưa khai báo giấy phép.

Bước tiếp theo được đề xuất:
- Thêm file `LICENSE` và cập nhật mục này để tham chiếu rõ ràng.
