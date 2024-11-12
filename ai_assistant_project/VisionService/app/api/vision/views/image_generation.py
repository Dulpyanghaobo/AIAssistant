from fastapi import APIRouter, Depends, HTTPException, WebSocket
from fastapi.responses import JSONResponse

from VisionService.app.api.vision.services.image_generator import ThirdPartyImageGenerator
from VisionService.app.dependencies.dependencies import get_image_generator
from pydantic import BaseModel

router = APIRouter()

class TextSchema(BaseModel):
    text: str
@router.post("/imageGeneration")
async def image_generation(text_schema: TextSchema, image_generator: ThirdPartyImageGenerator = Depends(get_image_generator)):
    result = await image_generator.generate_image(text_schema.text+"Pixar style --v 5.1 --iw 2")
    if result is None:
        raise HTTPException(status_code=500, detail="Error generating image")
    print(text_schema.text)
    # return JSONResponse(content={"imageUrl": "https://media.discordapp.net/attachments/1116695781722816646/1125824055308734614/inavarro_girl_38584d1d-cd9b-48b1-aaf9-414aeef0a9f8.png"})
    return JSONResponse(content={"imageUrl": result})
