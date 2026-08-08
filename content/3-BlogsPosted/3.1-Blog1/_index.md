---
title: "Blog 1"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Automating AWS Systems Manager Activation for Hybrid-Managed Node Registration

Hello AWS community,

In this post, I would like to summarize an automated solution for managing hybrid infrastructure (on-premises and cloud environments) using AWS Systems Manager (SSM), based on an official article from the AWS Cloud Operations Blog.

## 1. Problem Statement

To manage physical servers or virtual machines (VMs) running in on-premises environments with AWS Systems Manager, administrators must first create a Hybrid Activation to obtain activation credentials, including an **Activation Code** and an **Activation ID**.

However, these credentials are limited by expiration dates and the maximum number of managed nodes that can be registered. Manually recreating activation credentials whenever they expire can be time-consuming and error-prone, especially in large-scale environments.

## 2. Solution Overview

The solution uses AWS CloudFormation to automatically deploy a serverless architecture that provisions and renews activation credentials as needed. The architecture consists of the following AWS services:

### Amazon API Gateway (Private Endpoint)

Provides a private REST API endpoint that allows on-premises servers to securely request activation credentials through a private network connection.

### AWS Lambda

Handles the core business logic. When a request is received from API Gateway, Lambda checks the current activation credentials stored in Parameter Store. If the credentials have expired or reached their registration limit, Lambda automatically calls the AWS Systems Manager API to generate a new activation.

### Amazon DynamoDB

Stores lock states (**Locked / Unlocked**) to prevent race conditions when multiple servers simultaneously request activation credentials.

### AWS Systems Manager Parameter Store

Securely stores the active Activation ID and Activation Code.

### Amazon VPC Endpoint

Ensures that traffic from on-premises environments to the API Gateway remains entirely within private network paths and does not traverse the public Internet.

## 3. Execution Flow

1. An on-premises client server sends a **GET request** to the Private API Gateway.
2. Internal DNS resolves the API URL to the private IP address of the VPC Endpoint.
3. API Gateway forwards the request to AWS Lambda.
4. Lambda acquires a lock in DynamoDB, validates or creates activation credentials, retrieves the information from Parameter Store, and returns a JSON response such as:

```json
{
  "ActivationId": "e50a8437-23dd-4326-9e79-5e3b7573493e",
  "ActivationCode": "vVcH9zJX4ROy2XTsh5cb"
}
```

5. The client uses the returned activation information together with a Linux Shell Script or Windows PowerShell script to automatically install and register the **amazon-ssm-agent** with AWS Systems Manager.

## 4. Solution Evaluation

### Advantages

* Significantly reduces operational overhead by eliminating manual activation management.
* Improves security by keeping communication within private network channels through VPC Endpoints.
* Enables centralized and repeatable infrastructure management using Infrastructure as Code (IaC) with AWS CloudFormation.
* Automatically handles activation renewal and registration limits without administrator intervention.

### Real-World Use Cases

This solution is particularly suitable for:

* Large-scale infrastructure management environments.
* Traditional data centers undergoing cloud migration.
* Organizations implementing hybrid cloud architectures with AWS.
* Enterprises seeking to automate Systems Manager onboarding for on-premises resources.

The complete CloudFormation templates, sample installation scripts, and implementation details can be found in the original AWS article:

**Automate AWS Systems Manager Activation for Hybrid-Managed Node Registration**

*Image: Architecture diagram for automated AWS Systems Manager activation of hybrid-managed nodes.*
![Log_1](/images/3-BlogsPosted/images_Log1.png)

*Reference:* *[Automate AWS Systems Manager activation for hybrid-managed node registration](https://aws.amazon.com/blogs/mt/automate-aws-systems-manager-activation-for-hybrid-managed-node-registration/)*

*Deployment Guide: Deploy the CloudFormation template, configure internal DNS records to point to the VPC Endpoint, and execute the Systems Manager agent registration script on on-premises servers.*

*Posting date: 03/07*

![Log_1](/images/3-BlogsPosted/LogPostComplete1.png)