---
title: "Worklog Tuần 7"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.7. </b> "
---

## TUẦN 7 (03/08-09/08): XÂY DỰNG GIAO DIỆN FRONTEND BẰNG STREAMLIT VÀ KIỂM THỬ TOÀN DIỆN (END-TO-END TESTING)

### 1. Mục tiêu tuần (Objectives)
* Phát triển giao diện web tương tác trực quan cho người dùng cuối bằng Streamlit.
* Kết nối an toàn ứng dụng web cục bộ với tài nguyên AWS.
* Thực hiện tái cấu trúc mã nguồn (Refactoring) để tối ưu hóa cấu trúc dự án.
* Chạy kiểm thử toàn diện toàn bộ hệ thống từ Frontend đến Backend.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Xây dựng Frontend bằng Streamlit:**
  * Viết mã nguồn giao diện web sử dụng thư viện Streamlit của Python. Thiết kế thanh sidebar hiển thị cấu hình hệ thống (S3 Bucket Name, AWS Region) và vùng upload ảnh kéo thả trực quan.
  * Sử dụng thư viện Pillow để hiển thị ảnh xem trước (preview) kèm theo các thông tin metadata của ảnh (tên tệp, dung lượng KB, kích thước pixel).
  * Viết nút bấm "🚀 Upload to S3 & Analyze" để đọc ảnh dưới dạng bytes và tải lên S3 thông qua thư viện `boto3`.
* **Cấu hình bảo mật và nạp biến môi trường:**
  * Cài đặt thư viện `python-dotenv`. Thiết lập tệp `.env` để lưu trữ `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, và `S3_BUCKET_NAME`.
  * Cập nhật code để tự động chạy `load_dotenv()` khi ứng dụng web khởi động, tránh việc hardcode khóa bảo mật trực tiếp trong file chạy chính.
* **Tái cấu trúc mã nguồn thành dạng Modular:**
  * Nhận thấy file `app.py` và `lambda_function.py` quá lớn, khó đọc, tôi đã tiến hành chia nhỏ thành các tệp tin đơn nhiệm:
    * `config.py` chứa cấu hình nạp từ `.env`.
    * `validation.py` chứa logic xác thực file.
    * `s3_service.py` chứa logic khởi tạo và tải file lên S3.
    * `ui_components.py` chứa mã nguồn giao diện Streamlit.
    * `app.py` đóng vai trò là file chạy chính siêu gọn nhẹ.
    * Phía Lambda cũng được tách thành `rekognition_service.py` và `dynamodb_service.py`.
* **Kiểm thử toàn diện hệ thống (End-to-End Testing):**
  * Chạy ứng dụng Streamlit trên localhost. Tạo và sử dụng một ảnh chân dung của một người phụ nữ đang cười tươi để làm mẫu thử nghiệm đầu vào.
  * Tiến hành nhấn upload trên web -> Xác nhận ảnh được đẩy lên S3 -> Hệ thống AWS tự chạy Lambda phân tích -> Kết quả lưu thành công vào bảng DynamoDB.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Modular Programming:** Hiểu cách thiết kế mã nguồn sạch, tách biệt các tầng giao diện (UI) và tầng xử lý logic (Service) để tăng tính tái sử dụng và dễ viết kiểm thử đơn vị.
* **Kỹ năng gỡ lỗi tích hợp:** Hiểu được cách phân tích chuỗi lỗi khi xảy ra lỗi ở giao tiếp giữa môi trường cục bộ (Local app) và đám mây (S3 API).

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn 1:** Khi upload ảnh từ Streamlit, giao diện báo lỗi `Upload Failed: AWS credentials not found`.
  * *Giải quyết:* Nhận ra ứng dụng chưa load tệp cấu hình `.env` chứa Access Key. Đã cài đặt `python-dotenv`, import và chạy `load_dotenv()` ở đầu tệp `app.py`.
* **Khó khăn 2:** Tiếp tục gặp lỗi `AccessDenied` từ AWS khi đẩy ảnh lên.
  * *Giải quyết:* Do tài khoản IAM User `streamlit-s3-uploader` chưa được cấp quyền `s3:PutObject` trên S3 Bucket mới. Đã vào AWS IAM Console, thêm Inline Policy cho phép hành động `PutObject` trên tài nguyên bucket đích và khởi động lại server.
* **Khó khăn 3:** Lỗi cài đặt Pillow trên môi trường chạy Python 3.14.3 cục bộ do phiên bản cũ `Pillow==10.3.0` trong `requirements.txt` không hỗ trợ bản Python mới này.
  * *Giải quyết:* Nâng cấp Pillow lên bản `12.3.0` để tương thích hoàn toàn.

### 5. Kết quả đạt được (Outcomes)
* Giao diện frontend Streamlit chạy mượt mà tại cổng 8501.
* Hệ thống chạy thử nghiệm thành công 100% end-to-end từ giao diện web đến cơ sở dữ liệu cloud.