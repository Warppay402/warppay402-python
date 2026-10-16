from typing import List
from llama_index.core.tools import FunctionTool
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
    OutageOracleTool,
    ForexOracleTool,
    ShippingRateEstimatorTool,
    GithubHealthAnalyzerTool,
    PropertyCompsEstimatorTool,
    UcpDealsOracleTool,
)

ALL_LANGCHAIN_TOOLS = [
    ArcDexOracleTool(), WebScraperTool(), BrowserScraperTool(), BaseAnalyticsTool(),
    ArcAnalyticsTool(), ArcNetworkQueryTool(), PdfExtractorTool(), RenderScreenshotTool(),
    ExtractJsonTool(), SmartContractVerifierTool(), AerodromeYieldsTool(), AerodromeSwapTool(),
    AerodromeClammTool(), AerodromeVeaeroTool(), DeployBaseContractTool(), DeploySolanaContractTool(),
    DeployArcContractTool(), ArcCctpBridgeTool(), PublicDataFeedTool(), DataFeedsTool(),
    RealEstateCalculatorTool(), AddressNormalizerTool(), WeatherOracleTool(), OutageOracleTool(),
    ForexOracleTool(), ShippingRateEstimatorTool(), GithubHealthAnalyzerTool(), PropertyCompsEstimatorTool(),
    UcpDealsOracleTool()
]

class WarpPayLlamaIndexTools:
    """Helper class to convert WarpPay402 tools into LlamaIndex FunctionTools."""

    @staticmethod
    def get_tools() -> List[FunctionTool]:
        """Returns all 29 WarpPay402 tools wrapped as LlamaIndex FunctionTool instances."""
        llamaindex_tools = []
        for tool in ALL_LANGCHAIN_TOOLS:
            # Wrap each LangChain tool's _run method as a LlamaIndex FunctionTool
            llamaindex_tool = FunctionTool.from_defaults(
                fn=tool._run,
                name=tool.name,
                description=tool.description,
            )
            llamaindex_tools.append(llamaindex_tool)
        return llamaindex_tools