---
title : "Các bước thực hiện"
date : 2024-01-01 
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---
# 5.3. Cấu hình Backend & Dịch vụ AWS

Trong phần này, bạn sẽ cấu hình các tài nguyên backend trên AWS và triển khai hàm xử lý sự kiện không máy chủ (Lambda function).

---

## Bước 1: Tạo Amazon S3 Bucket

S3 bucket dùng để lưu trữ các hình ảnh tải lên, đóng vai trò là tác nhân kích hoạt cho pipeline serverless của chúng ta.

1. Mở **Amazon S3 Console**.
![Picture_16](/images/5-Workshop/16.png)
2. Chọn **Create bucket** (Tạo bucket).
![Picture_17](/images/5-Workshop/17.png)
3. Cấu hình các thông số sau:
   - **Bucket name:** `my-facial-emotion-recognition-<hậu-tố-duy-nhất>` (Tên S3 bucket phải là duy nhất trên toàn cầu).
   - **AWS Region:** Chọn `ap-southeast-1` (Singapore) hoặc vùng bạn mong muốn.
   ![Picture_18](/images/5-Workshop/18.png)
   - Giữ nguyên tùy chọn **Block all public access** (Chặn tất cả quyền truy cập công khai - Khuyến nghị bảo mật).
   ![Picture_19](/images/5-Workshop/19.png)
4. Chọn **Create bucket** ở cuối trang.
![Picture_20](/images/5-Workshop/20.png)

---

## Bước 2: Tạo Bảng Amazon DynamoDB

Bảng DynamoDB sẽ lưu trữ nhật ký siêu dữ liệu phân tích cảm xúc của từng hình ảnh đã được xử lý.

1. Mở **Amazon DynamoDB Console**.
![Picture_21](/images/5-Workshop/21.png)
2. Chọn **Create table** (Tạo bảng).
![Picture_22](/images/5-Workshop/22.png)
3. Cấu hình các thông số:
   - **Table name:** `FaceEmotionLogs`.
   - **Partition key:** `LogID` (Kiểu dữ liệu: `String`).
   - Giữ nguyên các cấu hình mặc định khác.
   ![Picture_23](/images/5-Workshop/23.png)
4. Chọn **Create table**.
![Picture_24](/images/5-Workshop/24.png)
![Picture_25](/images/5-Workshop/25.png)

---

## Bước 3: Tạo IAM Execution Role cho Lambda

Hàm Lambda cần có quyền đọc đối tượng từ S3, gọi các API của Rekognition và ghi dữ liệu vào DynamoDB.

1. Mở **IAM Console**.
2. Chọn **Roles** (Vai trò) -> **Create role** (Tạo vai trò).
![Picture_26](/images/5-Workshop/26.png)
![Picture_27](/images/5-Workshop/27.png)
3. Trong phần **Trusted entity type** (Loại thực thể tin cậy), chọn **AWS service** (Dịch vụ AWS) và chọn **Lambda** từ danh sách dịch vụ. Nhấp **Next**.
![Picture_28](/images/5-Workshop/28.png)
4. Chọn **Create policy** (Tạo chính sách - hành động này sẽ mở ra một tab mới). Chuyển sang tab **JSON** và dán chính sách sau:
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
5. Nhấp **Next**, đặt tên cho chính sách là `workshop-lambda-policy` và nhấp **Create policy**.
![Picture_32](/images/5-Workshop/32.png)
![Picture_33](/images/5-Workshop/33.png)
![Picture_34](/images/5-Workshop/34.png)
6. Quay lại tab **Create role**, tải lại danh sách chính sách, tìm kiếm và tích chọn `workshop-lambda-policy`. Nhấp **Next**.
![Picture_35](/images/5-Workshop/35.png)
7. Đặt tên cho vai trò là `workshop-lambda-role` và chọn **Create role**.
![Picture_36](/images/5-Workshop/36.png)
![Picture_37](/images/5-Workshop/37.png)

---

## Bước 4: Viết các Module mã nguồn cho Lambda

Tạo ba tệp Python trong một thư mục có tên là `backend/` trên máy tính của bạn.

### 4.1. Rekognition Service (`rekognition_service.py`)
Module hỗ trợ gọi client Rekognition để phân tích khuôn mặt.

