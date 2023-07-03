from fastapi import APIRouter, UploadFile, File, Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service

router = APIRouter()

@router.post("/")
async def analyze_content(document: UploadFile = File(...), ocr_service: OCRService = Depends(get_ocr_service)):
    contents = ocr_service.process_input(input_data=document, processor_type="text")
    result = ocr_service.analyze(data=contents, analyzer_type="content_analyze")
    return result
