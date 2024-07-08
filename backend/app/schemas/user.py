# -*- coding: UTF-8 -*- #
"""
@filename:user.py
@author:wdh
@time:2024-06-25
"""

from pydantic import BaseModel, EmailStr

# 用户创建模型
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# 用户模型
class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # 使 Pydantic 与 ORM 模型兼容

# 数据库中的用户模型
class UserInDB(User):
    hashed_password: str

