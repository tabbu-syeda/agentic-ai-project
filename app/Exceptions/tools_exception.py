class ToolException(Exception):
    """
    Base exception for all tool errors.
    """
    pass


class ToolNotFoundException(ToolException):
    pass


class ToolExecutionException(ToolException):
    pass