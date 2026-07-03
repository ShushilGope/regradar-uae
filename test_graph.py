from agents.graph import app_graph

result = app_graph.invoke({"query": "Does DFSA and PDPL differ on data breach notification timelines?"})
print("Bodies:", result["reg_bodies"])
print("\nConflict Report:\n", result["conflict_report"])
print("\nAnswer:\n", result["answer"])
print("\nCitations:\n", result["citations"])