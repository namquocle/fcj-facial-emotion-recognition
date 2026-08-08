---
title: "Event 3"
date: 2026-08-01
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# REPORT ON “Agent Forge - Deepdive Day 2”

## Event Purpose
- **Share best practices:** Provide a clear roadmap for building and developing a career as a Cloud & AI Engineer during the first three years.
- **Introduce Agentic AI Architecture:** Dive deep into the Level L300 (Advanced) architecture of the Amazon Bedrock Agent Core ecosystem.
- **System Storage & Supervision:** Introduce mechanisms for managing Memory, comprehensive monitoring (Observability), and quality evaluation (Evaluation) for AI Agents.
- **Expansion & Safety Controls:** Present extended capabilities including Policy enforcement (Cedar Language), Human-in-the-Loop mechanisms, Agent Browser, Payment integration, Registry, Optimization (Red Teaming), and Agent Harness architecture.

---

## Speakers List
- **Nghia Tran:** Agentic SA
- **Anh Pham:** Cloud Consultant G-AsiaPasific VietNam

---

## Key Highlights

### 1. Development Roadmap for AI & Cloud Engineers (First 3 Years)
- **Year 1:** Focus deeply on a single core technical skill. Advance applications from *Prototype/Pilot* to *Production* systems to build execution confidence.
- **Year 2:** Expand knowledge into supporting domains that back production environments (Network Engineering, cost estimation, data engineering, etc.).
- **Year 3:** Deepen domain-specific and business logic knowledge to build a multi-dimensional growth model (**Breadth & Depth**).
- **Necessary & Sufficient Conditions:** Certifications (e.g., AWS) are an encouraging plus. The sufficient conditions are practical hard skills (Security, cost optimization, monitoring, responsible AI mindset) and soft skills (explaining technical concepts to non-technical stakeholders, ownership mindset).

### 2. AI Market Context & Workshop Introduction
- **Technology Trends:** The AI market in Vietnam is booming across Fintech, Manufacturing, Logistics, EdTech, HealthTech, and Developer Tools. AI is rapidly shifting from *Generative AI* to *Agentic AI* (utilizing advanced techniques like *Harness Engineering* and *Loop Engineering*).
- **Agentic Force Workshop Series (3 Days):**
  - **Day 1:** Agentic AI Overview; 3 core pillars (*Runtime*, *Gateway*, *Identity*).
  - **Day 2 (Current Session):** 3 core pillars (*Memory*, *Evaluation*, *Observability*) and extended features.
  - **Day 3:** DevOps, Real-World Use Cases, and Best Practices for Enterprise-grade Agentic Systems.

### 3. Agent Core Memory
- **Context Window Limits & The Need for Memory:** Token limits (256k–1M) are heavily consumed by System Prompts, Tools, Rules, etc. Memory serves as a bridge between *Short-term Conversation* and *Long-term Understanding*, enabling personalized user experiences.
- **Short-term & Long-term Memory Mechanics:**
  - *Short-term (Synchronous):* Stores raw messages, *Agent State*, and *Timestamp* as *Events* managed by Agent Core.
  - *Long-term (Asynchronous):* A parallel *Memory Extraction* module extracts *Key Insights/Knowledge* and compresses them into Vector representations.
  - *Best Practice:* When re-initiating a conversation, the Agent combines the most recent short-term messages with long-term insights to optimize token context usage.
- **Data Structure & Management:** Hierarchical organization (`Memory ID` → `Actor ID` → `Session ID` → `Event`). Uses Namespace folder paths (`/Strategy/Actor/Exception`) to isolate data and narrow retrieval scopes.
- **4 Long-term Strategies:** *Summary*, *User Preference*, *Semantic*, *Episodic*.

### 4. Agent Core Observability
- **Philosophy:** *"You cannot fix what you cannot see"* — A dedicated supervision layer is required to debug and optimize system behavior.
- **Latency Analysis:** Root-cause latency across 3 tiers: *User Input* (excessively long prompts) → *Agent Level* (suboptimal system prompts, indexing delay for tools) → *Infra Level* (GPU/CPU resource overload during request spikes).
- **3 Pillars of Observability:**
  - *Log (What happened):* Records error logs and request/report streams.
  * *Trace (How it happened):* Tracks execution flow across `Conversation` → `Span` → `Subspan`.
  * *Metric (How much it affected):* Measures token consumption, latency metrics, and resource utilization.
- **Integration & Pricing:** Standardized via **OpenTelemetry** protocols with pay-as-you-go pricing similar to **AWS CloudWatch**.

### 5. Agent Core Evaluation
- **Purpose:** Evaluates the accuracy (*Correctness*), usefulness (*Helpfulness*), and goal completion capability (*Goal Achievement*) of the Agent.
- **2 Evaluation Modes:** *On-demand* (used in Dev environments prior to release) and *Online* (real-time continuous monitoring on Production).
- **3 Evaluation Criteria Levels:**
  - *Session Level:* Evaluates overall conversation goals.
  - *Trace Level:* Evaluates response quality and safety (preventing *Harmful Content* or sensitive data exposure).
  * *Span Level:* Evaluates tool selection accuracy and parameter passing correctness.
