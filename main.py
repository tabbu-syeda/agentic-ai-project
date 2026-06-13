from app.agents.executor_agent import ExecutorAgent
from app.services.taskmanager import TaskExecutionService
from app.agents.planner_agent import PlannerAgent

 

if __name__ == "__main__": 
    user_input = input("Enter your goal: ") 
    agent = PlannerAgent() 
    executor_agent = ExecutorAgent() 
    execute = TaskExecutionService(planner_agent=agent, executor_agent=executor_agent) 
    response = execute.execute(user_input)
    print(response) 