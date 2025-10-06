# app_config.py
"""
配置模块，用于管理应用程序配置
"""

import os
import json
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class Config:
    """配置类，用于管理应用程序配置"""

    ## 默认stdio
    TYPE=os.getenv("TYPE","stdio")
    PORT = os.getenv("PORT", 9087)
    CONTEXT_PATH = os.getenv("CONTEXT_PATH", "")
    # 服务器配置
    SERVER_NAME = os.getenv("SERVER_NAME", "Jewei-MCP-Server")

# 创建默认配置实例
config = Config()