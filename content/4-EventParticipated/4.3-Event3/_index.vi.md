---
title: "Event 3"
date: 2026-08-08
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# BÀI THU HOẠCH “Agent Forge - Deepdive Day 2”

## Mục Đích Của Sự Kiện
- **Chia sẻ best practices:** Cung cấp lộ trình xây dựng và phát triển sự nghiệp kỹ sư Cloud & AI trong 3 năm đầu.
- **Giới thiệu kiến trúc Agentic AI:** Đi sâu vào kiến trúc nâng cao Level L300 (Advanced) của hệ sinh thái Amazon Bedrock Agent Core.
- **Lưu trữ & Giám sát hệ thống:** Giới thiệu cơ chế quản lý bộ nhớ (Memory), khả năng giám sát toàn diện (Observability) và đánh giá chất lượng (Evaluation) của AI Agent.
- **Mở rộng & Kiểm soát an toàn:** Giới thiệu các tính năng mở rộng như Policy (Cedar Language), Human-in-the-Loop, Agent Browser, Payment, Registry, Optimization (Red Teaming) và kiến trúc Agent Harness.

---

## Danh Sách Diễn Giả
- **Nghia Tran:** Agentic SA
- **Anh Pham:** Cloud Consultant G-AsiaPasific VietNam

---

## Nội Dung Nổi Bật

### 1. Lộ trình phát triển Kỹ sư AI & Cloud (3 năm đầu)
- **Năm 1:** Tập trung chuyên sâu vào một kỹ năng kỹ thuật cốt lõi, phát triển ứng dụng từ mô hình *Prototype/Pilot* chuyển sang hệ thống *Production* để tạo dựng sự tự tin.
- **Năm 2:** Mở rộng kiến thức sang các mảng phụ trợ hỗ trợ mô hình sản xuất (Network Engineering, quản lý chi phí, dữ liệu,...).
- **Năm 3:** Bồi đắp kiến thức chuyên môn & nghiệp vụ ngành để xây dựng mô hình phát triển đa chiều (**Rộng & Sâu**).
- **Điều kiện cần và đủ:** Chứng chỉ (như AWS) chỉ là điểm khuyến khích. Điều kiện đủ là kỹ năng cứng thực tế (Security, tối ưu chi phí, giám sát, tư duy AI an toàn/có trách nhiệm) và kỹ năng mềm (giao tiếp technical cho non-technical, tư duy làm chủ).

### 2. Bối cảnh Thị trường AI & Giới thiệu Workshop
- **Xu hướng công nghệ:** Thị trường AI Việt Nam bùng nổ trong các ngành Fintech, Sản xuất, Logistics, EdTech, HealthTech và Developer Tools. AI chuyển dịch mạnh mẽ từ *Generative AI* sang *Agentic AI* (với các kỹ thuật *Harness Engineering*, *Loop Engineering*).
- **Chuỗi Workshop Agentic Force (3 Ngày):**
  - **Day 1:** Tổng quan Agentic AI; 3 trụ cột *Runtime*, *Gateway*, *Identity*.
  - **Day 2 (Buổi hiện tại):** 3 trụ cột *Memory*, *Evaluation*, *Observability* và các tính năng mở rộng.
  - **Day 3:** DevOps, Use Cases và Best Practices cho hệ thống Agentic mức Enterprise.

### 3. Agent Core Memory
- **Giới hạn Context Window & Lý do cần Memory:** Giới hạn Token (256k–1M) bị tiêu tốn bởi System Prompt, Tools, Rules,... Memory đóng vai trò là cầu nối giữa *Short-term Conversation* và *Long-term Understanding*, giúp cá nhân hóa (Personalization) trải nghiệm người dùng.
- **Cơ chế Short-term & Long-term Memory:**
  - *Short-term (Đồng bộ - Synchronous):* Lưu trữ tin nhắn thô (*raw messages*), *Agent State*, *Timestamp* thành các *Events* do Agent Core quản lý.
  - *Long-term (Bất đồng bộ - Asynchronous):* Module *Memory Extraction* tự động trích xuất các *Key Insights/Knowledge* nén thành Vector.
  - *Best Practice:* Khi tái khởi tạo hội thoại, Agent kết hợp một phần tin nhắn gần nhất từ Short-term và các insight từ Long-term để tiết kiệm token.
- **Cấu trúc dữ liệu & Quản lý:** Phân cấp dữ liệu theo `Memory ID` → `Actor ID` → `Session ID` → `Event`. Sử dụng định dạng thư mục Namespace (`/Strategy/Actor/Exception`) giúp cô lập dữ liệu và thu hẹp phạm vi truy xuất.
- **4 Chiến lược Long-term (Strategies):** *Summary*, *User Preference*, *Semantic*, *Episodic*.

