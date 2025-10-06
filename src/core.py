# core.py
"""
核心模块
"""

from .app_config import config

# 测试管理
engine = None

def helloworld(text):
    """回显输入文本"""
    return "Hello, World!"+text