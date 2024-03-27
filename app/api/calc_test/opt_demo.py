# -*- coding: UTF-8 -*- #
"""
@filename:opt_demo.py
@author:wdh
@time:2024-01-15
"""


#curd.py
from sqlalchemy.orm import Session
from ... database import engine,Base

def init_table():
    Base.metadata.create_all(bind=engine)



