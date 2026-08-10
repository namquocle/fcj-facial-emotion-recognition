---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
# BẢN ĐỀ XUẤT DỰ ÁN CUỐI KHÓA (PROJECT PROPOSAL)
**Đề tài:** Serverless Facial Emotion Recognition Analytics Platform
**Chuyên ngành:** Công nghệ Thông tin 
**Học viên đề xuất:** Lê Quốc Nam

---

## 1. TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

Dự án **"Serverless Facial Emotion Recognition Analytics Platform"** là một hệ thống phân tích cảm xúc khuôn mặt từ hình ảnh được xây dựng dựa trên kiến trúc không máy chủ (Serverless) của Amazon Web Services (AWS). Nền tảng cho phép người dùng cuối tương tác thông qua giao diện Web trực quan để tải ảnh chân dung lên, từ đó tự động kích hoạt một chuỗi quy trình xử lý dữ liệu hướng sự kiện (Event-driven pipeline) ở backend để nhận diện cảm xúc khuôn mặt và lập nhật ký báo cáo.

Các công nghệ cốt lõi được tích hợp trong dự án bao gồm:
* **Giao diện người dùng (Frontend):** Ứng dụng Streamlit (Python) tối giản, linh hoạt, chạy trên môi trường cục bộ hoặc máy ảo.
* **Lưu trữ đối tượng (Storage):** **Amazon S3** chịu trách nhiệm lưu trữ an toàn các tệp hình ảnh đầu vào.
* **Tính toán không máy chủ (Compute):** **AWS Lambda** (Python 3.12 sử dụng thư viện SDK `boto3`) làm nhiệm vụ điều phối và xử lý logic nghiệp vụ.
* **Trí tuệ nhân tạo (AI/ML Service):** **Amazon Rekognition** (API `DetectFaces`) đóng vai trò là công cụ thị giác máy tính nhận diện khuôn mặt và bóc tách các chỉ số cảm xúc.
* **Cơ sở dữ liệu (Database):** **Amazon DynamoDB** (bảng NoSQL) lưu trữ nhật ký phân tích cuối cùng với thời gian thực hiện tối ưu.

**Điểm nổi bật của giải pháp:** Khả năng tự động co giãn (Auto-scaling) từ không đến hàng ngàn yêu cầu cùng lúc mà không cần quản trị hạ tầng, vận hành với chi phí cực thấp (gần như $0 USD nhờ tối ưu hóa gói AWS Free Tier) và kiến trúc mã nguồn modular sạch sẽ, dễ bảo trì.

---

## 2. TUYÊN BỐ VẤN ĐỀ (PROBLEM STATEMENT)

### Bối cảnh thực tế:
Trong kỷ nguyên số hóa, việc thấu hiểu cảm xúc của con người đóng vai trò sống còn trong việc nâng cao trải nghiệm khách hàng (Customer Experience - CX) trong ngành bán lẻ, dịch vụ, hay đo lường độ tập trung của học viên trong giáo dục trực tuyến (E-learning). Tuy nhiên, các phương pháp truyền thống như khảo sát thủ công (surveys) thường có tỷ lệ phản hồi thấp, tốn thời gian và mang tính chủ quan cao.

### Thách thức về mặt kỹ thuật:
Xây dựng một hệ thống phân tích hình ảnh ứng dụng trí tuệ nhân tạo (AI/ML) theo cách truyền thống đối mặt với các rào cản lớn:
1. **Chi phí hạ tầng lớn:** Yêu cầu các máy chủ ảo (ví dụ: Amazon EC2) có GPU mạnh mẽ để chạy các mô hình Deep Learning. Các máy chủ này phải hoạt động liên tục 24/7, phát sinh chi phí lãng phí rất lớn trong những khung giờ không có người sử dụng (Idle cost).
2. **Khó khăn trong vận hành:** Người quản trị phải liên tục cấu hình hệ điều hành, vá lỗi bảo mật phần mềm, thiết lập cơ chế cân bằng tải (Load Balancer) và tự động co giãn (Auto Scaling Groups) phức tạp.
3. **Độ trễ và quá tải:** Hệ thống dễ bị nghẽn mạng khi có lượng người dùng truy cập đột biến (Spike traffic) tại một thời điểm.

