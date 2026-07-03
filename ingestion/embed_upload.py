import json, time
import google.generativeai as genai
from pinecone import Pinecone
from config import GEMINI_API_KEY, PINECONE_API_KEY, PINECONE_INDEX_NAME, EMBED_MODEL

genai.configure(api_key=GEMINI_API_KEY)
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

def embed_text(text: str):
    result = genai.embed_content(
        model=EMBED_MODEL,
        content=text,
        task_type="retrieval_document",
        output_dimensionality=768
    )
    return result["embedding"]

def upload_chunks(chunks, batch_size=50):
    batch = []
    for i, c in enumerate(chunks):
        vec = embed_text(c["text"])
        batch.append({
            "id": f"{c['metadata']['reg_body']}-{i}",
            "values": vec,
            "metadata": {**c["metadata"], "text": c["text"]}
        })
        if len(batch) >= batch_size:
            index.upsert(vectors=batch)
            print(f"Uploaded {i+1}/{len(chunks)}")
            batch = []
            time.sleep(1)
    if batch:
        index.upsert(vectors=batch)
    print("Upload complete.")

if __name__ == "__main__":
    with open("data/all_chunks.json") as f:
        chunks = json.load(f)
    upload_chunks(chunks)