# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-03
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Algorithm(BaseModel):
    id: str
    filename: str
    filepath: str
    uploaded_at: datetime

