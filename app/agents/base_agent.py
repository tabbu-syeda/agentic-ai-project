
from app.services.llmservice import LLMService


class BaseAgent:
    def __init__(self):
        self.llm_service = LLMService()

    def run(self, input):
        raise NotImplementedError("Subclasses must implement this method")