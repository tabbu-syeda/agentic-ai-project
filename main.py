from app.factories.agent_factories import AgentFactory
from app.services.agent_orchestrator import OrchestratorService 


if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("app.api.goals:api", host="127.0.0.1", port=8000, reload=True)