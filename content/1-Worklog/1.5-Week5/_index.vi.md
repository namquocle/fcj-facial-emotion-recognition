---
title: "Worklog Tuần 5"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

## TUẦN 5 (20/07 - 26/07): THỰC HÀNH DỰ ÁN - PHASE 2: PHÁT TRIỂN MÃ NGUỒN AWS LAMBDA VỚI BOTO3 VÀ PYTHON

### 1. Mục tiêu tuần (Objectives)
* Lập trình mã nguồn chính xử lý sự kiện cho AWS Lambda bằng ngôn ngữ Python.
* Sử dụng thư viện SDK `boto3` để kết nối và gọi các dịch vụ Amazon Rekognition và DynamoDB.
* Đảm bảo mã nguồn xử lý tốt các tình huống ngoại lệ như ảnh không chứa khuôn mặt hoặc định dạng dữ liệu không tương thích.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Khởi tạo môi trường phát triển cục bộ và viết code:**
  * Viết mã nguồn chính `lambda_function.py`. Đặt các dòng khởi tạo client `boto3.client('rekognition')` và `boto3.resource('dynamodb')` ở ngoài hàm chính `lambda_handler` để tận dụng cơ chế ấm (warm container), tối ưu hiệu năng chạy.
* **Xử lý logic đọc sự kiện S3:**
  * Lập trình vòng lặp để duyệt qua toàn bộ danh sách `Records` được gửi đến từ sự kiện S3.
  * Sử dụng thư viện giải mã URL để xử lý các ký tự đặc biệt (như khoảng trắng hoặc dấu cộng) trong tên file ảnh (Object Key).
* **Tích hợp gọi dịch vụ Amazon Rekognition:**
  * Viết hàm `analyze_image_with_rekognition` để gọi phương thức `detect_faces` truyền vào tham số hình ảnh nằm trên S3 Bucket. Cấu hình tham số `Attributes=['ALL']` để Rekognition phân tích toàn bộ đặc điểm cảm xúc.
* **Viết hàm xử lý cảm xúc chủ đạo:**
  * Viết hàm `get_dominant_emotion` duyệt qua danh sách các cảm xúc trả về, sử dụng hàm `max()` với khóa là độ tin cậy để tìm ra cảm xúc có giá trị lớn nhất.
  * Xử lý trường hợp ảnh không phát hiện được khuôn mặt nào (`face_count == 0`), thiết lập giá trị cảm xúc mặc định là `NO_FACE_DETECTED` và độ tin cậy bằng `0.0`.
* **Ghi dữ liệu vào DynamoDB:**
  * Sử dụng phương thức `put_item` để lưu bản ghi phân tích vào bảng `FaceEmotionLogs`.
  * *Lưu ý kỹ thuật:* Chuyển đổi giá trị độ tin cậy kiểu float thành kiểu string trước khi lưu vì DynamoDB có cơ chế quản lý kiểu số thực khắt khe có thể gây lỗi lưu trữ.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Lập trình SDK boto3:** Nắm vững cấu trúc gọi hàm và định dạng tham số của boto3 cho dịch vụ S3, Rekognition và DynamoDB.
* **Xử lý ngoại lệ:** Học được cách viết mã nguồn an toàn chống lỗi crash hệ thống khi dữ liệu đầu vào không hợp lệ bằng các khối lệnh `try...except ClientError`.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Khi chạy thử nghiệm, Lambda báo lỗi *KeyError: 'Emotions'* khi xử lý hình ảnh chụp phong cảnh không chứa người.
* **Giải quyết:** Bổ sung khối lệnh kiểm tra số lượng phần tử `FaceDetails` trả về từ Rekognition. Nếu độ dài bằng 0, bỏ qua bước duyệt Emotions và gán ngay nhãn `NO_FACE_DETECTED`.

### 5. Kết quả đạt được (Outcomes)
* File mã nguồn `lambda_function.py` hoàn chỉnh được Deploy lên AWS Lambda Console.
* Code chạy ổn định trên môi trường thử nghiệm và ghi nhận log đầy đủ ra CloudWatch.