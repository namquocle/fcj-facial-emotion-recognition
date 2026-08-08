---
title: "Worklog Tuần 8"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

## TUẦN 8 (10/08-15/08): HOÀN THIỆN BÁO CÁO KỸ THUẬT SONG NGỮ, HƯỚNG DẪN DỌN DẸP TÀI NGUYÊN VÀ TỔNG KẾT KHÓA THỰC TẬP

### 1. Mục tiêu tuần (Objectives)
* Hoàn thiện báo cáo thực tập chi tiết mô tả đầy đủ kiến trúc, mã nguồn và kết quả kiểm thử dự án.
* Soạn thảo tài liệu hướng dẫn dọn dẹp (Clean-up Guide) để tránh phát sinh chi phí ngoài ý muốn trên AWS.
* Tổng kết toàn bộ kết quả học tập và kỹ năng đạt được sau 8 tuần tham gia chương trình AWS First Cloud Journey.

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Viết Báo cáo kỹ thuật song ngữ:**
  * Soạn thảo tài liệu mô tả chi tiết bằng tiếng Việt và tiếng Anh. Trình bày rõ ràng sơ đồ kiến trúc hệ thống, cấu hình chi tiết của S3, Lambda, DynamoDB, các chính sách bảo mật IAM được áp dụng và cấu trúc mã nguồn modular.
  * Đính kèm các hình ảnh minh chứng kiểm thử thành công, bao gồm ảnh mẫu đầu vào và ảnh chụp kết quả log ghi nhận trên bảng DynamoDB.
* **Xây dựng Tài liệu Hướng dẫn dọn dẹp tài nguyên (Clean-up Guide):**
  * Soạn thảo các bước cụ thể để xóa bỏ các tài nguyên tránh phát sinh chi phí sau khi kết thúc dự án:
    1. Vào S3 bucket, chọn tất cả các tệp ảnh và thực hiện xóa vĩnh viễn (permanently delete), sau đó xóa bỏ bản thân S3 Bucket.
    2. Vào DynamoDB, chọn bảng `FaceEmotionLogs` và tiến hành xóa bảng để dừng tính phí lưu trữ dữ liệu.
    3. Vào Lambda, xóa hàm `FaceEmotionRecognizer` để giải phóng dung lượng lưu trữ code.
    4. Vào CloudWatch Logs, xóa các Log Groups của Lambda để dừng tính phí ghi nhật ký log.
    5. Vào IAM, xóa User `streamlit-s3-uploader` và Role `LambdaEmotionRecognitionRole` để thu hồi toàn bộ quyền truy cập.
* **Tổng kết khóa thực tập:**
  * Xem lại tiến độ công việc, viết lời cảm ơn đến các Mentor hỗ trợ trong suốt chương trình. Chuẩn bị slide thuyết trình demo sản phẩm để chuẩn bị báo cáo trước hội đồng đánh giá thực tập.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **Viết tài liệu kỹ thuật:** Kỹ năng trình bày báo cáo chuyên nghiệp, mạch lạc, dễ hiểu cho cả đối tượng kỹ thuật và quản lý.
* **Quản trị chi phí đám mây (FinOps):** Hiểu rõ tầm quan trọng của việc quản lý vòng đời tài nguyên trên cloud, hình thành thói quen dọn dẹp tài nguyên thừa để tối ưu chi phí hạ tầng.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Việc dọn dẹp S3 Bucket đôi khi bị lỗi nếu bucket vẫn còn chứa các phiên bản cũ của file ảnh (do bật tính năng Versioning ở Tuần 2).
* **Giải quyết:** Viết hướng dẫn chi tiết yêu cầu người dùng phải tích chọn xóa cả "Objects" và các "Object versions" trước khi thực hiện xóa bucket hoàn toàn.

### 5. Kết quả đạt được (Outcomes)
* Báo cáo thực tập hoàn chỉnh dài hơn 15 trang Word được hoàn thiện sạch sẽ.
* Tài liệu hướng dẫn dọn dẹp rõ ràng, chi tiết.
* Nhận chứng nhận hoàn thành khóa học thực tập Cloud Computing từ chương trình AWS First Cloud Journey.