from fastapi import APIRouter, UploadFile, File, Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service

router = APIRouter()

@router.post("/")
async def analyze_image(image: UploadFile = File(...), ocr_service: OCRService = Depends(get_ocr_service)):
    contents = ocr_service.process_input(input_data=image, processor_type="image")
    result = ocr_service.analyze(data=contents, analyzer_type="image_analyze")
    return result

