---
title: "Week 2 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.2. </b> "
---

# WEEK 2 (29/06 - 05/07): OBJECT STORAGE AND CLOUD DATABASES (AMAZON S3 & AMAZON DYNAMODB)

## 1. Weekly Objectives

* Learn about Amazon S3 object storage and static data management policies.
* Understand the differences between relational databases (SQL) and non-relational databases (NoSQL) in cloud environments.
* Practice creating tables and performing queries using Amazon DynamoDB.
* Finalize the internship project idea: **Serverless Facial Emotion Recognition Analytics Platform**.

## 2. Tasks Completed

### Amazon S3 Hands-on Practice

* Created an Amazon S3 bucket with a globally unique name and learned the Key-Value storage structure of S3, where the **Key** represents the file path and the **Value** represents the file content.
* Enabled **Versioning** to manage multiple versions of the same object, allowing recovery of accidentally deleted or modified files.
* Configured **S3 Lifecycle Rules**:

  * Automatically transition objects to the **Standard-IA (Infrequent Access)** storage class after 30 days.
  * Automatically delete objects permanently or archive them to **Amazon S3 Glacier** after 90 days to optimize storage costs.
* Configured an **S3 Bucket Policy** to allow read access (`GetObject`) only from IP addresses belonging to the company's or university's internal network.

### Amazon DynamoDB Hands-on Practice

* Created a test table in DynamoDB.
* Configured:

  * **Partition Key:** `ID`
  * **Sort Key:** `Timestamp`
* Practiced common operations using both the AWS Console and AWS CLI:

  * `PutItem` (insert data)
  * `GetItem` (retrieve data)
  * `Scan` (scan the entire table)
  * `Query` (efficient data retrieval based on keys)
* Explored DynamoDB capacity management options:

  * **Provisioned Capacity with Auto Scaling**
  * **On-Demand Capacity Mode**

### Project Planning and Architecture Design

* Analyzed the project requirements for a facial emotion recognition system:

  * Amazon S3 was selected for reliable image storage.
  * Amazon DynamoDB was selected for storing lightweight analysis logs that require fast retrieval by ID.
* Drafted the initial architecture and workflow for the serverless solution.

## 3. Knowledge and Skills Acquired

### S3 Storage Classes

* Learned the cost and performance differences among:

  * S3 Standard
  * S3 Standard-IA
  * S3 One Zone-IA
  * S3 Glacier
* Understood how to choose appropriate storage classes to optimize AWS costs while maintaining required accessibility.

### NoSQL Databases

* Gained a clear understanding of DynamoDB's schema-less design.
* Learned why DynamoDB is well suited for application logging workloads due to:

  * Millisecond-level read and write latency.
  * Extremely high scalability and availability.
  * Fully managed infrastructure without the need to maintain operating systems, database servers, or caching layers as required in traditional SQL databases such as Amazon RDS.

## 4. Challenges and Troubleshooting

### Challenge

Encountered an **Access Denied** error when attempting to access image files stored in an S3 bucket through a web browser, despite having configured a Bucket Policy that allowed access.

### Resolution

* Identified that **S3 Block Public Access** was enabled by default at the bucket/account level, which overrode the Bucket Policy settings.
* Updated the configuration by disabling the conflicting Block Public Access setting and refining permissions to provide read-only access exclusively for authorized internal applications.

## 5. Outcomes

* Successfully acquired practical skills in working with Amazon S3 and Amazon DynamoDB.
* Completed and presented the project proposal for the **Serverless Facial Emotion Recognition Analytics Platform**, which was reviewed and approved by the internship mentor.
