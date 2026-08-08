---
title : "Main Modules"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---
# 5.3. Backend & AWS Services Setup

In this module, you will configure the backend resources on AWS and deploy the serverless event processing Lambda function.

---

## Step 1: Create Amazon S3 Bucket

The S3 bucket stores the uploaded images, which acts as the entry trigger for our serverless pipeline.

1. Open the **Amazon S3 Console**.
![Picture_16](/images/5-Workshop/16.png)
2. Click **Create bucket**.
![Picture_17](/images/5-Workshop/17.png)
3. Configure the following settings:
   - **Bucket name:** `my-facial-emotion-recognition-<your-unique-suffix>` (S3 bucket names must be globally unique).
   - **AWS Region:** Select `ap-southeast-1` (Singapore) or your preferred region.
   ![Picture_18](/images/5-Workshop/18.png)
   - Keep **Block all public access** enabled (best practice).
   ![Picture_19](/images/5-Workshop/19.png)
4. Click **Create bucket** at the bottom of the page.
![Picture_20](/images/5-Workshop/20.png)

---

## Step 2: Create Amazon DynamoDB Table

The DynamoDB table stores the metadata logs for every analyzed image.

1. Open the **Amazon DynamoDB Console**.
![Picture_21](/images/5-Workshop/21.png)
2. Click **Create table**.
![Picture_22](/images/5-Workshop/22.png)
3. Configure the settings:
   - **Table name:** `FaceEmotionLogs`.
   - **Partition key:** `LogID` (Type: `String`).
   - Keep default settings.
   ![Picture_23](/images/5-Workshop/23.png)
4. Click **Create table**.
![Picture_24](/images/5-Workshop/24.png)
![Picture_25](/images/5-Workshop/25.png)

---

## Step 3: Create IAM Execution Role for Lambda

The Lambda function needs permissions to read objects from S3, call Rekognition APIs, and write data into DynamoDB.

1. Open the **IAM Console**.
2. Click **Roles** -> **Create role**.
![Picture_26](/images/5-Workshop/26.png)
![Picture_27](/images/5-Workshop/27.png)
3. Under **Trusted entity type**, choose **AWS service**, and select **Lambda** from the service dropdown. Click **Next**.
![Picture_28](/images/5-Workshop/28.png)
4. Click **Create policy** (this opens a new tab). Go to the **JSON** tab and paste the following policy:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "logs:CreateLogGroup",
                   "logs:CreateLogStream",
                   "logs:PutLogEvents"
               ],
               "Resource": "arn:aws:logs:*:*:*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject"
               ],
               "Resource": "arn:aws:s3:::my-facial-emotion-recognition-*/*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "rekognition:DetectFaces"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "dynamodb:PutItem"
               ],
               "Resource": "arn:aws:dynamodb:*:*:table/FaceEmotionLogs"
           }
       ]
   }
   ```
   ![Picture_29](/images/5-Workshop/29.png)
   ![Picture_30](/images/5-Workshop/30.png)
   ![Picture_31](/images/5-Workshop/31.png)
5. Click **Next**, name the policy `workshop-lambda-policy`, and click **Create policy**.
![Picture_32](/images/5-Workshop/32.png)
![Picture_33](/images/5-Workshop/33.png)
![Picture_34](/images/5-Workshop/34.png)
6. Return to the **Create role** tab, refresh the policies list, search for and check `workshop-lambda-policy`. Click **Next**.
![Picture_35](/images/5-Workshop/35.png)
7. Name the role `workshop-lambda-role` and click **Create role**.
![Picture_36](/images/5-Workshop/36.png)
![Picture_37](/images/5-Workshop/37.png)

---

## Step 4: Write Lambda Code Modules

Create three Python files in a folder named `backend/` on your local machine.

### 4.1. Rekognition Service (`rekognition_service.py`)
This helper calls the Rekognition client to run face analysis.

```python
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

rekognition_client = boto3.client("rekognition")

def get_dominant_emotion(emotions: list) -> tuple[str, float]:
    """Finds the emotion with the highest confidence score."""
    if not emotions:
        return "UNKNOWN", 0.0
    dominant = max(emotions, key=lambda e: e.get("Confidence", 0))
    return dominant.get("Type", "UNKNOWN"), round(dominant.get("Confidence", 0.0), 2)

def analyze_image_with_rekognition(bucket: str, key: str) -> dict:
    """Calls Amazon Rekognition to analyze faces in an S3 image."""
    logger.info("Calling Rekognition for s3://%s/%s", bucket, key)
    response = rekognition_client.detect_faces(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        Attributes=["ALL"],
    )
    return response
```

### 4.2. DynamoDB Service (`dynamodb_service.py`)
This helper writes records to DynamoDB.

```python
import os
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dynamodb_resource = boto3.resource("dynamodb")
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME", "FaceEmotionLogs")

