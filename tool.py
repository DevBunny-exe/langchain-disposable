from langchain.tools import StructuredTool
from disposable import run


def execute_python(code: str) -> str:
    """
    Execute Python code safely in Disposable sandbox.
    """

    result = run(code)

    if result.get("stderr"):
        return f"Error:\n{result['stderr']}"

    return result.get("stdout", "")


disposable_tool = StructuredTool.from_function(
    name="execute_python",
    func=execute_python,
    description="Execute Python code safely using disposable sandbox"
)
