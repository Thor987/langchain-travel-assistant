# 智能旅游助手

基于 [LangChain](https://www.langchain.com/) 和 [智谱AI (GLM-4)](https://open.bigmodel.cn/) 构建的智能旅游助手。助手能够回答旅游相关问题、提供实时天气信息、计算旅行预算，并推荐旅游景点。

## 功能特点

- 🌤️ **天气查询** – 实时查询任意城市的天气信息
- 💰 **预算计算** – 根据每日预算和天数计算旅行总费用
- 🗺️ **旅游推荐** – AI 驱动的景点和行程建议
- 🧠 **对话记忆** – 支持多轮对话，保持上下文
- 🌐 **中英双语** – 支持中英文交互

## 系统架构

```
用户输入
    │
    ▼
LangChain Agent (CONVERSATIONAL_REACT_DESCRIPTION)
    │
    ├──► 天气查询工具  ──► wttr.in API
    ├──► 预算计算工具  ──► 本地计算
    └──► 旅游推荐工具  ──► 智谱AI GLM-4
    │
    ▼
对话记忆 (ConversationBufferMemory)
    │
    ▼
返回给用户
```

## 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/Thor987/langchain-travel-assistant.git
cd langchain-travel-assistant
```

2. **创建并激活虚拟环境**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **安装依赖**

```bash
pip install -r requirements.txt
```

4. **配置环境变量**

```bash
cp .env.example .env
# 编辑 .env 文件，填入您的 ZHIPUAI_API_KEY
```

## 配置说明

在 `.env` 文件中设置以下环境变量：

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `ZHIPUAI_API_KEY` | 智谱AI API 密钥 | *(必填)* |
| `MODEL_NAME` | 模型名称 | `glm-4` |
| `TEMPERATURE` | 模型温度参数 | `0.5` |

## 使用方法

**启动交互式助手：**

```bash
python -m src.main
```

**示例对话：**

```
欢迎使用智能旅游助手！
Welcome to Intelligent Travel Assistant!

请输入您的问题（输入'退出'结束）：北京天气怎么样？
助手回答：北京: 🌤️ +8°C

请输入您的问题（输入'退出'结束）：我打算玩3天，每天700元，总费用是多少？
助手回答：您的旅行预算为 2100.00 元。

请输入您的问题（输入'退出'结束）：推荐北京的景点
助手回答：北京有许多著名景点，推荐您参观故宫、天安门广场、颐和园、长城等...

请输入您的问题（输入'退出'结束）：退出
感谢使用智能旅游助手，再见！
```

## 工具说明

| 工具名称 | 功能描述 | 输入格式 |
|----------|----------|----------|
| 天气查询 | 通过 wttr.in 获取城市实时天气 | 城市名称 |
| 预算计算 | 计算旅行总费用 | `每日预算,天数`（如：`700,3`）|
| 旅游推荐 | 通过智谱AI 提供旅游建议 | 问题描述 |

## 项目结构

```
langchain-travel-assistant/
├── README.md
├── README_CN.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── .env.example
├── notebook/
│   └── Langchain_Curriculum_Design.ipynb
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── tools.py
│   ├── agent.py
│   └── main.py
├── docs/
│   ├── experiment_report.md
│   └── experiment_report_cn.md
├── examples/
│   └── usage_example.py
└── tests/
    └── test_tools.py
```

## 运行测试

```bash
python -m pytest tests/
```

## 技术栈

- **LangChain** 0.3.13 – Agent 框架与工具编排
- **智谱AI GLM-4** – 旅游推荐大语言模型
- **wttr.in** – 天气数据 API
- **python-dotenv** – 环境变量管理
- **PyJWT** – JWT 认证支持

## 贡献指南

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m '添加新功能'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 提交 Pull Request

## 许可证

本项目采用 MIT 许可证 – 详情见 [LICENSE](LICENSE) 文件。

## 致谢

- [LangChain](https://www.langchain.com/) 提供 Agent 框架
- [智谱AI](https://open.bigmodel.cn/) 提供 GLM-4 大语言模型
- [wttr.in](https://wttr.in/) 提供天气 API
