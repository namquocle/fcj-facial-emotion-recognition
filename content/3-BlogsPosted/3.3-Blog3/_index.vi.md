---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# Xây dựng Hệ thống Tự động Đưa ra Khuyến nghị Tối ưu Hiệu suất Amazon Redshift bằng AI (Amazon Bedrock)
## 1. Bài toán & Thách thức
Khi vận hành các hệ thống dữ liệu lớn với Amazon Redshift, việc giám sát và tối ưu hóa hiệu suất (performance tuning) luôn là một thách thức không hề nhỏ đối với các đội ngũ Data Platform:
* Các chỉ số telemetry nằm rải rác ở nhiều hệ thống view (SYS_QUERY_HISTORY, SVV_TABLE_INFO, SVV_ALTER_TABLE_RECOMMENDATIONS) và chỉ số CloudWatch.
* Việc diễn giải dữ liệu cực kỳ phức tạp: Phải mất nhiều giờ phân tích thủ công để liên kết một đợt tăng đột biến thời gian commit (QueryRuntimeBreakdown) với hàng trăm câu lệnh INSERT nhỏ, hoặc kết nối hiện tượng tràn đĩa (disk spill) với việc cấu hình thiếu tài nguyên tính toán.
## 2. Kiến trúc giải pháp (Architecture Overview)
Giải pháp này xây dựng một luồng xử lý tự động, không máy chủ (serverless) theo cơ chế dựa trên tín hiệu (signal-based design). Thay vì đẩy trực tiếp toàn bộ dữ liệu thô vào LLM, hệ thống sẽ tiền tính toán các tín hiệu hiệu suất, liên kết chúng với CloudWatch rồi mới đưa vào Amazon Bedrock để mô hình AI đưa ra các khuyến nghị chính xác theo ngữ cảnh.
Pipeline hoạt động trên lịch trình 24 giờ của Amazon EventBridge bao gồm 2 hàm Lambda chính:
* Collector Lambda: Chạy 13 câu lệnh SQL chẩn đoán đối với Amazon Redshift Serverless, đọc cấu hình quản lý tải công việc (WLM) và thu thập các chỉ số Amazon CloudWatch. Từ đó, hàm này tính toán ra các "tín hiệu hiệu suất" (performance signals) và lưu file telemetry JSON vào Amazon S3.
* Analyzer Lambda: Đọc file dữ liệu từ S3, xây dựng một cấu trúc prompt chặt chẽ (chứa các cặp liên kết chỉ số CloudWatch - Tín hiệu), sau đó gọi Amazon Bedrock (sử dụng model Anthropic Claude Sonnet) để phân tích và xuất file khuyến nghị JSON về S3.
* Amazon SNS: Gửi email tóm tắt các khuyến nghị quan trọng nhất trực tiếp đến quản trị viên.

## 3. Các bước triển khai cơ bản
* Bước 1: Thiết lập tài nguyên bổ sung: Tạo S3 bucket lưu báo cáo, cấu hình Amazon SNS topic/subscription để nhận email, và lưu thông tin quản trị viên (credentials) vào AWS Secrets Manager để kết nối Redshift an toàn.
* Bước 2: Phân quyền IAM Role: Tạo IAM Role cấp quyền tối thiểu cần thiết (least-privilege) cho phép hai Lambda function tương tác với Redshift Data API, S3, SNS, Bedrock và CloudWatch.
* Bước 3: Triển khai và Cấu hình Lambda: Đóng gói mã nguồn (collector.py đi kèm các file SQL chẩn đoán) và analyzer.py, thiết lập các biến môi trường (Environment Variables) cần thiết như WORKGROUP, DATABASE, SECRET_ARN, và MODEL_ID.
* Bước 4: Đặt lịch và Kiểm thử: Cấu hình EventBridge tự động kích hoạt mỗi 24 giờ, sau đó chạy thử nghiệm (Test) thủ công trên console để xác thực luồng dữ liệu end-to-end hoạt động chính xác.

## 4. Lợi ích cốt lõi (Key Benefits)
* Khuyến nghị có mục tiêu cao (Không chung chung): Nhờ thiết kế tiền tính toán tín hiệu và liên kết ngữ cảnh trước khi gửi tới AI, các khuyến nghị trả về luôn chỉ đích danh các ID câu lệnh truy vấn, tên bảng cụ thể và các giá trị số liệu thực tế.
* Phân loại mức độ ưu tiên rõ ràng: Mỗi khuyến nghị đều đi kèm với mức độ ưu tiên (Critical, High, Medium, Low) và phân nhóm danh mục (tối ưu truy vấn, thiết kế bảng, dung lượng, bảo trì...) giúp đội ngũ vận hành dễ dàng lên kế hoạch xử lý.
* Tối ưu hóa tài nguyên: Giúp các kỹ sư dữ liệu giảm từ vài giờ phân tích thủ công xuống còn vài phút nhận báo cáo tự động, nhanh chóng phát hiện các lỗi thiết kế như lệch dòng (row-skew) nghiêm trọng hay thiếu nén cột (column compression).

Mã nguồn triển khai chi tiết và các câu lệnh mẫu để thử nghiệm được cung cấp tại kho lưu trữ GitHub sample-ai-performance-advisor-for-amazon-redshift.

*Hình ảnh: Sơ đồ kiến trúc Advisor hiệu suất Amazon Redshift bằng AI.*
![Log_3](/images/3-BlogsPosted/images_Log3.png)

*Link tham khảo: [sample-ai-performance-advisor-for-amazon-redshift trên GitHub](https://github.com/aws-samples/sample-ai-performance-advisor-for-amazon-redshift)*

*Hướng dẫn triển khai: Thiết lập S3 bucket và SNS topic, phân quyền IAM Role hạn chế quyền tối thiểu và cấu hình các biến môi trường cho Lambda.*

*Ngày đăng bài: 27/07.*

![Log_3](/images/3-BlogsPosted/LogPostComplete3.png)