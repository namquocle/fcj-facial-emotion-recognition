---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Tự động hóa kích hoạt AWS Systems Manager để đăng ký Hybrid-Managed Node
Chào anh/chị trong cộng đồng AWS Việt Nam, sau đây em xin tóm tắt về giải pháp tự động hóa quản lý hạ tầng hybrid (kết hợp on-premises và cloud) sử dụng AWS Systems Manager (SSM) dựa trên tài liệu chính thức từ AWS Cloud Operations Blog.
## 1. Đặt vấn đề (Problem Statement)
Để quản lý các máy chủ vật lý hoặc máy ảo (VMs) chạy dưới môi trường on-premises bằng AWS Systems Manager, chúng ta cần khởi tạo tính năng Hybrid Activations để lấy thông tin xác thực (Activation Code và Activation ID).
Tuy nhiên, các thông tin xác thực này đều có giới hạn về thời gian hết hạn hoặc số lượng thiết bị được đăng ký tối đa. Việc khởi tạo lại thủ công khi code hết hạn gây tốn thời gian và dễ xảy ra sai sót trong vận hành hệ thống quy mô lớn.
## 2. Giải pháp Kiến trúc (Solution Overview)
Giải pháp sử dụng AWS CloudFormation để triển khai tự động một hệ thống serverless chịu trách nhiệm cấp phát và gia hạn thông tin kích hoạt tự động bao gồm:
Amazon API Gateway (Private Type): Cung cấp Endpoint dạng REST API nội bộ để các máy chủ on-premises gửi request lấy Code/ID an toàn qua kết nối mạng riêng.
* AWS Lambda: Đóng vai trò xử lý logic chính. Khi nhận request từ API Gateway, Lambda sẽ kiểm tra mã kích hoạt hiện tại trong Parameter Store. Nếu mã đã hết hạn hoặc đạt giới hạn đăng ký, Lambda sẽ tự động gọi API của Systems Manager để tạo một mã mới.
* Amazon DynamoDB: Lưu trữ trạng thái (Locked / Unlocked) để tránh tình trạng xung đột (race conditions) khi có nhiều máy chủ cùng yêu cầu cấp mã một lúc.
* AWS Systems Manager Parameter Store: Nơi lưu trữ bảo mật cặp Activation ID/Code đang hoạt động.
* Amazon VPC Endpoint: Đảm bảo lưu lượng mạng từ on-premises truy cập vào API Gateway hoàn toàn đi qua đường truyền riêng tư, không public ra ngoài Internet.
## 3. Quy trình thực thi (Execution Flow)
1.Máy chủ client (on-premises) gửi lệnh gọi (GET request) tới Private API Gateway.
2.Hệ thống DNS nội bộ phân giải URL sang IP private của VPC Endpoint.
3.API Gateway chuyển tiếp request sang AWS Lambda.
4.Lambda khóa trạng thái trong DynamoDB, kiểm tra/tạo mới thông tin kích hoạt từ Parameter Store rồi trả về cho client dưới định dạng JSON:
JSON
{
 "ActivationId": "e50a8437-23dd-4326-9e79-5e3b7573493e",
 "ActivationCode": "vVcH9zJX4ROy2XTsh5cb"
}

5.Client sử dụng đoạn mã nhận được kết hợp với Shell Script (Linux) hoặc PowerShell (Windows) để tự động cài đặt mã và đăng ký agent (amazon-ssm-agent) lên AWS Systems Manager.
## 4. Đánh giá giải pháp
* Ưu điểm: Giảm thiểu tối đa tác vụ quản trị thủ công (Operational Overhead), tăng tính bảo mật nhờ việc đóng gói lưu lượng trong mạng nội bộ (VPC Endpoint) và quản lý tập trung bằng mã nguồn hạ tầng (IaC - CloudFormation).
* Ứng dụng thực tế: Phù hợp cho các bài toán quản lý hạ tầng lớn, các hệ thống Data Center truyền thống đang trong quá trình dịch chuyển hoặc tích hợp Hybrid Cloud với AWS.
Chi tiết mã nguồn CloudFormation và các đoạn script cài đặt mẫu có thể tham khảo trực tiếp tại bài viết gốc:Automate AWS Systems Manager activation for hybrid-managed node registration.

*Hình ảnh: Sơ đồ kiến trúc tự động hóa kích hoạt SSM cho Hybrid Nodes.*
![Log_1](/images/3-BlogsPosted/images_Log1.png)

*Link tham khảo: [Automate AWS Systems Manager activation for hybrid-managed node registration](https://aws.amazon.com/blogs/mt/automate-aws-systems-manager-activation-for-hybrid-managed-node-registration/)*

*Hướng dẫn triển khai: Triển khai file template CloudFormation, cấu hình DNS nội bộ trỏ về VPC Endpoint và chạy script đăng ký agent trên máy chủ on-premises.*

*Ngày đăng bài: 03/07.*

![Log_1](/images/3-BlogsPosted/LogPostComplete1.png)