---
title : "Các bước chuẩn bị"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

# 5.2. Yêu cầu tiên quyết

Trước khi bắt đầu thực hành workshop này, hãy đảm bảo rằng bạn đã chuẩn bị đầy đủ môi trường phát triển, các công cụ cần thiết và quyền truy cập tài khoản AWS.

---

## 1. Cấu hình Tài khoản AWS & IAM

Để triển khai và chạy các tài nguyên trong workshop này, bạn cần có một tài khoản AWS đang hoạt động. Nếu bạn đang tham gia khóa học, bạn có thể sử dụng môi trường **AWS Academy Learner Labs**.

### Bước 1.1: Tạo IAM User (Dành cho việc phát triển cục bộ)
Nếu bạn sử dụng tài khoản AWS cá nhân/doanh nghiệp thông thường:
1. Truy cập **IAM Console**.
![Picture_1](/images/5-Workshop/1.png)
2. Chọn **Users** (Người dùng) -> **Create user** (Tạo người dùng).
![Picture_2](/images/5-Workshop/2.png)
![Picture_3](/images/5-Workshop/3.png)
3. Đặt tên cho user (Ví dụ: `workshop-developer`).
![Picture_4](/images/5-Workshop/4.png)
4. Gán trực tiếp các chính sách (Managed Policies) sau cho user này (để phục vụ việc thực hành, mặc dù trong thực tế sản xuất bạn nên áp dụng nguyên tắc đặc quyền tối thiểu):
   - `AmazonS3FullAccess`
   - `AmazonDynamoDBFullAccess`
   - `AmazonRekognitionFullAccess`
   - `AWSLambda_FullAccess`
   - `IAMFullAccess`
![Picture_5](/images/5-Workshop/5.png)
![Picture_6](/images/5-Workshop/6.png)
![Picture_7](/images/5-Workshop/7.png)
![Picture_8](/images/5-Workshop/8.png)
![Picture_9](/images/5-Workshop/9.png)
![Picture_10](/images/5-Workshop/10.png)

### Bước 1.2: Tạo Access Keys (Khóa truy cập)
1. Trong giao diện chi tiết của user vừa tạo, chọn tab **Security credentials** (Thông tin bảo mật).
![Picture_11](/images/5-Workshop/11.png)
![Picture_12](/images/5-Workshop/12.png)
2. Cuộn xuống phần **Access keys**, chọn **Create access key** (Tạo khóa truy cập).
![Picture_13](/images/5-Workshop/13.png)
3. Chọn mục **Command Line Interface (CLI)** và tích vào hộp thoại xác nhận.
![Picture_14](/images/5-Workshop/14.png)
4. Tải xuống tệp `.csv` chứa `Access key ID` và `Secret access key`.
![Picture_15](/images/5-Workshop/15.png)

{{% notice warning %}}
Tuyệt đối không đẩy tệp chứa AWS Access Keys hoặc tệp cấu hình `.env` lên các kho lưu trữ mã nguồn công khai như GitHub. Việc lộ thông tin xác thực này có thể dẫn đến việc tài khoản bị lạm dụng và phát sinh chi phí khổng lồ.
{{% /notice %}}

---

## 2. Thiết lập Môi trường Cục bộ

### Bước 2.1: Cài đặt Python
Đảm bảo máy tính của bạn đã cài đặt phiên bản Python từ **3.12** trở lên. Kiểm tra phiên bản bằng dòng lệnh:
```bash
python --version
```

### Bước 2.2: Thiết lập AWS CLI
1. Tải xuống và cài đặt bộ công cụ AWS CLI phù hợp với Hệ điều hành của bạn:
   - [Hướng dẫn cài đặt AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Mở terminal (Command Prompt, PowerShell hoặc bash) và chạy lệnh:
   ```bash
   aws configure
   ```
3. Nhập các thông tin xác thực của bạn khi được nhắc:
   ```text
   AWS Access Key ID [None]: <MÃ_ACCESS_KEY_ID_CỦA_BẠN>
   AWS Secret Access Key [None]: <MÃ_SECRET_ACCESS_KEY_CỦA_BẠN>
   Default region name [None]: ap-southeast-1
   Default output format [None]: json
   ```

---

## 3. Khởi tạo dự án & Cài đặt thư viện

### Bước 3.1: Tạo Thư mục dự án
Tạo một thư mục chứa mã nguồn và di chuyển vào trong thư mục đó:
```bash
mkdir Emotion-recognition-app
cd Emotion-recognition-app
```

### Bước 3.2: Khởi tạo môi trường ảo (Virtual Environment)
Khuyến nghị sử dụng môi trường ảo Python để cô lập các thư viện của dự án:

**Trên Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**Trên macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 3.3: Cài đặt các thư viện cần thiết
Tạo một tệp có tên `requirements.txt` với nội dung như sau:
```text
streamlit
boto3
Pillow
python-dotenv
```

Tiến hành cài đặt các thư viện này thông qua công cụ quản lý gói `pip`:
```bash
pip install -r requirements.txt
```
