from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from AuthService.app.api.models.Models import UserToken
import datetime
from AuthService.app.utils.database import get_db
import hashlib
import secrets
import uuid
import time
import jwt
from dotenv import load_dotenv
import os
load_dotenv()
wechat_secret_key = os.getenv("WECHAT_SECRET_KEY")

def generate_user_key(user_id=None):
    if user_id is None:
        # 生成一个唯一的用户ID
        user_id = str(uuid.uuid4())

    # 生成一个随机数
    random_number = secrets.randbelow(10 ** 10)

    # 生成字符串
    raw_string = user_id + str(random_number)

    # 生成哈希值
    hash_value = hashlib.sha256(raw_string.encode()).hexdigest()

    return hash_value


def generate_jwt(user_id, secret_key, expiration=3600):
    # 使用提供的用户ID生成唯一的用户key
    user_key = generate_user_key(user_id)

    # 设置JWT的头部和有效载荷
    header = {
        'typ': 'JWT',
        'alg': 'HS256'
    }
    payload = {
        'user_id': user_id,
        'user_key': user_key,
        'exp': time.time() + expiration
    }

    # 使用提供的密钥生成JWT
    jwt_token = jwt.encode(payload, secret_key, algorithm='HS256', headers=header)

    return jwt_token.decode()


# 使用FastAPI的OAuth2PasswordBearer类声明token的来源
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/login/wechat")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_user_from_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, wechat_secret_key, algorithms=["HS256"])
        user_id: str = payload.get("user_id")
        user_key: str = payload.get("user_key")
        if user_id is None or user_key is None:
            raise credentials_exception
    except IOError:
        raise credentials_exception
    return user_key
