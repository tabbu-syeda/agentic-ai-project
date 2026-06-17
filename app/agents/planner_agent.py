import json
from app.agents.base_agent import BaseAgent
from app.models.schemas import TaskList
import traceback

class PlannerAgent(BaseAgent): 
    def run(self, goal):
        AVAILABLE_TOOLS = [
            "web_search",
            "calculator"
        ]
        goal_json = json.dumps(goal)
        prompt = f"""
        You are a planning agent.

        Break the user goal into tasks.

        Only use these exact Available tools names when planning tasks that require tool usage:
        - web_search
        - calculator

        Return ONLY valid JSON.

        JSON format:

        {{
            "goal": {goal_json},
            "tasks": [
                {{
                    "id": "task_1",
                    "title": "title",
                    "description": "description",
                    "status": "pending",
                    "type" : "RESEARCH | CALCULATION | GENERAL",
                    "planned_tools": [
                        {{
                            "tool_name": "name of the tool to call",
                            "input": "input to the tool"
                        }}
                    ]  ,
                    "tool_results" : []                  
                }} 
            ],
            "reasoning": "why tasks were created"
        }} 
        """
        
        try:
            response = self.llm_service.generate(prompt)
            cleaned_response = self.clean_json_response(response)
            validated = TaskList.model_validate_json(cleaned_response)
            return validated
        except Exception as ex:
            traceback.print_exc()
            return {"error": f"Failed to parse response: {str(ex)}"}