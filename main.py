from app.services.llmservice import LLMService
from app.agents.planner_agent import PlannerAgent

agent = PlannerAgent()

response = agent.run("How to make cold coffee?")
print(response)