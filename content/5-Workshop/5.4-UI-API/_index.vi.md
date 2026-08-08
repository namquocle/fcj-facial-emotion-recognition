---
title : "Giao diện & Tích hợp API"
date : 2024-01-01 
weight : 4
chapter : false
pre : " <b> 5.4. </b> "
---
# 5.4. Giao diện & Tích hợp API

Trong phần này, bạn sẽ xây dựng ứng dụng giao diện web (Frontend) bằng thư viện Streamlit và kết nối nó với S3 bucket của bạn bằng AWS SDK cho Python (`boto3`).

---

## Bước 1: Thiết lập các Biến Môi trường Cục bộ

Tạo một tệp tin có tên `.env` ở thư mục gốc của dự án cục bộ để lưu trữ cấu hình kết nối AWS:

```text
AWS_ACCESS_KEY_ID=ma_access_key_cua_ban
AWS_SECRET_ACCESS_KEY=ma_secret_access_key_cua_ban
AWS_REGION=ap-southeast-1
S3_BUCKET_NAME=my-facial-emotion-recognition-<hau-to-duy-nhat>
```

---

## Bước 2: Viết các Module mã nguồn

Chúng ta sẽ tạo cấu trúc mã nguồn dạng modular sạch sẽ, trong đó mỗi tệp tin chỉ thực hiện một nhiệm vụ duy nhất.

### 2.1. Cấu hình Ứng dụng (`config.py`)
Tệp này tải các biến từ `.env` và định nghĩa các hằng số.

```python
import os
from dotenv import load_dotenv

# Tải các biến môi trường từ tệp .env
load_dotenv()

DEFAULT_REGION = "ap-southeast-1"
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME", "your-emotion-recognition-bucket")
AWS_REGION     = os.environ.get("AWS_REGION", DEFAULT_REGION)

# Các định dạng ảnh được phép upload lên Streamlit
ACCEPTED_IMAGE_TYPES = ["jpg", "jpeg", "png"]

# Kích thước tệp tối đa được phép tải lên (tính bằng MB)
MAX_FILE_SIZE_MB = 5
```

### 2.2. Kiểm tra tính hợp lệ của Tệp (`validation.py`)
Xác thực phần mở rộng và kích thước hình ảnh tải lên trước khi gửi đến S3.

```python
from config import ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB

def validate_file(uploaded_file) -> tuple[bool, str]:
    """Kiểm tra phần mở rộng và kích thước của tệp tải lên."""
    file_ext = uploaded_file.name.rsplit(".", 1)[-1].lower()
    if file_ext not in ACCEPTED_IMAGE_TYPES:
        return False, f"Unsupported file type '.{file_ext}'. Accepted: {ACCEPTED_IMAGE_TYPES}"

    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        return False, f"File size ({file_size_mb:.1f} MB) exceeds limit of {MAX_FILE_SIZE_MB} MB."

    return True, ""
```

### 2.3. Dịch vụ lưu trữ S3 (`s3_service.py`)
Xử lý khởi tạo client S3 và upload tệp tin.

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
    """Khởi tạo và cache client S3 boto3."""
    return boto3.client("s3", region_name=AWS_REGION)

def upload_image_to_s3(file_bytes: bytes, filename: str, bucket: str) -> tuple[bool, str]:
    """Tải tệp tin ảnh lên Amazon S3 vào thư mục uploads/."""
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

### 2.4. Các Thành phần Giao diện (`ui_components.py`)
Gói gọn mã giao diện người dùng giúp tệp `app.py` ngắn gọn, rõ ràng hơn.

```python
import io
from datetime import datetime, timezone
import streamlit as st
from PIL import Image

from config import S3_BUCKET_NAME, AWS_REGION, ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB
from validation import validate_file
from s3_service import upload_image_to_s3

def render_sidebar():
    """Hiển thị sidebar chứa thông tin cấu hình."""
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
    """Hiển thị nội dung chính của ứng dụng."""
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
                    st.info("🔄 Pipeline triggered! Lambda đang tự động phân tích cảm xúc khuôn mặt bằng Rekognition và lưu log vào DynamoDB.")
                else:
                    st.error(f"❌ Upload Failed: {message}")
    else:
        st.info("Vui lòng tải lên một hình ảnh chứa khuôn mặt để phân tích cảm xúc.")
```

### 2.5. Điểm khởi chạy Ứng dụng chính (`app.py`)
Tệp này khởi tạo cấu hình trang Streamlit và điều phối hiển thị giao diện.

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

## Bước 3: Khởi chạy Ứng dụng Streamlit

Chạy lệnh sau trên terminal của bạn sau khi môi trường ảo đã được kích hoạt:

```bash
streamlit run app.py
```

Lệnh này sẽ khởi tạo một máy chủ cục bộ (thông thường tại cổng `http://localhost:8501`) và tự động mở một tab mới trên trình duyệt web hiển thị giao diện phân tích cảm xúc của bạn.
