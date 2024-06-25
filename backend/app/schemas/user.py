# -*- coding: UTF-8 -*- #
"""
@filename:user.py
@author:wdh
@time:2024-06-25
"""

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str
