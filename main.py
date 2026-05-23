from app.services.llmservice import LLMService


client = LLMService()
 
response = client.generate("What is today's date?") 
print(response)