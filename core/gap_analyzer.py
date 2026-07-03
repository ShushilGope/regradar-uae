import google.generativeai as genai
from config import GEMINI_API_KEY, LLM_MODEL, REG_BODIES
from agents.retrieval_agents import retrieve
from core.citation import build_context_block, format_citations
from core.llm_utils import call_with_retry

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(LLM_MODEL)

def analyze_gap(feature_description: str) -> dict:
    retrieved = {}
    for body in REG_BODIES:
        retrieved[body] = retrieve(feature_description, body, top_k=3)

    context = build_context_block(retrieved)
    citations = format_citations(retrieved)

    prompt = f"""You are a compliance gap analyser for UAE fintech products.

Product feature description:
{feature_description}

Relevant regulatory clauses:
{context}

Task:
1. List which regulatory clauses APPLY to this feature (cite [n]).
2. For each applicable clause, state whether the requirement appears MET, UNMET, or UNCLEAR based on the feature description.
3. Give a short overall compliance risk summary (Low/Medium/High).

Format as markdown with headers: Applicable Clauses, Gap Assessment, Risk Summary."""

    result = call_with_retry(model.generate_content, prompt).text.strip()
    return {"analysis": result, "citations": citations}