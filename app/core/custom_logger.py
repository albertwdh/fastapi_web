# -*- coding: UTF-8 -*- #
"""
@filename:custom_logger.py
@author:wdh
@time:2024-01-15
"""


import logging

def get_custom_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    # 配置日志格式和处理器等
    return logger