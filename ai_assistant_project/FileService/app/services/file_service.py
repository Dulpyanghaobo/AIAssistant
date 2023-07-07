from abc import ABC, abstractmethod
from dotenv import load_dotenv
import os
import oss2


# 加载.env文件中的环境变量
load_dotenv()

# Now you can access the variables
ACCESS_KEY_ID = os.getenv("ACCESS_KEY_ID")
ACCESS_KEY_SECRET = os.getenv("ACCESS_KEY_SECRET")
ENDPOINT = os.getenv("ENDPOINT")
BUCKET_NAME = os.getenv("BUCKET_NAME")
class FileUploader(ABC):
    @abstractmethod
    def upload_file(self, local_file, remote_file):
        pass
class OSSUploader:
    def __init__(self):
        self.bucket = oss2.Bucket(oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET), ENDPOINT, BUCKET_NAME)

    def upload_file(self, local_file, remote_file):
        self.bucket.put_object_from_file(local_file, remote_file)
        # 设置URL的有效时间，例如3600秒
        expiration_time = 3600
        url = self.bucket.sign_url('GET', remote_file, expiration_time)
        return url
