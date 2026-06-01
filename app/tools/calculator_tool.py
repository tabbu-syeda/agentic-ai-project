from app.tools.base_tool import BaseTool


class CalculatorTool(BaseTool):
    name = "calculator"
    description = "A tool for performing mathematical calculations. Input should be a string representing the mathematical expression to evaluate. For example, '2 + 2' or 'sqrt(16)'."

    def run(self, expression: str):
        try:
            # WARNING: Using eval can be dangerous. In production, consider using a safe math parser.
            result = eval(expression)
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {str(e)}"