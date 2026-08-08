---
title: "Tự đánh giá"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---
# 6. Tự đánh giá bản thân

Mục này chứa nội dung tự đánh giá cá nhân của tôi về quá trình học tập và làm việc trong chương trình thực tập **AWS Workforce Bootcamp - First Cloud AI Journey**. Tài liệu bao gồm các kiến thức đã tích lũy, kết quả đạt được, tiêu chí tự đánh giá, điểm mạnh, điểm cần cải thiện và kế hoạch hành động trong tương lai.

---

## 🏆 Những kết quả đã đạt được

### 1. Kiến thức chuyên môn & Công nghệ tích lũy
- **Điện toán đám mây & Kiến trúc Serverless:** Hiểu sâu sắc cách vận hành của các dịch vụ cốt lõi trên AWS. Xây dựng thành công pipeline xử lý hướng sự kiện không máy chủ (serverless event-driven pipeline) kết hợp **Amazon S3** (Lưu trữ đối tượng), **AWS Lambda** (Tính toán serverless) và **Amazon DynamoDB** (Cơ sở dữ liệu NoSQL).
- **Tích hợp Trí tuệ nhân tạo (AI/ML):** Tích lũy kinh nghiệm thực tế về Thị giác máy tính (Computer Vision) thông qua tích hợp dịch vụ **Amazon Rekognition** (gọi API `DetectFaces`) để phát hiện cấu trúc khuôn mặt, phân tích các chỉ số cảm xúc và xác định cảm xúc chủ đạo.
- **Phát triển ứng dụng Web UI:** Làm chủ việc xây dựng giao diện người dùng hiện đại, trực quan bằng thư viện **Streamlit** (Python), tích hợp tính năng tải ảnh trực tiếp lên Cloud qua thư viện **boto3** SDK.
- **Thiết kế mã nguồn Modular:** Tổ chức lại cấu trúc mã nguồn từ dạng nguyên khối (monolithic) sang các module đơn nhiệm (single-responsibility), giúp nâng cao tính bảo trì, xác thực dữ liệu và dễ dàng kiểm tra lỗi.

### 2. Kỹ năng mềm thu hoạch được
- **Viết tài liệu kỹ thuật (Documentation):** Hoàn thiện báo cáo kỹ thuật và tài liệu hướng dẫn workshop chi tiết dưới dạng song ngữ (Anh/Việt), nâng cao khả năng diễn giải các luồng kỹ thuật đám mây phức tạp một cách rõ ràng.
- **Giải quyết vấn đề (Troubleshooting):** Giải quyết thành công các lỗi phát sinh trong quá trình tích hợp hệ thống như xung đột thư viện môi trường ảo, kết nối thông tin xác thực AWS cục bộ và định dạng kiểu dữ liệu trên DynamoDB (chuyển đổi số thực sang chuỗi).
- **Quản lý thời gian:** Hoàn thành tốt các mốc công việc đề ra theo đúng lộ trình thực tập hàng tuần, ghi nhận nhật ký công việc (Worklog) một cách tuần tự.

---

## 📊 Tiêu chí tự đánh giá

Bảng dưới đây thể hiện mức độ tự đánh giá của tôi đối với các hoạt động chính trong suốt kỳ thực tập:

| Tiêu chí | Mức độ hoàn thành | Điểm số (1-5) | Ghi chú / Đánh giá chi tiết |
| :--- | :---: | :---: | :--- |
| **Tiến độ công việc** (Worklog & Proposal) | 95% | 4.8 / 5.0 | Hoàn thành đúng hạn toàn bộ các mục tiêu đặt ra theo tuần. Bản đề xuất dự án (Proposal) được xây dựng bài bản, cấu trúc rõ ràng và bám sát yêu cầu chương trình. |
| **Chất lượng bài viết & Workshop** (Blogs & Workshop) | 90% | 4.5 / 5.0 | Biên soạn tài liệu hướng dẫn từng bước chi tiết sử dụng Hugo Markdown và các hộp thông báo cảnh báo. Mã nguồn dự án được chạy thử nghiệm thành công và phân chia thành các file module sạch sẽ. |
| **Tinh thần chủ động & Nghiên cứu** (Events & Research) | 90% | 4.5 / 5.0 | Chủ động nghiên cứu về mô hình tính giá của AWS, các giải pháp tối ưu hóa chi phí, cấu hình chính sách bảo mật IAM và tối ưu hóa hiệu năng gọi API boto3 (tái sử dụng Lambda container). |

---

## 🔍 Điểm mạnh & Điểm cần cải thiện

### Điểm mạnh
- **Khả năng tự nghiên cứu và tiếp thu nhanh:** Nhanh chóng tìm hiểu, làm quen và áp dụng thành công các API dịch vụ Cloud và framework mới (S3 event triggers, Streamlit caching).
- **Tư duy giải quyết lỗi logic:** Thực hiện kiểm thử và cô lập lỗi hệ thống một cách có hệ thống (gỡ lỗi quyền truy cập AWS credentials, chuyển đổi kiểu dữ liệu float sang string cho DynamoDB).
- **Chỉn chu trong viết tài liệu:** Luôn chú trọng việc trình bày tài liệu kỹ thuật sạch sẽ, cấu trúc rõ ràng và ghi chú mã nguồn trực quan, giúp các lập trình viên khác dễ dàng tiếp cận sản phẩm.

### Điểm cần cải thiện
- **Tự động hóa hạ tầng (IaC):** Mặc dù đã thành thạo việc tạo tài nguyên thủ công trên AWS Console, tôi cần học cách tự động hóa triển khai hạ tầng bằng công cụ như **AWS CloudFormation** hoặc **Terraform**.
- **Cấu hình bảo mật nâng cao:** Cần nghiên cứu sâu hơn về việc bảo mật dữ liệu lưu trữ (data at rest), ví dụ như áp dụng khóa mã hóa do người dùng quản lý KMS (Customer-managed keys) trên S3 và DynamoDB.
- **Kiểm thử tự động nâng cao:** Cần xây dựng thêm các bộ kiểm thử đơn vị tự động (unit tests) sử dụng `pytest` và thư viện mock dịch vụ AWS như `moto` thay vì chỉ dựa vào kiểm thử thủ công toàn trình.

---

## 🚀 Kế hoạch phát triển tiếp theo

1. **Thi lấy chứng chỉ AWS:** Ôn tập và thi đạt chứng chỉ **AWS Certified Cloud Practitioner** hoặc **AWS Certified Solutions Architect – Associate** trong vòng 3 tháng tới để chuẩn hóa kiến thức điện toán đám mây.
2. **Áp dụng hạ tầng dạng mã (IaC):** Thay vì thao tác thủ công trên console, tôi sẽ triển khai toàn bộ hạ tầng backend (VPC, Lambda, DynamoDB, S3) bằng **Terraform** hoặc **AWS SAM (Serverless Application Model)** trong dự án tiếp theo.
3. **Tìm hiểu DevSecOps:** Xây dựng các pipeline CI/CD tự động (ví dụ qua GitHub Actions) để thực hiện kiểm tra định dạng code (linting), chạy test tự động và tự động deploy hàm serverless lên môi trường Cloud của AWS.
