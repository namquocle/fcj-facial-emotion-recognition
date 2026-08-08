# =============================================================================
# Project: Serverless Facial Emotion Recognition Analytics Platform
# Description: Lambda function entry point.
#              Processes S3 events and delegates work to helper modules.
# Runtime: Python 3.12
# =============================================================================

import json
import uuid
import logging
from datetime import datetime, timezone
from botocore.exceptions import ClientError

from rekognition_service import analyze_image_with_rekognition, get_dominant_emotion
from dynamodb_service import save_to_dynamodb

# Cấu hình logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event: dict, context) -> dict:
    """
    Entry point của Lambda function.
    Lambda function entry point.

    Luồng xử lý:
    1. Đọc S3 event để lấy bucket & key
    2. Gọi Rekognition helper để nhận dạng
    3. Phân tích cảm xúc
    4. Lưu kết quả vào DynamoDB helper
    """
    logger.info("Lambda invoked. Event: %s", json.dumps(event))
    results = []

    for s3_record in event.get("Records", []):
        try:
            # 1. Trích xuất thông tin S3 từ event
            bucket_name = s3_record["s3"]["bucket"]["name"]
            object_key = s3_record["s3"]["object"]["key"].replace("+", " ")
            image_name = object_key.split("/")[-1]

            logger.info("Processing image: s3://%s/%s", bucket_name, object_key)

            # 2. Gọi Amazon Rekognition
            rekognition_response = analyze_image_with_rekognition(bucket_name, object_key)
            face_details = rekognition_response.get("FaceDetails", [])
            face_count = len(face_details)

            logger.info("Rekognition detected %d face(s) in %s", face_count, image_name)

            # 3. Phân tích cảm xúc
            top_emotion = "NO_FACE_DETECTED"
            confidence_score = 0.0

            if face_count > 0:
                first_face_emotions = face_details[0].get("Emotions", [])
                top_emotion, confidence_score = get_dominant_emotion(first_face_emotions)

            logger.info("Top emotion for %s: %s (%.2f%%)", image_name, top_emotion, confidence_score)

            # 4. Tạo bản ghi log và lưu vào DynamoDB
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
                "confidence": confidence_score,
            })

        except ClientError as boto_err:
            error_msg = boto_err.response["Error"]["Message"]
            logger.error("AWS ClientError processing record: %s", error_msg, exc_info=True)
            results.append({"record": str(s3_record), "status": "FAILED", "error": error_msg})

        except KeyError as key_err:
            logger.error("KeyError parsing S3 event record: %s", key_err, exc_info=True)
            results.append({"record": str(s3_record), "status": "FAILED", "error": str(key_err)})

        except Exception as unexpected_err:
            logger.error("Unexpected error processing record: %s", unexpected_err, exc_info=True)
            results.append({"record": str(s3_record), "status": "FAILED", "error": str(unexpected_err)})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Processing complete",
            "results": results,
        }),
    }