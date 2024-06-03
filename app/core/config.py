# -*- coding: UTF-8 -*- #
"""
@filename:config.py
@author:wdh
@time:2024-06-03
"""


from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Algorithm Platform"
    SCHEDULER_CONFIG: dict = {
        "apscheduler.jobstores.default": {
            "type": "sqlalchemy",
            "url": "sqlite:///jobs.sqlite"
        },
        "apscheduler.executors.default": {
            "class": "apscheduler.executors.pool:ThreadPoolExecutor",
            "max_workers": "20"
        },
        "apscheduler.job_defaults.coalesce": "false",
        "apscheduler.job_defaults.max_instances": "3",
    }

settings = Settings()