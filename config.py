import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "regradar-uae"
EMBED_MODEL = "models/gemini-embedding-001"
LLM_MODEL = "gemini-2.5-flash"
REG_BODIES = ["DFSA", "CBUAE", "VARA", "PDPL"]