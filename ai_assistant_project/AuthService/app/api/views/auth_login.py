from fastapi import HTTPException,APIRouter, Depends
from pydantic import BaseModel
from AuthService.app.api.services.AuthTokenStrategy.AuthTokenStrategy import WechatAuthTokenStrategy, OtherAppAuthTokenStrategy
from AuthService.app.api.services.auth_service import AuthService
from AuthService.app.api.models.Models import User
from AuthService.app.utils.generate_token import get_user_from_token
router = APIRouter()

class LoginData(BaseModel):
    code: str
    type: str

@router.post("/auth/token")
async def auth_token(data: LoginData):
    if data.type == 'mini_wechat':
        strategy = WechatAuthTokenStrategy()
    elif data.type == 'otherapp':
        strategy = OtherAppAuthTokenStrategy()
    else:
        raise HTTPException(status_code=400, detail="Invalid login type")

    authService = AuthService(strategy)
    try:
        token = authService.authtoken(code= data.code)
        return {"access_token": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# 在需要身份认证的API接口中使用它
@router.get("/verify/token/{token}/type/{type}")
async def verify_token(token: str, type: str):
    if type == 'mini_wechat':
        strategy = WechatAuthTokenStrategy()
    else:
        raise HTTPException(status_code=400, detail="Invalid login type")
    return {"user": strategy.verifytoken(token)}

# @router.post("/refresh")
# async def refresh(refresh_token: str):
#     # 从数据库中获取对应的用户token
#     engine = create_engine('mysql+pymysql://root:@localhost:3306/auth_service_db_0')
#     session = Session(bind=engine)
#     user_token = session.query(UserToken).filter(UserToken.refresh_token == refresh_token).first()
#
#     # 如果没有找到或者刷新token已过期，返回错误
#     if not user_token or user_token.refresh_expires_at < datetime.datetime.utcnow():
#         raise HTTPException(status_code=400, detail="Invalid refresh token")
#
#     # 生成新的token和刷新token
#     token = generate_token()
#     refresh_token = generate_refresh_token()
#
#     # 更新数据库
#     user_token.token = token
#     user_token.refresh_token = refresh_token
#     user_token.expires_at = datetime.datetime.utcnow() + datetime.timedelta(days=1)
#     user_token.refresh_expires_at = datetime.datetime.utcnow() + datetime.timedelta(days=30)
#     session.commit()
#
#     # 返回新的token
#     return {
#         "access_token": token,
#         "refresh_token": refresh_token,
#         "expires_in": 3600 * 24,
#         "refresh_expires_in": 3600 * 24 * 30
#     }
