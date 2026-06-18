from app.agents.executor_agent import ExecutorAgent
from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.writer_agent import WriterAgent
from app.services.taskmanager import TaskExecutionService


if __name__ == "__main__":
    user_input = input("Enter your goal: ")
    planner_agent = PlannerAgent()
    executor_agent = ExecutorAgent()
    research_agent = ResearchAgent()
    writer_agent = WriterAgent()  
    execute = TaskExecutionService(
        planner_agent=planner_agent,
        executor_agent=executor_agent,
        research_agent=research_agent,
        writer_agent=writer_agent)
    response = execute.execute(user_input)
    print(response) 