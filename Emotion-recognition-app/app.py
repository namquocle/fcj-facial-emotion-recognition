# =============================================================================
# File: app.py
# Project: Serverless Facial Emotion Recognition Analytics Platform
# Description: Giao diện web Streamlit cho phép người dùng upload ảnh lên S3
#              để kích hoạt pipeline nhận diện cảm xúc tự động.
#              Streamlit web UI allowing users to upload images to S3
#              to trigger the automated emotion recognition pipeline.
# Run: streamlit run app.py
# =============================================================================

import streamlit as st
from ui_components import render_sidebar, render_main

# Cấu hình trang Streamlit / Streamlit page configuration
st.set_page_config(
    page_title="Emotion Recognition | FCJ Workshop",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded",
)


def main():
    """Hàm chính khởi chạy ứng dụng Streamlit / Main function to launch the Streamlit app."""
    render_sidebar()
    render_main()


if __name__ == "__main__":
    main()