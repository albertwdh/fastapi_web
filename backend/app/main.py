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

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(user.router)
app.include_router(algorithm.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