def save_to_dynamodb(record: dict) -> None:
    """Saves the facial analysis log record to DynamoDB."""
    table = dynamodb_resource.Table(DYNAMODB_TABLE_NAME)
    item = {
        "LogID":      record["LogID"],
        "Timestamp":  record["Timestamp"],
        "ImageName":  record["ImageName"],
        "FaceCount":  record["FaceCount"],
        "TopEmotion": record["TopEmotion"],
        "Confidence": str(record["Confidence"]), # Decimal conversion
    }
    table.put_item(Item=item)
    logger.info("Saved record LogID=%s to DynamoDB", record["LogID"])
```

### 4.3. Lambda Handler Entrypoint (`lambda_function.py`)
This is the entry coordinator file that is invoked by S3 events.

```python
import json
import uuid
import logging
from datetime import datetime, timezone
from botocore.exceptions import ClientError

from rekognition_service import analyze_image_with_rekognition, get_dominant_emotion
from dynamodb_service import save_to_dynamodb

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def lambda_handler(event: dict, context) -> dict:
    logger.info("Lambda invoked. Event: %s", json.dumps(event))
    results = []

    for s3_record in event.get("Records", []):
        try:
            bucket_name = s3_record["s3"]["bucket"]["name"]
            object_key = s3_record["s3"]["object"]["key"].replace("+", " ")
            image_name = object_key.split("/")[-1]

            logger.info("Processing image: s3://%s/%s", bucket_name, object_key)

            # 1. Invoke Amazon Rekognition
            rekognition_response = analyze_image_with_rekognition(bucket_name, object_key)
            face_details = rekognition_response.get("FaceDetails", [])
            face_count = len(face_details)

            # 2. Extract top emotion
            top_emotion = "NO_FACE_DETECTED"
            confidence_score = 0.0
            if face_count > 0:
                first_face_emotions = face_details[0].get("Emotions", [])
                top_emotion, confidence_score = get_dominant_emotion(first_face_emotions)

            # 3. Save logs to DynamoDB
            log_record = {
                "LogID":      str(uuid.uuid4()),
                "Timestamp":  datetime.now(timezone.utc).isoformat(),
                "ImageName":  image_name,
                "FaceCount":  face_count,
                "TopEmotion": top_emotion,
                "Confidence": confidence_score,
            }
            save_to_dynamodb(log_record)

            results.append({
                "image": image_name,
                "status": "SUCCESS",
                "topEmotion": top_emotion,
                "confidence": confidence_score
            })
        except Exception as err:
            logger.error("Error processing record: %s", err, exc_info=True)
            results.append({"status": "FAILED", "error": str(err)})

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Processing complete", "results": results})
    }
```

---

## Step 5: Package & Deploy Lambda Function

1. Zip the three files together locally:
   ```bash
   zip -j lambda_function.zip lambda_function.py rekognition_service.py dynamodb_service.py
   ```
2. Open the **AWS Lambda Console** and click **Create function**.
![Picture_38](/images/5-Workshop/38.png)
3. Configure the settings:
   - Choose **Author from scratch**.
   - **Function name:** `FaceEmotionRecognitionHandler`.
   - **Runtime:** `Python 3.12`.
   ![Picture_39](/images/5-Workshop/39.png)
   - Under **Change default execution role**, choose **Use an existing role** and select `workshop-lambda-role`.
   ![Picture_40](/images/5-Workshop/40.png)
4. Click **Create function**.
![Picture_41](/images/5-Workshop/41.png)
5. In the **Code** tab, click **Upload from** -> **.zip file** and upload your `lambda_function.zip` file.
![Picture_42](/images/5-Workshop/42.png)
![Picture_43](/images/5-Workshop/43.png)
![Picture_44](/images/5-Workshop/44.png)

---

## Step 6: Configure S3 Bucket Event Trigger

1. Go back to your bucket in the **Amazon S3 Console**.
2. Select the **Properties** tab.
![Picture_45](/images/5-Workshop/45.png)
3. Scroll down to **Event notifications** and click **Create event notification**.
![Picture_46](/images/5-Workshop/46.png)
4. Configure the settings:
   - **Event name:** `TriggerLambdaOnUpload`.
   - **Prefix:** `uploads/` (Ensures only images uploaded to the `uploads/` folder trigger processing).
   ![Picture_47](/images/5-Workshop/47.png)
   - **Event types:** Under **Object creation**, check **All object create events**.
   ![Picture_48](/images/5-Workshop/48.png)
   - **Destination:** Choose **Lambda function** and select your `FaceEmotionRecognitionHandler` from the dropdown list.
5. Click **Save changes**.
![Picture_49](/images/5-Workshop/49.png)