```python
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

rekognition_client = boto3.client("rekognition")

def get_dominant_emotion(emotions: list) -> tuple[str, float]:
    """Tìm cảm xúc chủ đạo có độ tin cậy cao nhất."""
    if not emotions:
        return "UNKNOWN", 0.0
    dominant = max(emotions, key=lambda e: e.get("Confidence", 0))
    return dominant.get("Type", "UNKNOWN"), round(dominant.get("Confidence", 0.0), 2)

def analyze_image_with_rekognition(bucket: str, key: str) -> dict:
    """Gọi Amazon Rekognition để phân tích khuôn mặt trong ảnh lưu trên S3."""
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
Module hỗ trợ ghi các bản ghi nhật ký vào DynamoDB.

```python
import os
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

dynamodb_resource = boto3.resource("dynamodb")
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME", "FaceEmotionLogs")

def save_to_dynamodb(record: dict) -> None:
    """Lưu bản ghi nhật ký phân tích khuôn mặt vào DynamoDB."""
    table = dynamodb_resource.Table(DYNAMODB_TABLE_NAME)
    item = {
        "LogID":      record["LogID"],
        "Timestamp":  record["Timestamp"],
        "ImageName":  record["ImageName"],
        "FaceCount":  record["FaceCount"],
        "TopEmotion": record["TopEmotion"],
        "Confidence": str(record["Confidence"]), # Chuyển đổi Decimal
    }
    table.put_item(Item=item)
    logger.info("Saved record LogID=%s to DynamoDB", record["LogID"])
```

### 4.3. Lambda Handler Entrypoint (`lambda_function.py`)
Đây là tệp điều phối chính nhận sự kiện từ S3 và thực hiện pipeline.

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

            # 1. Gọi Amazon Rekognition
            rekognition_response = analyze_image_with_rekognition(bucket_name, object_key)
            face_details = rekognition_response.get("FaceDetails", [])
            face_count = len(face_details)

            # 2. Phân tích cảm xúc
            top_emotion = "NO_FACE_DETECTED"
            confidence_score = 0.0
            if face_count > 0:
                first_face_emotions = face_details[0].get("Emotions", [])
                top_emotion, confidence_score = get_dominant_emotion(first_face_emotions)

            # 3. Lưu log vào DynamoDB
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

## Bước 5: Đóng gói & Triển khai Lambda Function

1. Tiến hành nén ba tệp tin trên thành một file `.zip` duy nhất trên máy tính của bạn:
   ```bash
   zip -j lambda_function.zip lambda_function.py rekognition_service.py dynamodb_service.py
   ```
2. Mở **AWS Lambda Console** và chọn **Create function** (Tạo hàm).
![Picture_38](/images/5-Workshop/38.png)
3. Cấu hình các thông số:
   - Chọn **Author from scratch** (Tác giả từ đầu).
   - **Function name:** `FaceEmotionRecognitionHandler`.
   - **Runtime:** Chọn `Python 3.12`.
   ![Picture_39](/images/5-Workshop/39.png)
   - Trong phần **Change default execution role**, chọn **Use an existing role** (Sử dụng vai trò có sẵn) và chọn vai trò `workshop-lambda-role` đã tạo ở Bước 3.
   ![Picture_40](/images/5-Workshop/40.png)
4. Chọn **Create function**.
![Picture_41](/images/5-Workshop/41.png)
5. Tại tab **Code**, chọn **Upload from** -> **.zip file** và tải lên tệp `lambda_function.zip` của bạn.
![Picture_42](/images/5-Workshop/42.png)
![Picture_43](/images/5-Workshop/43.png)
![Picture_44](/images/5-Workshop/44.png)

---

## Bước 6: Cấu hình Sự kiện Kích hoạt S3 (S3 Event Trigger)

1. Quay lại trang quản lý bucket của bạn trên **Amazon S3 Console**.
2. Chọn tab **Properties** (Thuộc tính).
![Picture_45](/images/5-Workshop/45.png)
3. Cuộn xuống phần **Event notifications** (Thông báo sự kiện) và chọn **Create event notification**.
![Picture_46](/images/5-Workshop/46.png)
4. Cấu hình các thông số:
   - **Event name:** `TriggerLambdaOnUpload`.
   - **Prefix:** `uploads/` (Đảm bảo chỉ có các ảnh được tải lên thư mục `uploads/` mới kích hoạt xử lý).
   ![Picture_47](/images/5-Workshop/47.png)
   - **Event types:** Trong phần **Object creation**, tích chọn **All object create events**.
   ![Picture_48](/images/5-Workshop/48.png)
   - **Destination:** Chọn **Lambda function** và chọn hàm `FaceEmotionRecognitionHandler` của bạn từ danh sách.
5. Chọn **Save changes**.
![Picture_49](/images/5-Workshop/49.png)
