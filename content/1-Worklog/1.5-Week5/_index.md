---
title: "Week 5 Worklog"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 1.5. </b> "
---

# WEEK 5 (20/07 - 26/07): PROJECT IMPLEMENTATION – PHASE 2: DEVELOPING AWS LAMBDA WITH PYTHON AND BOTO3

## 1. Weekly Objectives

* Develop the core event-processing logic for AWS Lambda using Python.
* Utilize the AWS SDK for Python (`boto3`) to interact with Amazon Rekognition and DynamoDB.
* Ensure the application can gracefully handle exceptional cases such as images without detectable faces or incompatible input data.

## 2. Tasks Completed

### Local Development Setup and Source Code Implementation

* Developed the main Lambda source file, `lambda_function.py`.
* Initialized the `boto3.client('rekognition')` and `boto3.resource('dynamodb')` objects outside the main `lambda_handler` function to take advantage of Lambda's execution environment reuse (warm containers), improving overall performance and reducing initialization overhead.

### S3 Event Processing Logic

* Implemented a loop to process all records contained in the S3 event payload.
* Used URL decoding techniques to correctly handle special characters in S3 object keys, including spaces and encoded symbols.

### Amazon Rekognition Integration

* Developed the function `analyze_image_with_rekognition()` to invoke the Amazon Rekognition `detect_faces` API on images stored in Amazon S3.
* Configured the API request with:

```text
Attributes=['ALL']
```

to enable comprehensive facial attribute and emotion analysis.

### Dominant Emotion Detection Logic

* Implemented the function `get_dominant_emotion()` to process the list of emotions returned by Rekognition.
* Utilized Python's built-in `max()` function with the confidence score as the comparison key to identify the most likely emotion.
* Added logic to handle images where no faces are detected:

  * Set the emotion label to `NO_FACE_DETECTED`.
  * Set the confidence score to `0.0`.

### DynamoDB Data Persistence

* Used the DynamoDB `put_item()` operation to store emotion analysis results in the `FaceEmotionLogs` table.
* Technical consideration:

  * Converted floating-point confidence values into string format before storage because DynamoDB enforces strict numeric type handling, which can cause serialization issues when using native Python floating-point values.

## 3. Knowledge and Skills Acquired

### AWS SDK (boto3) Development

* Gained practical experience using boto3 to interact with:

  * Amazon S3
  * Amazon Rekognition
  * Amazon DynamoDB
* Developed a solid understanding of API request structures, response formats, and service integration patterns.

### Exception Handling and Reliability

* Learned how to build resilient Lambda functions using `try...except ClientError` blocks.
* Improved the application's ability to handle unexpected input and service exceptions without causing system crashes.

## 4. Challenges and Troubleshooting

### Challenge

During testing, the Lambda function generated the following error when processing landscape images that did not contain any human faces:

```text
KeyError: 'Emotions'
```

This occurred because Amazon Rekognition returned an empty `FaceDetails` array, resulting in the absence of emotion-related data.

### Resolution

* Added validation logic to verify the number of elements returned in the `FaceDetails` array.
* If no faces are detected (`len(FaceDetails) == 0`):

  * Skip the emotion-processing workflow.
  * Assign the predefined label `NO_FACE_DETECTED`.
  * Continue execution without generating an exception.

This enhancement improved the stability and robustness of the Lambda function.

## 5. Outcomes

* Successfully completed the development of the `lambda_function.py` source code and deployed it to AWS Lambda.
* Verified that the application operates reliably in the testing environment.
* Confirmed successful integration with Amazon Rekognition and DynamoDB.
* Validated that all execution logs are properly captured and monitored through Amazon CloudWatch.
