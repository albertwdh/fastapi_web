# -*- coding: UTF-8 -*- #
"""
@filename:celery_app.py
@author:wdh
@time:2024-07-09
"""


# celery_app.py
from celery import Celery
import time

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'



# 在include 中必须导入要使用的模块
celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=['app.task.test','app.task.celery_task']
)


# backend        celery -A app.celery_app worker --loglevel=info --pool=solo