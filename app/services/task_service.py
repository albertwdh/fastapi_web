# -*- coding: UTF-8 -*- #
"""
@filename:task_service.py
@author:wdh
@time:2024-06-03
"""

from app.models.task import Task

class TaskService:
    @staticmethod
    def add_task(task: Task):
        # 添加任务的逻辑，例如保存到数据库
        pass

    @staticmethod
    def get_algorithm_path(task: Task) -> str:
        return f"./files/{task.algorithm_filename}"