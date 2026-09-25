import sys
import asyncio
from mcp.server.mcpserver import MCPServer
from warppay402_mcp.tools import (
    ArcDexOracleTool,
    WebScraperTool,
    BrowserScraperTool,
    BaseAnalyticsTool,
    ArcAnalyticsTool,
    ArcNetworkQueryTool,
    PdfExtractorTool,
    RenderScreenshotTool,
    ExtractJsonTool,
    SmartContractVerifierTool,
    AerodromeYieldsTool,
    AerodromeSwapTool,
    AerodromeClammTool,
    AerodromeVeaeroTool,
    DeployBaseContractTool,
    DeploySolanaContractTool,
    DeployArcContractTool,
    ArcCctpBridgeTool,
    PublicDataFeedTool,
    DataFeedsTool,
    RealEstateCalculatorTool,
    AddressNormalizerTool,
    WeatherOracleTool,
    ForexOracleTool,
    ShippingRateEstimatorTool,
    GithubHealthAnalyzerTool,
    PropertyCompsEstimatorTool,
)

# Initialize MCPServer (mcp 2.x)
mcp = MCPServer("WarpPay402 MCP Gateway")

# Instantiate all 28 tools
tools = [
    ArcDexOracleTool(), WebScraperTool(), BrowserScraperTool(), BaseAnalyticsTool(),
    ArcAnalyticsTool(), ArcNetworkQueryTool(), PdfExtractorTool(), RenderScreenshotTool(),
    ExtractJsonTool(), SmartContractVerifierTool(), AerodromeYieldsTool(), AerodromeSwapTool(),
    AerodromeClammTool(), AerodromeVeaeroTool(), DeployBaseContractTool(), DeploySolanaContractTool(),
    DeployArcContractTool(), ArcCctpBridgeTool(), PublicDataFeedTool(), DataFeedsTool(),
    RealEstateCalculatorTool(), AddressNormalizerTool(), WeatherOracleTool(), ForexOracleTool(),
    ShippingRateEstimatorTool(), GithubHealthAnalyzerTool(), PropertyCompsEstimatorTool()
]

def register_tool(tool_instance):
    """Factory helper to capture unique closure scope for each tool."""
    def handler(*args, **kwargs):
        return tool_instance._run(*args, **kwargs)
    
    handler.__name__ = tool_instance.name
    return mcp.tool(name=tool_instance.name, description=tool_instance.description)(handler)

# Properly register each tool with MCPServer
for tool in tools:
    register_tool(tool)

def main():
    """Main CLI entry point for warppay402-mcp server process."""
    mcp.run()

if __name__ == "__main__":
    main()