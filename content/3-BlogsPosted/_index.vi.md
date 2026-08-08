---
title: "Các bài blogs đã đăng"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---
# Các bài Blogs đã đăng 

## BLOG 1
### TỰ ĐỘNG HÓA KÍCH HOẠT AWS SYSTEMS MANAGER ĐỂ ĐĂNG KÝ HYBRID-MANAGED NODE

*Bài viết này chia sẻ giải pháp tự động hóa quản lý hạ tầng hybrid kết hợp giữa on-premises và đám mây sử dụng AWS Systems Manager (SSM). Nhằm khắc phục khó khăn khi các thông tin xác thực (Activation Code và Activation ID) hết hạn hoặc vượt giới hạn đăng ký thiết bị tối đa, giải pháp đề xuất một hệ thống serverless tự động cấp phát và gia hạn mã kích hoạt qua mạng riêng ảo.*

*Các điểm chính cần nắm:*
- *Sử dụng AWS CloudFormation để tự động hóa hoàn toàn việc triển khai hạ tầng serverless giúp giảm thiểu tối đa các tác vụ quản trị thủ công (Operational Overhead).*
- *Thiết lập Private API Gateway kết hợp với AWS Lambda và Amazon VPC Endpoint để bảo vệ lưu lượng mạng nội bộ từ on-premises không đi qua Internet công cộng.*
- *Ứng dụng Amazon DynamoDB để quản lý trạng thái khóa (Locked/Unlocked) nhằm tránh tình trạng xung đột (race conditions) khi nhiều máy chủ yêu cầu cấp mã đồng thời.*
- *Lưu trữ bảo mật cặp Activation ID/Code đang hoạt động trong Parameter Store và tự động tạo mới qua API của Systems Manager khi mã hiện tại hết hiệu lực.*

*Giải pháp giúp tối ưu hóa hiệu quả quản trị hạ tầng, nâng cao mức độ bảo mật mạng thông qua việc kiểm soát tập trung bằng hạ tầng dạng mã (IaC), đặc biệt phù hợp cho các doanh nghiệp đang chuyển dịch hệ thống Datacenter truyền thống tích hợp Hybrid Cloud với AWS.*

