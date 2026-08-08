---
title : "Dọn dẹp tài nguyên"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

# 5.6. Dọn dẹp tài nguyên

Để tránh phát sinh chi phí ngoài ý muốn trên tài khoản AWS và giữ cho môi trường cloud luôn sạch sẽ, bạn cần xóa bỏ toàn bộ các tài nguyên đã khởi tạo trong workshop này sau khi hoàn thành kiểm thử.

---

## Bước 1: Dừng ứng dụng Web Streamlit

1. Truy cập vào terminal cục bộ đang chạy ứng dụng Streamlit.
2. Nhấn tổ hợp phím `Ctrl + C` để dừng máy chủ web.
3. Đóng tab giao diện ứng dụng trên trình duyệt.

---

## Bước 2: Làm rỗng và Xóa S3 Bucket

S3 bucket không thể xóa nếu nó còn chứa dữ liệu bên trong.

1. Mở **Amazon S3 Console**.
2. Chọn bucket của bạn (Ví dụ: `my-facial-emotion-recognition-<hau-to-duy-nhat>`).
3. Chọn nút **Empty** (Làm rỗng).
![Picture_62](/images/5-Workshop/62.png)
4. Nhập `permanently delete` vào ô văn bản để xác nhận, sau đó nhấp **Empty**.
![Picture_63](/images/5-Workshop/63.png)
5. Sau khi thùng chứa trống, quay lại danh sách bucket, chọn bucket cần xóa và nhấp **Delete** (Xóa).
![Picture_64](/images/5-Workshop/64.png)
6. Nhập chính xác tên của bucket để xác nhận và nhấp **Delete bucket**.
![Picture_65](/images/5-Workshop/65.png)

---

## Bước 3: Xóa bảng Amazon DynamoDB

1. Mở **Amazon DynamoDB Console**.
2. Tại menu bên trái, nhấp chọn **Tables** (Các bảng).
![Picture_66](/images/5-Workshop/66.png)
3. Tích chọn bảng `FaceEmotionLogs`.
4. Nhấp vào nút **Delete** ở góc trên bên phải.
![Picture_67](/images/5-Workshop/67.png)
5. Xác nhận bằng cách nhập `delete` vào ô nhắc, sau đó nhấp **Delete**.
![Picture_68](/images/5-Workshop/68.png)

---

## Bước 4: Xóa AWS Lambda Function

1. Mở **AWS Lambda Console**.
2. Tìm hàm `FaceEmotionRecognitionHandler`.
3. Tích chọn ô vuông bên cạnh hàm, chọn menu thả xuống **Actions** và chọn **Delete**.
![Picture_69](/images/5-Workshop/69.png)
4. Chọn **Delete** trong hộp thoại xác nhận.
![Picture_70](/images/5-Workshop/70.png)

---

## Bước 5: Dọn dẹp IAM Policies & Roles

1. Mở **IAM Console**.
![Picture_71](/images/5-Workshop/71.png)
2. Chọn **Roles** (Vai trò) ở thanh điều hướng bên trái. Tìm kiếm và chọn vai trò `workshop-lambda-role`, chọn **Delete**. Xác nhận bằng cách nhập tên vai trò.
![Picture_72](/images/5-Workshop/72.png)
3. Chọn **Policies** (Chính sách) ở thanh điều hướng bên trái. Tìm kiếm chính sách `workshop-lambda-policy`, chọn **Actions** -> **Delete** và bấm xác nhận xóa.
![Picture_73](/images/5-Workshop/73.png)
![Picture_74](/images/5-Workshop/74.png)

---

{{% notice note %}}
**Lưu ý về Chi phí AWS:**
Việc xóa bỏ tài nguyên sẽ ngay lập tức ngăn chặn việc tích lũy dung lượng sử dụng trên tài khoản của bạn. Mặc dù các dịch vụ như S3, DynamoDB và Lambda có hạn mức Free Tier rất rộng rãi (Ví dụ: S3 cho phép 5GB lưu trữ, DynamoDB cho phép 25GB, Lambda cho phép 1 triệu yêu cầu miễn phí mỗi tháng), việc giữ các tài nguyên không sử dụng vẫn có thể phát sinh chi phí ngoài ý muốn khi tài khoản của bạn hết thời gian 12 tháng Free Tier. Hãy luôn duy trì thói quen dọn dẹp tài nguyên sau khi thực hành.
{{% /notice %}}
