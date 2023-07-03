from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from OCRService.app.api.routes import router as api_router
from OCRService.app.services.ocr_service import OCRService
from OCRService.app.global_dependencies import get_ocr_service

app = FastAPI()

# Use CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(api_router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    # Initialize OCRService
    ocr_service = get_ocr_service()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)
