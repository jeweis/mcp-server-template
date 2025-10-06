# core.py
"""
核心模块
"""

from .app_config import config

# 测试管理
engine = None

def helloworld(name):
    """回显输入名称"""
    return "Hello, World!"+name