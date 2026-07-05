from ingestion.chunker import load_and_chunk
from ingestion.embed_upload import embed_text, index
from ingestion.embed_upload import index

def list_docs_by_body(reg_body: str):
    """Returns unique doc_names for a reg_body by sampling metadata."""
    dummy_vec = [0.0] * 768
    res = index.query(
        vector=dummy_vec, top_k=1000, include_metadata=True,
        filter={"reg_body": {"$eq": reg_body}}
    )
    docs = {}
    for m in res["matches"]:
        name = m["metadata"]["doc_name"]
        docs[name] = docs.get(name, 0) + 1
    return docs  # {doc_name: chunk_count}

def delete_doc(doc_name: str):
    index.delete(filter={"doc_name": {"$eq": doc_name}})

def delete_existing_doc(doc_name: str):
    index.delete(filter={"doc_name": {"$eq": doc_name}})

def ingest_single_pdf(pdf_path: str, reg_body: str, doc_name: str) -> int:
    delete_existing_doc(doc_name)
    chunks = load_and_chunk(pdf_path, reg_body, doc_name)
    batch = []
    for i, c in enumerate(chunks):
        vec = embed_text(c["text"])
        batch.append({
            "id": f"{reg_body}-{doc_name}-{i}",
            "values": vec,
            "metadata": {**c["metadata"], "text": c["text"]}
        })
        if len(batch) >= 50:
            index.upsert(vectors=batch)
            batch = []
    if batch:
        index.upsert(vectors=batch)
    return len(chunks)