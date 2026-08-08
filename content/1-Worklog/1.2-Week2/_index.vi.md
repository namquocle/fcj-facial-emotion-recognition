---
title: "Worklog Tuần 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

## TUẦN 2 (29/06 - 05/07): LƯU TRỮ ĐỐI TƯỢNG VÀ CƠ SỞ DỮ LIỆU TRÊN CLOUD (AMAZON S3 & AMAZON DYNAMODB)

### 1. Mục tiêu tuần (Objectives)
* Tìm hiểu dịch vụ lưu trữ đối tượng Amazon S3 và các chính sách quản lý dữ liệu tĩnh.
* Phân biệt giữa cơ sở dữ liệu quan hệ (SQL) và cơ sở dữ liệu phi quan hệ (NoSQL) trên đám mây.
* Thực hành tạo bảng và truy vấn trên Amazon DynamoDB.
* Chốt ý tưởng đề tài thực tập cá nhân: Hệ thống phân tích cảm xúc khuôn mặt Serverless.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Thực hành với Amazon S3:**
  * Tạo một S3 Bucket với tên duy nhất toàn cầu. Tìm hiểu cấu trúc lưu trữ dạng Key-Value của S3 (trong đó Key là đường dẫn file và Value là nội dung file).
  * Thực hành bật tính năng Versioning để quản lý các phiên bản khác nhau của cùng một tệp tin, giúp khôi phục dữ liệu khi bị xóa nhầm.
  * Cấu hình S3 Lifecycle Rules: Thiết lập tự động chuyển các tệp tin lưu trữ sau 30 ngày sang lớp Standard-IA (Infrequent Access) và tự động xóa vĩnh viễn hoặc chuyển sang Glacier Archive sau 90 ngày nhằm tiết kiệm chi phí lưu trữ tối đa.
  * Thiết lập S3 Bucket Policy để chỉ cho phép các IP thuộc mạng nội bộ của công ty/trường học truy cập đọc dữ liệu (GetObject).
* **Thực hành với Amazon DynamoDB:**
  * Tạo một bảng thử nghiệm trên DynamoDB. Lập cấu hình Partition Key (khóa phân vùng) là `ID` và Sort Key (khóa sắp xếp) là `Timestamp`.
  * Thực hành ghi dữ liệu (PutItem), đọc dữ liệu (GetItem), quét bảng (Scan) và truy vấn tối ưu (Query) bằng AWS Console và AWS CLI.
  * Trải nghiệm cấu hình tự động co giãn dung lượng đọc/ghi (Provisioned Capacity Auto Scaling) và chế độ tính phí theo yêu cầu (On-Demand Capacity).
* **Xây dựng ý tưởng dự án:**
  * Phân tích yêu cầu bài toán: Hệ thống nhận diện cảm xúc cần một nơi lưu trữ ảnh đầu vào ổn định (chọn Amazon S3) và một nơi lưu trữ log phân tích dạng cấu trúc nhẹ, truy vấn nhanh theo ID (chọn DynamoDB).
  * Phác thảo mô hình hoạt động của dự án Serverless.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **S3 Storage Classes:** Hiểu sự khác biệt về chi phí và hiệu năng giữa Standard, Standard-IA, One Zone-IA và Glacier để tối ưu hóa hóa đơn AWS.
* **NoSQL Database:** Nắm rõ đặc điểm schema-less của DynamoDB, hiểu tại sao nó lại phù hợp cho các tác vụ lưu trữ log của ứng dụng web nhờ tốc độ đọc ghi tính bằng mili-giây và khả năng chịu tải cực cao mà không cần quản lý hệ điều hành hay bộ nhớ đệm như RDS SQL thông thường.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Gặp lỗi *Access Denied* khi cố gắng truy cập file ảnh trong S3 Bucket bằng trình duyệt dù đã cấu hình Bucket Policy mở.
* **Giải quyết:** Nhận ra tính năng *Block Public Access* mặc định của S3 đang được bật ở cấp độ tài khoản/bucket, ghi đè lên Bucket Policy. Đã tắt tính năng Block Public Access này và cập nhật lại quyền truy cập chỉ cho phép đọc đối với các ứng dụng nội bộ.

### 5. Kết quả đạt được (Outcomes)
* Nắm giữ toàn bộ kỹ năng thao tác cơ bản với S3 và DynamoDB.
* Báo cáo đề xuất dự án "Serverless Facial Emotion Recognition Analytics Platform" được Mentor duyệt thông qua.