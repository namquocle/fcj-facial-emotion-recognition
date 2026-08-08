---
title: "Blog 3"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.3. </b> "
---

# Building an AI-Powered Amazon Redshift Performance Advisor with Amazon Bedrock

## 1. Problem Statement & Challenges

Operating large-scale data platforms on Amazon Redshift requires continuous performance monitoring and optimization. However, performance tuning remains a complex and time-consuming task for data engineering teams due to several challenges:

* Telemetry data is distributed across multiple system views such as `SYS_QUERY_HISTORY`, `SVV_TABLE_INFO`, `SVV_ALTER_TABLE_RECOMMENDATIONS`, and various Amazon CloudWatch metrics.
* Interpreting performance data often requires extensive manual investigation. For example, correlating a spike in commit time (QueryRuntimeBreakdown) with hundreds of small INSERT statements or identifying disk spill issues caused by insufficient compute resources can take hours of analysis.

## 2. Architecture Overview

This solution implements a fully serverless, signal-based architecture that automatically generates Amazon Redshift performance recommendations using generative AI.

Rather than sending raw telemetry data directly to a Large Language Model (LLM), the system first calculates performance signals and correlates them with CloudWatch metrics. This enriched context is then provided to Amazon Bedrock, enabling the AI model to produce more accurate and actionable recommendations.

The workflow runs on a 24-hour schedule using Amazon EventBridge and consists of two primary Lambda functions:

### Collector Lambda

The Collector Lambda performs the following tasks:

* Executes 13 diagnostic SQL queries against Amazon Redshift Serverless.
* Retrieves Workload Management (WLM) configuration information.
* Collects relevant Amazon CloudWatch metrics.
* Generates performance signals from the collected data.
* Stores telemetry information as JSON files in Amazon S3.

### Analyzer Lambda

The Analyzer Lambda:

* Reads telemetry JSON files from Amazon S3.
* Constructs a structured prompt containing correlated CloudWatch metrics and performance signals.
* Invokes Amazon Bedrock using the Anthropic Claude Sonnet model.
* Generates optimization recommendations and stores the resulting JSON report in Amazon S3.

### Amazon SNS

Amazon SNS distributes email notifications containing the most important optimization recommendations directly to database administrators and platform teams.

## 3. Basic Deployment Steps

### Step 1: Configure Supporting Resources

Create the required supporting infrastructure:

* An Amazon S3 bucket for telemetry and recommendation reports.
* An Amazon SNS topic and subscription for email notifications.
* AWS Secrets Manager secrets to securely store Amazon Redshift credentials.

### Step 2: Create IAM Roles

Configure least-privilege IAM roles that allow the Lambda functions to interact with:

* Amazon Redshift Data API
* Amazon S3
* Amazon SNS
* Amazon Bedrock
* Amazon CloudWatch

### Step 3: Deploy and Configure Lambda Functions

Package and deploy:

* `collector.py` together with the diagnostic SQL files.
* `analyzer.py`.

Configure the required environment variables, including:

* `WORKGROUP`
* `DATABASE`
* `SECRET_ARN`
* `MODEL_ID`

### Step 4: Schedule and Test the Workflow

Create an Amazon EventBridge rule to trigger the workflow every 24 hours.

Perform a manual test from the AWS Console to verify that the entire end-to-end process works correctly, from telemetry collection through AI analysis and notification delivery.

## 4. Key Benefits

### Highly Actionable Recommendations

Because performance signals are precomputed and contextualized before being sent to the AI model, the generated recommendations are highly specific rather than generic.

Recommendations can directly reference:

* Query IDs
* Table names
* Actual performance metrics
* Resource utilization statistics

### Clear Prioritization

Each recommendation includes:

* Priority level (Critical, High, Medium, or Low)
* Category classification (Query Optimization, Table Design, Capacity Planning, Maintenance, and more)

This enables platform teams to efficiently prioritize remediation efforts.

### Improved Operational Efficiency

The solution reduces manual performance analysis from several hours to just a few minutes by automatically generating detailed optimization reports.

It also helps engineers quickly identify critical issues such as:

* Severe row skew
* Missing column compression
* Inefficient workload management configurations
* Resource bottlenecks and disk spill events

The complete implementation, sample SQL diagnostics, and deployment resources are available in the GitHub repository **sample-ai-performance-advisor-for-amazon-redshift**.

*Image: Architecture diagram for an AI-powered Amazon Redshift Performance Advisor.*
![Log_3](/images/3-BlogsPosted/images_Log3.png)

*Reference:* *[sample-ai-performance-advisor-for-amazon-redshift on GitHub](https://github.com/aws-samples/sample-ai-performance-advisor-for-amazon-redshift)*

*Deployment Guide: Create the Amazon S3 bucket and SNS topic, apply least-privilege IAM roles, and configure the required Lambda environment variables before deployment.*

*Posting date: 27/07*

![Log_3](/images/3-BlogsPosted/LogPostComplete3.png)