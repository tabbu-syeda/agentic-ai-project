from pydantic import BaseModel
from typing import Any, List, Optional
from enum import Enum
from datetime import datetime

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

class ToolCall(BaseModel):
    tool_name: str
    input: str

class ToolResult(BaseModel):
    tool_name: str
    query: str
    result: Any
    success: bool = True
    error: Optional[str] = None
    timestamp: datetime

class Task(BaseModel):
    id: str
    title: str
    description: str
    status: TaskStatus
    planned_tools: Optional[List[ToolCall]] = None
    tool_results: Optional[List[ToolResult]] = None
    result: Optional[str] = None


class TaskList(BaseModel):
    goal: str
    tasks: List[Task]
    reasoning: str


class AgentResponse(BaseModel):
    agent_name: str
    content: str
    task_list: Optional[TaskList] = None