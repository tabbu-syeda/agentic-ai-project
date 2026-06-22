# README.md

# Agentic AI Multi-Agent System

A learning-focused yet scalable **Agentic AI platform** built with Python, local LLMs, FastAPI, and Streamlit.

This project demonstrates how to move beyond simple prompt-response applications and build a modular AI system capable of:

- Planning tasks
- Executing actions
- Performing research
- Generating reports
- Orchestrating multiple specialized agents
- Integrating external tools
- Supporting future memory and RAG capabilities

The project follows a structured roadmap from basic LLM integration to a complete multi-agent architecture.

---

# Project Vision

Most beginner AI projects stop at:

```text
User
 ↓
Prompt
 ↓
LLM
 ↓
Response
```

This project goes further:

```text
User
 ↓
API / UI
 ↓
Orchestrator
 ↓
Specialized Agents
 ↓
Tools + LLM
 ↓
Final Response
```

The goal is to understand the core concepts behind modern agent systems rather than relying heavily on third-party frameworks.

---

# Features

## Multi-Agent Architecture

The system currently supports:

### Planner Agent

Responsible for:

- Understanding user goals
- Breaking goals into tasks
- Creating structured execution plans
- Selecting appropriate tools

Example:

```text
User:
Compare AWS Lambda and Azure Functions

Planner:
1. Research AWS Lambda
2. Research Azure Functions
3. Compare pricing
4. Generate recommendation
```

---

### Executor Agent

Responsible for:

- Executing tasks
- Calling tools
- Running LLM tasks
- Collecting execution results
- Updating task status

Supports:

- Tool execution path
- Direct LLM execution path

---

### Research Agent

Responsible for:

- Handling research-oriented tasks
- Performing iterative information gathering
- Aggregating findings
- Generating structured research output

Unlike the Executor Agent, the Research Agent is designed to perform multi-step research workflows.

---

### Writer Agent

Responsible for:

- Combining task outputs
- Formatting final responses
- Generating reports
- Producing user-friendly summaries

---

### Orchestrator Service

Acts as the central coordinator.

Responsibilities:

- Task routing
- Agent selection
- Workflow management
- Aggregating outputs
- Coordinating end-to-end execution

The Orchestrator evolved from a simple task execution service into a workflow engine for multi-agent collaboration.

---

# Architecture

```text
                         ┌─────────────┐
                         │    User     │
                         └──────┬──────┘
                                │
                                ▼
                    ┌────────────────────┐
                    │ FastAPI / Streamlit│
                    └─────────┬──────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │  Orchestrator Service  │
                 └───────────┬────────────┘
                             │
      ┌──────────────────────┼──────────────────────┐
      │                      │                      │
      ▼                      ▼                      ▼
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│ PlannerAgent│      │ResearchAgent│      │WriterAgent  │
└──────┬──────┘      └──────┬──────┘      └──────┬──────┘
       │                    │                    │
       ▼                    ▼                    │
 ┌─────────────┐     ┌─────────────┐             │
 │ Task List   │     │ExecutorAgent│             │
 └──────┬──────┘     └──────┬──────┘             │
        │                   │                    │
        ▼                   ▼                    ▼
  ┌──────────┐      ┌────────────────┐   Final Response
  │   Tools  │      │  LLM Service   │
  └──────────┘      └────────────────┘
```

---

# Technology Stack

