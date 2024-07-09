# -*- coding: UTF-8 -*- #
"""
@filename:public.py
@author:wdh
@time:2024-07-09
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.user import UserCreate, User
from app.services.user_service import get_user_by_username, get_user_by_email, create_user, authenticate_user, create_token_for_user
from app.db import get_db
router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/")
def root():
    return {"message": "Hello World"}


@router.post("/register", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.post("/token", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_token_for_user(user)
    return {"access_token": access_token, "token_type": "bearer"}
