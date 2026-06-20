
from app.agents.base_agent import BaseAgent
from app.agents.executor_agent import ExecutorAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.writer_agent import WriterAgent


class AgentFactory:
    
    @staticmethod
    def create_agent(agent_type: str, **kwargs) -> BaseAgent:
        if agent_type == "planner":
            return PlannerAgent(**kwargs)
        elif agent_type == "executor":
            return ExecutorAgent(**kwargs)
        elif agent_type == "research":
            return ResearchAgent(**kwargs)
        elif agent_type == "writer":
            return WriterAgent(**kwargs)
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")