| Layer                    | Technology                                                           |
| ------------------------ | -------------------------------------------------------------------- |
| Language                 | Python 3.11+                                                         |
| LLM Runtime              | [Ollama](https://ollama.com/?utm_source=chatgpt.com)                 |
| Models                   | Qwen2.5, Llama 3.x                                                   |
| API Framework            | [FastAPI](https://fastapi.tiangolo.com/?utm_source=chatgpt.com)      |
| Frontend                 | [Streamlit](https://streamlit.io/?utm_source=chatgpt.com)            |
| Validation               | [Pydantic](https://docs.pydantic.dev/latest/?utm_source=chatgpt.com) |
| Search                   | DuckDuckGo Search                                                    |
| Vector Database (Future) | [ChromaDB](https://www.trychroma.com/?utm_source=chatgpt.com)        |
| Embeddings (Future)      | SentenceTransformers                                                 |
| Agent Framework          | Custom Python Framework                                              |

Based on the original roadmap's recommended stack.

---

# Project Structure

```text
app/
│
├── agents/
│   ├── base_agent.py
│   ├── planner_agent.py
│   ├── executor_agent.py
│   ├── research_agent.py
│   └── writer_agent.py
│
├── services/
│   ├── llm_service.py
│   ├── orchestrator_service.py
│   └── agent_factory.py
│
├── tools/
│   ├── base_tool.py
│   ├── web_search_tool.py
│   ├── calculator_tool.py
│   └── tool_registry.py
│
├── models/
│   ├── schemas.py
│   ├── request_models.py
│   └── response_models.py
│
├── exceptions/
│   ├── tool_exceptions.py
│   ├── agent_exceptions.py
│   └── llm_exceptions.py
│
├── api/
│   └── routes.py
│
└── main.py
```

---

# Workflow

## Step 1 – User Request

```text
Compare AWS Lambda and Azure Functions
```

---

## Step 2 – Planner Agent

Creates structured tasks.

Example:

```text
1. Research AWS Lambda
2. Research Azure Functions
3. Compare Features
4. Generate Recommendation
```

---

## Step 3 – Orchestrator

Routes tasks based on task type.

```text
Research Task
    ↓
ResearchAgent

Execution Task
    ↓
ExecutorAgent
```

---

## Step 4 – Execution

The Executor Agent:

- Executes tools
- Runs LLM tasks
- Collects results

```text
Task
 ↓
Tool Execution
 ↓
Tool Result
 ↓
LLM Synthesis
 ↓
Final Task Output
```

This synthesis step is what transforms raw tool output into useful answers.

---

## Step 5 – Writer Agent

Combines outputs:

```text
Task Results
 ↓
Formatting
 ↓
Final Report
```

---

## Step 6 – API/UI Response

Result is returned through:

- FastAPI endpoint
- Streamlit UI

---

# API Endpoints

## Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "goal": "What is an AI Agent?"
}
```

Response:

```json
{
  "response": "..."
}
```

FastAPI becomes the primary entry point for testing once the API layer is added.

---

# Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

```bash
ollama serve
```

---

## Pull Model

```bash
ollama pull qwen2.5:7b
```

or

```bash
ollama pull llama3.1:8b
```

---

## Run FastAPI

```bash
python -m main
```

---

## Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
streamlit run app/ui/streamlit_app.py
```

---

# Future Enhancements

## 1. Conversation Memory

Add:

```text
Short-Term Memory
```

Capabilities:

- Chat history
- Context retention
- Personalized responses

Planned as Day 13 functionality.

---

## 2. RAG (Retrieval-Augmented Generation)

Add:

- Document ingestion
- Embeddings
- Semantic search
- Knowledge retrieval

Using:

- ChromaDB
- SentenceTransformers

Planned in Week 3.

---

## 3. Execution Tracing

Track:

```text
Task
Agent
Duration
Status
```

Useful for:

- Debugging
- Monitoring
- Agent analytics

Suggested during orchestrator evolution.

---

## 4. Additional Agents

Potential future agents:

- Coding Agent
- Reviewer Agent
- Memory Agent
- Data Analysis Agent
- Planning Agent V2
- Critic Agent

---

## 5. Async Execution

Support:

- Parallel tool calls
- Faster research workflows
- Better scalability

Planned for later project stages.

---

## 6. LangGraph Integration

Current architecture intentionally avoids heavy frameworks.

Future migration path:

```text
Custom Orchestrator
        ↓
LangGraph
```

for advanced workflow management.

---

## 7. Multi-Tool Research Workflows

Enhance ResearchAgent to:

```text
Generate Research Questions
 ↓
Multiple Searches
 ↓
Evidence Collection
 ↓
Analysis
 ↓
Final Report
```

This is the natural evolution of the current research workflow.

---

# Learning Outcomes

By building this project, you gain hands-on experience with:

### AI Concepts

- Prompt Engineering
- Tool Calling
- Agent Design
- Multi-Agent Systems
- Memory Systems
- RAG
- Structured Outputs

### Software Engineering Concepts

- Modular Architecture
- Service Layer Design
- Dependency Injection
- Factory Pattern
- Orchestration
- API Development
- Exception Handling

### Agentic AI Concepts

- Task Decomposition
- Planning
- Execution
- Research Workflows
- Agent Collaboration
- Workflow Orchestration

These learning outcomes align directly with the original project roadmap.

---

# Future Applications

This architecture can be extended into:

- AI Research Assistant
- Enterprise Knowledge Bot
- CRM Assistant
- Document Analysis System
- Coding Assistant
- Internal Business Copilot
- Workflow Automation Platform
- RAG-powered Enterprise Search
