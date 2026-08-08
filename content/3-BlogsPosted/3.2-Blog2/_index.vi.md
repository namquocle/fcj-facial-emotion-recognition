---
title: "Blog 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# Tối ưu hóa và tăng tốc phân tích Log quy mô lớn với AWS Glue và Apache Iceberg Materialized Views
## 1. Đặt vấn đề & Thách thức
Khi vận hành các hệ thống lớn, việc quản lý và phân tích dữ liệu log ứng dụng (application logs) khổng lồ luôn đi kèm với nhiều bài toán khó:
* Hiệu suất truy vấn giảm mạnh khi dung lượng dữ liệu lên tới hàng Terabyte.
* Chi phí tính toán cao và tốn thời gian khi phải quét qua toàn bộ dữ liệu thô (raw data) để thực hiện các câu lệnh gom cụm (aggregations) phức tạp.
* Khó khăn trong việc duy trì hiệu suất phân tích theo thời gian thực (near real-time) đối với dòng dữ liệu streaming.
## 2. Kiến trúc giải pháp (Architecture Overview)
Giải pháp này xây dựng một pipeline xử lý log tự động, không máy chủ (serverless) và sử dụng Materialized Views (Bảng chế xuất/Bảng biểu diễn tài liệu) dựa trên định dạng table mã nguồn mở Apache Iceberg để lưu trữ kết quả truy vấn được tính toán trước.
Pipeline bao gồm các thành phần phối hợp như sau:
* Amazon CloudWatch Logs: Tiếp nhận log từ ứng dụng và định tuyến qua Subscription Filters (có cơ chế tự động thử lại lên đến 24 giờ nếu lỗi).
* AWS Lambda: Lớp trung gian thực hiện parse (phân tích), làm giàu dữ liệu (enrichment) và chuẩn hóa cấu trúc log.
* Amazon Data Firehose: Buffer (đệm) dữ liệu và tối ưu hóa việc ghi theo batch vào các bảng Apache Iceberg, đồng thời xử lý logic ghi lại nếu thất bại.
* Apache Iceberg (trên Amazon S3): Cung cấp hỗ trợ giao dịch ACID, tiến hóa schema linh hoạt và tối ưu hiệu suất truy vấn. Các Materialized Views được quản lý trong AWS Glue Data Catalog.
* AWS Glue: Thực hiện hai nhiệm vụ chính:
    * Chạy một job khởi tạo (one-time job) để thiết lập database, base table và cấu trúc Materialized View.
    * Chạy một job lập lịch định kỳ (scheduled job) để làm mới (refresh) dữ liệu trong Materialized View từ bảng gốc.

## 3. Các bước triển khai cơ bản
* Bước 1: Triển khai Infrastructure bằng AWS CloudFormation Sử dụng template CloudFormation để tạo tự động các tài nguyên: S3 bucket, IAM roles, Firehose delivery stream, Lambda function và các Glue jobs.
* Bước 2: Kiểm thử Pipeline End-to-End Gửi các log mẫu (chứa id, customer_name, amount, order_date) vào CloudWatch Log Group để kiểm tra luồng dữ liệu đẩy về S3 dưới định dạng Iceberg.
* Bước 3: Xác thực dữ liệu và Lập lịch Refresh Sử dụng Amazon Athena để truy vấn trực tiếp bảng gốc nhằm đảm bảo log được nạp thành công. Sau đó cấu hình cron schedule cho Glue job (ví dụ: hàng giờ hoặc hàng ngày) để tự động cập nhật dữ liệu cho Materialized View.

## 4. Tại sao giải pháp này hiệu quả? (Key Benefits)
* Tăng tốc độ truy vấn vượt trội: Thay vì quét hàng triệu dòng dữ liệu thô ở bảng gốc mỗi khi ứng dụng dashboard yêu cầu tính toán (như doanh thu theo ngày, số đơn hàng theo vùng), Athena chỉ cần đọc trực tiếp từ bảng Materialized View đã được thu gọn và tính toán sẵn. Các truy vấn tốn vài phút nay chỉ mất vài giây.
* Tối ưu hóa chi phí: Giảm thiểu tối đa dung lượng dữ liệu cần quét (data scanned) trên Amazon Athena, giúp tiết kiệm chi phí vận hành đáng kể ở quy mô lớn.
* Kiến trúc Serverless bền bỉ: Khả năng tự động mở rộng (auto-scaling) theo lưu lượng log, đi kèm cơ chế xử lý lỗi (DLQ) đẩy các bản ghi lỗi về S3 để phân tích và chạy lại sau (replay), đảm bảo không mất mát dữ liệu.
Giải pháp thay thế nâng cao: Nếu không muốn tự quản lý logic refresh thông qua AWS Glue, bạn hoàn toàn có thể cân nhắc sử dụng Amazon S3 Tables – một tính năng quản lý Apache Iceberg toàn phần (fully managed) có hỗ trợ sẵn Native Materialized Views để đơn giản hóa vận hành.

Chi tiết mã nguồn và script mẫu để thử nghiệm có thể tham khảo tại kho lưu trữ sample-log-analytics-iceberg-mv trên GitHub.

*Hình ảnh: Sơ đồ luồng dữ liệu phân tích Log quy mô lớn với Apache Iceberg.*
![Log_2](/images/3-BlogsPosted/images_Log2.png)

*Link tham khảo: [sample-log-analytics-iceberg-mv trên GitHub](https://github.com/aws-samples/sample-log-analytics-iceberg-mv)*

*Hướng dẫn triển khai: Triển khai tài nguyên thông qua CloudFormation, thực hiện kiểm thử pipeline end-to-end bằng log mẫu và cấu hình cron schedule cho Glue job.*

*Ngày đăng bài: 15/07.*

![Log_2](/images/3-BlogsPosted/LogPostComplete2.png)