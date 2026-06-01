from app.agents.base_agent import BaseAgent
from app.services.llmservice import LLMService


class ExecutorService:
    def __init__(self):
        # Initialize any necessary resources, such as tool registry, LLM service, etc.
        pass

    def execute(self, user_input: str, agent : BaseAgent):
        # Parse the user input to determine which tools to use and what actions to take
        response = agent.run(user_input)
        return response