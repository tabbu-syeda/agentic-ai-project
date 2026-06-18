from app.Exceptions.agent_exceptions import WriterException
from app.agents.base_agent import BaseAgent
from app.models.schemas import AgentResponse, TaskList, TaskStatus


class WriterAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def run(self, task_list : TaskList) -> AgentResponse:
  
        writer_context =  "\n".join( [
            f"task Title: {task.title}\n Result: {task.result}"
            for task in task_list.tasks
            if task.status == TaskStatus.COMPLETED 
        ])

        prompt = f"""
        You are a writing assistant. Follow the below instructions for task results:
        {writer_context}

        Instructions:
        - Review the task results.
        - Write a coherent and comprehensive report based on the task.
        - Ensure the report is well-structured, clear, and concise and free of grammatical errors. 
        - Improve readability, clarity, and flow without changing the meaning of the source information.
        - Highlight important findings, insights, risks, and recommendations when they are supported by the provided data.
        - NEVER invent facts, numbers, dates, sources, conclusions, or recommendations.
        - NEVER make assumptions beyond the provided task results.
        - NEVER fill information gaps using prior knowledge.
        Writing Style
            Professional and objective.
            Clear, concise, and well-structured.
            Focus on actionable understanding rather than raw data repetition.
            Avoid unnecessary jargon.
            Use bullet points, tables, and sections when they improve readability.
        """

        response = self.llm_service.generate(prompt)
        if response is None:
            raise WriterException("Writer Agent failed: no response generated")

        return AgentResponse(
            agent_name="writer",
            content=response)
        