### Giải pháp đề xuất:
Dự án đề xuất giải quyết các bài toán trên bằng cách chuyển dịch sang kiến trúc **Serverless** kết hợp với **Managed AI Services** trên AWS. Giải pháp này giúp loại bỏ hoàn toàn việc quản lý máy chủ vật lý hay hệ điều hành, tự động co giãn tức thời theo yêu cầu thực tế, và chỉ tính phí khi có yêu cầu được xử lý (Pay-as-you-go).

---

## 3. KIẾN TRÚC GIẢI PHÁP (SOLUTION ARCHITECTURE)

Hệ thống được thiết kế theo kiến trúc hướng sự kiện (Event-Driven Architecture) với luồng dữ liệu tuần tự khép kín như sau:

![Structure diagram](/images/2-Proposal/Structure-diagram.png) 

### Chi tiết vai trò của các dịch vụ AWS trong hệ thống:

* **Amazon S3 (`my-facial-emotion-recognition-2026`):** Lưu trữ các file ảnh định dạng JPG/PNG được tải lên từ Frontend. Nó hoạt động như một kho lưu trữ đối tượng bền vững và an toàn (chặn truy cập public mặc định).
* **AWS Lambda (`FaceEmotionRecognizer`):** Đóng vai trò là "bộ não" trung tâm của backend. Lambda được kích hoạt tự động bằng cơ chế S3 Event Trigger. Khi chạy, Lambda đọc siêu dữ liệu (metadata) của sự kiện để biết chính xác bucket nào và tệp tin nào vừa được tạo, sau đó điều phối lời gọi đến Rekognition và lưu kết quả vào DynamoDB.
* **Amazon Rekognition:** Phân tích ảnh đầu vào từ S3, phát hiện số lượng khuôn mặt và trả về tập hợp các thuộc tính hình ảnh bao gồm mảng cảm xúc (HAPPY, SAD, ANGRY, CONFUSED, etc.) với mức độ tin cậy tương ứng.
* **Amazon DynamoDB (`FaceEmotionLogs`):** Cơ sở dữ liệu NoSQL lưu trữ bản ghi nhật ký phân tích. Mỗi bản ghi bao gồm:
  * `LogID` (Partition Key - String): UUID ngẫu nhiên định danh bản ghi.
  * `Timestamp` (String): Thời gian phân tích hệ thống (ISO-8601 UTC).
  * `ImageName` (String): Tên file ảnh gốc.
  * `FaceCount` (Number): Số khuôn mặt được nhận diện trong ảnh.
  * `TopEmotion` (String): Cảm xúc chủ đạo chiếm tỷ lệ tin cậy cao nhất.
  * `Confidence` (String): Độ tin cậy tính theo phần trăm của cảm xúc chủ đạo đó.
* **AWS CloudWatch logs:** Ghi nhận toàn bộ nhật ký thực thi của Lambda để phục vụ việc giám sát hoạt động và gỡ lỗi (Debugging).

---

## 4. TRIỂN KHAI KỸ THUẬT (TECHNICAL IMPLEMENTATION)

Dự án được phân rã kỹ thuật và triển khai qua 3 giai đoạn chính:

### Giai đoạn A: Thiết lập hạ tầng và Cấu hình bảo mật IAM (Security First)
* **Lưu trữ:** Tạo S3 bucket và bật mã hóa mặc định SSE-S3. Thiết lập thuộc tính chặn truy cập public.
* **Cơ sở dữ liệu:** Khởi tạo bảng DynamoDB với khóa chính là `LogID`. Cấu hình Capacity Mode ở trạng thái **On-Demand** để chỉ tính phí khi có truy vấn đọc/ghi xảy ra.
* **Phân quyền Least Privilege:**
  * Tạo IAM User tên `streamlit-s3-uploader` dành riêng cho Client Frontend, chỉ gắn kèm chính sách (Policy) cấp quyền `s3:PutObject` lên đúng bucket đích.
  * Tạo IAM Role tên `LambdaEmotionRecognitionRole` làm vai trò thực thi cho Lambda. Gắn các quyền hạn tối thiểu: đọc file từ S3 (`s3:GetObject`), gọi API nhận diện khuôn mặt (`rekognition:DetectFaces`), và ghi log vào DynamoDB (`dynamodb:PutItem`).

