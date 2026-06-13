from app.agents.base_agent import BaseAgent 


class TaskExecutionService:
    def __init__(self, planner_agent: BaseAgent, executor_agent: BaseAgent):
        self.planner_agent = planner_agent
        self.executor_agent = executor_agent

    def execute(self, user_input: str): 
        task_list = self.planner_agent.run(user_input)
        print(f"Planner Agent created the following tasks: {task_list}")
        response = self.executor_agent.run(task_list)
        return response