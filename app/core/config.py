# -*- coding: UTF-8 -*- #
"""
@filename:config.py
@author:wdh
@time:2024-01-15
"""
class Settings:
    database_url: str = "sqlite:///./test.db"
    secret_key: str = "SECRET_KEY"

settings = Settings()