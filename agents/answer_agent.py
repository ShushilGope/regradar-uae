import google.generativeai as genai
from config import GEMINI_API_KEY, LLM_MODEL
from core.citation import build_context_block, format_citations

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(LLM_MODEL)

def generate_answer(query: str, retrieved: dict) -> dict:
    context = build_context_block(retrieved)
    citations = format_citations(retrieved)

    prompt = f"""Answer using ONLY the numbered sources below. Cite sources inline like [1], [2].
If the sources don't contain enough info, say "Insufficient regulatory basis found" — do NOT guess.

Sources:
{context}

Question: {query}

Answer (with inline [n] citations):"""

    answer = model.generate_content(prompt).text.strip()
    return {"answer": answer, "citations": citations}