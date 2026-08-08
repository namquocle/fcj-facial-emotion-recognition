import os
import logging
from datetime import datetime, timezone
import boto3
import streamlit as st
from botocore.exceptions import ClientError, NoCredentialsError
from config import AWS_REGION

logger = logging.getLogger(__name__)

@st.cache_resource
def get_s3_client():
    """
    Tạo và cache S3 client boto3.
    Create and cache a boto3 S3 client.

    Returns:
        boto3.client: S3 client instance
    """
    return boto3.client(
        "s3",
        region_name          = AWS_REGION,
        aws_access_key_id     = os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY"),
        aws_session_token     = os.environ.get("AWS_SESSION_TOKEN"),  # cần nếu dùng Learner Lab
    )


def upload_image_to_s3(file_bytes: bytes, filename: str, bucket: str) -> tuple[bool, str]:
    """
    Upload file ảnh lên Amazon S3.
    Upload an image file to Amazon S3.

    Args:
        file_bytes (bytes): Nội dung nhị phân của file
        filename   (str):   Tên file gốc
        bucket     (str):   Tên S3 bucket đích

    Returns:
        tuple[bool, str]: (Thành công, Thông báo)
    """
    date_prefix = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    object_key  = f"uploads/{date_prefix}/{filename}"

    try:
        s3_client = get_s3_client()

        logger.info("Uploading %s to s3://%s/%s", filename, bucket, object_key)

        s3_client.put_object(
            Bucket      = bucket,
            Key         = object_key,
            Body        = file_bytes,
            ContentType = f"image/{filename.rsplit('.', 1)[-1].lower()}",
        )

        s3_url = f"s3://{bucket}/{object_key}"
        logger.info("Upload successful: %s", s3_url)
        return True, s3_url

    except NoCredentialsError:
        msg = "AWS credentials not found. Please configure your AWS credentials."
        logger.error(msg)
        return False, msg

    except ClientError as e:
        error_code = e.response["Error"]["Code"]
        error_msg  = e.response["Error"]["Message"]
        msg = f"S3 Upload failed [{error_code}]: {error_msg}"
        logger.error(msg)
        return False, msg

    except Exception as e:
        msg = f"Unexpected error during upload: {str(e)}"
        logger.error(msg, exc_info=True)
        return False, msg
