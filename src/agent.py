from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from .tools import weather_tool, budget_tool, place_tool, chat

tools = [weather_tool, budget_tool, place_tool]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

prompt = PromptTemplate(
    input_variables=["chat_history", "input"],
    template=(
        "以下是用户和助手的聊天记录：\n{chat_history}\n\n"
        "用户提问：{input}\n\n"
        "请根据以上内容提供旅游相关的专业回答。"
        "使用中文分析作答"
    ),
)

llm_chain = LLMChain(
    llm=chat,
    prompt=prompt,
    memory=memory,
)

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory,
)
