from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ingestion.section_tagger import extract_section

def load_and_chunk(pdf_path: str, reg_body: str, doc_name: str):
    reader = PdfReader(pdf_path)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = []
    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if not text.strip():
            continue
        for chunk in splitter.split_text(text):
            chunks.append({
                "text": chunk,
                "metadata": {
                    "reg_body": reg_body,
                    "doc_name": doc_name,
                    "page": page_num,
                    "section": extract_section(chunk)
                }
            })
    return chunks