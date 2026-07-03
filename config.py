import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

def get_secret(key):
    if key in os.environ:
        return os.environ[key]
    try:
        return st.secrets[key]
    except Exception:
        return None

GEMINI_API_KEY = get_secret("GEMINI_API_KEY")
PINECONE_API_KEY = get_secret("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "regradar-uae"
EMBED_MODEL = "models/gemini-embedding-001"
LLM_MODEL = "gemini-2.5-flash"
REG_BODIES = ["DFSA", "CBUAE", "VARA", "PDPL"]