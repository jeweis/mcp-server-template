# server.py
"""
MCP服务器主模块，各种 mcp 工具入口
"""

from fastmcp import FastMCP

from src.app_config import config
from src.core import helloworld

# 创建MCP服务器实例
mcp = FastMCP(name=config.SERVER_NAME)

@mcp.tool
def hello_word_tool(name: str) -> str:
    """Hello world tool that echoes the input name"""
    return helloworld(name)


def main():
    """主函数，用于启动mcp服务器"""
    print("启动 MCP 服务器...")
    if config.TYPE=="streamable-http":
        mcp.run(transport="streamable-http", host="0.0.0.0", port=config.PORT,path=config.CONTEXT_PATH)
    elif config.TYPE=="sse":
        mcp.run(transport="sse", host="0.0.0.0", port=config.PORT,path=config.CONTEXT_PATH)
    else:
        mcp.run()

if __name__ == "__main__":
    main()
