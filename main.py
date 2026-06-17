from app.agents.executor_agent import ExecutorAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.services.taskmanager import TaskExecutionService


if __name__ == "__main__":
    user_input = input("Enter your goal: ")
    planner_agent = PlannerAgent()
    executor_agent = ExecutorAgent()
    research_agent = ResearchAgent()
    execute = TaskExecutionService(
        planner_agent=planner_agent,
        executor_agent=executor_agent,
        research_agent=research_agent,
    )
    response = execute.execute(user_input)
    print(response) 