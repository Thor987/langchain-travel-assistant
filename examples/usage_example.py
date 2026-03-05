"""
Example usage of the LangChain Travel Assistant
"""
from src.agent import agent

# Example 1: Query weather
print("Example 1: Query Beijing weather")
response = agent.run("北京近期的天气如何？")
print(f"Response: {response}\n")

# Example 2: Calculate budget
print("Example 2: Calculate travel budget")
response = agent.run("我打算在北京玩3天，每天的预算是700元，请帮我计算总开销？")
print(f"Response: {response}\n")

# Example 3: Get recommendations
print("Example 3: Get travel recommendations")
response = agent.run("请推荐北京的景点")
print(f"Response: {response}\n")
