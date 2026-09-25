import requests
from typing import Optional, Dict, Any
from langchain_core.tools import BaseTool

BASE_URL = "https://api.warppay402.com/api/v1/tools"

class ArcDexOracleTool(BaseTool):
    name: str = "arc_dex_oracle"
    description: str = "Real-time ETH/USDC spot price resolver and DEX liquidity oracle for Arc Mainnet ($0.001 USDC)."

    def _run(self, pair: str = "ETH/USDC") -> str:
        res = requests.post(f"{BASE_URL}/arc-dex-oracle", json={"pair": pair})
        return res.text

class WebScraperTool(BaseTool):
    name: str = "web_scraper"
    description: str = "Scrapes any public webpage URL into clean Markdown for AI context window ingestion ($0.001 USDC)."

    def _run(self, url: str) -> str:
        res = requests.post(f"{BASE_URL}/web-scraper", json={"url": url})
        return res.text

class BrowserScraperTool(BaseTool):
    name: str = "browser_scraper"
    description: str = "Executes unblockable JavaScript Chromium rendering via proxy workers ($0.005 USDC)."

    def _run(self, url: str) -> str:
        res = requests.post(f"{BASE_URL}/browser-scraper", json={"url": url})
        return res.text

class BaseAnalyticsTool(BaseTool):
    name: str = "base_analytics"
    description: str = "Fetches ETH balance, nonce, and account stats for any 0x wallet on Base Mainnet ($0.002 USDC)."

    def _run(self, address: str) -> str:
        res = requests.post(f"{BASE_URL}/base-analytics", json={"address": address})
        return res.text

class ArcAnalyticsTool(BaseTool):
    name: str = "arc_analytics"
    description: str = "Fetches live block height, gas price, and RPC latency from Arc Mainnet ($0.001 USDC)."

    def _run(self) -> str:
        res = requests.post(f"{BASE_URL}/arc-analytics")
        return res.text

class ArcNetworkQueryTool(BaseTool):
    name: str = "arc_network_oracle_query"
    description: str = "Pre-flight Arc Mainnet telemetry: RPC latency (ms), gas prices (Gwei), native USDC balance, and account nonce ($0.10 USDC)."

    def _run(self, includeGasTrends: bool = True, checkMerchantAccount: bool = True) -> str:
        payload = {"includeGasTrends": includeGasTrends, "checkMerchantAccount": checkMerchantAccount}
        res = requests.post(f"{BASE_URL}/arc-network-query", json=payload)
        return res.text

class PdfExtractorTool(BaseTool):
    name: str = "pdf_extractor"
    description: str = "Downloads and extracts clean plain text preview from public PDF document URLs ($0.005 USDC)."

    def _run(self, pdfUrl: str) -> str:
        res = requests.post(f"{BASE_URL}/pdf-extractor", json={"pdfUrl": pdfUrl})
        return res.text

class RenderScreenshotTool(BaseTool):
    name: str = "render_screenshot"
    description: str = "Captures full-page rendered screenshot image data from target URL ($0.01 USDC)."

    def _run(self, url: str) -> str:
        res = requests.post(f"{BASE_URL}/render-screenshot", json={"url": url})
        return res.text

class ExtractJsonTool(BaseTool):
    name: str = "extract_json"
    description: str = "Extracts structured JSON schema data from web page HTML content ($0.01 USDC)."

    def _run(self, url: str, schema: Optional[Dict[str, Any]] = None) -> str:
        payload = {"url": url, "schema": schema or {}}
        res = requests.post(f"{BASE_URL}/extract-json", json=payload)
        return res.text

class SmartContractVerifierTool(BaseTool):
    name: str = "smart_contract_verifier"
    description: str = "Source code analysis, bytecode validation, ABI fetching, and proxy detection on Basescan ($0.02 USDC)."

    def _run(self, address: str) -> str:
        res = requests.post(f"{BASE_URL}/smart-contract-verifier", json={"address": address})
        return res.text

