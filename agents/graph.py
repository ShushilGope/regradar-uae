from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.supervisor import classify_query
from agents.retrieval_agents import retrieve
from agents.conflict_agent import detect_conflict
from agents.answer_agent import generate_answer


class AgentState(TypedDict):
    query: str
    reg_bodies: list
    retrieved: dict
    conflict_report: str
    answer: str
    citations: str


def supervisor_node(state: AgentState):
    bodies = classify_query(state["query"])
    return {"reg_bodies": bodies}


def retrieval_node(state: AgentState):
    retrieved = {}
    for body in state["reg_bodies"]:
        retrieved[body] = retrieve(state["query"], body, top_k=3)
    return {"retrieved": retrieved}


def conflict_node(state: AgentState):
    report = detect_conflict(state["query"], state["retrieved"])
    return {"conflict_report": report}


def answer_node(state: AgentState):
    result = generate_answer(state["query"], state["retrieved"])
    return {"answer": result["answer"], "citations": result["citations"]}


graph = StateGraph(AgentState)
graph.add_node("supervisor", supervisor_node)
graph.add_node("retrieval", retrieval_node)
graph.add_node("conflict", conflict_node)
graph.add_node("answer_node", answer_node)

graph.set_entry_point("supervisor")
graph.add_edge("supervisor", "retrieval")
graph.add_edge("retrieval", "conflict")
graph.add_edge("conflict", "answer_node")
graph.add_edge("answer_node", END)

app_graph = graph.compile()