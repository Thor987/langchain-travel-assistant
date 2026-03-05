import requests
from langchain.agents import Tool
from langchain_community.chat_models import ChatZhipuAI
from langchain.schema import SystemMessage, HumanMessage
from .config import ZHIPUAI_API_KEY, MODEL_NAME, TEMPERATURE


def query_weather(city: str) -> str:
    """Query weather information for a city"""
    api_url = f"http://wttr.in/{city}?format=3"
    try:
        response = requests.get(api_url, timeout=10)
        return response.text
    except Exception as e:
        return f"Unable to get weather for {city}: {str(e)}"


weather_tool = Tool(
    name="Weather Query",
    func=query_weather,
    description="Query current weather information for a city. Input city name.",
)


def calculate_budget_internal(daily_budget: float, days: int) -> str:
    """Calculate total travel budget based on daily budget and number of days"""
    try:
        total_budget = daily_budget * days
        return f"Your travel budget is {total_budget:.2f} yuan."
    except Exception as e:
        return f"Unable to calculate budget: {str(e)}"


def calculate_budget(input_data: str) -> str:
    """Parse input and calculate budget"""
    try:
        parts = input_data.split(",")
        if len(parts) != 2:
            return "Input format error. Please use format: 'daily_budget,days' e.g., '500,3'"
        daily_budget = float(parts[0].strip())
        days = int(parts[1].strip())
        return calculate_budget_internal(daily_budget, days)
    except ValueError:
        return "Input format error. Please use format: 'daily_budget,days' e.g., '500,3'"


budget_tool = Tool(
    name="Budget Calculator",
    func=calculate_budget,
    description="Calculate total travel budget based on daily budget and days. Input format: 'daily_budget,days', e.g., '500,3'.",
)


chat = ChatZhipuAI(
    api_key=ZHIPUAI_API_KEY,
    model=MODEL_NAME,
    temperature=TEMPERATURE,
)


def recommend_place(question: str) -> str:
    """Use ZhipuAI to answer travel-related questions"""
    messages = [
        SystemMessage(content="Your role is a travel assistant."),
        HumanMessage(content=question),
    ]
    response = chat.invoke(messages)
    return response.content


place_tool = Tool(
    name="Travel Recommendation",
    func=recommend_place,
    description="Answer user questions about travel, such as recommending attractions. Input question description.",
)
