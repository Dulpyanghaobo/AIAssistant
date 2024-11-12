from fastapi import APIRouter
from AiKunService.app.api.views import file_upload

router = APIRouter()

router.include_router(file_upload.router, tags=["aikun"], prefix="/api/v1/ai_kun")
