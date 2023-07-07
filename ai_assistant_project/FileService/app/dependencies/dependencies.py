from FileService.app.services.file_service import FileUploader, OSSUploader


def get_file_uploader() -> FileUploader:
    return OSSUploader()  # 或者你自己的实现