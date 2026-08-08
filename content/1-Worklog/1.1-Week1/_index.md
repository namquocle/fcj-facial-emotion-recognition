---
title: "Week 1 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

# WEEK 1 (22/06-28/06): GETTING STARTED WITH CLOUD AND CORE INFRASTRUCTURE SERVICES (IAM, VPC, EC2)

## 1. Weekly Objectives

* Become familiar with the AWS Cloud ecosystem through AWS Academy and AWS Educate.
* Understand the AWS Shared Responsibility Model and its role in cloud security.
* Set up and secure an AWS account using IAM best practices.
* Build and configure an isolated virtual network (VPC) for deploying cloud resources such as EC2 instances.

## 2. Tasks Completed

### Account Setup and Security Configuration

* Activated the AWS Academy learning account and enabled Multi-Factor Authentication (MFA) for the Root account to prevent unauthorized access.
* Learned how to create IAM Users and IAM Groups.
* Assigned permissions to groups using AWS Managed Policies such as `AdministratorAccess` (used only for delegated administrator accounts) and `PowerUserAccess`.
* Practiced creating Custom IAM Policies in JSON format to allow a specific IAM user to perform read/write operations only within a designated resource scope.

### AWS VPC (Virtual Private Cloud) Network Setup

* Designed a basic network architecture consisting of one VPC with the CIDR block `10.0.0.0/16`.
* Divided the VPC into two subnets:

  * **Public Subnet:** `10.0.1.0/24`, configured for Internet access through an Internet Gateway (IGW).
  * **Private Subnet:** `10.0.2.0/24`, intended for hosting databases or secure backend services.
* Configured a Route Table for the Public Subnet, routing outbound traffic (`0.0.0.0/0`) through the Internet Gateway.

### Amazon EC2 Deployment

* Launched an Amazon EC2 instance running **Ubuntu Server 22.04 LTS** using the **t2.micro** instance type (AWS Free Tier eligible).
* Created and downloaded a `.pem` Key Pair for secure SSH access from a local machine.
* Configured the Security Group:

  * Allowed SSH access (port 22) only from the personal public IP address (**My IP**).
  * Allowed HTTP access (port 80) from the Internet (`0.0.0.0/0`).
* Successfully connected to the EC2 instance via SSH from a local terminal.
* Performed system updates and installed a test web server (Apache/Nginx) to verify web page accessibility through a browser.

## 3. Knowledge and Skills Acquired

### IAM Security

* Understood the importance of avoiding the Root account for daily administrative activities.
* Learned the difference between:

  * **Security Groups** – Instance-level, stateful firewalls.
  * **Network ACLs** – Subnet-level, stateless firewalls.

### Cloud Networking

* Gained an understanding of routing mechanisms and CIDR-based network segmentation for application environment isolation.

### Linux and EC2 Administration

* Learned how to manage the EC2 instance lifecycle (Start, Stop, and Terminate).
* Developed practical experience securing server access using SSH key authentication.

## 4. Challenges and Troubleshooting

### Challenge

Unable to establish an SSH connection to the EC2 instance after deployment. The connection attempt resulted in a **Connection Timeout** error.

### Resolution

* Verified the Route Table configuration and confirmed whether the subnet containing the EC2 instance was associated with an Internet Gateway.
* Identified that the Security Group had an incorrect SSH source IP range configured.
* Updated the Security Group inbound rule to allow SSH access only from the current **My IP** address, which resolved the issue.

## 5. Outcomes

* Successfully secured the AWS account using IAM best practices and MFA.
* Successfully deployed a standardized VPC environment and an EC2 instance running a web server that is accessible from the Internet.
