import os
import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Khởi tạo DynamoDB client ở ngoài handler để tối ưu hiệu năng
dynamodb_resource = boto3.resource("dynamodb")
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME", "FaceEmotionLogs")

def save_to_dynamodb(record: dict) -> None:
    """
    Lưu bản ghi phân tích cảm xúc vào bảng DynamoDB.

    Args:
        record (dict): Dữ liệu cần lưu
    """
    table = dynamodb_resource.Table(DYNAMODB_TABLE_NAME)

    # DynamoDB không hỗ trợ float trực tiếp, chuyển về str
    item = {
        "LogID":      record["LogID"],
        "Timestamp":  record["Timestamp"],
        "ImageName":  record["ImageName"],
        "FaceCount":  record["FaceCount"],
        "TopEmotion": record["TopEmotion"],
        "Confidence": str(record["Confidence"]),
    }

    table.put_item(Item=item)
    logger.info("Saved record LogID=%s to DynamoDB table %s", record["LogID"], DYNAMODB_TABLE_NAME)
