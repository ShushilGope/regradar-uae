import google.generativeai as genai
from config import GEMINI_API_KEY, LLM_MODEL, REG_BODIES

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(LLM_MODEL)

def classify_query(query: str) -> list[str]:
    prompt = f"""Classify this compliance question into one or more of: {REG_BODIES}.
Return ONLY a comma-separated list, no explanation.
Question: {query}"""
    resp = model.generate_content(prompt).text.strip()
    bodies = [b.strip().upper() for b in resp.split(",") if b.strip().upper() in REG_BODIES]
    return bodies or ["DFSA"]  # fallback