from langchain.tools import Tool
from disposable_exec import run


def execute_python(code: str):
    result = run(code)
    return result["stdout"]


disposable_tool = Tool(
    name="execute_python",
    func=execute_python,
    description="Execute Python code safely in disposable sandbox"
)