import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEFAULT_REGION = "ap-southeast-1"
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "your-emotion-recognition-bucket")
AWS_REGION     = os.environ.get("AWS_REGION", DEFAULT_REGION)

# Acceptable image types for Streamlit uploader
ACCEPTED_IMAGE_TYPES = ["jpg", "jpeg", "png"]

# Maximum allowed file size in Megabytes
MAX_FILE_SIZE_MB = 5
