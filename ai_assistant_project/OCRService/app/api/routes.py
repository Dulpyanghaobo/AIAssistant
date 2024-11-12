from fastapi import APIRouter

from OCRService.app.api.views import (analyze_image, optimize_document, recognize_text,
                           translate, organize_document, analyze_content,
                           repair_photo, solve_question, convert_document)

router = APIRouter()

router.include_router(analyze_image.router, tags=["Image Analysis"], prefix="/ocr/v1/analyze_image")
router.include_router(optimize_document.router, tags=["Document Optimization"], prefix="/ocr/v1/optimize_document")
router.include_router(recognize_text.router, tags=["Text Recognition"], prefix="/ocr/v1/recognize_text")
router.include_router(translate.router, tags=["Language Translation"], prefix="/ocr/v1/translate")
router.include_router(organize_document.router, tags=["Document Organization"], prefix="/ocr/v1/organize_document")
router.include_router(analyze_content.router, tags=["Content Analysis"], prefix="/ocr/v1/analyze_content")
router.include_router(repair_photo.router, tags=["Photo Repair"], prefix="/ocr/v1/repair_photo")
router.include_router(solve_question.router, tags=["Problem Solving"], prefix="/ocr/v1/solve_question")
router.include_router(convert_document.router, tags=["Document Conversion"], prefix="/ocr/v1/convert_document")
