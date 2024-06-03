# -*- coding: UTF-8 -*- #
"""
@filename:task.py
@author:wdh
@time:2024-06-03
"""

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
class Task(BaseModel):
    name: str
    description: Optional[str] = None
    execute_at: datetime
    algorithm_filename: str  # 添加算法文件名字段