### Giai đoạn B: Phát triển mã nguồn Backend (AWS Lambda)
* Sử dụng ngôn ngữ **Python 3.12** kết hợp thư viện AWS SDK (`boto3`).
* Tách biệt mã nguồn Lambda thành dạng các module đơn nhiệm (Modular Code) để nâng cao khả năng kiểm thử và bảo trì:
  * `rekognition_service.py`: Chứa các hàm giao tiếp trực tiếp với Amazon Rekognition và thuật toán xác định cảm xúc chủ đạo (`get_dominant_emotion`).
  * `dynamodb_service.py`: Khởi tạo và ghi log vào bảng DynamoDB.
  * `lambda_function.py`: Điểm vào chính (main handler), chịu trách nhiệm điều phối các dịch vụ và xử lý ngoại lệ an toàn (`try...except`).
* Đóng gói toàn bộ các file module này thành một file ZIP để triển khai lên AWS Lambda Console.

### Giai đoạn C: Phát triển Frontend (Streamlit)
* Xây dựng giao diện web cục bộ tương tác đơn giản bằng thư viện **Streamlit**.
* Áp dụng cấu trúc modular hóa cho mã nguồn chạy local:
  * `config.py`: Tải các khóa bảo mật và cấu hình bucket từ file ẩn `.env` bằng thư viện `python-dotenv`.
  * `validation.py`: Kiểm tra định dạng đuôi file (.jpg, .png) và giới hạn dung lượng tải lên tối đa là 5MB để tối ưu băng thông mạng.
  * `s3_service.py`: Khởi tạo S3 client sử dụng credentials của user hạn chế quyền và thực hiện upload ảnh.
  * `ui_components.py`: Thiết kế chi tiết giao diện màn hình chính, hiển thị preview ảnh qua thư viện Pillow, và hiển thị kết quả phân tích.
  * `app.py`: Khởi động ứng dụng Streamlit.

---

## 5. LỘ TRÌNH VÀ CÁC MỐC TRIỂN KHAI (ROADMAP & MILESTONES)

Lộ trình dự án kéo dài đúng **2 tháng (8 tuần)**, được phân chia cụ thể như sau:

```
[Tháng 1: Học tập & Thiết kế] ────> [Tháng 2: Triển khai & Đánh giá]
  ├─ Tuần 1: Học AWS cơ bản            ├─ Tuần 5: Viết code Backend Lambda
  ├─ Tuần 2: Storage & Databases       ├─ Tuần 6: Tích hợp S3 Trigger & CloudWatch
  ├─ Tuần 3: Serverless & AI/ML        ├─ Tuần 7: Xây dựng Streamlit UI & E2E Test
  └─ Tuần 4: Khởi tạo hạ tầng S3/DB    └─ Tuần 8: Báo cáo, Clean-up & Tổng kết
```

### Chi tiết các cột mốc quan trọng (Key Milestones):
* **Mốc 1 (Cuối Tuần 3):** Hoàn thành thiết kế sơ đồ kiến trúc hệ thống và nhận phê duyệt đề tài dự án từ mentor hướng dẫn.
* **Mốc 2 (Cuối Tuần 4):** Thiết lập xong toàn bộ tài nguyên lưu trữ (S3), cơ sở dữ liệu (DynamoDB) và cấu hình phân quyền bảo mật IAM chuẩn chỉnh.
* **Mốc 3 (Cuối Tuần 6):** Triển khai xong mã nguồn Lambda ở backend, cấu hình thành công S3 trigger để tự động hóa luồng xử lý và ghi nhận log vào DynamoDB.
* **Mốc 4 (Cuối Tuần 7):** Kết nối thành công giao diện frontend Streamlit với các tài nguyên AWS, hoàn thành kiểm thử tích hợp toàn diện (E2E Testing).
* **Mốc 5 (Cuối Tuần 8):** Nộp báo cáo kỹ thuật song ngữ cuối khóa, thực hiện dọn dẹp tài nguyên để tránh phát sinh chi phí và thuyết trình bảo vệ dự án.

---

## 6. ƯỚC TÍNH NGÂN SÁCH (BUDGET ESTIMATE)

Dự án được tối ưu hóa về mặt chi phí nhờ tận dụng tối đa gói **AWS Free Tier (Gói miễn phí)** dành cho các tài khoản mới lập nghiệp (trong vòng 12 tháng đầu).

### Bảng phân tích chi phí ước tính (Mức sử dụng thử nghiệm khoảng 1,000 ảnh/tháng):

