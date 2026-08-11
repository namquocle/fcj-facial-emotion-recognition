---
title: "Event 2"
date: 2026-08-01
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# BÀI THU HOẠCH “Agent Forge - Deepdive Day 1”

# Mục Đích Của Sự Kiện
- Chia sẻ kiến trúc và best practices trong thiết kế, triển khai hệ thống **Agentic AI** ở quy mô Enterprise.
- Giới thiệu hạ tầng thực thi **AWS Agent Core Runtime** và cơ chế cô lập an toàn bằng **Firecracker MicroVM**.
- Hướng dẫn xây dựng và quản trị tập trung hàng trăm Agent & Tool thông qua **Agent Core Gateway**.
- Giới thiệu các phương pháp chuẩn hóa giao tiếp (**MCP Schema**, **Semantic Search**) và quản trị bảo mật (**Identity**, **HitL**, **Guardrails**).

# Danh Sách Diễn Giả
- **Nghia Tran:** Agentic SA
- **Anh Pham:** Cloud Consultant G-AsiaPasific VietNam

---

# Nội Dung Nổi Bật

## 1. Tổng quan Agent Core Runtime & Hiệu năng Thực thi
* **4 Protocol kết nối chính:**
  * **HTTP/API:** Kết nối tiêu chuẩn cho Web App và Mobile App.
  * **MCP (Model Context Protocol):** Giao thức chuẩn giúp Agent giao tiếp và điều khiển các Tools/Plugins.
  * **Agent-to-Agent:** Cơ chế tương tác đa Agent (Multi-Agent System).
  * **Agent-to-User (Real-time Text Streaming):** Tối ưu hóa trải nghiệm người dùng qua phản hồi liên tục (tương tự ChatGPT), giải quyết bài toán lớn về *Inference Time* và *Response Time*.
* **Hạ tầng Cô lập (Firecracker MicroVM):**
  * Triển khai Agent qua Docker Container trên các MicroVM độc lập hoàn toàn về Compute, Hardware, Memory và File system.
  * Triệt tiêu rủi ro rò rỉ dữ liệu (*Data Leakage*) giữa các User Sessions.
* **Xử lý tác vụ phức tạp:** Hỗ trợ cơ chế **Async & Long-running jobs**, cho phép chia nhỏ bài toán lớn thành các sub-task để Multi-Agent xử lý song song.

## 2. Identity, Authentication & Security
* **Cơ chế Authorization:** Hỗ trợ App ID/Token, OAuth 2.0 (SSO 3-legged), API Key và chuẩn xác thực Payment Host.
* **Lớp Quản lý Identity:** Bao gồm Workload Identity (Work Token), Credentials Management và **Token Vault** (kho lưu trữ Token mã hóa tập trung).
* **Cấu hình Inbound & Outbound:**
  * *Outbound Host:* Tích hợp với AWS Cognito (qua Discovery URL / Client ID) hoặc IDP bên thứ ba.
  * *Inbound Host:* Phân quyền qua AWS IAM Permission (nội bộ AWS) hoặc JWT (Shared/JSON Web Token).

## 3. Agent Core Gateway & Guardrails
* **Giải pháp Mở rộng (Scalability):** Tạo lớp Middleware tập trung quản lý giao tiếp giữa hàng trăm Agent và hàng nghìn Tools/MCP Servers mà không cần kết nối point-to-point.
* **Human-in-the-Loop (HitL):** Cơ chế cho phép Admin xem xét, phê duyệt (**Approve**) hoặc từ chối (**Deny**) các yêu cầu ngoại lệ hoặc vượt quá hạn mức Policy quy định (ví dụ: duyệt yêu cầu refund $200 cho chính sách tiêu chuẩn $100).
* **Guardrails:** Lớp bộ lọc tự động kiểm tra và làm sạch (*sanitize*) dữ liệu nhạy cảm (Sensitive Data/PII) trước khi trả phản hồi về cho User.

## 4. Tool Targets, MCP Schema & Observability
* **Đa dạng Target Types:** Hỗ trợ API Gateway Target, REST OpenAPI, AWS Lambda Target (IAM Policy) và MCP Server Target (Machine-to-Machine / End-to-End Token).
* **Chuẩn MCP Schema:** Bọc Tool bằng lớp JSON Schema (`Name`, `Description`, `Parameters`) giúp Agent hiểu ngữ cảnh công dụng của Tool thay vì gọi Endpoint cứng.
* **Semantic Search:** Tích hợp Indexing tự động tìm kiếm và chỉ tải về các *Useful Tools* thực sự cần thiết, tránh quá tải Context Window.
* **Observability (AWS CloudWatch):** Đẩy toàn bộ Logs, Metrics, Alerts về CloudWatch để lưu vết kiểm toán (*Audit Trail*) cho ngân hàng/tài chính và phục vụ tính phí (*Billing*).

