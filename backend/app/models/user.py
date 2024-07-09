# -*- coding: UTF-8 -*- #
"""
@filename:user.py
@author:wdh
@time:2024-06-25
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base

# 用户模型
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # 主键
    username = Column(String(50), unique=True, index=True, nullable=False)  # 用户名
    email = Column(String(100), unique=True, index=True, nullable=False)  # 电子邮件
    hashed_password = Column(String(200), nullable=False)  # 哈希密码

    algorithms = relationship("Algorithm", back_populates="owner")