# -*- coding: UTF-8 -*- #
"""
@filename:main.py
@author:wdh
@time:2024-06-03
"""
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI, APIRouter, HTTPException
from app.api.v1 import algorithm, tasks, extensions
from app.core.scheduler import start_scheduler
from app.utils.dynamic_import import scan_directory

# 动态设置 PYTHONPATH

app = FastAPI(title="Algorithm Platform")

# 包含静态路由
app.include_router(algorithm.router, prefix="/api/v1/algorithms", tags=["Algorithms"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["Tasks"])
app.include_router(extensions.router, prefix="/api/v1/extensions", tags=["Extensions"])

# 动态添加路由
def add_dynamic_routes():
    modules = scan_directory('./files')
    for module in modules:
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type):  # 检查是否是类
                if hasattr(attr, 'run'):  # 检查类是否有run方法
                    router = APIRouter()
                    route_path = f"/run/{attr.__name__}"

                    def create_route(cls):
                        async def run_algorithm():
                            instance = cls()
                            try:
                                result = instance.run()
                                return {"result": result}
                            except Exception as e:
                                raise HTTPException(status_code=500, detail=str(e))
                        return run_algorithm

                    router.get(route_path)(create_route(attr))
                    app.include_router(router)

@app.on_event("startup")
def on_startup():
    add_dynamic_routes()
    start_scheduler()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)