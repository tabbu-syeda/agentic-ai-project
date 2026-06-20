from pydantic import BaseModel

from app.Exceptions.agent_exceptions import AgentException
from app.Exceptions.llm_exceptions import LLMResponseException
from app.agents.base_agent import BaseAgent
from app.models.schemas import Task, TaskList, TaskType
from app.utils.logger import logger


class OrchestratorService:
    def __init__(
        self,
        planner_agent: BaseAgent | None = None,
        executor_agent: BaseAgent | None = None,
        research_agent: BaseAgent | None = None,
        writer_agent: BaseAgent | None = None
    ):
        self.agents = {
            "planner": planner_agent,
            "executor": executor_agent,
            "research": research_agent,
            "writer": writer_agent
        } 
        
    def execute(self, user_input: str):
        task_list = self.agents["planner"].run(user_input)
        logger.info(f"Planner Agent created the following tasks: {task_list}")

        if isinstance(task_list, dict) and "error" in task_list:
            return task_list["error"]

        if not isinstance(task_list, TaskList):
            return str(task_list)
        
        taskList = []
        execution_log = []
        response = None
        for task in task_list.tasks: 
            executionLog = ExecutionRecord(
                task_id=task.id,
                task_title=task.title,
                status=task.status,
                agent_name="default"
            )
            task = self.route_task(task, executionLog)
            taskList.append(task)            
            execution_log.append(executionLog)

        if task_list.tasks and self.agents["writer"] is not None:
            logger.info(f"Generating report with Writer Agent")
            response = self.agents["writer"].run(task_list).content
        
        if response is None:
            raise LLMResponseException("Writer Agent failed: no response generated")
        
        return response
    

    def route_task(self, task: Task, execution_log: ExecutionRecord) -> Task:
        if task.type == TaskType.RESEARCH:
             if self.agents["research"] is None:
                raise AgentException(
                    "Research agent not configured"
                )
             execution_log.agent_name = "research"
             return self.agents["research"].run_task(task)
        else:
            if self.agents["executor"] is None:
                raise AgentException(
                    "Executor agent not configured"
                )
            execution_log.agent_name = "executor"
            return self.agents["executor"].run_task(task)
        

class ExecutionRecord(BaseModel):
    task_id: str
    task_title: str
    agent_name: str
    status: str