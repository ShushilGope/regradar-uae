# 🇦🇪 RegRadar UAE — Agentic GCC Regulatory Intelligence Platform

An agentic Retrieval-Augmented Generation (RAG) system that answers UAE/GCC financial compliance questions by reasoning across multiple regulatory bodies (DFSA, CBUAE, VARA, PDPL) — not a single monolithic retriever, but a graph of cooperating specialist agents.

**Live demo:** [add Streamlit URL after deployment]

---

## Problem

Fintech and digital banking teams operating in the UAE must comply simultaneously with overlapping, sometimes conflicting regulatory regimes — DFSA (DIFC financial services), CBUAE (federal banking/payments), VARA (virtual assets, Dubai), and UAE PDPL (data protection). Manually cross-referencing rulebooks is slow and error-prone. Generic RAG chatbots hallucinate citations and can't detect cross-regulator conflicts.

## Architecture

┌──────────────────┐
                    │    User Query      │
                    └─────────┬──────────┘
                              ▼
                  ┌────────────────────────┐
                  │    Supervisor Agent       │  ← Gemini 2.5 Flash
                  │  (query classification)   │
                  └─────────┬──────────────┘
                              ▼
        ┌───────────┬───────────┬───────────┬───────────┐
        ▼           ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
   │  DFSA     │ │  CBUAE    │ │  VARA     │ │  PDPL     │   ← Specialist Retrieval
   │  Agent    │ │  Agent    │ │  Agent    │ │  Agent    │      Agents (Pinecone
   └─────┬───┘ └─────┬───┘ └─────┬───┘ └─────┬───┘      metadata-filtered)
         └───────────┴───────────┴───────────┘
                              ▼
                  ┌────────────────────────┐
                  │     Conflict Agent        │  ← flags contradictions
                  │   (cross-regulator)       │     when 2+ bodies retrieved
                  └─────────┬──────────────┘
                              ▼
                  ┌────────────────────────┐
                  │      Answer Agent          │  ← grounded generation,
                  │  (citation-first,          │     refuses if unsupported
                  │   hallucination guard)     │
                  └─────────┬──────────────┘
                              ▼
                  ┌────────────────────────┐
                  │      Streamlit UI            │
                  └────────────────────────┘


Orchestrated as a stateful graph using **LangGraph**, not a linear chain — enables conditional routing and multi-agent state sharing (`AgentState` TypedDict flows through supervisor → retrieval → conflict → answer nodes).

## Key Design Decisions

| Decision | Rationale |
|---|---|
| Multi-agent routing over single retriever | Regulatory bodies have distinct scope/jurisdiction; a monolithic retriever conflates DIFC-specific DFSA rules with federal CBUAE rules, degrading precision |
| Metadata-filtered Pinecone queries (not separate indexes) | Single index with `reg_body` metadata filter keeps infra simple while still enabling per-agent scoped retrieval |
| Explicit Conflict Agent | Cross-regulatory queries are the highest-value/highest-risk use case; silent merging of contradictory clauses is a compliance liability |
| Citation-first answer generation | Every claim must map to `[doc_name, section, page]`; model instructed to say "Insufficient regulatory basis found" rather than guess — mitigates hallucination in a legal-adjacent domain |
| Gemini 2.5 Flash | Low latency + cost for multi-hop agentic calls (supervisor + N retrievers + conflict + answer = 4-7 LLM calls per query) |

## Tech Stack

- **LLM:** Gemini 2.5 Flash (Google AI SDK)
- **Embeddings:** `gemini-embedding-001`, truncated to 768-dim
- **Orchestration:** LangChain + LangGraph (stateful agent graph)
- **Vector store:** Pinecone (serverless, cosine similarity)
- **Frontend:** Streamlit
- **Source documents:** DFSA Rulebook, CBUAE AML/CFT Regulations, VARA Rulebook, UAE PDPL (Federal Decree Law No. 45 of 2021)

## Features

1. **Multi-agent routing** — Supervisor classifies query into DFSA/CBUAE/VARA/PDPL (single or multi-label), routes to specialist retrievers
2. **Regulatory conflict detection** — dedicated agent cross-examines clauses from 2+ bodies, flags contradictions with explanation
3. **Citation-first answers** — every response cites exact document, article/section, page number; hallucination guard refuses ungrounded claims
4. **Compliance gap analyser** — paste a product feature description → system maps applicable clauses across all 4 bodies and flags MET/UNMET/UNCLEAR per clause + overall risk rating
5. **Change detection (v1 stub)** — `ingestion/run_all.py` + `ingestion/embed_upload.py` are designed to be re-run on a schedule (cron/Airflow in v2) when source PDFs are updated; re-ingestion is idempotent via deterministic chunk IDs

## Project Structure
regradar-uae/
├── app.py                    # Streamlit entrypoint
├── config.py                 # env/secrets loader
├── agents/
│   ├── supervisor.py         # query classifier
│   ├── retrieval_agents.py   # per-regulator retriever
│   ├── conflict_agent.py     # cross-regulatory conflict detection
│   ├── answer_agent.py       # grounded answer generation
│   └── graph.py              # LangGraph state machine
├── core/
│   ├── citation.py           # citation formatter
│   └── gap_analyzer.py       # compliance gap analysis
├── ingestion/
│   ├── chunker.py            # PDF → chunks + metadata
│   ├── section_tagger.py     # regex Article/Section extraction
│   ├── setup_index.py        # Pinecone index creation
│   ├── embed_upload.py       # embedding + upsert
│   └── run_all.py            # batch ingestion runner
└── ui/
└── styles.py              # custom CSS

## Setup

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add GEMINI_API_KEY, PINECONE_API_KEY
python -m ingestion.setup_index
python -m ingestion.embed_upload
streamlit run app.py
```

## Limitations & Roadmap

- Source PDFs currently ingested manually (v1); v2 would add scheduled scraping + diffing against previous version to trigger re-embedding only for changed sections
- Section/Article extraction uses regex heuristics — works well for numbered clauses, less reliable for prose-style rulebook sections
- Not legal advice — outputs are informational aids for compliance teams, not a substitute for legal counsel

---
*Built as a demonstration of agentic RAG architecture for GCC RegTech use cases.*