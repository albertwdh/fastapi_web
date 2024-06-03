# -*- coding: UTF-8 -*- #
"""
@filename:algorithm.py
@author:wdh
@time:2024-06-03
"""

from fastapi import APIRouter, HTTPException, UploadFile, File
from app.services.algorithm_service import AlgorithmService
from app.utils.dynamic_import import dynamic_import

router = APIRouter()


@router.post("/upload")
async def upload_algorithm(file: UploadFile = File(...)):
    try:
        filepath = await AlgorithmService.save_algorithm(file)

        # 动态导入模块
        module = dynamic_import(filepath)

        # 假设模块中有一个类
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type):  # 检查是否是类
                if hasattr(attr, 'run'):  # 检查类是否有run方法
                    def create_route(cls):
                        async def run_algorithm():
                            instance = cls()
                            try:
                                result = instance.run()
                                return {"result": result}
                            except Exception as e:
                                raise HTTPException(status_code=500, detail=str(e))

                        return run_algorithm

                    router.get(f"/run/{attr.__name__}")(create_route(attr))
                    return {"message": "Algorithm uploaded and route created", "route": f"/run/{attr.__name__}"}

        raise HTTPException(status_code=400, detail="Module does not contain a suitable class with a run method")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))