from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from AuthService.app.api.routes import router as api_router

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
app.include_router(api_router, prefix="/auth")

# @app.on_event("startup")
# async def startup_event():
#     # Initialize OCRService
#     ocr_service = get_ocr_service()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)
