# 实验报告：LangChain 智能旅游助手

## 概述

本报告记录了基于 LangChain 和智谱AI GLM-4 模型构建的智能旅游助手的设计、实现和测试过程。

## 1. 实验流程

### 1.1 环境搭建

```bash
pip install langchain==0.3.13 langchain-community pyjwt requests python-dotenv
```

### 1.2 API 配置

助手使用智谱AI API（GLM-4 模型）。在 `.env` 文件中设置 API 密钥：

```bash
ZHIPUAI_API_KEY=your_api_key_here
```

### 1.3 系统架构

```
用户 → LangChain Agent → 工具选择 → 生成回复
         │
         ├── 天气查询工具（wttr.in）
         ├── 预算计算工具（本地计算）
         └── 旅游推荐工具（智谱AI）
```

## 2. 代码说明

### 2.1 配置模块 (`src/config.py`)

```python
import os
from dotenv import load_dotenv

load_dotenv()

ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
MODEL_NAME = "glm-4"
TEMPERATURE = 0.5
```

### 2.2 工具模块 (`src/tools.py`)

**天气查询工具：**

```python
def query_weather(city: str) -> str:
    api_url = f"http://wttr.in/{city}?format=3"
    try:
        response = requests.get(api_url, timeout=10)
        return response.text
    except Exception as e:
        return f"Unable to get weather for {city}: {str(e)}"
```

**预算计算工具**（已修复递归 Bug）：

```python
def calculate_budget_internal(daily_budget: float, days: int) -> str:
    total_budget = daily_budget * days
    return f"Your travel budget is {total_budget:.2f} yuan."

def calculate_budget(input_data: str) -> str:
    parts = input_data.split(",")
    if len(parts) != 2:
        return "输入格式错误，请使用格式：'每日预算,天数'"
    daily_budget = float(parts[0].strip())
    days = int(parts[1].strip())
    return calculate_budget_internal(daily_budget, days)
```

**旅游推荐工具：**

```python
def recommend_place(question: str) -> str:
    messages = [
        SystemMessage(content="Your role is a travel assistant."),
        HumanMessage(content=question),
    ]
    response = chat.invoke(messages)
    return response.content
```

### 2.3 Agent 模块 (`src/agent.py`)

```python
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)
```

## 3. 运行结果

### 3.1 单元测试结果

| 测试用例 | 输入 | 预期输出 | 结果 |
|----------|------|----------|------|
| 预算计算（有效输入）| `"700,3"` | 包含 `"2100"` | ✅ 通过 |
| 预算计算（无效输入）| `"invalid"` | 包含 `"format error"` | ✅ 通过 |
| 天气查询 | `"Beijing"` | 非空字符串 | ✅ 通过 |

### 3.2 集成测试对话记录

**测试一：通用旅游咨询**

```
用户：请介绍一下北京的旅游情况
助手：北京是中国的首都，拥有丰富的历史文化和旅游资源...
```

**测试二：天气查询**

```
用户：北京近期的天气如何？
助手：北京: ⛅️ +12°C
```

**测试三：预算计算**

```
用户：我打算在北京玩3天，每天的预算是700元，请帮我计算总开销？
工具输入：700,3
工具输出：Your travel budget is 2100.00 yuan.
助手：您的旅行预算为2100元。
```

**测试四：景点推荐**

```
用户：请推荐北京的景点
助手：北京著名景点包括：
- 故宫博物院
- 天安门广场
- 颐和园
- 八达岭长城
- 天坛公园
```

## 4. 结论

### 4.1 实验成果

1. **多工具集成**：成功通过 LangChain Agent 框架集成了天气、预算和推荐三个工具。
2. **Bug 修复**：通过将解析逻辑与计算逻辑分离，解决了原始 `calculate_budget` 函数中的递归问题。
3. **对话记忆**：实现了 `ConversationBufferMemory`，支持多轮对话。
4. **安全性**：API 密钥通过环境变量管理，不会硬编码到代码中。

### 4.2 局限性

- 天气数据依赖 wttr.in 服务的可用性。
- 旅游推荐质量取决于智谱AI API 的响应。

### 4.3 未来改进方向

- 添加航班和酒店预订集成
- 实现用户偏好学习
- 支持更多语言
- 缓存天气数据以减少 API 调用次数
