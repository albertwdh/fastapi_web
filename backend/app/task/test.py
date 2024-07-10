# -*- coding: UTF-8 -*- #
"""
@filename:test.py
@author:wdh
@time:2024-07-05
"""

from app.celery_app import celery_app
import time
@celery_app.task
def long_task():
    for i in range(10):
        time.sleep(1)
    return 123123213


def get_task_result(task_id):
    task = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status, "result": task.result}
