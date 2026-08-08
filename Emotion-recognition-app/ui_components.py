import io
from datetime import datetime, timezone
import streamlit as st
from PIL import Image

from config import S3_BUCKET_NAME, AWS_REGION, ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB
from validation import validate_file
from s3_service import upload_image_to_s3

def render_sidebar():
    """Render thanh sidebar với thông tin cấu hình / Render sidebar with config info."""
    with st.sidebar:
        st.image(
            "https://d0.awsstatic.com/logos/powered-by-aws-white.png",
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
        st.markdown(
            "```\n"
            "Upload  →  S3\n"
            "   ↓\n"
            "Lambda Trigger\n"
            "   ↓\n"
            "Rekognition\n"
            "   ↓\n"
            "DynamoDB Log\n"
            "```"
        )


def render_main():
    """Render phần nội dung chính / Render the main content area."""

    # Tiêu đề / Title
    st.title("😊 Facial Emotion Recognition")
    st.markdown(
        "> **FCJ Workshop** · Serverless AI Analytics Platform  \n"
        "> Upload a face image to trigger the emotion analysis pipeline."
    )
    st.divider()

    # Khu vực upload file / File upload area
    st.markdown("### 📤 Upload Image")
    uploaded_file = st.file_uploader(
        label        = "Drag & drop or click to browse",
        type         = ACCEPTED_IMAGE_TYPES,
        help         = f"Supported formats: JPG, PNG | Max size: {MAX_FILE_SIZE_MB} MB",
        label_visibility = "collapsed",
    )

    if uploaded_file is not None:
        # Hiển thị preview ảnh và thông tin metadata
        col1, col2 = st.columns([1, 1])

        with col1:
            st.markdown("**Preview:**")
            # Mở ảnh bằng Pillow để hiển thị an toàn
            image = Image.open(io.BytesIO(uploaded_file.getvalue()))
            st.image(image, use_container_width=True)

        with col2:
            st.markdown("**File Info:**")
            file_size_kb = uploaded_file.size / 1024
            st.markdown(f"- 📄 **Name:** `{uploaded_file.name}`")
            st.markdown(f"- 📦 **Size:** `{file_size_kb:.1f} KB`")
            st.markdown(f"- 🖼️ **Dimensions:** `{image.width} × {image.height} px`")
            st.markdown(f"- 🗂️ **Format:** `{image.format or uploaded_file.type}`")

        st.divider()

        # Nút Upload
        if st.button(
            label = "🚀 Upload to S3 & Analyze",
            type  = "primary",
            use_container_width = True,
        ):
            # Xác thực file trước khi upload
            is_valid, validation_msg = validate_file(uploaded_file)

            if not is_valid:
                st.error(f"❌ Validation Error: {validation_msg}")
            else:
                # Hiển thị spinner trong khi đang upload
                with st.spinner("⏳ Uploading image to Amazon S3..."):
                    file_bytes = uploaded_file.getvalue()
                    success, message = upload_image_to_s3(
                        file_bytes = file_bytes,
                        filename   = uploaded_file.name,
                        bucket     = S3_BUCKET_NAME,
                    )

                if success:
                    st.success("✅ Image uploaded successfully!")
                    st.balloons()

                    st.markdown("#### 📊 Upload Details")
                    detail_col1, detail_col2 = st.columns(2)
                    with detail_col1:
                        st.metric("Status",   "SUCCESS ✅")
                        st.metric("File",     uploaded_file.name)
                    with detail_col2:
                        st.metric("Destination", message)
                        st.metric(
                            "Triggered At",
                            datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                        )

                    st.info(
                        "🔄 **Pipeline triggered!**  \n"
                        "The Lambda function will automatically process this image using "
                        "**Amazon Rekognition** and save the emotion analysis results to "
                        "**DynamoDB** within seconds."
                    )
                else:
                    st.error(f"❌ Upload Failed: {message}")
                    st.markdown(
                        "**Troubleshooting:**\n"
                        "- Verify your AWS credentials are configured correctly\n"
                        "- Ensure the S3 bucket name and region are correct\n"
                        "- Check that your IAM user/role has `s3:PutObject` permission"
                    )

    else:
        # Placeholder khi chưa có file
        st.markdown(
            """
            <div style="
                border: 2px dashed #4A90D9;
                border-radius: 10px;
                padding: 40px;
                text-align: center;
                color: #666;
                background-color: #f8f9ff;
            ">
                <h3>📁 No image selected</h3>
                <p>Use the uploader above to select a face image.<br>
                Supported formats: <strong>JPG, JPEG, PNG</strong></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
