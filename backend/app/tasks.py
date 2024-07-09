# -*- coding: UTF-8 -*- #
"""
@filename:tasks.py
@author:wdh
@time:2024-07-05
"""


from celery import Celery
import aio_pika
from app.config import settings

# 配置 Celery
celery_app = Celery(
    'tasks',
    broker=f'amqp://{settings.RABBITMQ_USER}:{settings.RABBITMQ_PASSWORD}@{settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}//'
)

# 定时任务示例
@celery_app.task
def run_algorithm(algorithm_id: int):
    # 模拟运行算法
    return f"Algorithm {algorithm_id} has been run"
