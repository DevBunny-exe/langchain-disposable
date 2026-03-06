# LangChain Disposable

Run AI generated Python code safely.

## Install

pip install langchain-disposable

## Usage

```python
from langchain_disposable import disposable_tool

tools = [disposable_tool]

agent.run("calculate factorial of 10")