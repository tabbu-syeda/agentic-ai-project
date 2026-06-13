class LLMException(Exception):
    pass


class LLMResponseException(LLMException):
    pass


class LLMConnectionException(LLMException):
    pass