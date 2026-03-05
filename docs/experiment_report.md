# Experiment Report: LangChain Travel Assistant

## Overview

This report documents the design, implementation, and testing of an intelligent travel assistant built with LangChain and ZhipuAI's GLM-4 model.

## 1. Experiment Process (实验流程)

### 1.1 Environment Setup

```bash
pip install langchain==0.3.13 langchain-community pyjwt requests python-dotenv
```

### 1.2 API Configuration

The assistant uses the ZhipuAI API (GLM-4 model). Set the API key in `.env`:

```bash
ZHIPUAI_API_KEY=your_api_key_here
```

### 1.3 System Architecture

```
User → LangChain Agent → Tool Selection → Response
         │
         ├── Weather Query Tool (wttr.in)
         ├── Budget Calculator Tool (local)
         └── Travel Recommendation Tool (ZhipuAI)
```

## 2. Code Description (代码说明)

### 2.1 Configuration (`src/config.py`)

```python
import os
from dotenv import load_dotenv

load_dotenv()

ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
MODEL_NAME = "glm-4"
TEMPERATURE = 0.5
```

### 2.2 Tools (`src/tools.py`)

**Weather Query Tool:**

```python
def query_weather(city: str) -> str:
    api_url = f"http://wttr.in/{city}?format=3"
    try:
        response = requests.get(api_url, timeout=10)
        return response.text
    except Exception as e:
        return f"Unable to get weather for {city}: {str(e)}"
```

**Budget Calculator Tool** (fixed recursion bug):

```python
def calculate_budget_internal(daily_budget: float, days: int) -> str:
    total_budget = daily_budget * days
    return f"Your travel budget is {total_budget:.2f} yuan."

def calculate_budget(input_data: str) -> str:
    parts = input_data.split(",")
    if len(parts) != 2:
        return "Input format error. Please use format: 'daily_budget,days'"
    daily_budget = float(parts[0].strip())
    days = int(parts[1].strip())
    return calculate_budget_internal(daily_budget, days)
```

**Travel Recommendation Tool:**

```python
def recommend_place(question: str) -> str:
    messages = [
        SystemMessage(content="Your role is a travel assistant."),
        HumanMessage(content=question),
    ]
    response = chat.invoke(messages)
    return response.content
```

### 2.3 Agent (`src/agent.py`)

```python
agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)
```

## 3. Test Results (运行结果)

### 3.1 Unit Tests

| Test Case | Input | Expected Output | Result |
|-----------|-------|-----------------|--------|
| Budget (valid) | `"700,3"` | Contains `"2100"` | ✅ Pass |
| Budget (invalid) | `"invalid"` | Contains `"format error"` | ✅ Pass |
| Weather Query | `"Beijing"` | Non-empty string | ✅ Pass |

### 3.2 Integration Test Conversations

**Test 1: General Travel Advice**

```
User: 请介绍一下北京的旅游情况
Assistant: 北京是中国的首都，拥有丰富的历史文化和旅游资源...
```

**Test 2: Weather Query**

```
User: 北京近期的天气如何？
Assistant: 北京: ⛅️ +12°C
```

**Test 3: Budget Calculation**

```
User: 我打算在北京玩3天，每天的预算是700元，请帮我计算总开销？
Tool Input: 700,3
Tool Output: Your travel budget is 2100.00 yuan.
Assistant: 您的旅行预算为2100元。
```

**Test 4: Itinerary Recommendation**

```
User: 请推荐北京的景点
Assistant: 北京著名景点包括：
- 故宫博物院
- 天安门广场
- 颐和园
- 八达岭长城
- 天坛公园
```

## 4. Conclusions (结论)

### 4.1 Achievements

1. **Multi-tool Integration**: Successfully integrated weather, budget, and recommendation tools via LangChain's agent framework.
2. **Bug Fix**: Resolved a recursion issue in the original `calculate_budget` function by separating parsing logic from calculation logic.
3. **Conversation Memory**: Implemented `ConversationBufferMemory` for multi-turn dialogue support.
4. **Security**: API keys are managed through environment variables, never hardcoded.

### 4.2 Limitations

- Weather data depends on the availability of the wttr.in service.
- Travel recommendation quality depends on the ZhipuAI API response.

### 4.3 Future Improvements

- Add flight and hotel booking integration
- Implement user preference learning
- Add support for more languages
- Cache weather data to reduce API calls
