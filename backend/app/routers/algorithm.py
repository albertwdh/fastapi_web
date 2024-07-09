# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""


from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.schemas.algorithm import AlgorithmCreate, Algorithm
from app.services.algorithm_service import get_algorithm, get_algorithms, create_algorithm
from app.db import get_db
from typing import List
import os
import logging
import importlib.util
import sys

from app.utils.auth import get_current_user
from app.models.user import User


# 上传算法文件并创建算法
router = APIRouter()


UPLOAD_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../uploaded_files"))


@router.post("/", response_model=Algorithm)
def upload_algorithm(
        name: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    logging.info(f"Uploading algorithm with name={name}, description={description}")
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # 确保写入权限
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
    except PermissionError as e:
        logging.error(f"Permission denied: {e}")
        raise HTTPException(status_code=500, detail="Permission denied: unable to write to directory")
    except Exception as e:
        logging.error(f"Error writing file: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    algorithm = AlgorithmCreate(name=name, description=description)
    try:
        created_algorithm = create_algorithm(db, algorithm, user_id=current_user.id, file_path=file_path)  # 使用默认用户ID
    except Exception as e:
        logging.error(f"Error creating algorithm: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return created_algorithm


def load_and_run_algorithm(file_path: str):
    # 动态导入Python模块
    spec = importlib.util.spec_from_file_location("uploaded_algorithm", file_path)
    uploaded_algorithm = importlib.util.module_from_spec(spec)
    sys.modules["uploaded_algorithm"] = uploaded_algorithm
    spec.loader.exec_module(uploaded_algorithm)

    # 假设算法文件中有一个名为 `run` 的函数
    if hasattr(uploaded_algorithm, "run"):
        result = uploaded_algorithm.run()
        return result
    else:
        raise HTTPException(status_code=400, detail="Algorithm file does not contain a 'run' function")


@router.post("/run/{algorithm_id}")
def run_algorithm(algorithm_id: int, db: Session = Depends(get_db)):
    algorithm = get_algorithm(db, algorithm_id=algorithm_id)
    if algorithm is None:
        raise HTTPException(status_code=404, detail="Algorithm not found")

    try:
        result = load_and_run_algorithm(algorithm.file_path)
    except Exception as e:
        logging.error(f"Error running algorithm: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    return {"result": result}


@router.get("/", response_model=List[Algorithm])
def read_algorithms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    algorithms = get_algorithms(db, skip=skip, limit=limit)
    return algorithms


@router.get("/{algorithm_id}", response_model=Algorithm)
def read_algorithm(algorithm_id: int, db: Session = Depends(get_db)):
    algorithm = get_algorithm(db, algorithm_id=algorithm_id)
    if algorithm is None:
        raise HTTPException(status_code=404, detail="Algorithm not found")
    return algorithm