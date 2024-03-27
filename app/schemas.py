# -*- coding: UTF-8 -*- #
"""
@filename:schemas.py
@author:wdh
@time:2024-01-15
"""


from pydantic import BaseModel
from typing import List, Optional
class CalculationInput(BaseModel):
    value: float

class CalculationResult(BaseModel):
    result: float

class Person(BaseModel):
    id: int
    username: str
    age: int

