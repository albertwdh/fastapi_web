# -*- coding: UTF-8 -*- #
"""
@filename:tasks.py
@author:wdh
@time:2024-06-03
"""


from fastapi import APIRouter, HTTPException
from app.models.task import Task
from app.services.task_service import TaskService
from app.services.algorithm_service import AlgorithmService

router = APIRouter()

@router.post("/add", response_model=Task)
async def add_task(task: Task):
    # try:
    # 添加任务逻辑
    TaskService.add_task(task)

    # 获取算法文件路径
    algorithm_path = TaskService.get_algorithm_path(task)

    # 运行算法并捕获结果
    result = AlgorithmService.run_algorithm(algorithm_path)

    # 返回任务及其执行结果
    return {"task": task, "result": result}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))