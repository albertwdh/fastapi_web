# -*- coding: UTF-8 -*- #
"""
@filename:algorithm_service.py
@author:wdh
@time:2024-06-03
"""
import os

import os
from uuid import uuid4  # 确保导入
from fastapi import UploadFile
import io
import contextlib

class AlgorithmService:
    @staticmethod
    async def save_algorithm(file: UploadFile):
        directory = './files'
        if not os.path.exists(directory):
            os.makedirs(directory)

        unique_filename = f"{uuid4()}.py"
        filepath = os.path.join(directory, unique_filename)
        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())

        return filepath

    @staticmethod
    def run_algorithm(filepath: str):
        # 捕获算法执行的标准输出
        with open(filepath, "r") as file:
            code = file.read()

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            exec(code, {'__name__': '__main__'})

        return output.getvalue()