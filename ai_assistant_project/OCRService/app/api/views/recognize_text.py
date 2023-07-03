from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/recognize_text")
async def recognize_text(file: UploadFile = File(...), ocr_service: OCRService = Depends(get_ocr_service)):
    # # Check uploaded file type
    # if not image.filename.endswith(".png") and not image.filename.endswith(".jpg"):
    #     raise HTTPException(status_code=400, detail="Invalid file type. Please upload a .png or .jpg file.")
    #
    # # Read uploaded file into memory
    # contents = await image.read()
    #
    # # Create an instance of OCRService
    # # Pass the image content to the OCR service for analysis
    contents = ocr_service.process_input(input_data=file, processor_type="image")
    result = ocr_service.analyze(data=contents, analyzer_type="text_recognize")

    return JSONResponse(content={"result": result})
