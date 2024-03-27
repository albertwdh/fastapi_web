# -*- coding: UTF-8 -*- #
"""
@filename:router.py
@author:wdh
@time:2024-01-15
"""



from fastapi import APIRouter
from .calc_test import calculation

api_router = APIRouter()
api_router.include_router(calculation.router, tags=["calculation"])
