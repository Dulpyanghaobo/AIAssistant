from fastapi import APIRouter

from VisionService.app.api.vision.views import image_generation

router = APIRouter()

router.include_router(image_generation.router, tags=["Image Generation"], prefix="/vision/v1/gen_image")
