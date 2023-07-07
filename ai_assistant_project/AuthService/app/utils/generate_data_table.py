from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from AuthService.app.api.models.Models import Base  # 引入你的Base

DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/auth_service_db_0'  # 请将这个连接字符串替换为你的数据库连接信息

class Database:
    def __init__(self, uri=DATABASE_URI):
        self.engine = create_engine(uri)
        self.session = sessionmaker(bind=self.engine)

    def create_db(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

        Base.metadata.create_all(self.engine)

    def drop_db(self):
        if database_exists(self.engine.url):
            drop_database(self.engine.url)
if __name__ == '__main__':
    Database().drop_db()
    Database().create_db()