from agents.supervisor import classify_query
from agents.retrieval_agents import retrieve

q = "What are the data protection requirements for a crypto exchange handling customer KYC?"
bodies = classify_query(q)
print("Routed to:", bodies)

for b in bodies:
    results = retrieve(q, b, top_k=2)
    print(f"\n--- {b} ---")
    for r in results:
        print(r["doc_name"], r["section"], r["page"], round(r["score"],3))