| Dịch vụ AWS | Loại chi phí phát sinh | Gói miễn phí Free Tier tương ứng | Chi phí dự kiến/tháng |
| :--- | :--- | :--- | :--- |
| **Amazon S3** | Dung lượng lưu trữ & Request PUT/GET | 5 GB lưu trữ tiêu chuẩn & 2,000 request PUT miễn phí. | **0.00 USD** |
| **AWS Lambda** | Số lượng request & Thời gian chạy (GB-seconds) | 1,000,000 request & 400,000 GB-seconds miễn phí/tháng. | **0.00 USD** |
| **Amazon Rekognition** | Số lượng hình ảnh cần phân tích thực tế | 5,000 hình ảnh miễn phí/tháng. | **0.00 USD** |
| **Amazon DynamoDB** | Dung lượng lưu trữ & Request đọc/ghi | 25 GB dữ liệu lưu trữ & Chế độ On-demand tính phí trên lượng ghi thực tế. | **Gần như 0.00 USD** |
| **CloudWatch Logs** | Dung lượng file log được ghi và lưu trữ | 5 GB dữ liệu ghi log/tháng miễn phí. | **0.00 USD** |
| **Tổng chi phí** | | | **0.00 USD** |

*Lưu ý:* Khi kết thúc thời hạn dùng thử miễn phí, chi phí duy trì hệ thống chạy ẩn cũng cực kỳ nhỏ (chỉ vài cent mỗi tháng cho việc lưu trữ dữ liệu tĩnh trên S3 và DynamoDB) vì hệ thống không hề tốn phí duy trì tài nguyên chạy rỗng (Idle cost).

---

## 7. ĐÁNH GIÁ VÀ GIẢM THIỂU RỦI RO (RISK ASSESSMENT)

| STT | Rủi ro xác định (Risk identified) | Mức độ | Chiến lược giảm thiểu (Mitigation Strategy) |
| :--- | :--- | :--- | :--- |
| 1 | **Rò rỉ AWS Access/Secret Key** lên các nền tảng public như GitHub gây mất an toàn thông tin tài khoản. | Cao | Không lưu thông tin credentials trực tiếp trong code. Sử dụng file ẩn `.env` và khai báo trong `.gitignore`. Áp dụng IAM Roles có thời hạn khi chạy trên Cloud thay vì Access Key cố định. |
| 2 | **Tải tệp tin dung lượng quá lớn** gây nghẽn băng thông hệ thống và làm tăng thời gian chạy của Lambda. | Trung bình | Tích hợp lớp kiểm tra kích thước file (Validation Layer) trên Streamlit Frontend, giới hạn kích thước tối đa là 5MB và chỉ chấp nhận định dạng `.jpg`, `.jpeg`, `.png`. |
| 3 | **Lỗi vòng lặp vô hạn (Infinite Loop)** làm phát sinh chi phí khổng lồ khi Lambda vô tình lưu ảnh kết quả vào cùng thư mục kích hoạt trigger của S3. | Cao | Định cấu hình S3 Event Trigger có giới hạn Prefix cụ thể là `uploads/`. Không cho phép Lambda ghi bất kỳ tệp tin nào ngược lại vào thư mục này. |
| 4 | **Lỗi phân quyền từ chối truy cập (AccessDenied)** khi triển khai ứng dụng thực tế. | Thấp | Kiểm tra log lỗi chi tiết từ AWS CloudWatch và bảng điều khiển S3 để xác định chính xác ARN của tài nguyên bị chặn, từ đó cập nhật Bucket Policy hoặc IAM Policy kịp thời. |

---

## 8. KẾT QUẢ KỲ VỌNG (EXPECTED OUTCOMES)

### Giá trị học thuật và kỹ thuật:
* Làm chủ phương pháp lập trình hướng sự kiện (Event-Driven Programming) trên môi trường điện toán đám mây.
* Thành thạo kỹ năng triển khai, tích hợp các dịch vụ Serverless chính của AWS như S3, Lambda, Rekognition và DynamoDB.
* Có kinh nghiệm thực tiễn trong việc cấu hình phân quyền bảo mật IAM theo đúng tiêu chuẩn an toàn thông tin trong doanh nghiệp.
* Học được cách thiết kế và phát triển mã nguồn sạch dạng Modular để tối ưu hóa dự án.

### Giá trị thực tiễn:
* Tạo ra một nền tảng nhận diện cảm xúc hoạt động ổn định, độ trễ phản hồi thấp, sẵn sàng đưa vào ứng dụng thực tế để tự động hóa quy trình phân tích và thu thập ý kiến khách hàng.
* Dự án đóng vai trò là một minh chứng hoàn chỉnh về năng lực triển khai giải pháp Cloud Computing của bản thân sau khi hoàn thành chương trình thực tập AWS First Cloud Journey.
