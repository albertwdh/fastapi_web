# -*- coding: UTF-8 -*- #
"""
@filename:config.py
@author:wdh
@time:2024-06-25
"""


import os
from pydantic import BaseSettings, EmailStr

class BaseConfig(BaseSettings):

    PROJECT_NAME: str = "Algorithm Platform"
    PROJECT_VERSION: str = "1.0.0"
    SECRET_KEY: str = "albertwangdh@sina.com"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # MySQL 配置
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "pwd"
    MYSQL_DB: str = "algorithms"
    MYSQL_HOST: str = "mysql"
    MYSQL_PORT: str = "3306"


    # MongoDB 配置
    MONGO_DB: str = "algorithm_mongo"
    MONGO_HOST: str = "mongodb://mongo:27017"

    # RabbitMQ 配置
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_PORT: int = 5672

    # 邮件
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool = True
    MAIL_SSL: bool = False

    MAIL_RECEIVE: str


    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

class DevelopmentConfig(BaseConfig):
    DEBUG: bool = True

class ProductionConfig(BaseConfig):
    DEBUG: bool = False

def get_settings():
    env = os.getenv("ENV", "development")
    if env == "production":
        return ProductionConfig()
    return DevelopmentConfig()

settings = get_settings()