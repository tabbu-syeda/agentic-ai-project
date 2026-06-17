# Agent that performs iterative search and research tasks

from app.agents.base_agent import BaseAgent
from app.models.schemas import AgentResponse, Task, TaskStatus
from app.tools.tool_registry import ToolRegistry


class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.registry = ToolRegistry()

    def run_task(self, task: Task) -> Task: 
        search_tool = self.registry.get_tool("web_search")
        if search_tool is None:
            task.status = TaskStatus.BLOCKED
            task.result = "web_search tool is not available"
            return AgentResponse(
                agent_name="research",
                content=task.result,
            )

        queries = []
        if task.planned_tools:
            queries.extend(tool.input for tool in task.planned_tools)
        else:
            queries.extend([task.title, task.description])

        collected_results = []
        for query in queries:
            result = search_tool.run(query)
            collected_results.append(f"Query: {query}\nResult:\n{result}")

        prompt = f"""
        You are a research assistant.

        Task Title:
        {task.title}

        Task Description:
        {task.description}

        Search Results:
        {chr(10).join(collected_results)}

        Instructions:
        - Aggregate the findings.
        - Highlight the most relevant points.
        - Provide a concise but useful summary.
        """

        response = self.llm_service.generate(prompt)
        if response is None:
            task.status = TaskStatus.BLOCKED
            task.result = "Research failed: no response generated"
            return AgentResponse(
                agent_name="research",
                content=task.result,
            )

        task.result = response
        task.status = TaskStatus.COMPLETED

        return task