class AerodromeYieldsTool(BaseTool):
    name: str = "get_aerodrome_yields"
    description: str = "Fetches top live Aerodrome DEX yield pools, APYs, and TVL on Base Mainnet ($0.003 USDC)."

    def _run(self) -> str:
        res = requests.get(f"{BASE_URL}/aerodrome-yields")
        return res.text

class AerodromeSwapTool(BaseTool):
    name: str = "aerodrome_swap"
    description: str = "Executes low-slippage token swaps directly via Aerodrome Finance Router on Base ($0.01 USDC)."

    def _run(self, tokenIn: str, tokenOut: str, amountIn: str, decimalsIn: int, isStable: bool) -> str:
        payload = {
            "tokenIn": tokenIn, "tokenOut": tokenOut,
            "amountIn": amountIn, "decimalsIn": decimalsIn, "isStable": isStable
        }
        res = requests.post(f"{BASE_URL}/aerodrome-swap", json=payload)
        return res.text

class AerodromeClammTool(BaseTool):
    name: str = "aerodrome_clamm"
    description: str = "Open, adjust, and rebalance concentrated liquidity ranges on Aerodrome Slipstream ($0.01 USDC)."

    def _run(self, action: str, token0: Optional[str] = None, token1: Optional[str] = None,
             tickLower: Optional[int] = None, tickUpper: Optional[int] = None,
             amount0Desired: Optional[str] = None, amount1Desired: Optional[str] = None,
             tokenId: Optional[str] = None) -> str:
        payload = {
            "action": action, "token0": token0, "token1": token1,
            "tickLower": tickLower, "tickUpper": tickUpper,
            "amount0Desired": amount0Desired, "amount1Desired": amount1Desired, "tokenId": tokenId
        }
        res = requests.post(f"{BASE_URL}/aerodrome-clamm", json=payload)
        return res.text

class AerodromeVeaeroTool(BaseTool):
    name: str = "aerodrome_veaero"
    description: str = "Automates $AERO locking, epoch gauge voting, and bribe reward harvesting on Aerodrome ($0.01 USDC)."

    def _run(self, action: str, amount: Optional[str] = None, lockDurationWeeks: Optional[int] = None,
             tokenId: Optional[str] = None, poolVoteAddresses: Optional[list] = None) -> str:
        payload = {
            "action": action, "amount": amount, "lockDurationWeeks": lockDurationWeeks,
            "tokenId": tokenId, "poolVoteAddresses": poolVoteAddresses
        }
        res = requests.post(f"{BASE_URL}/aerodrome-veaero", json=payload)
        return res.text

class DeployBaseContractTool(BaseTool):
    name: str = "deploy_contract"
    description: str = "Programmatically deploys custom Escrow, Bounty, or Subscription contracts to Base Mainnet ($5.00 USDC)."

    def _run(self, contractType: str = "escrow") -> str:
        res = requests.post(f"{BASE_URL}/deploy-contract", json={"contractType": contractType})
        return res.text

class DeploySolanaContractTool(BaseTool):
    name: str = "deploy_solana_contract"
    description: str = "Initializes SPL Escrows, cNFT Badge Issuers, or Raydium Vaults on Solana Mainnet ($5.00 USDC)."

    def _run(self, contractType: str, params: Dict[str, Any]) -> str:
        payload = {"contractType": contractType, "params": params}
        res = requests.post(f"{BASE_URL}/deploy-solana-contract", json=payload)
        return res.text

class DeployArcContractTool(BaseTool):
    name: str = "deploy_arc_contract"
    description: str = "Programmatically deploys custom Escrow, Bounty, or Agent contracts directly to Arc Mainnet ($5.00 USDC)."

    def _run(self, contractType: str = "escrow") -> str:
        res = requests.post(f"{BASE_URL}/deploy-arc-contract", json={"contractType": contractType})
        return res.text

class ArcCctpBridgeTool(BaseTool):
    name: str = "arc_cctp_bridge"
    description: str = "Bridges USDC cross-chain from Arc Mainnet via Circle CCTP V2 ($0.25 USDC)."

    def _run(self, amountUsdc: str, destinationChain: str, recipientAddress: str) -> str:
        payload = {
            "amountUsdc": amountUsdc, "destinationChain": destinationChain, "recipientAddress": recipientAddress
        }
        res = requests.post(f"{BASE_URL}/arc-cctp-bridge", json=payload)
        return res.text

