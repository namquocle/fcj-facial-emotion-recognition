---
title : "UI & API Integration"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---
# 5.4. UI & API Integration

In this module, you will build the frontend client using Streamlit and connect it to your S3 bucket using the AWS SDK (`boto3`).

---

## Step 1: Set Up Local Environment Variables

Create a `.env` file in the root of your local project directory to store your AWS configuration:

```text
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=ap-southeast-1
S3_BUCKET_NAME=my-facial-emotion-recognition-<your-unique-suffix>
```

---

## Step 2: Write the Code Modules

We will create a clean, modular structure where each file has a single responsibility.

### 2.1. App Configuration (`config.py`)
This file loads variables from the `.env` file and defines constants.

```python
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
```

### 2.2. File Validation Helper (`validation.py`)
Validates that the file uploaded by the user is an acceptable type and is not too large.

```python
from config import ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB

def validate_file(uploaded_file) -> tuple[bool, str]:
    """Validate the uploaded file extension and size."""
    file_ext = uploaded_file.name.rsplit(".", 1)[-1].lower()
    if file_ext not in ACCEPTED_IMAGE_TYPES:
        return False, f"Unsupported file type '.{file_ext}'. Accepted: {ACCEPTED_IMAGE_TYPES}"

    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        return False, f"File size ({file_size_mb:.1f} MB) exceeds limit of {MAX_FILE_SIZE_MB} MB."

    return True, ""
```

### 2.3. S3 Storage Service (`s3_service.py`)
Handles S3 client creation and file uploading.

```python
import logging
from datetime import datetime, timezone
import boto3
import streamlit as st
from botocore.exceptions import ClientError, NoCredentialsError
from config import AWS_REGION

logger = logging.getLogger(__name__)

@st.cache_resource
def get_s3_client():
    """Create and cache a boto3 S3 client."""
    return boto3.client("s3", region_name=AWS_REGION)

def upload_image_to_s3(file_bytes: bytes, filename: str, bucket: str) -> tuple[bool, str]:
    """Uploads the image file to Amazon S3 into the uploads/ folder."""
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
        return True, s3_url

    except NoCredentialsError:
        return False, "AWS credentials not found. Please configure credentials."
    except ClientError as e:
        return False, e.response["Error"]["Message"]
    except Exception as e:
        return False, str(e)
```

### 2.4. UI Rendering Components (`ui_components.py`)
Encapsulates UI rendering code to keep `app.py` clean.

```python
import io
from datetime import datetime, timezone
import streamlit as st
from PIL import Image

from config import S3_BUCKET_NAME, AWS_REGION, ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB
from validation import validate_file
from s3_service import upload_image_to_s3

def render_sidebar():
    """Render sidebar with config details."""
    with st.sidebar:
        st.image(
            "https://d1.awsstatic.com/logos/aws-logo-lockups/poweredbyaws/PB_AWS_logo_RGB_REV_SQ.91cd4af40773cbfbd15577a3c2b8a346fe3e8fa2.png",
            width=180,
        )
        st.markdown("## ⚙️ Configuration")
        st.info(f"**S3 Bucket:** `{S3_BUCKET_NAME}`")
        st.info(f"**AWS Region:** `{AWS_REGION}`")
        st.markdown("---")
        st.markdown("## 📋 Supported Formats")
        st.markdown("- `.jpg` / `.jpeg`\n- `.png`")
        st.markdown(f"**Max size:** {MAX_FILE_SIZE_MB} MB")
        st.markdown("---")
        st.markdown("## 🔗 Pipeline")
        st.markdown("```\nUpload -> S3 -> Lambda -> Rekognition -> DynamoDB\n```")

def render_main():
    """Render main user interface content."""
    st.title("😊 Facial Emotion Recognition")
    st.markdown("> **FCJ Workshop** · Serverless AI Analytics Platform")
    st.divider()

    st.markdown("### 📤 Upload Image")
    uploaded_file = st.file_uploader(
        label="Select a face image",
        type=ACCEPTED_IMAGE_TYPES,
        label_visibility="collapsed",
    )

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Preview:**")
            image = Image.open(io.BytesIO(uploaded_file.getvalue()))
            st.image(image, use_container_width=True)
        with col2:
            st.markdown("**File Info:**")
            st.markdown(f"- 📄 **Name:** `{uploaded_file.name}`")
            st.markdown(f"- 📦 **Size:** `{uploaded_file.size/1024:.1f} KB`")

        st.divider()

        if st.button("🚀 Upload to S3 & Analyze", type="primary", use_container_width=True):
            is_valid, validation_msg = validate_file(uploaded_file)
            if not is_valid:
                st.error(validation_msg)
            else:
                with st.spinner("⏳ Uploading to S3..."):
                    success, message = upload_image_to_s3(
                        file_bytes = uploaded_file.getvalue(),
                        filename   = uploaded_file.name,
                        bucket     = S3_BUCKET_NAME,
                    )
                if success:
                    st.success("✅ Image uploaded successfully!")
                    st.balloons()
                    st.info("🔄 Pipeline triggered! Lambda is processing the image using Rekognition and DynamoDB.")
                else:
                    st.error(f"❌ Upload Failed: {message}")
    else:
        st.info("Please upload an image to analyze emotions.")
```

### 2.5. Main Application Entry Point (`app.py`)
This file initializes the page configuration and coordinates components.

```python
import streamlit as st
from ui_components import render_sidebar, render_main

st.set_page_config(
    page_title="Emotion Recognition | FCJ Workshop",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded",
)

def main():
    render_sidebar()
    render_main()

if __name__ == "__main__":
    main()
```

---

## Step 3: Run the Streamlit Application

Execute the following command in your terminal within the activated virtual environment:

```bash
streamlit run app.py
```

This will spin up a local web server (usually at `http://localhost:8501`) and automatically open a tab in your web browser showing your new interface.
