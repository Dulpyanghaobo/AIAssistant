import asyncio
import base64
import hashlib
import hmac
import json
import random
import time
from abc import ABC, abstractmethod

import websockets
import re

WEBSOCKET_BASE_URL='wss://midjourney-api.ai3.design/ws'
ACCESS_KEY='09l61NveoaVTTMqPrzG5EQ89zo7YzeJPiE06JMZBZ9dTQQve8Upouw'
SECRET_KEY='33_7VPyROJ170zCq-2tcii7M50OyZB5PYSKuZ3JIFkAqkD1g0SE_cg'

class ImageGenerator(ABC):
    @abstractmethod
    def generate_image(self, text: str):
        pass
class ThirdPartyImageGenerator:
    def __init__(self):
        self.access_key = ACCESS_KEY
        self.secret_key = SECRET_KEY
        self.websocket_base_url = WEBSOCKET_BASE_URL

    async def connect(self):
        self.ws = await websockets.connect(self.websocket_base_url)
        await self.send_auth()

    def sign_string(self, string_to_sign):
        secret_key = self.secret_key.encode()
        string_to_sign = string_to_sign.encode()
        digester = hmac.new(secret_key, string_to_sign, hashlib.sha256)
        signature = digester.digest()

        signature_base64 = base64.urlsafe_b64encode(signature).decode()
        return signature_base64.rstrip('=')

    async def send_auth(self):
        nonce = random.randint(0, 1e16)
        timestamp = int(time.time())
        string_to_sign = f"access_key={self.access_key}&nonce={nonce}&timestamp={timestamp}"
        signature = self.sign_string(string_to_sign)
        auth_message = {
            "type": 7,
            "data": {
                "access_key": self.access_key,
                "timestamp": timestamp,
                "nonce": nonce,
                "signature": signature,
            }
        }
        await self.ws.send(json.dumps(auth_message))

    async def send_heartbeat(self):
        heartbeat_message = {
            "type": 1,
            "data": {
                "access_key": self.access_key
            }
        }
        while True:
            await self.ws.send(json.dumps(heartbeat_message))
            await asyncio.sleep(5)  # delay for 5 seconds

    async def send_imagine_task(self, prompt):
        imagine_task = {
            "type": 4,
            "data": {
                "mode": "Fast",
                "type": 1,
                "imagine": {
                    "prompt": prompt
                }
            }
        }
        await self.ws.send(json.dumps(imagine_task))

    async def generate_image(self, prompt):
        await self.connect()
        asyncio.ensure_future(self.send_heartbeat())
        await self.send_imagine_task(prompt)
        while True:
            message = await self.ws.recv()
            print(f"Received message: {message}")

            message_json = json.loads(message)  # Convert message to JSON object

            # Check if the necessary keys are present in the JSON object
            if "data" in message_json and "progress" in message_json["data"] and "images" in message_json["data"][
                "progress"]:
                for image in message_json["data"]["progress"]["images"]:
                    # Check if the image has the required width and height
                    if "width" in image and image["width"] == 2048 and "height" in image and image["height"] == 2048:
                        # Return the proxy URL if it exists
                        if "proxy_url" in image:
                            await self.ws.close()  # 关闭WebSocket连接
                            return image["proxy_url"]

        return None  # Return None if no suitable image was found