class PublicDataFeedTool(BaseTool):
    name: str = "public_data_feed"
    description: str = "Retrieves signed attestation JSON payloads from the public data feed ($0.0001 USDC)."

    def _run(self, filename: str) -> str:
        res = requests.get(f"https://api.warppay402.com/public_data_feed/{filename}")
        return res.text

class DataFeedsTool(BaseTool):
    name: str = "data_feeds"
    description: str = "Fetches pre-scraped market data feeds and yield reports ($0.001 USDC)."

    def _run(self, feedId: str) -> str:
        res = requests.get(f"https://api.warppay402.com/api/v1/feeds/{feedId}")
        return res.text

class RealEstateCalculatorTool(BaseTool):
    name: str = "real_estate_calculator"
    description: str = "Calculates NOI, Cap Rate, Monthly Cash Flow, and DSCR for real estate deals ($0.0005 USDC)."

    def _run(self, purchasePrice: float, monthlyRent: float, annualTaxes: Optional[float] = None,
             annualInsurance: Optional[float] = None, interestRate: float = 6.5, downPaymentPct: float = 20.0) -> str:
        payload = {
            "purchasePrice": purchasePrice,
            "monthlyRent": monthlyRent,
            "annualTaxes": annualTaxes,
            "annualInsurance": annualInsurance,
            "interestRate": interestRate,
            "downPaymentPct": downPaymentPct,
        }
        res = requests.post(f"{BASE_URL}/real-estate-calculator", json=payload)
        return res.text

class AddressNormalizerTool(BaseTool):
    name: str = "address_normalizer"
    description: str = "Standardizes informal address queries and resolves lat/lon coordinates ($0.001 USDC)."

    def _run(self, address: str) -> str:
        res = requests.post(f"{BASE_URL}/address-normalizer", json={"address": address})
        return res.text

class WeatherOracleTool(BaseTool):
    name: str = "weather_oracle"
    description: str = "Fetches live atmospheric conditions, wind speed, visibility, and flight safety clearances ($0.001 USDC)."

    def _run(self, latitude: float, longitude: float) -> str:
        payload = {"latitude": latitude, "longitude": longitude}
        res = requests.post(f"{BASE_URL}/weather-oracle", json=payload)
        return res.text

class ForexOracleTool(BaseTool):
    name: str = "forex_oracle"
    description: str = "Resolves real-time global foreign exchange fiat rates ($0.0005 USDC)."

    def _run(self, baseCurrency: str = "USD") -> str:
        res = requests.post(f"{BASE_URL}/forex-oracle", json={"baseCurrency": baseCurrency})
        return res.text

class ShippingRateEstimatorTool(BaseTool):
    name: str = "shipping_rate_estimator"
    description: str = "Calculates ground, priority, and express shipping rates for e-commerce ($0.001 USDC)."

    def _run(self, weightLbs: float, originZip: str, destinationZip: str) -> str:
        payload = {"weightLbs": weightLbs, "originZip": originZip, "destinationZip": destinationZip}
        res = requests.post(f"{BASE_URL}/shipping-rate-estimator", json=payload)
        return res.text

class GithubHealthAnalyzerTool(BaseTool):
    name: str = "github_health_analyzer"
    description: str = "Queries public GitHub repo stars, open issues, licenses, and push activity ($0.002 USDC)."

    def _run(self, repository: str) -> str:
        res = requests.post(f"{BASE_URL}/github-health-analyzer", json={"repository": repository})
        return res.text

class PropertyCompsEstimatorTool(BaseTool):
    name: str = "property_comps_estimator"
    description: str = "Generates market valuations, price-per-sqft comps, and annual tax estimates ($0.005 USDC)."

    def _run(self, squareFeet: float, bedrooms: int, zipCode: str) -> str:
        payload = {"squareFeet": squareFeet, "bedrooms": bedrooms, "zipCode": zipCode}
        res = requests.post(f"{BASE_URL}/property-comps-estimator", json=payload)
        return res.text