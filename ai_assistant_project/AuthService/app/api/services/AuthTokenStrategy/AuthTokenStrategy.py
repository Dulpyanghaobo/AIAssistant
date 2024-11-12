from abc import ABC, abstractmethod
import os
from typing import Dict, Union

import requests
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy.orm import Session
from pydantic import BaseModel
from AuthService.app.api.models.Models import WechatUser,User, UserToken
from sqlalchemy import create_engine
import datetime
from AuthService.app.utils.generate_token import generate_jwt, get_user_from_token
from AuthService.app.events.kafka_producer import KafkaProducerFactory
# 假设你已经在环境变量中设置了appid和secret
appid = os.getenv("WECHAT_APPID")
secret = os.getenv("WECHAT_SECRET")
wechat_secret_key = os.getenv("WECHAT_SECRET_KEY")

class AuthTokenStrategy(ABC):
    @abstractmethod
    def authtoken(self,  code: str) -> str:
        pass

    @abstractmethod
    def verifytoken(self, token: str) -> str:
        pass
        return get_user_from_token(token=token)
class WechatAuthTokenStrategy(AuthTokenStrategy):
    def __init__(self, producer_factory: KafkaProducerFactory):
        self.producer = producer_factory.get_producer()
    def authtoken(self, code: str) -> str:
        # 调用微信API
        url = f"https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code"
        response = requests.post(url)

        # 解析返回结果
        data = response.json()
        print("data" + str(data))

        # 保存用户信息
        engine = create_engine('mysql+pymysql://root:@localhost:3306/auth_service_db_0')  # 使用你自己的数据库URL
        session = Session(bind=engine)  # 假设engine是你已经配置好的SQLAlchemy引擎

        wechat_user = session.query(WechatUser).filter_by(openid=data['openid']).first()
        if not wechat_user:
            # If the user doesn't exist, create a new User and WechatUser
            user = User(username=data['openid'], email=f"{data['openid']}@example.com", password_hash='...', salt='...')
            session.add(user)
            session.flush()  # This is needed to populate the id of the new User

            wechat_user = WechatUser(user_id=user.id, openid=data['openid'], session_key=data['session_key'])
            session.add(wechat_user)
            # 发送新用户信息到 Kafka
            user_info = {'user_id': user.id, 'openid': data['openid']}
            self.producer.send('user_info_topic', key=user.id, value=user_info)
        else:
            # If the user does exist, update the session key
            wechat_user.session_key = data['session_key']

        # 生成token和刷新token
        token = generate_jwt(user_id=wechat_user.openid, secret_key=wechat_secret_key)
        # 保存token信息
        user_token = UserToken(user_id=wechat_user.user_id, token=token, refresh_token=token, expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=1), refresh_expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=30))
        session.add(user_token)
        session.commit()
        # 返回token信息
        return token

    def verifytoken(self, token: str) -> str:
        return get_user_from_token(secret_key=wechat_secret_key, token=token)
class OtherAppAuthTokenStrategy(AuthTokenStrategy):
    def authtoken(self, code: str) -> str:
        # 实现其他应用的登录逻辑
        pass

if __name__ == '__main__':
    WechatAuthTokenStrategy().authtoken("0c1h3tFa1V71CF0HxXGa1vsAiG3h3tF0")