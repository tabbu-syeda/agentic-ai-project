from app.agents.base_agent import BaseAgent


class PlannerAgent(BaseAgent):

    def run(self, goal):

        prompt = f"""
        Break this goal into clear numbered tasks.

        Goal:
        {goal}
        """

        return self.llm_service.generate(prompt)