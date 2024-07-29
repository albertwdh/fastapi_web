# -*- coding: UTF-8 -*- #
"""
@filename:main.py
@author:wdh
@time:2024-06-25
"""


import sys
import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.utils.auth import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db import get_db

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from app.routers import user, algorithm, public
from app.task.test import long_task, get_task_result
from app.init_db import init_db

from app.services.user_service import get_user_by_username, get_user_by_email, create_user, authenticate_user, create_token_for_user



app = FastAPI()

# 设置 CORS 中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=False,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)



@app.post("/api/token", response_model=dict)
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



# 包含公共路由，不需要身份验证
app.include_router(public.router, prefix="/api", dependencies=[Depends(get_current_user)])

# 包含用户和算法的路由
app.include_router(user.router, prefix="/user", tags=["User"], dependencies=[Depends(get_current_user)])
app.include_router(algorithm.router, prefix="/algorithm", tags=["Algorithm"], dependencies=[Depends(get_current_user)])


@app.on_event("startup")
def on_startup():
    init_db()


#
# @app.get("/celery_test")
# def celery_test():
#     task = long_task.delay()
#     return {"task_id": task.id, "status": task.status}
#
#
#
# @app.get("/task/{task_id}")
# def get_task_status(task_id: str):
#     return get_task_result(task_id)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)



# 命令行启动
# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload