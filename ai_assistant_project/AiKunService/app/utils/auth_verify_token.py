import requests
from fastapi import HTTPException

def verify_token(token: str):
    url = 'http://localhost:9005/auth/api/v1/login/wechat'
    headers = {'Authorization': f'Bearer {token}'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return response.json()  # 假设接口返回的是JSON数据
