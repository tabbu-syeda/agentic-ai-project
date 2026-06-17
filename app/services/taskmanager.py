from app.agents.base_agent import BaseAgent
from app.models.schemas import TaskList, TaskType


class TaskExecutionService:
    def __init__(
        self,
        planner_agent: BaseAgent,
        executor_agent: BaseAgent,
        research_agent: BaseAgent | None = None,
    ):
        self.planner_agent = planner_agent
        self.executor_agent = executor_agent
        self.research_agent = research_agent

    def execute(self, user_input: str):
        task_list = self.planner_agent.run(user_input)
        print(f"Planner Agent created the following tasks: {task_list}")

        if isinstance(task_list, dict) and "error" in task_list:
            return task_list["error"]

        if not isinstance(task_list, TaskList):
            return str(task_list)
        
        response = []
        for task in task_list.tasks: 
            if task.type == TaskType.RESEARCH:
                 task = self.research_agent.run_task(task)
            else:
                task = self.executor_agent.run_task(task)
            response.append(task.result)
        
        return response