# -*- coding: UTF-8 -*- #
"""
@filename:public.py
@author:wdh
@time:2024-07-09
"""
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field
from fastapi.security import OAuth2PasswordRequestForm
from app.config import settings
from app.schemas.user import UserCreate, User
from app.services.user_service import get_user_by_username, get_user_by_email, create_user, authenticate_user, create_token_for_user
from app.db import get_db
from app.mail import send_email
from app.celery_app import celery_app
from app.task.celery_task import to_mail, to_mail_result

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/")
def root():
    return {"message": "Hello World"}


class EmailSchema(BaseModel):
    email_to: EmailStr = Field(default=settings.MAIL_RECEIVE)
    subject: str
    body: str

@router.post("/send_email_background")
def send_email_background(
    email: EmailSchema,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):
    background_tasks.add_task(send_email, email.subject, email.email_to, email.body)
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})

@router.post("/send-email")
def auto_send_email_endpoint(
    email: EmailSchema
):
    result = to_mail.delay(email.subject, email.email_to, email.body)
    return JSONResponse(status_code=200, content={"task_id": result.id, "status": result.status})

@router.post("/get-email-result/{task_id}")
def get_task_result(task_id):
    result = to_mail_result(task_id)
    return JSONResponse(status_code=200, content=result)



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
