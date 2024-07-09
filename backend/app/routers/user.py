# -*- coding: UTF-8 -*- #
"""
@filename:user.py
@author:wdh
@time:2024-06-25
"""

from fastapi import APIRouter, Depends
from app.schemas.user import User

from app.utils.auth import get_current_user, revoke_token, oauth2_scheme
router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    revoke_token(token)
    return {"msg": "Successfully logged out"}

