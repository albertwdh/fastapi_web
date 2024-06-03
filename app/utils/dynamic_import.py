# -*- coding: UTF-8 -*- #
"""
@filename:dynamic_import.py
@author:wdh
@time:2024-06-03
"""
import importlib.util
import os
import sys


def dynamic_import(filepath: str):
    module_name = os.path.splitext(os.path.basename(filepath))[0]

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

    return module


def scan_directory(directory: str):
    modules = []
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            module = dynamic_import(filepath)
            modules.append(module)
    return modules