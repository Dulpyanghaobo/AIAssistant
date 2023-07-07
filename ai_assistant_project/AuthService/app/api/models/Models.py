from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# 用户表
# 微信登录用户表
class WechatUser(Base):
    __tablename__ = 'wechatuser'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))  # 关联到User表的id
    openid = Column(String(128), unique=True)  # 微信用户唯一标识
    session_key = Column(String(128))  # 微信会话密钥
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user = relationship('User')

# 用户表
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    salt = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = relationship('Role', secondary='user_role', back_populates='users')
    wechatuser = relationship('WechatUser', uselist=False, back_populates='user')

#其他表的结构不变
#...

# 角色表
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(String(256))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    users = relationship('User', secondary='user_role', back_populates='roles')
    permissions = relationship('Permission', secondary='role_permission', back_populates='roles')

# 权限表
class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    description = Column(String(256))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    roles = relationship('Role', secondary='role_permission', back_populates='permissions')

# 用户角色关系表
user_role = Table(
    'user_role', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('role_id', Integer, ForeignKey('role.id'))
)

# 角色权限关系表
role_permission = Table(
    'role_permission', Base.metadata,
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('permission_id', Integer, ForeignKey('permission.id'))
)

# 第三方应用表
class OAuthApp(Base):
    __tablename__ = 'oauthapp'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    client_id = Column(String(64), nullable=False)
    client_secret = Column(String(128), nullable=False)
    redirect_uri = Column(String(256), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# 用户令牌表
class UserToken(Base):
    __tablename__ = 'usertoken'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    token = Column(String(256), nullable=False)
    refresh_token = Column(String(256))  # 新增的刷新令牌字段
    expires_at = Column(DateTime, nullable=False)
    refresh_expires_at = Column(DateTime)  # 新增的刷新令牌过期时间字段
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
