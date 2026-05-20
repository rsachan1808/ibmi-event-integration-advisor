# IBMi Event Integration Advisor

An AI agent that guides IBMi developers through integrating legacy 
IBMi applications with modern event-driven architectures using 
Kafka and Confluent.

---

## What it solves

Companies modernising their IBMi application stacks have few 
practical guides for one of the most effective modernisation 
approaches available — event-driven architecture. Most organisations 
are adopting event-driven patterns to decouple application components, 
but documentation for connecting IBMi systems to Kafka is sparse, 
generic, and does not reflect the realities of production IBMi 
environments.

This advisor fills that gap. It provides guidance at each step of 
moving IBMi applications toward event-driven integration — from 
architecture decisions through to implementation patterns — based 
on knowledge from a real production implementation.

No other tool combines IBMi/RPG expertise, Confluent/Kafka 
integration patterns, and AI-assisted guidance in one place.

---

## Who this is for

IBMi developers and architects who are:
- Looking to connect existing IBMi applications to a Kafka-based 
  event-driven architecture
- Familiar with IBMi pub-sub concepts, JSON parsing in RPG, and 
  the role of Kafka connectors
- Trying to make design decisions that production experience shows 
  are harder than they initially appear

---

## The question no Google search answers well

Two decisions trip up almost every IBMi + Kafka integration team 
that encounters them for the first time:

**Where should JSON parsing happen?** The instinct is to parse at 
the entry point and pass structured data downstream. The production 
lesson is the opposite — parse as close to where the data is needed 
as possible. The entry point should stay payload-agnostic. This 
advisor explains why and documents the pattern that works in 
production.

**Which message format to use?** Kafka supports multiple formats — 
JSON, Avro, Protobuf. JSON is the most accessible for IBMi teams 
but requires explicit handling for every type conversion. Avro and 
Protobuf offer schema enforcement and efficiency benefits but add 
complexity on the IBMi parsing side. This advisor documents the 
JSON approach as implemented in production and notes the tradeoffs 
against other formats.

---

## Architecture
User question
↓
LangGraph agent — reasons about which tool to call
↓
├── search_integration_patterns
│   Retrieves architecture guidance, design principles,
│   JSON parsing steps, type conversion reference
│
└── search_lessons_learned
Retrieves documented mistakes and lessons from
a real production implementation
Hybrid RAG pipeline (BM25 + semantic embeddings)
↓
Claude synthesises answer from retrieved documentation

### Why two specialised tools instead of one

A single general-purpose retrieval tool forces the agent to make 
good query decisions consistently — and LLMs are not always 
consistent. Two tools with explicit descriptions make routing 
deterministic. Architecture questions reliably hit 
`search_integration_patterns`. Mistakes and lessons questions 
reliably hit `search_lessons_learned`. This eliminates a category 
of silent failures where the agent answers from general knowledge 
instead of the documentation.

---

## Knowledge base

### Currently documented — IBMi program design (Chapter 3)
3.1 The translation boundary principle
Why JSON parsing belongs in application programs not the entry point
3.2 Entry point program structure
Standalone program design, routing table pattern, logging program
as decision point, step-by-step flow from RPC call to data queue
3.3 JSON parsing on IBMi using YAJL
Six-step parsing process, tree-node navigation, DoWhile loop pattern,
simple vs complex attribute handling, array processing
3.4 Type conversion reference
JSON type to RPG type mapping with conversion notes and gotchas
for each type including null handling
3.5 Common mistakes and lessons learned
Five documented mistakes from a production implementation:
security setup, silent failures, null handling, connector
complexity, and scaling

### Planned chapters
Chapter 1 — Integration architecture options
Infoview connector pattern, REST from RPG,
journal-based CDC, IBM MQ bridge, when to use which
Chapter 2 — Error handling
Payload-as-data pattern, schema registry for contracts,
IBMi retry for recoverable failures
Chapter 4 — Observability and latency
Per-hop instrumentation, round trip threshold alerting,
IBMi-side latency factors
Chapter 5 — Decision framework
When to use which pattern, format selection (JSON vs
Avro vs Protobuf), common tradeoffs

---

## How to run it

**Install dependencies:**
```bash
pip install langchain langchain-community langchain-anthropic
pip install langchain-voyageai chromadb rank_bm25 anthropic
pip install langgraph fastapi uvicorn python-dotenv
```

**Create a .env file:**
ANTHROPIC_API_KEY=your-anthropic-key
VOYAGE_API_KEY=your-voyageai-key

**Run the agent directly:**
```bash
python integration_advisor_agent.py
```

**Run as HTTP API:**
```bash
uvicorn api:app --reload --port 8000
```

Then open http://localhost:8000/docs for the interactive API 
documentation.

**Run as Docker container:**
```bash
docker build -t ibmi-integration-advisor .
docker run -p 8000:8000 --env-file .env ibmi-integration-advisor
```

---

## Example questions
"What is the translation boundary principle and why does it matter?"
"How does JSON parsing work on IBMi using YAJL?"
"What are the common mistakes when building an IBMi Kafka integration?"
"Why should JSON parsing happen in application programs rather
than the entry point?"
"What type conversion is needed when mapping JSON numbers to RPG
packed decimal fields?"

---

## Evaluation

The agent includes an automated evaluation framework with two 
evaluation methods per test case:

- **Keyword check** — verifies required terms are present
- **LLM judge** — evaluates correctness and completeness

Note: The LLM judge may score lower for answers containing 
specialist IBMi terminology (Infoview, YAJL, data queues) that 
is not in general training data. Keyword check is the primary 
signal for specialist content questions.

**Current evaluation results: 3/3 passing at 100%**

```bash
python evaluate_agent.py
```

---

## Legal note

This knowledge base documents transferable patterns and principles 
from production experience. No proprietary employer details, 
specific configuration values, program names, or client information 
are included. All content is written at the pattern level and is 
safe for public sharing.

---

Built with: Anthropic Claude · LangGraph · LangChain · ChromaDB ·
VoyageAI Embeddings · BM25 · FastAPI · Docker
Knowledge base: Chapter 3 complete — Chapters 1, 2, 4, 5 in progress