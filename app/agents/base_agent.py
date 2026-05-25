
from app.services.llmservice import LLMService


class BaseAgent:
    def __init__(self):
        self.llm_service = LLMService()

    def run(self, input):
        raise NotImplementedError("Subclasses must implement this method")
    
    def clean_json_response( self,content):
        content = content.strip()

        if content.startswith("```json"):
            content = content.replace("```json", "")

        if content.endswith("```"):
            content = content[:-3]

        return content.strip()