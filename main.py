from app.services.llmservice import LLMService
from app.agents.planner_agent import PlannerAgent

agent = PlannerAgent()

response = agent.run("Plan 2 days visit to Goa, India for solo traveller.")
print(response)