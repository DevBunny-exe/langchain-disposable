from setuptools import setup, find_packages

setup(
    name="langchain-disposable",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "disposable-exec"
    ],
)
