from datetime import datetime
import traceback

from app.Exceptions.llm_exceptions import LLMResponseException
from app.Exceptions.tools_exception import ToolNotFoundException
from app.agents.base_agent import BaseAgent
from app.models.schemas import  Task, TaskStatus, ToolResult
from app.tools.tool_registry import ToolRegistry 


class ExecutorAgent(BaseAgent):
    def __init__(self):
        super().__init__()  # this will initialize the llm_service from BaseAgent
        self.registry = ToolRegistry()

    def run(self, task_list):
        
        results =[] 
        for task in task_list.tasks:
            try:
                print(
                    f"Executing: {task.title}"
                ) 

                if task.planned_tools:
                    self.execute_tool(task)                    
                else:
                    print(
                        f"Executing without tools: {task.title}"
                    )

                    self.execute_llm_task(
                        task
                    )

                results.append(
                    f"{task.title}: {task.result}"
                )

            except Exception as ex:

                task.status = (
                    TaskStatus.BLOCKED
                )

                task.result = str(ex)

                results.append(
                    f"{task.title}: FAILED"
                )
                print(f"Error executing task {task.title}: {traceback.format_exc()}")

        return "\n".join(results)
    
    def execute_tool(self, task):
       
        for tool in task.planned_tools:

            print(f"Executing task : {task.title} with tool {tool.tool_name} and input {tool.input}")

            tool_func = self.registry.get_tool(tool.tool_name)
             

            if tool_func:
                result = tool_func.run(tool.input)

                tool_result = ToolResult(
                            tool_name=tool.tool_name,
                            query=tool.input,
                            result=result,
                            success=True,
                            timestamp = datetime.now()
                        )  
                
                task.tool_results.append(tool_result) 
            else:
                tool_result = ToolResult(
                    tool_name=tool.tool_name,
                    query=tool.input,
                    result=None,
                    success=False,
                    error="Tool not found",
                    timestamp = datetime.now()
                ) 
                task.tool_results.append(tool_result)
                task.status = TaskStatus.BLOCKED
                task.result = "Tool not found"
                print(f"Default tool added for {tool.tool_name} for task {task.title}")
                raise ToolNotFoundException(f"Tool {tool.tool_name} is not registered.");
               
        
        tool_context = "\n".join( [
            str(t.result)
            for t in task.tool_results
            if t.success
        ])
        print(f"Tool context for task {task.title}: {tool_context}")
        prompt = f"""
            Use the following tool output to
            complete the task.

            Task:
            {task.description}

            Tool Output:
            {tool_context}

            Return a concise answer.
            """

        final_answer = self.llm_service.generate( prompt)
        
        task.result = final_answer
        task.status = TaskStatus.COMPLETED 



    def execute_llm_task(self, task):
        prompt = f"""
            Complete the following task.

            Title:
            {task.title}

            Description:
            {task.description}

            Return concise output.
            """

        output = self.llm_service.generate( prompt)
        if output is None:
            raise LLMResponseException("LLM failed to generate a response")
        
        task.result = output

        task.status = ( TaskStatus.COMPLETED )


    def run_task(self, task: Task) -> Task:

        if task.planned_tools:
            self.execute_tool(task)
        else:
            self.execute_llm_task(task)

        return task