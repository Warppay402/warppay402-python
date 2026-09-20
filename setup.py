from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="warppay402-mcp",
    version="1.1.1",
    description="Keyless, zero-API LangChain & CrewAI tool suite for WarpPay402 x402 micropayment infrastructure across Base, Solana, Arbitrum, and Arc Mainnet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "keyless",
        "zero-api",
        "x402",
        "micropayments",
        "langchain",
        "crewai",
        "mcp",
        "base-chain",
        "solana",
        "arbitrum",
        "arc-mainnet",
        "ai-agents",
        "crypto-payments"
    ],
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
        "langchain-core>=0.1.0",
    ],
)