from app.factories.agent_factories import AgentFactory
from app.services.agent_orchestrator import OrchestratorService 


if __name__ == "__main__":
    user_input = input("Enter your goal: ")

    planner_agent = AgentFactory.create_agent("planner")
    executor_agent = AgentFactory.create_agent("executor")
    research_agent = AgentFactory.create_agent("research")
    writer_agent = AgentFactory.create_agent("writer")
    orchestrator = OrchestratorService(
        planner_agent=planner_agent,
        executor_agent=executor_agent,
        research_agent=research_agent,
        writer_agent=writer_agent)
    response = orchestrator.execute(user_input)
    print(response) 