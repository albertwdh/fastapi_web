# -*- coding: UTF-8 -*- #
"""
@filename:main.py
@author:wdh
@time:2024-06-25
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import user, algorithm

app = FastAPI()

# 设置 CORS 中间件，允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有HTTP方法
    allow_headers=["*"],  # 允许所有请求头
)

# 包含用户和算法的路由
app.include_router(user.router)
app.include_router(algorithm.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

