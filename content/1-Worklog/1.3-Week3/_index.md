---
title: "Week 3 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.3. </b> "
---

# WEEK 3 (06/07 - 12/07): DEEP DIVE INTO SERVERLESS ARCHITECTURE (AWS LAMBDA) AND AMAZON REKOGNITION

## 1. Weekly Objectives

* Gain an in-depth understanding of the Serverless computing model and AWS Lambda.
* Explore the capabilities of Amazon Rekognition for computer vision and facial analysis.
* Design the detailed system architecture and define the project data flow.

## 2. Tasks Completed

### AWS Lambda Research

* Learned how to configure Lambda memory allocation (from 128 MB to 10 GB) and understood that increasing memory also proportionally increases available CPU resources.
* Studied various Lambda trigger mechanisms from AWS services such as:

  * Amazon S3
  * Amazon API Gateway
  * DynamoDB Streams
* Investigated strategies to mitigate the **Cold Start** issue, including:

  * Configuring **Provisioned Concurrency**
  * Optimizing deployment package size to reduce initialization time

### Amazon Rekognition Research

* Used the AWS Console demonstration tools to experiment with the **Facial Analysis** feature.
* Reviewed the Amazon Rekognition API documentation to understand:

  * The request structure containing the S3 image location.
  * The JSON response structure containing the `FaceDetails` array.
* Studied emotion detection capabilities:

  * Rekognition returns a list of eight emotional states, each associated with a confidence score.
  * Developed the logic required to identify the dominant emotion by selecting the emotion with the highest confidence value.

### System Architecture Design

* Used **Draw.io** to create a complete Serverless system architecture diagram.
* Defined the end-to-end workflow as follows:

  1. A user uploads an image through the frontend application.
  2. The image is stored directly in Amazon S3.
  3. Amazon S3 generates an `ObjectCreated` event.
  4. AWS Lambda is triggered automatically by the event.
  5. Lambda invokes Amazon Rekognition to analyze the image.
  6. The analysis result is stored in Amazon DynamoDB.

## 3. Knowledge and Skills Acquired

### Serverless Architecture Concepts

* Developed a strong understanding of the core advantages of Serverless computing:

  * Automatic scaling from zero to thousands of requests without manual intervention.
  * Pay-as-you-go pricing based on actual usage.
  * Reduced infrastructure management responsibilities.

### AI and Machine Learning Integration

* Learned how to process and interpret the output of a computer vision machine learning model.
* Gained experience working with structured JSON responses and extracting meaningful insights from AI-generated results.

## 4. Challenges and Troubleshooting

### Challenge

The initial system design used AWS Lambda to receive image uploads directly from the frontend and then upload the images to Amazon S3.

This approach introduced several drawbacks:

* Increased Lambda execution time.
* Higher risk of timeout errors.
* Potential payload size limitations, as synchronous Lambda invocations support a maximum payload size of 6 MB.

### Resolution

The architecture was redesigned using an **event-driven approach**:

1. The frontend uploads images directly to Amazon S3.
2. Amazon S3 generates an event after the upload is completed.
3. AWS Lambda processes the image asynchronously.

This design significantly improves scalability, reduces Lambda execution duration, and eliminates upload-related bottlenecks.

## 5. Outcomes

* Successfully completed the architecture design for the **Serverless Facial Emotion Recognition System**.
* Acquired a solid theoretical understanding of AWS Lambda deployment and Amazon Rekognition API integration.
