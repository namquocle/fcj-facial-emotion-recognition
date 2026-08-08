import logging
import boto3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Khởi tạo Rekognition client ở ngoài handler để tận dụng Lambda container reuse
rekognition_client = boto3.client("rekognition")

def get_dominant_emotion(emotions: list) -> tuple[str, float]:
    """
    Tìm cảm xúc có độ tin cậy (Confidence) cao nhất từ danh sách kết quả
    trả về bởi Amazon Rekognition.

    Args:
        emotions (list): Danh sách dict cảm xúc, mỗi phần tử có dạng
                         {'Type': 'HAPPY', 'Confidence': 99.5}

    Returns:
        tuple[str, float]: (Tên cảm xúc, Độ tin cậy)
    """
    if not emotions:
        return "UNKNOWN", 0.0

    dominant = max(emotions, key=lambda e: e.get("Confidence", 0))
    return dominant.get("Type", "UNKNOWN"), round(dominant.get("Confidence", 0.0), 2)


def analyze_image_with_rekognition(bucket: str, key: str) -> dict:
    """
    Gọi Amazon Rekognition để phân tích khuôn mặt trong ảnh được lưu trên S3.

    Args:
        bucket (str): Tên S3 bucket chứa ảnh
        key    (str): Object key của ảnh trong S3

    Returns:
        dict: Kết quả detect_faces từ Rekognition
    """
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
