from app.agents.executor_agent import ExecutorAgent
from app.services.executor import ExecutorService
from app.agents.planner_agent import PlannerAgent


# response = agent.run("Plan 2 days visit to Goa, India for solo traveller.")
# print(response)

if __name__ == "__main__":
    agent = PlannerAgent() 
    user_input = input("Enter your goal: ")
    execute = ExecutorService()
    taks_list = execute.execute(user_input, agent) 
    executor_agent = ExecutorAgent()
    response = executor_agent.run(taks_list)
    print(response)