def format_citations(retrieved: dict) -> str:
    """Turns retrieved chunks into a numbered source list for the prompt + display."""
    lines = []
    idx = 1
    for body, chunks in retrieved.items():
        for c in chunks:
            lines.append(f"[{idx}] {body} — {c['doc_name']}, {c['section']}, p.{c['page']}")
            idx += 1
    return "\n".join(lines)

def build_context_block(retrieved: dict) -> str:
    """Numbered context text fed to LLM, aligned with citation indices."""
    block, idx = "", 1
    for body, chunks in retrieved.items():
        for c in chunks:
            block += f"\n[{idx}] ({body} | {c['doc_name']} | {c['section']} | p.{int(c['page'])}\n{c['text']}\n"
            idx += 1
    return block