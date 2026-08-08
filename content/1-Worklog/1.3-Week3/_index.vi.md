---
title: "Worklog Tuần 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

## TUẦN 3 (06/07 - 12/07): TÌM HIỂU CHUYÊN SÂU KIẾN TRÚC SERVERLESS (AWS LAMBDA) VÀ AMAZON REKOGNITION

### 1. Mục tiêu tuần (Objectives)
* Nghiên cứu sâu về triết lý Serverless và cách thức hoạt động của AWS Lambda.
* Khám phá năng lực của dịch vụ thị giác máy tính Amazon Rekognition.
* Thiết kế sơ đồ kiến trúc chi tiết cho dự án và xác định luồng dữ liệu (Dataflow).

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Nghiên cứu AWS Lambda:**
  * Học cách cấu hình RAM (từ 128MB đến 10GB) cho Lambda, hiểu việc tăng RAM sẽ tự động tăng sức mạnh CPU tương ứng.
  * Tìm hiểu về cơ chế kích hoạt (Triggers) từ các dịch vụ khác như S3, API Gateway, DynamoDB Streams.
  * Học cách xử lý vấn đề Cold Start bằng cách cấu hình Provisioned Concurrency hoặc tối ưu hóa kích thước gói code (package size).
* **Nghiên cứu Amazon Rekognition:**
  * Sử dụng công cụ AWS Console demo để thử nghiệm tính năng Facial Analysis (phân tích khuôn mặt).
  * Đọc tài liệu API của Amazon Rekognition để hiểu cấu trúc yêu cầu (Request Body) chứa đường dẫn S3 của ảnh và cấu trúc phản hồi (Response Body) dạng JSON chứa mảng `FaceDetails`.
  * Nghiên cứu cách lấy thông tin cảm xúc: Rekognition trả về danh sách cảm xúc gồm 8 loại trạng thái kèm theo mức độ phần trăm tin cậy. Nhiệm vụ của lập trình viên là viết code để tìm ra cảm xúc có giá trị lớn nhất.
* **Thiết kế sơ đồ kiến trúc hệ thống:**
  * Sử dụng công cụ Draw.io để vẽ sơ đồ kiến trúc hệ thống Serverless hoàn chỉnh.
  * Xác định rõ: Khi người dùng tương tác với frontend, ảnh được đưa thẳng lên S3 -> S3 phát sinh sự kiện ObjectCreated -> Lambda bắt sự kiện này -> Gọi Rekognition xử lý ảnh -> Lưu kết quả vào DynamoDB.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Tư duy Serverless:** Hiểu được lợi ích lớn nhất của Serverless là khả năng tự động co giãn theo lượng truy cập (Auto-scaling) từ 0 đến hàng ngàn request mà không cần người quản trị can thiệp, cùng mô hình trả tiền theo lượng sử dụng thực tế (Pay-as-you-go).
* **Khai phá AI/ML:** Hiểu cách đọc và xử lý kết quả trả về từ một mô hình học máy thị giác máy tính phức tạp thông qua định dạng chuẩn JSON.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Thiết kế ban đầu sử dụng Lambda để nhận ảnh trực tiếp từ Frontend rồi mới tải lên S3. Tuy nhiên, cách này làm chậm thời gian phản hồi của Lambda và dễ bị lỗi timeout hoặc vượt quá giới hạn dung lượng payload của Lambda (6MB cho lời gọi đồng bộ).
* **Giải quyết:** Thay đổi thiết kế kiến trúc sang hướng sự kiện (Event-driven): Frontend sẽ tải ảnh trực tiếp lên S3 trước, sau đó S3 mới kích hoạt Lambda xử lý bất đồng bộ. Cách này giúp hệ thống chịu tải tốt hơn và giảm thiểu thời gian chạy của Lambda.

### 5. Kết quả đạt được (Outcomes)
* Hoàn thiện bản vẽ sơ đồ kiến trúc hệ thống Serverless Facial Emotion Recognition.
* Nắm chắc lý thuyết triển khai Lambda và gọi API Rekognition.