### 4. Agent Core Observability
- **Triết lý:** *"You cannot fix what you cannot see"* — Cần lớp giám sát để debug và tối ưu hệ thống.
- **Phân tích Latency (Độ trễ):** Xác định nguyên nhân gây trễ từ 3 tầng: *User Input* (Prompt quá dài) → *Agent Level* (System Prompt chưa tối ưu, tốn thời gian index Tools) → *Infra Level* (GPU/CPU quá tải khi request tăng đột biến).
- **3 Trụ cột Observability:**
  - *Log (What happened):* Ghi nhận lỗi và các luồng request/report.
  - *Trace (How it happened):* Theo dõi chuỗi diễn biến qua các cấp `Conversation` → `Span` → `Subspan`.
  - *Metric (How much it affected):* Đo lường chi phí token, độ trễ và tài nguyên tiêu thụ.
- **Tích hợp & Chi phí:** Chuẩn hóa qua giao thức **OpenTelemetry**, mô hình tính phí pay-as-you-go tương tự **AWS CloudWatch**.

### 5. Agent Core Evaluation
- **Mục đích:** Đánh giá tính chính xác (*Correctness*), độ hữu ích (*Helpfulness*) và khả năng hoàn thành mục tiêu (*Goal Achievement*) của Agent.
- **2 Chế độ Đánh giá:** *On-demand* (dùng trong môi trường Dev trước khi release) và *Online* (đánh giá Real-time trên Production).
- **3 Cấp độ Đánh giá (Criteria Levels):**
  - *Session Level:* Đánh giá mục tiêu tổng thể cuộc hội thoại.
  - *Trace Level:* Đánh giá chất lượng câu trả lời và độ an toàn (tránh *Harmful content*, rò rỉ thông tin cá nhân).
  - *Span Level:* Đánh giá việc chọn đúng Tool và truyền đúng tham số.
- **Cơ chế & Vai trò SME:** Kết hợp giữa *Built-in Evaluators / LLM Judge* tự động và chuyên gia lĩnh vực (*Subject Matter Expert - SME*) để so sánh giữa câu trả lời dự đoán (*Predicted Response*) và câu trả lời chuẩn (*Ground Truth Response*).

### 6. Các tính năng & Cơ chế kiểm soát mở rộng
- **Policy & Cedar Language:** Thiết lập bộ quy tắc nghiệp vụ dạng *If-Else* kiểm soát hành vi Agent theo nguyên tắc **Least Privilege** (tối thiểu quyền hạn). Kỹ sư có thể nhập policy bằng tiếng Anh tự nhiên (*Plain English*), hệ thống tự chuyển đổi sang **Cedar Language**.
- **Human-in-the-Loop:** Cơ chế cho phép Admin trực tiếp kiểm duyệt (Approve/Deny) đối với các tác vụ nhạy cảm hoặc vượt ngưỡng (ví dụ: duyệt hoàn tiền đơn hàng > $100).
- **Agent Core Browser:** Môi trường Browser cách ly an toàn cho Agent thực hiện Web Navigation, Data Scraping và Workflow Automation.
- **Payment Integration:** Tích hợp các cổng thanh toán (Stripe, MoMo, VietQR, PayOS...) giúp Agent thực hiện giao dịch tự động trong Trading, Finance, Market Research.
- **Registry & A2A Protocol:** Hub quản lý tập trung trong doanh nghiệp giúp tái sử dụng Agent/Skill/Tool. Hỗ trợ giao thức **Agent-to-Agent (A2A)** cho phép các Agent tự kết nối với nhau.
- **Optimization & Red Teaming:** Tối ưu hóa hiệu năng Agent qua 4 bước (dựa trên data từ Observability/Evaluation) và giả lập kịch bản tấn công (*Red Teaming*) để vá lỗ hổng bảo mật.
- **Agent Harness Engineering:** Phân rã Agent thành mô hình tối giản gồm 3 phần (*LLM Model, System Prompt, Internal Tools*), mọi khả năng mở rộng kết nối được đảm nhận bởi lớp Harness giúp hệ thống dễ dàng mở rộng theo chiều ngang (*Horizontal Scaling*).

---

## Những Gì Học Được

