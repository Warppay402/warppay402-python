from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="warppay402-mcp",
    version="1.1.0",
    description="LangChain and CrewAI tool wrappers for WarpPay402 x402 micropayment APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "langchain-core>=0.1.0",
    ],
)