- **Mechanisms & SME Role:** Combines automated *Built-in Evaluators / LLM Judge* with domain experts (*Subject Matter Experts - SMEs*) to benchmark *Predicted Responses* against *Ground Truth Responses*.

### 6. Extended Control Features & Mechanisms
- **Policy & Cedar Language:** Implements *If-Else* style business rules enforcing the **Least Privilege** principle. Engineers can write policies in *Plain English*, which the system automatically validates and converts into **Cedar Language**.
- **Human-in-the-Loop:** Enables manual Admin review (Approve/Deny) for sensitive or high-threshold actions (e.g., approving order refunds over $100).
- **Agent Core Browser:** An isolated, secure browser environment enabling Agents to perform Web Navigation, Data Scraping, and Workflow Automation safely.
- **Payment Integration:** Connects with payment gateways (Stripe, MoMo, VietQR, PayOS, etc.) to allow automated financial transactions for Trading, Finance, and Market Research.
- **Registry & A2A Protocol:** A centralized hub within the enterprise for sharing and reusing Agents, Skills, and Tools. Supports **Agent-to-Agent (A2A)** protocols for inter-agent communication.
- **Optimization & Red Teaming:** Optimizes Agent performance through a 4-step pipeline (driven by Observability/Evaluation data) and simulates attack vectors (*Red Teaming*) to patch security vulnerabilities.
- **Agent Harness Engineering:** Decouples the Agent into a lightweight core comprising 3 elements (*LLM Model, System Prompt, Internal Tools*). External integrations are delegated to the Harness layer to facilitate seamless *Horizontal Scaling*.

---

## Key Takeaways & Insights

### Design Mindset
- **Product & Enterprise Mindset:** Designing an AI Agent requires more than simple prompt engineering; it demands an enterprise-grade system perspective embracing security, monitoring, cost optimization, and authority controls.
- **Abstraction & Microservices Decoupling:** Understanding how AWS abstracts complex mechanisms into console controls, alongside leveraging Agent Harness decomposition for horizontal scalability.
- **Least Privilege Principle:** Strictly implementing Policies and Human-in-the-Loop controls to govern Agent actions, preventing unvetted execution on Production systems.

### Technical Architecture
- **Memory Differentiation & Orchestration:** Mastering the distinction between Short-term Memory (synchronous raw chat logging) and Long-term Memory (asynchronous vector extraction), combining both to keep context windows lean.
- **3-Pillared Monitoring Techniques:** Utilizing Logs, Traces (Conversation → Span → Subspan), and Metrics via OpenTelemetry to proactively catch bugs and mitigate latency bottlenecks.
- **Multi-level Evaluation Workflow:** Applying built-in evaluators, LLM Judges, and SME validations to measure Agent effectiveness scientifically based on empirical data rather than intuition.

### Control & Growth Strategy
- **Agent Lifecycle Optimization:** A closed-loop pipeline spanning *Development* → *Evaluation* → *Optimization (A/B Testing & Red Teaming)* → *Production*.
- **Enterprise Resource Reuse:** Leveraging Agent Registries and A2A protocols to share APIs, tools, and skills across engineering teams, eliminating redundant development efforts.

---

## Practical Application to Work Projects
- **Optimizing Current Chatbot Projects:** Implementing a hybrid Short-term & Long-term Memory architecture to preserve consultation context without blowing past LLM context limits.
- **Integrating Observability & Logging Layers:** Setting up inference latency metrics and centralized log collection to streamline debugging and prompt iteration.
- **Establishing Safety Policy Rules:** Applying Policy definitions (Cedar Language) and Human-in-the-Loop workflows for high-risk system operations.
- **Community Engagement & Practice:** Actively competing in enterprise Hackathons and collaborating within the *First Cloud Hand-on Journey (FCH)* community to sharpen hands-on skills.

---

## Event Experience

### Learning from Industry Experts
- Direct insights from Mr. Gia Hung Nguyen, Mr. Hieu, and Senior AWS Solution Architects who regularly build and deploy large-scale Enterprise Cloud/AI systems.
- A dense, **140-slide** presentation delivered at Level L300 (Advanced), providing a comprehensive view of modern AI infrastructure.

### Practical Technical Hands-on
- Direct exposure to standardized infrastructure on Amazon Bedrock Agent Core.
- Engaging in hands-on labs directly inside the **AWS Console** right after the theoretical lecture, translating complex concepts into concrete configuration steps.

### Final Thoughts
- A core hard skill for an AI Engineer is not merely training models, but possessing the capability to make models *Production Ready* in a secure, compliant, and cost-effective manner.
- AI technologies are advancing at a rapid pace (from Generative AI to Agentic AI, Harness Engineering, and Loop Engineering); continuous monthly learning is mandatory to remain at the cutting edge.

## Event Media & Photographs
![MeetEvent3-1](/images/4-EventParticipated/MeetEvent3-1.jpg)
![MeetEvent3-2](/images/4-EventParticipated/MeetEvent3-2.jpg)
![MeetEvent3-3](/images/4-EventParticipated/MeetEvent3-3.jpg)