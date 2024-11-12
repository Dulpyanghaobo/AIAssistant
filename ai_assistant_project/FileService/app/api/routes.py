from fastapi import APIRouter
from FileService.app.api.views import file_upload

router = APIRouter()

router.include_router(file_upload.router, tags=["Uploader"], prefix="/file/v1/upload")
