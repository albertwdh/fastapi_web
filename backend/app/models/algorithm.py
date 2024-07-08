# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

# 算法模型
class Algorithm(Base):
    __tablename__ = "algorithms"

    id = Column(Integer, primary_key=True, index=True)  # 主键
    name = Column(String(100), index=True)  # 算法名称
    description = Column(String(250))  # 算法描述
    file_path = Column(String(250))  # 文件路径
    user_id = Column(Integer, ForeignKey("users.id"))  # 外键，关联用户

    owner = relationship("User", back_populates="algorithms")  # 关系定义