## 5. Kiến trúc Tích hợp Enterprise (Hybrid / On-Premise)
* **Multi-VPC trên AWS:** Các dịch vụ client ở VPC khác kết nối an toàn tới Agent Core Gateway thông qua **NAT Gateway**.
* **On-Premise Client:** Ưu tiên sử dụng kênh kết nối riêng tư (Direct Connect / Private VPN) để đảm bảo an toàn dữ liệu doanh nghiệp thay vì kết nối qua Public Endpoint.

---

# Những Gì Học Được

## Tư Duy Thiết Kế
* **Engine-first approach:** Hiểu rằng Agentic AI là một hệ thống Engine hoàn chỉnh tích hợp giữa Planning, Memory và Identity, không chỉ dừng lại ở một mô hình ngôn ngữ (LLM) đơn lẻ.
* **Governance & Security First:** Bắt buộc phải có lớp Abstraction (Gateway, Token Vault, Guardrails) khi đưa Agent vào môi trường Production thực tế.

## Kiến Trúc Kỹ Thuật
* **MicroVM vs Container Isolation:** Hiểu cách Firecracker MicroVM phân tách cứng tài nguyên tài khoản/session để ngăn rò rỉ dữ liệu.
* **Semantic Tool Routing:** Cách áp dụng Vector Indexing trên Gateway để tối ưu hóa việc chọn Tool cho Agent mà không làm lãng phí Token.
* **Human-in-the-Loop:** Tầm quan trọng của việc kết hợp giữa tự động hóa AI và sự kiểm soát của con người đối với các tác vụ rủi ro cao.

---

# Ứng Dụng Vào Công Việc
* **Chuẩn hóa Tool/API:** Bọc các API/Tool hiện tại trong dự án theo chuẩn cấu trúc **MCP JSON Schema** (`Name`, `Description`, `Parameters`) để Agent dễ dàng hiểu và sử dụng.
* **Áp dụng Real-time Streaming:** Tích hợp Streaming Response API vào giao diện Chatbot để tối ưu trải nghiệm phản hồi người dùng.
* **Thiết kế Middleware Gateway:** Xây dựng lớp trung gian xử lý các chính sách bảo mật, lọc thông tin nhạy cảm (Guardrails) trước khi gửi kết quả về cho client.

---

# Trải nghiệm trong event
Tham gia workshop **“AWS Agent Core Runtime & Agentic AI”** là một trải nghiệm rất bổ ích, giúp em có cái nhìn toàn diện về cách xây dựng, vận hành và bảo mật hệ thống AI Agent ở quy mô doanh nghiệp. Một số trải nghiệm nổi bật:

## Học hỏi từ các diễn giả có chuyên môn cao
* Nghe chia sẻ thực tế về gần 100 slides lý thuyết chuyên sâu, đi từ tổng quan Agentic AI đến các bài toán phức tạp về Inference Time và Data Leakage.
* Tiếp thu cách AWS giải quyết bài toán mở rộng (Scaling) từ vài Agent lên hàng trăm Agent thông qua lớp Middleware Gateway.

## Trải nghiệm kỹ thuật thực tế & Hands-on Lab
* Nắm vững bức tranh tổng thể qua các trụ cột: Planning, Memory, Identity, Guardrails và Observability.
* Tham gia phiên **Hands-on Lab** ngay sau buổi lý thuyết giúp chuyển hóa các khái niệm trừu tượng (như MicroVM, MCP Schema, NAT Gateway) thành kỹ năng thực hành thực tế.

---

# Bài học rút ra
* **Thực hành là yếu tố quyết định:** Khối lượng lý thuyết về Agentic AI rất lớn và dễ quên; việc kết hợp Hands-on Lab ngay sau bài giảng giúp khắc sâu kiến thức.
* **Cân bằng giữa Automation và Control:** Không nên để AI hoàn toàn tự quyết định ở các nghiệp vụ quan trọng; cơ chế **Human-in-the-Loop** là mắt xích bắt buộc để đảm bảo an toàn cho hệ thống Enterprise.
* **Lộ trình triển khai rõ ràng:** Chuyển đổi từ các Use Cases cơ bản đến nâng cao và tuân thủ chặt chẽ các Best Practices của AWS khi đưa Agentic System vào hệ thống Production.

## Một số hình ảnh khi tham gia sự kiện
![MeetEvent2-1](/images/4-EventParticipated/MeetEvent2-1.jpg)
![MeetEvent2-2](/images/4-EventParticipated/MeetEvent2-2.jpg)
![MeetEvent2-3](/images/4-EventParticipated/MeetEvent2-3.jpg)