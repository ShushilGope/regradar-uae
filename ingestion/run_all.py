from ingestion.chunker import load_and_chunk
import json

DOCS = [
    ("data/raw_pdfs/dfsa_rulebook.pdf", "DFSA", "DFSA Rulebook"),
    ("data/raw_pdfs/cbuae_regulation.pdf", "CBUAE", "CBUAE Regulation"),
    ("data/raw_pdfs/vara_rulebook.pdf", "VARA", "VARA Rulebook"),
    ("data/raw_pdfs/pdpl_law.pdf", "PDPL", "UAE PDPL Federal Decree Law No. 45 of 2021"),
]

all_chunks = []
for path, body, name in DOCS:
    chunks = load_and_chunk(path, body, name)
    print(f"{body}: {len(chunks)} chunks")
    all_chunks.extend(chunks)

print("TOTAL:", len(all_chunks))
with open("data/all_chunks.json", "w") as f:
    json.dump(all_chunks, f, indent=2)