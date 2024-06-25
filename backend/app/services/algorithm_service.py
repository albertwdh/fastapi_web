# -*- coding: UTF-8 -*- #
"""
@filename:algorithm_service.py
@author:wdh
@time:2024-06-25
"""


from sqlalchemy.orm import Session

from app.models import algorithm as models
from app.schemas import algorithm as schemas

def get_algorithm(db: Session, algorithm_id: int):
    return db.query(models.Algorithm).filter(models.Algorithm.id == algorithm_id).first()

def get_algorithms(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Algorithm).offset(skip).limit(limit).all()

def create_algorithm(db: Session, algorithm: schemas.AlgorithmCreate, user_id: int):
    db_algorithm = models.Algorithm(**algorithm.dict(), owner_id=user_id)
    db.add(db_algorithm)
    db.commit()
    db.refresh(db_algorithm)
    return db_algorithm

