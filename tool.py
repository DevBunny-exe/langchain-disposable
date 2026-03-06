from langchain.tools import tool
from disposable import run


@tool
def execute_python(code: str) -> str:
    """
    Execute Python code safely using Disposable sandbox.
    """

    result = run(code)

    if result["stderr"]:
        return result["stderr"]

    return result["stdout"]
