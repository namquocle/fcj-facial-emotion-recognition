---
title: "Worklog Tuần 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

## TUẦN 1 (22/06-28/06): KHỞI ĐỘNG, LÀM QUEN VỚI NỀN TẢNG CLOUD VÀ DỊCH VỤ HẠ TẦNG CƠ BẢN (IAM, VPC, EC2)

### 1. Mục tiêu tuần (Objectives)
* Làm quen với hệ thống Cloud AWS thông qua AWS Academy và AWS Educate.
* Hiểu rõ mô hình Shared Responsibility Model (Mô hình chia sẻ trách nhiệm bảo mật) của AWS.
* Thiết lập tài khoản và thực hành các nguyên tắc bảo mật tài khoản gốc bằng IAM.
* Xây dựng và cấu hình hệ thống mạng ảo cô lập (VPC) phục vụ triển khai các tài nguyên ảo hóa (EC2).

### 2. Chi tiết công việc đã thực hiện (Tasks Completed)
* **Khởi tạo và cấu hình bảo mật tài khoản:**
  * Kích hoạt tài khoản học tập AWS Academy. Thiết lập xác thực đa yếu tố (MFA) cho tài khoản Root để ngăn chặn các truy cập trái phép.
  * Tìm hiểu cách tạo IAM User và IAM Group. Phân quyền cho Group sử dụng các IAM Policies định sẵn (Managed Policies) như `AdministratorAccess` (chỉ dùng cho tài khoản quản trị phụ) và `PowerUserAccess`.
  * Thực hành viết các chính sách bảo mật tùy chỉnh (Custom Policies) bằng định dạng JSON để chỉ cho phép một IAM User cụ thể đọc/ghi trong một phân vùng tài nguyên nhất định.
* **Thiết lập hạ tầng mạng ảo AWS VPC (Virtual Private Cloud):**
  * Thiết kế sơ đồ mạng cơ bản gồm 1 VPC có dải IP CIDR là `10.0.0.0/16`.
  * Chia nhỏ VPC thành 2 Subnets: 1 Public Subnet (`10.0.1.0/24`) có định tuyến ra ngoài Internet qua Internet Gateway (IGW) và 1 Private Subnet (`10.0.2.0/24`) để chứa cơ sở dữ liệu hoặc backend bảo mật.
  * Cấu hình Route Table cho Public Subnet để trỏ luồng mạng `0.0.0.0/0` đi qua Internet Gateway.
* **Triển khai máy chủ ảo Amazon EC2:**
  * Khởi tạo một thực thể máy chủ EC2 với hệ điều hành Ubuntu Server 22.04 LTS (loại instance `t2.micro` thuộc Free Tier).
  * Tạo cặp khóa bảo mật (Key Pair) dạng `.pem` và tải về máy cục bộ để phục vụ kết nối SSH.
  * Cấu hình Security Group (tường lửa lớp máy ảo): Chỉ mở cổng 22 (SSH) cho địa chỉ IP public của máy tính cá nhân (My IP) và mở cổng 80 (HTTP) cho toàn bộ Internet (`0.0.0.0/0`).
  * Thực hiện kết nối SSH từ máy cá nhân vào EC2 thông qua terminal, tiến hành cập nhật hệ thống và cài đặt thử nghiệm máy chủ web Apache/Nginx để kiểm tra khả năng hiển thị trang web mặc định trên trình duyệt.

### 3. Kiến thức & Kỹ năng tích lũy (Knowledge Acquired)
* **IAM Security:** Hiểu rõ tầm quan trọng của việc không sử dụng tài khoản Root cho các tác vụ hàng ngày. Nắm vững sự khác nhau giữa Security Group (hoạt động ở tầng instance, có trạng thái - stateful) và Network ACL (hoạt động ở tầng subnet, không trạng thái - stateless).
* **Mạng đám mây:** Hiểu cơ chế định tuyến (Routing) và cách thức phân chia dải mạng CIDR phục vụ cô lập môi trường ứng dụng.
* **Quản trị Linux & EC2:** Nắm được cách quản lý vòng đời của EC2 (Start, Stop, Terminate) và cách thức bảo mật máy chủ qua SSH key.

### 4. Khó khăn gặp phải & Cách giải quyết (Challenges & Troubleshooting)
* **Khó khăn:** Không thể kết nối SSH vào máy chủ EC2 sau khi khởi tạo, hệ thống báo lỗi *Connection Timeout*.
* **Giải quyết:** Kiểm tra lại cấu hình Route Table của Subnet chứa EC2 xem đã gắn Internet Gateway chưa, đồng thời phát hiện Security Group của EC2 đang cấu hình nhầm cổng SSH cho một dải IP không tồn tại. Đã cập nhật lại nguồn (Source IP) trong Security Group thành `My IP` hiện tại.

### 5. Kết quả đạt được (Outcomes)
* Tài khoản AWS được bảo mật tốt với IAM và MFA.
* Triển khai thành công 1 VPC chuẩn hóa và 1 máy chủ EC2 chạy web server có thể truy cập được từ bên ngoài.