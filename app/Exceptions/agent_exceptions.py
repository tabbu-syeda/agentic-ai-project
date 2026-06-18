class AgentException(Exception):
    pass


class PlannerException(AgentException):
    pass


class ExecutorException(AgentException):
    pass

class WriterException(AgentException):
    pass