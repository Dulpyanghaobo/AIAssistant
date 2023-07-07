from abc import ABC, abstractmethod
import os
import requests
from sqlalchemy.orm import Session
from pydantic import BaseModel
from AuthService.app.api.models.Models import WechatUser
from sqlalchemy import engine

# 假设你已经在环境变量中设置了appid和secret
appid = os.getenv("WECHAT_APPID")
secret = os.getenv("WECHAT_SECRET")

class LoginStrategy(ABC):
    @abstractmethod
    def login(self, code: str) -> str:
        pass

class WechatLoginStrategy(LoginStrategy):
    def login(self, code: str) -> str:
        # 调用微信API
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code"
        response = requests.get(url)

        # 解析返回结果
        data = response.json()
        print("data"+str(data))
        # wechat_response = WechatResponse(**data)
        #
        # if wechat_response.errcode != 0:
        #     raise Exception(f"Error from Wechat API: {wechat_response.errmsg}")
        #
        # # 保存用户信息
        # session = Session(bind=engine)  # 假设engine是你已经配置好的SQLAlchemy引擎
        # wechat_user = WechatUser(openid=wechat_response.openid, session_key=wechat_response.session_key)
        # session.add(wechat_user)
        # session.commit()

        # 返回用户的openid作为token（实际中你可能需要生成一个真正的token）
        return data

class OtherAppLoginStrategy(LoginStrategy):
    def login(self, code: str) -> str:
        # 实现其他应用的登录逻辑
        pass

if __name__ == '__main__':
    WechatLoginStrategy().login("0c1h3tFa1V71CF0HxXGa1vsAiG3h3tF0")