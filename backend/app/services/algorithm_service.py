# -*- coding: UTF-8 -*- #
"""
@filename:algorithm_service.py
@author:wdh
@time:2024-06-25
"""

from sqlalchemy.orm import Session
from app.models.algorithm import Algorithm
from app.schemas.algorithm import AlgorithmCreate
import logging
def get_algorithm(db: Session, algorithm_id: int):
    return db.query(Algorithm).filter(Algorithm.id == algorithm_id).first()

def get_algorithms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Algorithm).offset(skip).limit(limit).all()

def create_algorithm(db: Session, algorithm: AlgorithmCreate, user_id: int, file_path: str):
    logging.info(
        f"Creating algorithm with name={algorithm.name}, description={algorithm.description}, file_path={file_path}, user_id={user_id}")
    db_algorithm = Algorithm(**algorithm.dict(), user_id=user_id, file_path=file_path)
    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    logging.info(f"Created algorithm with id={db_algorithm.id}")
    return db_algorithm