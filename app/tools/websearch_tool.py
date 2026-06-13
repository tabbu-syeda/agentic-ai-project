from app.tools.base_tool import BaseTool
from ddgs import DDGS


class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Use this tool to search the web for information relevant to the task. Input should be a search query string."

    def run(self, query: str):
        # Placeholder implementation - replace with actual web search logic
        with DDGS() as ddgs:

            results = ddgs.text(
                query,
                max_results=5
            )
        return f"{results}"