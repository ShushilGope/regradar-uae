from ingestion.chunker import load_and_chunk

chunks = load_and_chunk("data/raw_pdfs/pdpl_law.pdf", "PDPL", "UAE PDPL Federal Decree Law No. 45 of 2021")
print("Total chunks:", len(chunks))
print(chunks[0])