from fastapi import APIRouter, UploadFile, File, Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service

router = APIRouter()

@router.post("/")
async def translate(text: str, ocr_service: OCRService = Depends(get_ocr_service)):
    result = ocr_service.analyze(data=text, analyzer_type="translator")
    return result
