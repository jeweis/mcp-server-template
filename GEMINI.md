# GEMINI.md

## 项目概述

这个项目是一个基于 Python 的服务器模板，使用 `fastmcp` 库。它作为创建具有自定义工具的服务器的基础示例。包含的 `echo_tool` 通过回显提供的任何文本来演示基本功能。服务器的配置通过环境变量进行管理，详见 `.env.example` 文件。

## 构建和运行

### 依赖项

项目的依赖项列在 `requirements.txt` 中。要安装它们，请运行：

```bash
pip install -r requirements.txt
```

### 配置

在运行服务器之前，在项目根目录创建 `.env` 文件。您可以使用 `.env.example` 文件作为模板。可以配置以下变量：

*   `SERVER_NAME`：您的 MCP 服务器的名称。
*   `CONTEXT_PATH`：服务器的上下文路径。
*   `PORT`：服务器运行的端口。
*   `TYPE`：服务器的传输类型（例如 `streamable-http`、`sse`）。

### 运行服务器

要在项目根目录运行服务器，请执行以下命令：

```bash
python server.py
```

服务器将使用您在 `.env` 文件中指定的配置启动。

## 开发约定

项目遵循标准的 Python 开发约定。主要应用程序逻辑分离到 `src` 目录中，配置在 `src/app_config.py` 中，核心功能在 `src/core.py` 中。主要服务器入口点是 `server.py`。所有新工具和功能都应在 `src` 目录中开发并集成到 `server.py` 中。
