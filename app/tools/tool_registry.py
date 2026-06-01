
from app.tools.calculator_tool import CalculatorTool
from app.tools.websearch_tool import WebSearchTool


class ToolRegistry:
    def __init__(self):
        self.tools = {
            "calculator" : CalculatorTool(),
            "web_search" : WebSearchTool()
        }

    def get_tool(self, tool_name: str): 
        return self.tools.get(tool_name, None)