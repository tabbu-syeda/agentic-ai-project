
from fastapi import FastAPI 
from app.factories.agent_factories import AgentFactory
from app.models.chat_response import ChatRequest
from app.services.agent_orchestrator import OrchestratorService


api = FastAPI()

@api.post("/chat")
def chat(request: ChatRequest):
    if request.goal:
        planner_agent = AgentFactory.create_agent("planner")
        executor_agent = AgentFactory.create_agent("executor")
        research_agent = AgentFactory.create_agent("research")
        writer_agent = AgentFactory.create_agent("writer")
        orchestrator = OrchestratorService(
            planner_agent=planner_agent,
            executor_agent=executor_agent,
            research_agent=research_agent,
            writer_agent=writer_agent)
        response = orchestrator.execute(request.goal)
    return {
        "response": response
    }