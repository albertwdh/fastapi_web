# -*- coding: UTF-8 -*- #
"""
@filename:main.py
@author:wdh
@time:2024-01-15
"""


from fastapi import FastAPI
from .api.router import api_router

app = FastAPI()

app.include_router(api_router)

