# -*- coding: UTF-8 -*- #
"""
@filename:config.py
@author:wdh
@time:2024-06-25
"""


import os

class Settings:
    PROJECT_NAME: str = "Algorithm Platform"
    PROJECT_VERSION: str = "1.0.0"

    MYSQL_USER: str = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD", "password")
    MYSQL_DB: str = os.getenv("MYSQL_DB", "algorithms")
    MYSQL_HOST: str = os.getenv("MYSQL_HOST", "mysql")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT", "3306")

    MONGO_DB: str = os.getenv("MONGO_DB", "algorithm_mongo")
    MONGO_HOST: str = os.getenv("MONGO_HOST", "mongodb://mongo:27017")

    SECRET_KEY: str = os.getenv("SECRET_KEY", "secret")

settings = Settings()
