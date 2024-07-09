# -*- coding: UTF-8 -*- #
"""
@filename:init_db.py
@author:wdh
@time:2024-07-09
"""
from app.db import engine
from app.models import user, algorithm

def init_db():
    # 在这里导入所有的模型，这样它们将被注册在元数据上
    # 否则你将不得不在调用 create_all() 之前导入它们
    user.Base.metadata.create_all(bind=engine)
    algorithm.Base.metadata.create_all(bind=engine)