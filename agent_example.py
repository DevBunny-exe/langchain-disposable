from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from langchain_disposable.tool import execute_python


tools = [execute_python]

llm = OpenAI()

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

agent.run(
    "Calculate fibonacci of 20 using python"
)
