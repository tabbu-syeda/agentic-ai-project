from app.tools.base_tool import BaseTool


class WebSearchTool(BaseTool):
    name = "web_search"
    description = "Use this tool to search the web for information relevant to the task. Input should be a search query string."

    def run(self, query: str):
        # Placeholder implementation - replace with actual web search logic
        return f"Search results for query: {query}"