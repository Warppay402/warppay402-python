# warppay402-mcp

LangChain-compatible `BaseTool` wrappers for WarpPay402 x402 micropayment APIs.

## Overview

This package provides a toolkit of agent-ready tools for on-chain analytics, web extraction, automation, and DeFi actions. The tools are implemented in `warppay402_mcp.tools` and use the WarpPay402 API endpoints under `https://api.warppay402.com/api/v1/tools`.

## Accepted payment options

The WarpPay402 server accepts the following payment methods for tool usage:

- Base USDC
- Arbitrum One USDC
- Solana USDC
- Arc USDC

## Installation

```bash
pip install warppay402-mcp
```

If you want to run the LangChain/OpenAI example below, install the optional integration package:

```bash
pip install langchain-openai
```

## Available tools

The package currently includes these tools:

| Tool | Price | Server capability | Typical call signature |
| --- | --- | --- | --- |
| `ArcDexOracleTool` | $0.001 USDC | Arc DEX spot price & liquidity oracle | `run(pair="ETH/USDC")` |
| `WebScraperTool` | $0.001 USDC | Public webpage to Markdown extraction | `run(url)` |
| `BrowserScraperTool` | $0.005 USDC | JS-rendered page scraping via browser | `run(url)` |
| `BaseAnalyticsTool` | $0.002 USDC | Wallet balance / nonce / account stats on Base | `run(address)` |
| `ArcAnalyticsTool` | $0.001 USDC | Arc network block / gas / latency telemetry | `run()` |
| `ArcNetworkQueryTool` | $0.10 USDC | Pre-flight Arc node + gas + merchant checks | `run(includeGasTrends=True, checkMerchantAccount=True)` |
| `PdfExtractorTool` | $0.005 USDC | Public PDF text extraction | `run(pdfUrl)` |
| `RenderScreenshotTool` | $0.01 USDC | Full-page screenshot capture | `run(url)` |
| `ExtractJsonTool` | $0.01 USDC | Schema-driven JSON extraction from HTML | `run(url, schema=None)` |
| `SmartContractVerifierTool` | $0.02 USDC | Contract source / ABI / proxy verification | `run(address)` |
| `AerodromeYieldsTool` | $0.003 USDC | Top yield pools and APY data | `run()` |
| `AerodromeSwapTool` | $0.01 USDC | Aerodrome router token swap execution | `run(tokenIn, tokenOut, amountIn, decimalsIn, isStable)` |
| `AerodromeClammTool` | $0.01 USDC | Constrained liquidity range actions | `run(action, token0=None, token1=None, tickLower=None, tickUpper=None, amount0Desired=None, amount1Desired=None, tokenId=None)` |
| `AerodromeVeaeroTool` | $0.01 USDC | Lock / vote / claim AERO governance actions | `run(action, amount=None, lockDurationWeeks=None, tokenId=None, poolVoteAddresses=None)` |
| `DeployBaseContractTool` | $5.00 USDC | Deploy contracts on Base | `run(contractType="escrow")` |
| `DeploySolanaContractTool` | $5.00 USDC | Deploy Solana contracts / vaults | `run(contractType, params)` |
| `DeployArcContractTool` | $5.00 USDC | Deploy contracts on Arc | `run(contractType="escrow")` |
| `ArcCctpBridgeTool` | $0.25 USDC | Cross-chain USDC bridge via CCTP | `run(amountUsdc, destinationChain, recipientAddress)` |
| `PublicDataFeedTool` | $0.0001 USDC | Signed public data feed retrieval | `run(filename)` |
| `DataFeedsTool` | $0.001 USDC | Market / yield feed retrieval | `run(feedId)` |
| `RealEstateCalculatorTool` | $0.0005 USDC | Real estate Cap Rate, NOI, and DSCR calculator | `run(purchasePrice, monthlyRent)` |
| `AddressNormalizerTool` | $0.001 USDC | Address geocoding & lat/lon resolution | `run(address)` |
| `WeatherOracleTool` | $0.001 USDC | Atmospheric weather & drone flight safety oracle | `run(latitude, longitude)` |
| `ForexOracleTool` | $0.0005 USDC | Global foreign exchange fiat spot rates | `run(baseCurrency="USD")` |
| `ShippingRateEstimatorTool` | $0.001 USDC | Domestic USPS parcel shipping rate estimator | `run(weightLbs, originZip, destinationZip)` |
| `GithubHealthAnalyzerTool` | $0.002 USDC | GitHub repository stars, issues & license inspector | `run(repository)` |
| `PropertyCompsEstimatorTool` | $0.005 USDC | Property valuations & tax assessor comps | `run(squareFeet, bedrooms, zipCode)` |
| `OutageOracleTool` | $0.002 USDC | Real-time power, ISP, and cellular outage oracle | `run(zipCode, state=None, serviceType="all")` |

This table is meant to make it easy for developers to point agents at the right server capability and understand the expected inputs and pricing before invoking a tool.

## Quickstart

### Direct tool usage

```python
from warppay402_mcp.tools import ArcDexOracleTool, AerodromeYieldsTool, WebScraperTool

oracle = ArcDexOracleTool()
print(oracle.run("ETH/USDC"))

yields_tool = AerodromeYieldsTool()
print(yields_tool.run())

scraper = WebScraperTool()
print(scraper.run("https://example.com"))
```

### LangChain agent usage

```python
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI

from warppay402_mcp.tools import ArcDexOracleTool

llm = ChatOpenAI(model="gpt-4o-mini")
tools = [ArcDexOracleTool()]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)

result = agent.invoke("What is the current ETH/USDC spot price?")
print(result)
```

## Example tool details

### `ArcDexOracleTool`

- Name: `arc_dex_oracle`
- Description: Real-time ETH/USDC spot price resolver and DEX liquidity oracle for Arc Mainnet ($0.001 USDC).
- Default pair: `ETH/USDC`

```python
from warppay402_mcp.tools import ArcDexOracleTool

tool = ArcDexOracleTool()
print(tool.run("ETH/USDC"))
```

### `AerodromeYieldsTool`

- Name: `get_aerodrome_yields`
- Description: Fetches top live Aerodrome DEX yield pools, APYs, and TVL on Base Mainnet ($0.003 USDC).

```python
from warppay402_mcp.tools import AerodromeYieldsTool

tool = AerodromeYieldsTool()
print(tool.run())
```

## Notes

- The package exports `ArcDexOracleTool` at the package root, but the full tool set is defined in `warppay402_mcp.tools`.
- Many tools accept simple Python arguments and return raw API response text as a string.
- This project depends on `requests` and `langchain-core` as configured in the package metadata.
- `langchain-openai` is required only for the `ChatOpenAI` example.
