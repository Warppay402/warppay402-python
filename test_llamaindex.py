import sys
import unittest
import logging
from unittest.mock import patch, MagicMock

# Configure verbose logging output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("TestWarpPayLlamaIndexTools")

class TestWarpPayLlamaIndexTools(unittest.TestCase):

    def test_import_and_fallback_behavior(self):
        """Test that WarpPayLlamaIndexTools imports cleanly or handles missing dependencies."""
        logger.info("==================================================")
        logger.info("TEST 1: Testing import and fallback behavior...")
        
        try:
            import llama_index.core.tools  # noqa: F401
            logger.info("  [✓] 'llama-index-core' is detected in the active environment.")
            
            from warppay402_mcp import WarpPayLlamaIndexTools
            self.assertIsNotNone(
                WarpPayLlamaIndexTools,
                "WarpPayLlamaIndexTools should be defined when llama-index-core is installed"
            )
            logger.info("  [✓] Successfully verified WarpPayLlamaIndexTools is available.")
            
        except ImportError as e:
            logger.warning(f"  [!] 'llama-index-core' is NOT installed: {e}")
            from warppay402_mcp import WarpPayLlamaIndexTools
            self.assertIsNone(
                WarpPayLlamaIndexTools,
                "WarpPayLlamaIndexTools should be None when llama-index-core is absent"
            )
            logger.info("  [✓] Verified graceful fallback: WarpPayLlamaIndexTools is set to None.")

    def test_get_tools_returns_all_29_tools(self):
        """Verify that get_tools() wraps all 29 tools as FunctionTool instances."""
        logger.info("==================================================")
        logger.info("TEST 2: Verifying LlamaIndex tool generation for all 29 tools...")

        try:
            import llama_index.core.tools  # noqa: F401
            logger.info("  [✓] Found 'llama-index-core'. Proceeding with tool generation check...")
        except ImportError:
            logger.warning("  [!] Skipping tool wrapping check because 'llama-index-core' is not installed.")
            self.skipTest("llama-index-core is not installed in the environment. Skipping mock test.")

        with patch("warppay402_mcp.llamaindex.FunctionTool") as mock_function_tool:
            # Helper function to create mock objects with attributes set properly
            def create_mock_tool(fn, name, description):
                mock_tool = MagicMock()
                mock_tool.name = name
                mock_tool.description = description
                mock_tool.metadata.name = name
                mock_tool.metadata.description = description
                return mock_tool

            mock_function_tool.from_defaults.side_effect = create_mock_tool

            from warppay402_mcp.llamaindex import WarpPayLlamaIndexTools, ALL_LANGCHAIN_TOOLS

            logger.info(f"  [ℹ] Source tools loaded: {len(ALL_LANGCHAIN_TOOLS)} tools in ALL_LANGCHAIN_TOOLS.")

            tools = WarpPayLlamaIndexTools.get_tools()
            logger.info(f"  [ℹ] Converted tools generated: {len(tools)} LlamaIndex FunctionTools.")

            # Print full itemized log of converted tools
            logger.info("  --------------------------------------------------")
            logger.info("  Itemized Converted Tool Log:")
            for idx, tool in enumerate(tools, start=1):
                logger.info(f"    {idx:02d}. Name: {tool.name:<28} | Description: {tool.description[:45]}...")
            logger.info("  --------------------------------------------------")

            # Assertions
            self.assertEqual(len(tools), 29, "Expected exactly 29 converted tools.")
            self.assertEqual(len(ALL_LANGCHAIN_TOOLS), 29, "Expected 29 source LangChain tools.")
            self.assertEqual(mock_function_tool.from_defaults.call_count, 29)
            logger.info("  [✓] Tool count assertion passed: 29/29 tools converted successfully.")

            # Specific capability checks
            names = [tool.name for tool in tools]
            required_sample_names = ["arc_dex_oracle", "get_aerodrome_yields", "web_scraper", "ucp_deals_oracle"]
            for name in required_sample_names:
                self.assertIn(name, names)
                logger.info(f"  [✓] Confirmed presence of sample capability: '{name}'")

        logger.info("==================================================")
        logger.info("TEST SUMMARY: All LlamaIndex integration tests completed successfully!")

if __name__ == "__main__":
    unittest.main(verbosity=2)