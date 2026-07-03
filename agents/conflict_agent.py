import google.generativeai as genai
from config import GEMINI_API_KEY, LLM_MODEL
from core.llm_utils import call_with_retry

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(LLM_MODEL)

def detect_conflict(query: str, retrieved_by_body: dict) -> str:
    if len(retrieved_by_body) < 2:
        return "N/A — single regulatory body, no conflict check needed."

    context = ""
    for body, chunks in retrieved_by_body.items():
        context += f"\n--- {body} ---\n"
        for c in chunks:
            context += f"[{c['doc_name']} | {c['section']} | p.{c['page']}]: {c['text'][:300]}\n"

    prompt = f"""You are a regulatory conflict detector. Question: {query}

Clauses from different regulators:
{context}

Do these clauses CONTRADICT or CONFLICT with each other on this question?
Reply in this format:
CONFLICT: Yes/No
EXPLANATION: <1-2 sentences if Yes, else "No conflicts found">"""
    return call_with_retry(model.generate_content, prompt).text.strip()