# -*- coding: UTF-8 -*- #
"""
@filename:extensions.py
@author:wdh
@time:2024-06-03
"""


from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_extensions():
    return {"message": "Extendable functionality goes here"}