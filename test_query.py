from ingestion.embed_upload import embed_text, index

q = embed_text("What are KYC requirements?")
res = index.query(vector=q, top_k=3, include_metadata=True)
for m in res["matches"]:
    print(m["score"], m["metadata"]["reg_body"], m["metadata"]["section"], m["metadata"]["page"])