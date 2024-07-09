# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-25
"""


from pydantic import BaseModel
from typing import Optional

# 算法基本模型
class AlgorithmBase(BaseModel):
    name: str
    description: Optional[str] = None

# 算法创建模型
class AlgorithmCreate(AlgorithmBase):
    pass

# 算法模型
class Algorithm(AlgorithmBase):
    id: int

    class Config:
        orm_mode = True  # 使 Pydantic 与 ORM 模型兼容
