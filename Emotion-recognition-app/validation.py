from config import ACCEPTED_IMAGE_TYPES, MAX_FILE_SIZE_MB

def validate_file(uploaded_file) -> tuple[bool, str]:
    """
    Kiểm tra tính hợp lệ của file được upload.
    Validate the uploaded file.

    Args:
        uploaded_file: Đối tượng UploadedFile từ Streamlit / Streamlit UploadedFile object

    Returns:
        tuple[bool, str]: (Hợp lệ / Is valid, Thông báo lỗi hoặc rỗng / Error message or empty)
    """
    # Kiểm tra phần mở rộng file / Check file extension
    file_ext = uploaded_file.name.rsplit(".", 1)[-1].lower()
    if file_ext not in ACCEPTED_IMAGE_TYPES:
        return False, f"Unsupported file type '.{file_ext}'. Accepted: {ACCEPTED_IMAGE_TYPES}"

    # Kiểm tra kích thước file / Check file size
    file_size_mb = uploaded_file.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        return False, f"File size ({file_size_mb:.1f} MB) exceeds limit of {MAX_FILE_SIZE_MB} MB."

    return True, ""
