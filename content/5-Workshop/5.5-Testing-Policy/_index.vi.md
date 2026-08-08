---
title : "Kiểm thử & Chính sách"
date : 2024-01-01 
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---
# 5.5. Kiểm thử & Xác minh Hệ thống

Trong phần này, bạn sẽ thực hiện kiểm thử toàn trình (End-to-End) toàn bộ pipeline nhận diện cảm xúc khuôn mặt không máy chủ để đảm bảo từng dịch vụ liên kết hoạt động chính xác.

---

## Bước 1: Chạy và Thử nghiệm Giao diện Streamlit

1. Khởi chạy ứng dụng cục bộ của bạn nếu nó chưa hoạt động:
   ```bash
   streamlit run app.py
   ```
2. Mở trình duyệt web và truy cập địa chỉ `http://localhost:8501`.
![Picture_50](/images/5-Workshop/50.png)
3. Chuẩn bị một hình ảnh thử nghiệm có chứa khuôn mặt rõ ràng (ví dụ: ảnh một người đang cười vui vẻ).
4. Kéo thả hoặc duyệt chọn hình ảnh đó vào vùng tải lên của ứng dụng Streamlit.
5. Kiểm tra thông tin hình ảnh hiển thị trong phần **File Info** và ảnh xem trước hiển thị trong phần **Preview**.
6. Nhấp vào nút màu xanh **🚀 Upload to S3 & Analyze**.
![Picture_51](/images/5-Workshop/51.png)
7. Đảm bảo ứng dụng hiển thị thông báo thành công: `✅ Image uploaded successfully!` và xuất hiện hiệu ứng bong bóng trên màn hình.
![Picture_52](/images/5-Workshop/52.png)

---

## Bước 2: Xác minh Hình ảnh tải lên Amazon S3

Đảm bảo rằng ứng dụng Streamlit đã đẩy tệp ảnh thành công lên thùng chứa S3 của bạn.

1. Truy cập **Amazon S3 Console**.
2. Nhấp vào tên bucket của bạn (Ví dụ: `my-facial-emotion-recognition-<hau-to-duy-nhat>`).
![Picture_53](/images/5-Workshop/53.png)
3. Điều hướng vào thư mục: `uploads/` -> `<Ngày-Hiện-Tại> (định dạng YYYY-MM-DD)/`.
![Picture_54](/images/5-Workshop/54.png)
![Picture_55](/images/5-Workshop/55.png)
4. Xác nhận rằng tệp ảnh bạn vừa tải lên đã xuất hiện trong danh sách.
![Picture_56](/images/5-Workshop/56.png)

---

## Bước 3: Kiểm tra Logs của Hàm Lambda (AWS CloudWatch)

Xác minh rằng sự kiện tải ảnh lên S3 đã kích hoạt hàm Lambda và Lambda xử lý ảnh thành công.

1. Truy cập **AWS Lambda Console** và chọn hàm của bạn: `FaceEmotionRecognitionHandler`.
![Picture_57](/images/5-Workshop/57.png)
2. Chọn tab **Monitor** (Giám sát).
3. Nhấp vào nút **View CloudWatch logs** (Xem log trên CloudWatch - tab mới sẽ mở ra nhóm logs tương ứng).
![Picture_58](/images/5-Workshop/58.png)
4. Chọn luồng ghi log mới nhất (Log Stream).
5. Xác minh các dòng thông báo log cho thấy pipeline chạy đúng luồng:
   ```text
   INFO Lambda invoked. Event: {"Records": [...]}
   INFO Processing image: s3://my-facial-emotion-recognition-.../uploads/2026-07-27/test_face.png
   INFO Calling Rekognition for s3://my-facial-emotion-recognition-...
   INFO Rekognition detected 1 face(s) in test_face.png
   INFO Top emotion for test_face.png: HAPPY (99.54%)
   INFO Saved record LogID=... to DynamoDB table FaceEmotionLogs
   ```

---

## Bước 4: Kiểm tra Dữ liệu Phân tích trong Amazon DynamoDB

Xác nhận siêu dữ liệu phân tích cảm xúc khuôn mặt đã được lưu thành công vào bảng NoSQL DynamoDB.

1. Truy cập **Amazon DynamoDB Console**.
2. Ở bảng điều hướng bên trái, chọn **Explore items** (Khám phá các mục).
![Picture_59](/images/5-Workshop/59.png)
3. Chọn bảng dữ liệu của bạn: `FaceEmotionLogs`.
![Picture_60](/images/5-Workshop/60.png)
4. Nhấp vào tìm kiếm để hiển thị toàn bộ bản ghi hiện có trong bảng.
5. Xác minh rằng một hàng dữ liệu mới đã được thêm vào chứa các trường sau:
   - `LogID` (một chuỗi UUID ngẫu nhiên duy nhất)
   - `Timestamp` (thời gian ghi log định dạng ISO-8601 UTC)
   - `ImageName` (tên của tệp ảnh được tải lên)
   - `FaceCount` (số lượng khuôn mặt phát hiện được trong ảnh)
   - `TopEmotion` (Cảm xúc chủ đạo phát hiện được, ví dụ: `HAPPY`, `SAD`, `ANGRY`)
   - `Confidence` (Điểm số phần trăm độ tin cậy của cảm xúc chủ đạo đó)
![Picture_61](/images/5-Workshop/61.png)
