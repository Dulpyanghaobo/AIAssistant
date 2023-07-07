from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from AuthService.app.api.services.LoginStrategy.LoginStrategy import WechatLoginStrategy, OtherAppLoginStrategy
from AuthService.app.api.services.auth_service import AuthService

app = FastAPI()

class LoginData(BaseModel):
    code: str
    type: str

@app.post("/api/auth/login")
async def login(data: LoginData):
    if data.type == 'mini_wechat':
        strategy = WechatLoginStrategy()
    elif data.type == 'otherapp':
        strategy = OtherAppLoginStrategy()
    else:
        raise HTTPException(status_code=400, detail="Invalid login type")

    authService = AuthService(strategy)
    try:
        token = authService.login(data.code)
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
