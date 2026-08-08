---
title: "Event 2"
date: 2026-08-01
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# REPORT ON “Agent Forge - Deepdive Day 1”

# Purpose of the Event
- Share best practices and architectural patterns for designing and deploying **Agentic AI** systems at enterprise scale.
- Introduce the **AWS Agent Core Runtime** execution environment and its isolation mechanism using **Firecracker MicroVM**.
- Guide the centralized management and governance of hundreds of Agents and Tools via **Agent Core Gateway**.
- Introduce standardization protocols (**MCP Schema**, **Semantic Search**) and security/governance mechanisms (**Identity**, **HitL**, **Guardrails**).

# Speakers
- **Nghia Tran:** Agentic SA
- **Anh Pham:** Cloud Consultant G-AsiaPasific VietNam

---

# Key Highlights

## 1. Overview of Agent Core Runtime & Execution Performance
* **4 Core Connection Protocols:**
  * **HTTP/API:** Standard connection for Web and Mobile applications.
  * **MCP (Model Context Protocol):** Standard protocol enabling Agents to communicate with and control Tools/Plugins.
  * **Agent-to-Agent:** Mechanism for Multi-Agent interaction and task coordination.
  * **Agent-to-User (Real-time Text Streaming):** Optimizes user experience via continuous response streaming (similar to ChatGPT), solving key challenges around *Inference Time* and *Response Time*.
* **Isolation Infrastructure (Firecracker MicroVM):**
  * Deploying Agents via Docker Containers on MicroVMs with complete separation of Compute, Hardware, Memory, and File systems.
  * Eliminates *Data Leakage* risks between different User Sessions.
* **Handling Complex Tasks:** Supports **Async & Long-running jobs**, allowing complex tasks to be decomposed into sub-tasks for parallel processing across Multi-Agents.

## 2. Identity, Authentication & Security
* **Authorization Mechanisms:** Supports App ID/Token, OAuth 2.0 (3-legged SSO), API Key, and Payment Host authentication standards.
* **Identity Management Layer:** Manages Workload Identity (Work Tokens), Credentials, and an encrypted **Token Vault** for secure key storage.
* **Inbound & Outbound Configuration:**
  * *Outbound Host:* Integrates seamlessly with AWS Cognito (via Discovery URL / Client ID) or third-party Identity Providers (IdP).
  * *Inbound Host:* Managed via AWS IAM Permissions (within AWS) or JWT (Shared/JSON Web Tokens).

## 3. Agent Core Gateway & Guardrails
* **Scalability Solution:** Provides a centralized Middleware layer to manage communications between hundreds of Agents and thousands of Tools/MCP Servers without requiring point-to-point connections.
* **Human-in-the-Loop (HitL):** Mechanism allowing Admins to review, **Approve**, or **Deny** exception requests or actions exceeding configured policies (e.g., approving a $200 refund request when the default policy limit is $100).
* **Guardrails:** Automated filtering layer that sanitizes sensitive data (PII / Confidential data) before returning the response to the user.

## 4. Tool Targets, MCP Schema & Observability
* **Diverse Target Types:** Supports API Gateway Targets, REST OpenAPI, AWS Lambda Targets (IAM Policy), and MCP Server Targets (Machine-to-Machine / End-to-End Tokens).
* **Standard MCP Schema:** Wraps Tools with JSON Schema definitions (`Name`, `Description`, `Parameters`), helping Agents understand tool capabilities semantically rather than relying on hardcoded API endpoints.
* **Semantic Search:** Utilizes Vector Indexing to automatically discover and retrieve only the most relevant *Useful Tools*, preventing Context Window bloat.
* **Observability (AWS CloudWatch):** Streams all Logs, Metrics, and Alerts to CloudWatch for audit trails (compliance in banking/finance) and billing calculations.

## 5. Enterprise Integration Architecture (Hybrid / On-Premise)
* **Multi-VPC on AWS:** Client services in separate VPCs connect securely to the Agent Core Gateway via **NAT Gateway**.
* **On-Premise Clients:** Prefers dedicated private channels (Direct Connect / Private VPN) to guarantee enterprise data security over public internet endpoints.

---

# Key Learnings

## Design Thinking
* **Engine-first approach:** Recognizing that Agentic AI is a complete engine system combining Planning, Memory, and Identity, rather than just a standalone Large Language Model (LLM).
* **Governance & Security First:** Establishing abstraction layers (Gateway, Token Vault, Guardrails) is mandatory when promoting Agents to production environments.

## Technical Architecture
* **MicroVM vs. Container Isolation:** Understanding how Firecracker MicroVMs enforce hard resource boundaries per session to prevent cross-tenant data leaks.
* **Semantic Tool Routing:** Applying Vector Indexing at the Gateway level to optimize tool selection without wasting LLM tokens.
* **Human-in-the-Loop:** The necessity of balancing AI automation with human oversight for high-risk operations.

---

# Application to Work
* **Standardizing Tools/APIs:** Wrapping existing project APIs/Tools into **MCP JSON Schema** format (`Name`, `Description`, `Parameters`) for seamless Agent interaction.
* **Implementing Real-time Streaming:** Integrating Streaming Response APIs into Chatbot interfaces to improve latency and user experience.
* **Building Middleware Gateways:** Designing custom middleware to enforce security policies and filter sensitive data (Guardrails) before serving responses to clients.

---

# Event Experience
Participating in the **“AWS Agent Core Runtime & Agentic AI Workshop”** was an extremely insightful experience, providing a comprehensive overview of building, operating, and securing AI Agent systems at an enterprise scale. Key takeaways include:

## Learning from Expert Speakers
* Gained deep insights from nearly 100 technical slides covering everything from Agentic AI foundations to complex challenges like Inference Time optimization and Data Leakage prevention.
* Learned how AWS addresses scaling challenges when moving from a few Agents to hundreds via centralized Middleware Gateways.

## Practical Technical Experience & Hands-on Lab
* Mastered the core architectural pillars: Planning, Memory, Identity, Guardrails, and Observability.
* Participated in the **Hands-on Lab** session immediately following the lecture, translating abstract technical concepts (such as MicroVMs, MCP Schema, NAT Gateway) into practical implementation skills.

---

# Lessons Learned
* **Hands-on Practice is Crucial:** The theoretical scope of Agentic AI is vast; applying concepts immediately in a lab setting is essential for retention.
* **Balancing Automation and Control:** High-value or sensitive operations should not rely purely on AI autonomy; **Human-in-the-Loop** mechanisms are essential for enterprise safety.
* **Structured Roadmap:** Successful adoption requires progressing from basic to advanced use cases while adhering strictly to AWS Best Practices for production deployment.

## Event Photos
![MeetEvent2-1](/images/4-EventParticipated/MeetEvent2-1.jpg)
![MeetEvent2-2](/images/4-EventParticipated/MeetEvent2-2.jpg)
![MeetEvent2-3](/images/4-EventParticipated/MeetEvent2-3.jpg)