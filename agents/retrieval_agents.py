from ingestion.embed_upload import embed_text, index

def retrieve(query: str, reg_body: str, top_k: int = 4):
    vec = embed_text(query)
    res = index.query(
        vector=vec, top_k=top_k, include_metadata=True,
        filter={"reg_body": {"$eq": reg_body}}
    )
    return [
        {
            "text": m["metadata"]["text"],
            "doc_name": m["metadata"]["doc_name"],
            "section": m["metadata"]["section"],
            "page": m["metadata"]["page"],
            "score": m["score"]
        }
        for m in res["matches"]
    ]