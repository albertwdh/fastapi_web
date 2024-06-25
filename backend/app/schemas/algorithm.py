# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""


from pydantic import BaseModel
from typing import Optional

class AlgorithmBase(BaseModel):
    name: str
    description: Optional[str] = None

class AlgorithmCreate(AlgorithmBase):
    pass

class Algorithm(AlgorithmBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
