---
title: "Self-Assessment"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---
# 6. Self-evaluation

This section contains my personal self-evaluation for the **AWS Workforce Bootcamp - First Cloud AI Journey** internship program. It outlines the knowledge acquired, key achievements, self-assessment criteria, strengths, areas for improvement, and my future development objectives.

---

## 🏆 Key Achievements

### 1. Technical Knowledge & Practical Skills
- **Cloud Computing & Serverless Architectures:** Developed a deep understanding of core AWS services. Built a fully functional serverless event-driven pipeline utilizing **Amazon S3** (Object Storage), **AWS Lambda** (Serverless Compute), and **Amazon DynamoDB** (NoSQL Database).
- **Artificial Intelligence Integration:** Gained practical experience in Computer Vision by integrating **Amazon Rekognition** (using the `DetectFaces` API) to detect facial structures, analyze emotional indices, and compute dominant emotions.
- **Frontend Development:** Mastered building clean, modern, and responsive user interfaces using the **Streamlit** Python framework, integrating direct cloud uploads using the **boto3** SDK.
- **Modular Clean-Code Design:** Refactored a monolithic codebase into single-responsibility, modular files, improving maintainability, validation, and ease of troubleshooting.

### 2. Professional & Soft Skills
- **Technical Documentation:** Authored a comprehensive, professional, and bilingual (English/Vietnamese) technical report and workshop guide, enhancing my ability to explain complex cloud workflows clearly.
- **Problem-Solving & Troubleshooting:** Successfully resolved integration roadblocks, such as virtual environment dependency conflicts, local AWS credential linkages, and database data-type compatibility issues (e.g., DynamoDB numeric formats).
- **Time Management:** Maintained steady progress by following a strict weekly plan, documenting milestones sequentially in the project Worklog.

---

## 📊 Self-Assessment Criteria

The table below outlines my self-evaluation across key performance indicators (KPIs) during the internship:

| Criteria | Completion | Score (1-5) | Notes / Detailed Evaluation |
| :--- | :---: | :---: | :--- |
| **Progress & Deliverables** (Worklog & Proposal) | 95% | 4.8 / 5.0 | All weekly milestones were completed on time. The final project proposal was well-structured and aligned with programmatic guidelines. |
| **Blog & Workshop Quality** (Blogs & Workshop) | 90% | 4.5 / 5.0 | Authored detailed step-by-step guides using Hugo-compliant Markdown and alert boxes. Code blocks are fully tested, functional, and split into clean modules. |
| **Proactivity & Research Initiative** (Events & Research) | 90% | 4.5 / 5.0 | Actively researched AWS pricing models, cost-avoidance strategies, IAM policy configurations, and Python boto3 client performance optimization (e.g. Lambda container reuse). |

---

## 🔍 Strengths & Areas for Improvement

### Strengths
- **Rapid Technology Adaptation:** Able to quickly research, learn, and implement unfamiliar cloud APIs and framework concepts (such as S3 event triggers and Streamlit state caches).
- **Logical Troubleshooting:** Methodical in isolating and resolving runtime bugs (e.g., debugging AWS authentication errors and handling float-to-string conversions for DynamoDB storage).
- **Documentation Integrity:** Highly committed to writing clear, structured documentation, ensuring code comments and step-by-step guides are intuitive for other developers.

### Areas for Improvement
- **Infrastructure as Code (IaC):** While comfortable configuring resources manually in the AWS Console, I need to learn to automate deployments using tools like **AWS CloudFormation** or **Terraform**.
- **Automated Security Best Practices:** Want to dive deeper into advanced security rules, such as configuring KMS customer-managed keys for data encryption at rest in S3 and DynamoDB.
- **Advanced Automated Testing:** Need to incorporate automated unit tests (e.g. using `pytest` and `moto` to mock AWS services) rather than relying entirely on manual end-to-end runs.

---

## 🚀 Future Action Plan

1. **Obtain AWS Certification:** Prepare for and pass the **AWS Certified Cloud Practitioner** or **AWS Certified Solutions Architect – Associate** exam within the next 3 months to formalize my cloud computing skills.
2. **Master Infrastructure as Code (IaC):** Transition from manual console setups to deploying all backend infrastructure (VPC, Lambda, DynamoDB, S3) using **Terraform** or **AWS SAM (Serverless Application Model)** in my next project.
3. **Explore Advanced DevSecOps:** Learn to build automated CI/CD pipelines (e.g., using GitHub Actions) that execute code linting, run unit tests, and automatically deploy serverless functions to AWS staging environments.
