from fastapi import APIRouter, UploadFile, File, Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service

router = APIRouter()

@router.post("/")
async def organize_document(document: UploadFile = File(...), ocr_service: OCRService = Depends(get_ocr_service)):
    contents = ocr_service.process_input(input_data=document, processor_type="text")
    result = ocr_service.export(data=contents, exporter_type="document_organizer")
    return result
