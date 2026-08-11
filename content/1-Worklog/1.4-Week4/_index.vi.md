---
title: "Worklog Tuần 4"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.4. </b> "
---

## TUẦN 4 (13/07 - 19/07): THỰC HÀNH DỰ ÁN - PHASE 1: THIẾT LẬP CƠ SỞ HẠ TẦNG S3, DYNAMODB VÀ CẤU HÌNH BẢO MẬT IAM

### 1. Mục tiêu tuần (Objectives)
* Hiện thực hóa giai đoạn 1 của dự án trên môi trường AWS thực tế.
* Tạo S3 Bucket lưu trữ ảnh đầu vào và bảng DynamoDB để lưu trữ log phân tích cảm xúc.
* Phân quyền IAM Roles cho Lambda và IAM User cho ứng dụng Frontend theo đúng chuẩn bảo mật Least Privilege.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Khởi tạo tài nguyên lưu trữ (S3):**
  * Tạo S3 Bucket tên là `my-facial-emotion-recognition-2026` đặt tại vùng `ap-southeast-1` (Singapore) để đảm bảo tốc độ phản hồi nhanh nhất về Việt Nam.
  * Cấu hình Block Public Access để bảo vệ ảnh tải lên của người dùng. Cấu hình mã hóa dữ liệu tĩnh mặc định bằng SSE-S3.
* **Khởi tạo tài nguyên cơ sở dữ liệu (DynamoDB):**
  * Tạo bảng DynamoDB tên là `FaceEmotionLogs`.
  * Khai báo thuộc tính khóa chính (Partition Key) là `LogID` với định dạng chuỗi ký tự (String) để chứa mã UUID ngẫu nhiên.
  * Lập cấu hình chế độ thanh toán là **On-Demand** để tiết kiệm chi phí tối đa trong giai đoạn thử nghiệm.
* **Thiết lập phân quyền bảo mật IAM:**
  * **Tạo IAM User cho Frontend:** Tạo tài khoản IAM `streamlit-s3-uploader`. Tạo Custom Policy chỉ cho phép hành động `s3:PutObject` lên tài nguyên `arn:aws:s3:::my-facial-emotion-recognition-2026/*`. Xuất file Access Key ID và Secret Access Key để tích hợp vào tệp cấu hình của ứng dụng web Streamlit.
  * **Tạo IAM Role cho Lambda:** Tạo một vai trò thực thi (Execution Role) tên là `LambdaEmotionRecognitionRole`. Gắn Policy hệ thống `AWSLambdaBasicExecutionRole` để Lambda có quyền tạo Log Group và ghi Log Stream vào CloudWatch. 
  * Viết một Inline Policy gắn kèm vào Role này để cho phép Lambda thực hiện: `s3:GetObject` trên bucket `my-facial-emotion-recognition-2026/*`, `rekognition:DetectFaces` trên toàn hệ thống, và `dynamodb:PutItem` lên bảng `FaceEmotionLogs`.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Thực hành an toàn thông tin:** Hiểu sâu về cách viết Policy định dạng JSON, nắm vững các thành phần quan trọng trong Policy: `Effect` (Allow/Deny), `Action` (các quyền cụ thể), `Resource` (ARN của tài nguyên cụ thể).
* **Quản lý tài nguyên đám mây:** Thành thạo quy trình thiết lập tài nguyên cơ bản trên hạ tầng AWS.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Khi viết Policy cho Lambda ghi dữ liệu vào DynamoDB, ban đầu em mở rộng quyền `Resource: "*"` dẫn đến cảnh báo bảo mật từ hệ thống cảnh báo tự động của AWS (AWS Security Hub).
* **Giải quyết:** Thực hiện thu hẹp phạm vi tài nguyên bằng cách lấy chính xác địa chỉ ARN của bảng DynamoDB `FaceEmotionLogs` (dạng `arn:aws:dynamodb:ap-southeast-1:account-id:table/FaceEmotionLogs`) để thay thế vào trường Resource của Policy.

### 5. Kết quả đạt được (Outcomes)
* S3 Bucket và bảng DynamoDB được tạo lập sẵn sàng.
* Hệ thống phân quyền bảo mật IAM hoàn tất, đảm bảo không có lỗ hổng rò rỉ quyền hạn chéo giữa các dịch vụ.