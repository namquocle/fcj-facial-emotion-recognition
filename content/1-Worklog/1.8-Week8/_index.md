---
title: "Week 8 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.8. </b> "
---

# WEEK 8 (10/08 - 15/08): COMPLETING THE BILINGUAL TECHNICAL REPORT, RESOURCE CLEAN-UP GUIDE, AND INTERNSHIP PROGRAM SUMMARY

## 1. Weekly Objectives

* Complete a comprehensive internship report documenting the project architecture, source code implementation, and testing results.
* Develop a resource clean-up guide to prevent unnecessary AWS charges after project completion.
* Summarize the knowledge, skills, and achievements gained throughout the 8-week AWS First Cloud Journey internship program.

## 2. Tasks Completed

### Bilingual Technical Report Development

* Prepared a detailed technical report in both Vietnamese and English.
* Documented the complete system architecture, including:

  * Amazon S3 configuration
  * AWS Lambda implementation
  * Amazon DynamoDB setup
  * IAM security policies
  * Modular source code structure
* Included supporting evidence and screenshots demonstrating successful system testing, such as:

  * Sample input images
  * DynamoDB log records
  * CloudWatch execution logs
  * End-to-end workflow validation results

### Resource Clean-Up Guide Development

* Created a step-by-step guide for safely removing AWS resources after project completion to avoid unexpected cloud charges.

#### Resource Removal Procedure

1. Access the Amazon S3 bucket.

   * Permanently delete all uploaded images and object versions.
   * Delete the S3 bucket after it becomes empty.

2. Access Amazon DynamoDB.

   * Locate the `FaceEmotionLogs` table.
   * Delete the table to stop storage-related charges.

3. Access AWS Lambda.

   * Delete the `FaceEmotionRecognizer` function.
   * Remove associated deployment packages and configurations.

4. Access Amazon CloudWatch Logs.

   * Delete Lambda-related Log Groups.
   * Prevent additional log storage costs.

5. Access AWS IAM.

   * Delete the IAM user `streamlit-s3-uploader`.
   * Delete the IAM role `LambdaEmotionRecognitionRole`.
   * Revoke all project-related access permissions.

### Internship Program Wrap-Up

* Reviewed the overall project progress and achievements throughout the internship period.
* Prepared an acknowledgment section expressing gratitude to mentors and instructors who provided guidance and support during the program.
* Developed presentation slides and demonstration materials for the final project evaluation and internship defense session.

## 3. Knowledge and Skills Acquired

### Technical Documentation Skills

* Improved the ability to write professional technical documentation.
* Learned how to communicate complex technical concepts in a clear and structured manner for both technical and non-technical audiences.
* Developed experience creating bilingual project reports suitable for academic and professional environments.

### Cloud Cost Management (FinOps)

* Gained a deeper understanding of cloud resource lifecycle management.
* Learned the importance of regularly reviewing and removing unused resources to optimize infrastructure costs.
* Developed awareness of operational best practices for maintaining cost-efficient cloud environments.

## 4. Challenges and Troubleshooting

### Challenge

Deleting an Amazon S3 bucket occasionally failed because the bucket still contained previous object versions created when Versioning was enabled during Week 2.

### Resolution

* Updated the clean-up guide with detailed instructions explaining that users must delete:

  * Current objects
  * Previous object versions
  * Delete markers

before attempting to remove the bucket itself.

* Verified the deletion process through testing to ensure complete bucket removal without errors.

## 5. Outcomes

* Successfully completed a comprehensive internship report exceeding 15 pages, including architecture diagrams, implementation details, testing results, and project analysis.
* Produced a detailed AWS resource clean-up guide to support future project maintenance and cost optimization.
* Completed all internship objectives and project deliverables.
* Received a certificate of completion from the **AWS First Cloud Journey** internship program.
* Successfully prepared project demonstration materials and presentation slides for the final evaluation session.