*Hình ảnh: Sơ đồ kiến trúc tự động hóa kích hoạt SSM cho Hybrid Nodes.*
![Log_1](/images/3-BlogsPosted/images_Log1.png)
*Link tham khảo: [Automate AWS Systems Manager activation for hybrid-managed node registration](https://aws.amazon.com/blogs/mt/automate-aws-systems-manager-activation-for-hybrid-managed-node-registration/)*

*Hướng dẫn triển khai: Triển khai file template CloudFormation, cấu hình DNS nội bộ trỏ về VPC Endpoint và chạy script đăng ký agent trên máy chủ on-premises.*

---

## BLOG 2
### TỐI ƯU HÓA VÀ TĂNG TỐC PHÂN TÍCH LOG QUY MÔ LỚN VỚI AWS GLUE VÀ APACHE ICEBERG MATERIALIZED VIEWS

*Bài viết này hướng dẫn xây dựng một pipeline xử lý log tự động, không máy chủ (serverless) sử dụng Materialized Views dựa trên định dạng table mã nguồn mở Apache Iceberg để lưu trữ kết quả truy vấn được tính toán trước. Giải pháp nhằm khắc phục tình trạng hiệu suất truy vấn giảm mạnh và chi phí quét dữ liệu thô (raw data) tăng cao khi dung lượng log ứng dụng đạt quy mô hàng Terabyte.*

*Các điểm chính cần nắm:*
- *Sử dụng Amazon CloudWatch Logs kết hợp Lambda và Data Firehose để thực hiện chuẩn hóa cấu trúc dữ liệu log và tối ưu hóa việc ghi theo batch vào S3.*
- *Tận dụng định dạng Apache Iceberg trên Amazon S3 giúp cung cấp hỗ trợ giao dịch ACID, tiến hóa schema linh hoạt và tối ưu hóa hiệu suất truy vấn.*
- *Cấu hình AWS Glue để quản lý các Materialized Views và chạy các job lập lịch định kỳ (scheduled jobs) để tự động làm mới dữ liệu từ bảng gốc.*
- *Sử dụng Amazon Athena để truy vấn trực tiếp từ bảng Materialized View đã được thu gọn giúp tăng tốc độ truy vấn từ vài phút xuống còn vài giây.*

*Giải pháp này mang lại khả năng tự động mở rộng theo lưu lượng log cực kỳ mạnh mẽ, giảm thiểu tối đa dữ liệu cần quét giúp tiết kiệm chi phí vận hành ở quy mô lớn, đồng thời cung cấp cơ chế xử lý lỗi (DLQ) bền bỉ giúp đảm bảo an toàn toàn vẹn dữ liệu.*

*Hình ảnh: Sơ đồ luồng dữ liệu phân tích Log quy mô lớn với Apache Iceberg.*
![Log_2](/images/3-BlogsPosted/images_Log2.png)
*Link tham khảo: [sample-log-analytics-iceberg-mv trên GitHub](https://github.com/aws-samples/sample-log-analytics-iceberg-mv)*

*Hướng dẫn triển khai: Triển khai tài nguyên thông qua CloudFormation, thực hiện kiểm thử pipeline end-to-end bằng log mẫu và cấu hình cron schedule cho Glue job.*

---

## BLOG 3
### XÂY DỰNG HỆ THỐNG TỰ ĐỘNG ĐƯA RA KHUYẾN NGHỊ TỐI ƯU HIỆU SUẤT AMAZON REDSHIFT BẰNG AI (AMAZON BEDROCK)

*Bài viết này giới thiệu giải pháp xây dựng một luồng xử lý tự động, không máy chủ (serverless) theo cơ chế dựa trên tín hiệu để đưa ra các khuyến nghị tối ưu hiệu suất Amazon Redshift bằng AI. Thay vì đẩy trực tiếp dữ liệu thô vào mô hình ngôn ngữ lớn (LLM), hệ thống tiến hành tính toán các tín hiệu hiệu suất, liên kết với CloudWatch rồi mới đưa vào Amazon Bedrock (Claude Sonnet) để AI phân tích chuyên sâu.*

*Các điểm chính cần nắm:*
- *Sử dụng Amazon EventBridge để lập lịch 24 giờ tự động kích hoạt quá trình thu thập và phân tích hiệu suất cơ sở dữ liệu.*
- *Triển khai Collector Lambda để chạy các câu lệnh SQL chẩn đoán đối với Redshift Serverless và lưu dữ liệu telemetry JSON vào S3.*
- *Triển khai Analyzer Lambda để xây dựng prompt có ngữ cảnh và gọi Amazon Bedrock (Claude Sonnet) nhằm xuất báo cáo khuyến nghị chi tiết.*
- *Tích hợp Amazon SNS để gửi email tóm tắt các khuyến nghị quan trọng nhất (như ID câu lệnh truy vấn, tên bảng cụ thể) trực tiếp đến quản trị viên.*

*Hệ thống giúp các kỹ sư dữ liệu giảm thiểu thời gian phân tích hiệu suất thủ công từ vài giờ xuống còn vài phút, phân loại mức độ ưu tiên của các khuyến nghị rõ ràng, đồng thời nhanh chóng phát hiện các lỗi thiết kế nghiêm trọng trong Redshift.*

*Hình ảnh: Sơ đồ kiến trúc Advisor hiệu suất Amazon Redshift bằng AI.*
![Log_3](/images/3-BlogsPosted/images_Log3.png)
*Link tham khảo: [sample-ai-performance-advisor-for-amazon-redshift trên GitHub](https://github.com/aws-samples/sample-ai-performance-advisor-for-amazon-redshift)*

*Hướng dẫn triển khai: Thiết lập S3 bucket và SNS topic, phân quyền IAM Role hạn chế quyền tối thiểu và cấu hình các biến môi trường cho Lambda.*
