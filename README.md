# AI Research & Task Assistant

## 🎯 Project Vision

Build an **agentic AI system** that accepts user goals, autonomously breaks them into tasks, gathers information through tools, and produces comprehensive reports. The system evolves through 4 phases from simple single-agent to production-ready multi-agent workflows with RAG capabilities.

### Example Use Cases

- "Research the best laptops under ₹80k" → Comparison report
- "Plan a 5-day trip to Sikkim" → Itinerary with bookings
- "Summarize latest AI news" → Daily digest
- "Create a Python learning roadmap" → Structured curriculum

---

## 📐 Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     User Input (Goal)                       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│            PHASE 1: Single Agent                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Planner Agent                                     │    │
│  │  - Decomposes goal into tasks                      │    │
│  │  - Uses Chain-of-Thought reasoning                 │    │
│  │  - Calls tools (search, files)                     │    │
│  └────────────────────────────────────────────────────┘    │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│            PHASE 2: Multi-Agent                             │
│  ┌─────────────┬──────────────────┬──────────────────┐     │
│  │ Planner Ag. │ Researcher Ag.   │ Writer Ag.       │     │
│  └─────────────┴──────────────────┴──────────────────┘     │
│  ┌──────────────────────────────────────────────────┐      │
│  │  Reviewer Agent (Quality Validation)             │      │
│  └──────────────────────────────────────────────────┘      │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│            PHASE 3: RAG (Context Augmentation)              │
│  ┌──────────────┐         ┌──────────────────────┐          │
│  │ Vector DB    │◄────────┤ Embeddings Engine    │          │
│  │ (ChromaDB)   │         │ (sentence-transform) │          │
│  └──────────────┘         └──────────────────────┘          │
│         ▲                                                   │
│         │ Retrieved Context (Docs, PDFs, Notes)            │
│         │                                                   │
│  ┌──────┴──────────────────────────────────────────┐       │
│  │  Agents now have access to knowledge base       │       │
│  │  - Semantic search over documents               │       │
│  │  - Relevant context injected into prompts       │       │
│  └────────────────────────────────────────────────┘       │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│            PHASE 4: Production Workflows                    │
│  ┌──────────────────────────────────────────────────┐      │
│  │         FastAPI Backend + Streamlit UI           │      │
│  │  ┌─────────────┬─────────────┬─────────────┐    │      │
│  │  │Research WF  │Coding WF    │Travel WF    │    │      │
│  │  └─────────────┴─────────────┴─────────────┘    │      │
│  │  ┌─────────────────────────────────────────┐   │      │
│  │  │  Async Workflows + State Management     │   │      │
│  │  │  with LangGraph                         │   │      │
│  │  └─────────────────────────────────────────┘   │      │
│  └──────────────────────────────────────────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

---
