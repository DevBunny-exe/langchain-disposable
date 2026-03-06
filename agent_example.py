from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI

from langchain_disposable.tool import disposable_tool


llm = ChatOpenAI(
    temperature=0,
)

tools = [disposable_tool]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
)

agent.run(
    "Use python to calculate factorial of 20"
)
