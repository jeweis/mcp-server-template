# MCP Server 项目模板

这是一个MCP Server 项目模板，提供了以下功能：

- 提供了工具echo_tool


## MCP 使用配置

本项目支持通过多种客户端配置 MCP 服务器，以便与各种 IDE 或工具集成。以下是一些常见客户端的配置示例：

### Windsurf / Cursor / Claude

对于基于 Windsurf 框架的客户端（如 Cursor 和 Claude），您可以在 `~/.codeium/windsurf/mcp_config.json` 文件中配置 MCP 服务器。以下是一个示例配置：

```json
{
  "mcpServers": {
    "mcp-server-template": {
      "disabled": false,
      "command": "uvx",
      "args": [
        "mcp-server-template"
      ]
    }
  }
}
```


### Cline

对于 Cline 客户端，您可以在其配置文件中添加类似的 MCP 服务器配置。具体的配置方式请参考 Cline 的官方文档。通常，您需要指定服务器的名称、命令、参数和环境变量。

```json
// Cline 配置文件示例 (具体格式请参考 Cline 文档)
{
  "mcpServers": {
    "mcp-server-template": {
      "command": "uvx",
      "args": [
        "mcp-server-template"
      ]
    }
  }
}
```

## 源码安装

1. 克隆仓库
2. 安装依赖：`pip install -r requirements.txt`
3. 配置环境变量（参见下文）

### 配置

在项目根目录创建`.env`文件，包含以下环境变量：

```
# 服务名
SERVER_NAME=My-MCP-Server
CONTEXT_PATH=
PORT=9087
TYPE=streamable-http
```

### 运行

### 使用uvx安装并运行（推荐）

```bash
uvx --from mcp-server-template
```


### 说明
1. “xxx.xx.xx.xxx”需要换成本机ip
2. 环境变量按实际需求配置

