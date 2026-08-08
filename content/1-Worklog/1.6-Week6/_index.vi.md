---
title: "Worklog Tuần 6"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.6. </b> "
---

## TUẦN 6 (27/07 - 02/08): THỰC HÀNH DỰ ÁN - PHASE 3: CẤU HÌNH S3 EVENT TRIGGER VÀ KIỂM THỬ KHẢ NĂNG TÍCH HỢP TỰ ĐỘNG

### 1. Mục tiêu tuần (Objectives)
* Thiết lập cấu hình tự động kích hoạt Lambda khi có đối tượng mới được đưa lên S3.
* Đảm bảo luồng dữ liệu chạy tự động từ S3 -> Lambda -> DynamoDB hoạt động mượt mà.
* Thực hiện giám sát và debug hệ thống thông qua AWS CloudWatch Logs.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Cấu hình S3 Event Trigger trên AWS Console:**
  * Vào giao diện cấu hình của Lambda Function `FaceEmotionRecognizer` -> Thêm Trigger mới là **S3**.
  * Chọn S3 Bucket tương ứng. Đặt Event type là `All object create events` (bao gồm PUT, POST, COPY).
  * Điền cấu hình bộ lọc đường dẫn **Prefix** là `uploads/` để Lambda chỉ chạy khi có file ảnh tải lên thư mục này. Tránh kích hoạt Lambda vô hạn khi có các tệp tin khác được tạo ra ở ngoài.
* **Cấu hình cấu trúc biến môi trường:**
  * Tạo biến môi trường `DYNAMODB_TABLE_NAME` cho Lambda và gán giá trị là `FaceEmotionLogs`. Thay đổi dòng code đọc tên bảng thành `os.environ.get('DYNAMODB_TABLE_NAME')`.
* **Tiến hành thử nghiệm tích hợp:**
  * Tải thủ công các ảnh mẫu có khuôn mặt biểu cảm khác nhau (vui, buồn, giận dữ) lên thư mục `uploads/` của S3 Bucket bằng trình quản lý S3 Console.
  * Truy cập dịch vụ **CloudWatch Logs**, tìm đến Log Group tương ứng với Lambda để xem chi tiết luồng xử lý: kiểm tra log in ra tên ảnh, số lượng khuôn mặt, và kết quả cảm xúc phân tích được.
  * Mở bảng **DynamoDB**, chọn tab Explore table items để xác nhận các bản ghi log phân tích đã xuất hiện đầy đủ trong bảng với đầy đủ thông tin thời gian thực.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Event-Driven Architecture:** Hiểu rõ cơ chế kiến trúc hướng sự kiện, hệ thống tự động phản hồi mà không cần thiết lập cơ chế thăm dò (polling) liên tục giúp tối ưu tài nguyên tính toán.
* **Giám sát hệ thống:** Kỹ năng phân tích log, đọc thông báo lỗi từ CloudWatch để xác định vị trí dòng code bị lỗi trong Lambda.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Lambda bị kích hoạt lặp đi lặp lại nhiều lần cho cùng một tệp tin ảnh khi tải lên, gây lãng phí tài nguyên và trùng lặp bản ghi trong DynamoDB.
* **Giải quyết:** Phát hiện ra cấu hình S3 trigger ban đầu không để Prefix, làm cho mọi hành động tạo file trong bucket đều kích hoạt Lambda. Đã giới hạn lại Prefix là `uploads/` để khoanh vùng sự kiện kích hoạt chính xác.

### 5. Kết quả đạt được (Outcomes)
* Xây dựng thành công luồng tự động hóa Serverless hoàn chỉnh ở backend.
* Log dữ liệu được lưu trữ tự động vào DynamoDB trong vòng chưa đầy 2 giây kể từ khi ảnh xuất hiện trên S3.