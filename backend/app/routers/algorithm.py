# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""


from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.schemas import algorithm as schemas
from app.services import algorithm_service
from app.db import get_db

router = APIRouter()

# 上传算法文件并创建算法
@router.post("/algorithms/", response_model=schemas.Algorithm)
async def create_algorithm(name: str, description: str, file: UploadFile = File(...), db: Session = Depends(get_db)):
    user_id = 1  # 这里需要获取当前登录用户的 ID
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    algorithm = schemas.AlgorithmCreate(name=name, description=description)
    return algorithm_service.create_algorithm(db=db, algorithm=algorithm, user_id=user_id)