### Tư Duy Thiết Kế
- **Product & Enterprise Mindset:** Xây dựng Agent không chỉ dừng ở việc prompt đơn giản mà cần tư duy hệ thống enterprise: bảo mật, giám sát, tối ưu chi phí và kiểm soát thẩm quyền.
- **Trừu tượng hóa & Phân rã Microservices:** Hiểu cách AWS trừu tượng hóa (*abstract*) các cơ chế phức tạp thành vài thao tác click trên Console, đồng thời áp dụng mô hình phân rã Agent Harness để dễ mở rộng theo chiều ngang.
- **Nguyên tắc Tối thiểu Quyền hạn (Least Privilege):** Bắt buộc phải áp dụng Policy và Human-in-the-Loop để kiểm soát hành vi của Agent, tránh trường hợp Agent tự do thực thi gây hậu quả tiêu cực trên môi trường Production.

### Kiến Trúc Kỹ Thuật
- **Phân biệt & Phối hợp Memory:** Nắm rõ sự khác biệt giữa Short-term Memory (đồng bộ, lưu raw chat) và Long-term Memory (bất đồng bộ, trích xuất vector insight) cũng như cách kết hợp cả hai để tối ưu Context Window.
- **Kỹ thuật Giám sát 3 Trụ cột:** Sử dụng Log, Trace (Conversation → Span → Subspan) và Metric thông qua chuẩn OpenTelemetry để chủ động phát hiện lỗi và xử lý trễ (Latency).
- **Quy trình Đánh giá Đa cấp độ:** Áp dụng các Evaluator tích hợp, LLM Judge và chuyên gia SME để đo lường hiệu quả Agent một cách khoa học dựa trên số liệu thực tế chứ không dựa vào cảm tính.

### Chiến Lược Kiểm Soát & Phát Triển
- **Hành trình Tối ưu hóa Vòng đời Agent:** Quy trình khép kín từ *Development* $\rightarrow$ *Evaluation* → *Optimization (A/B Testing & Red Teaming)* → *Production*.
- **Tái sử dụng Tài nguyên Doanh nghiệp:** Tận dụng Agent Registry và giao thức A2A để chia sẻ API, Tool và Skill giữa các phòng ban, tránh lãng phí tài nguyên phát triển.

---

## Ứng Dụng Vào Công Việc
- **Tối ưu dự án Chatbot hiện tại:** Áp dụng mô hình kết hợp Short-term & Long-term Memory để lưu giữ ngữ cảnh tư vấn mà không làm quá tải Context Window của LLM.
- **Tích hợp Lớp Observability & Logging:** Thiết lập các chỉ số theo dõi đợt suy luận (Latency) và lưu trữ log tập trung để phục vụ việc debug và cải thiện prompt.
- **Xây dựng Bộ Quy tắc Safety Policy:** Áp dụng tư duy thiết lập Policy (Cedar Language) và cơ chế Human-in-the-Loop đối với các tác vụ quan trọng trong hệ thống.
- **Tham gia Cộng đồng & Thực hành:** Tích cực cọ xát tại các cuộc thi Hackathon doanh nghiệp và cộng đồng *First Cloud Hand-on Journey (FCH)* để nâng cao tay nghề thực tế.

---

## Trải Nghiệm Trong Event

### Học hỏi từ các diễn giả có chuyên môn cao
- Được lắng nghe chia sẻ từ anh Nguyễn Gia Hưng, anh Hiếu và các Senior Solution Architects từ AWS — những người trực tiếp triển khai các hệ thống Cloud/AI lớn cho doanh nghiệp.
- Bài giảng nén gọn **140 slide** lý thuyết Level L300 (Advanced) mang lại cái nhìn chuyên sâu và toàn diện về hạ tầng AI hiện đại.

### Trải nghiệm kỹ thuật thực tế
- Tiếp thu trực tiếp kiến thức chuẩn hóa về hạ tầng Amazon Bedrock Agent Core.
- Được tham gia phần thực hành hands-on trực tiếp trên **AWS Console** ngay sau phiên lý thuyết, giúp chuyển hóa kiến thức phức tạp thành thao tác cấu hình thực tế.

### Bài học rút ra
- Kỹ năng cứng cốt lõi của một Kỹ sư AI không chỉ là huấn luyện mô hình, mà còn là năng lực đưa mô hình vào môi trường sản xuất (*Production Ready*) một cách an toàn, bảo mật và tối ưu chi phí.
- Công nghệ AI tiến triển rất nhanh (từ Generative AI đến Agentic AI, Harness Engineering, Loop Engineering); việc liên tục cập nhật kiến thức hàng tháng là bắt buộc để không bị lạc hậu.

## Một Số Hình Ảnh Khi Tham Gia Sự Kiện
![MeetEvent3-1](/images/4-EventParticipated/MeetEvent3-1.jpg)
![MeetEvent3-2](/images/4-EventParticipated/MeetEvent3-2.jpg)
![MeetEvent3-3](/images/4-EventParticipated/MeetEvent3-3.jpg)

---
