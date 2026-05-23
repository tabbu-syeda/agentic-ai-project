import os
import ollama
from app.utils.logger import logger

from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")

class LLMService:

    def __init__(self):

        self.model = os.getenv("MODEL_NAME")

    def generate(self, prompt):

        try:
            
            logger.info("Calling local model")
            response = ollama.chat(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response["message"]["content"]

        except Exception as ex:
            logger.error(f"LLM Error : {str(ex)}")
            return None