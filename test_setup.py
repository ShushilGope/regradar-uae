from config import GEMINI_API_KEY, PINECONE_API_KEY
print("Gemini key loaded:", bool(GEMINI_API_KEY))
print("Pinecone key loaded:", bool(PINECONE_API_KEY))

import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")
print(model.generate_content("Say OK").text)