# LangChain Travel Assistant / 智能旅游助手

[English](#english) | [中文](#chinese)

---

## English

### Project Overview

An intelligent travel assistant built with [LangChain](https://www.langchain.com/) and [ZhipuAI (GLM-4)](https://open.bigmodel.cn/). The assistant can answer travel-related questions, provide real-time weather information, calculate travel budgets, and recommend tourist attractions.

### Features

- 🌤️ **Weather Query** – Real-time weather information for any city
- 💰 **Budget Calculator** – Calculate total trip cost based on daily budget and days
- 🗺️ **Travel Recommendation** – AI-powered attraction and itinerary suggestions
- 🧠 **Conversation Memory** – Maintains context across multi-turn conversations
- 🌐 **Bilingual** – Supports both Chinese and English interactions

### Architecture

```
User Input
    │
    ▼
LangChain Agent (CONVERSATIONAL_REACT_DESCRIPTION)
    │
    ├──► Weather Query Tool  ──► wttr.in API
    ├──► Budget Calculator Tool  ──► Local Calculation
    └──► Travel Recommendation Tool  ──► ZhipuAI GLM-4
    │
    ▼
ConversationBufferMemory
    │
    ▼
Response to User
```

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Thor987/langchain-travel-assistant.git
cd langchain-travel-assistant
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

```bash
cp .env.example .env
# Edit .env and set your ZHIPUAI_API_KEY
```

### Configuration

Set the following environment variables in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `ZHIPUAI_API_KEY` | Your ZhipuAI API key | *(required)* |
| `MODEL_NAME` | ZhipuAI model name | `glm-4` |
| `TEMPERATURE` | Model temperature | `0.5` |

### Usage

**Run the interactive assistant:**

```bash
python -m src.main
```

**Example conversation:**

```
欢迎使用智能旅游助手！
Welcome to Intelligent Travel Assistant!

请输入您的问题（输入'退出'结束）：北京天气怎么样？
助手回答：北京: 🌤️ +8°C

请输入您的问题（输入'退出'结束）：我打算玩3天，每天700元，总费用是多少？
助手回答：Your travel budget is 2100.00 yuan.

请输入您的问题（输入'退出'结束）：推荐北京的景点
助手回答：北京有许多著名景点，推荐您参观故宫、天安门广场、颐和园、长城等...
```

### Tool Descriptions

| Tool | Description | Input |
|------|-------------|-------|
| Weather Query | Gets real-time weather for a city via wttr.in | City name |
| Budget Calculator | Calculates total trip cost | `daily_budget,days` (e.g., `700,3`) |
| Travel Recommendation | AI-powered travel advice via ZhipuAI | Question text |

### Project Structure

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

### Running Tests

```bash
python -m pytest tests/
```

### Tech Stack

- **LangChain** 0.3.13 – Agent framework and tool orchestration
- **ZhipuAI GLM-4** – Large language model for travel recommendations
- **wttr.in** – Weather data API
- **python-dotenv** – Environment variable management
- **PyJWT** – JWT authentication support

### Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [LangChain](https://www.langchain.com/) for the agent framework
- [ZhipuAI](https://open.bigmodel.cn/) for the GLM-4 language model
- [wttr.in](https://wttr.in/) for the weather API

---

## Chinese

请查看 [README_CN.md](README_CN.md) 获取完整中文文档。