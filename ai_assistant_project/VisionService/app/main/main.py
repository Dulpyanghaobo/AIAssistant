from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from VisionService.app.api.vision.routes import router as api_router

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)
