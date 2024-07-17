# -*- coding: UTF-8 -*- #
"""
@filename:celery_task.py
@author:wdh
@time:2024-07-17
"""




from app.celery_app import celery_app
from app.mail import send_email
import time
@celery_app.task
def to_mail(subject: str, email_to: str, body: str):
    send_email(subject, email_to, body)


def to_mail_result(task_id):
    task = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task.status, "result": task.result}

