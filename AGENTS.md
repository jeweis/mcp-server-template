# MCP 服务器模板的代理指南

## 构建/测试命令
- **安装依赖**: `pip install -r requirements.txt`
- **运行服务器**: `python server.py`
- **单个测试**: 未配置测试框架 - 添加 pytest 并在 `tests/` 目录中创建测试

## 代码风格指南

### 导入
- 标准库导入优先
- 第三方导入其次
- 本地导入最后（使用相对导入 `.`）
- 每行一个导入

### 命名约定
- **函数/方法**: `snake_case`
- **类**: `PascalCase`
- **常量**: `UPPER_CASE`
- **变量**: `snake_case`

### 类型提示
- 为函数参数和返回值使用类型提示
- 从 `typing` 导入: `Dict`, `List`, `Optional`, `Union`, `Any`

### 文档
- 为模块、类和函数使用三引号文档字符串
- 为与现有代码保持一致，文档字符串使用中文

### 配置
- 通过 `python-dotenv` 使用环境变量进行配置
- 在 `src/app_config.py` 的 `Config` 类中存储默认值
- 通过 `from src.app_config import config` 访问配置

### 错误处理
- 为缺失的环境变量使用默认值
- 最小的异常处理 - 依赖框架默认值

### 项目结构
- 源代码在 `src/` 包中
- 主入口点在 `server.py`
- 配置在 `src/app_config.py`
- 核心逻辑在 `src/core.py`