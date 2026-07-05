import streamlit as st
import os
from config import REG_BODIES
from ingestion.reingest_single import ingest_single_pdf, list_docs_by_body, delete_doc

UPLOAD_DIR = "data/raw_pdfs"

def admin_upload_ui():
    st.subheader("📤 Upload New Regulatory Document")
    reg_body = st.selectbox("Regulatory Body", REG_BODIES)
    doc_name = st.text_input("Document Name (e.g. 'DFSA AML Module v3')")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    if st.button("Ingest Document", type="primary"):
        if not uploaded_file or not doc_name.strip():
            st.warning("Provide both a document name and a PDF file.")
            return
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Chunking, embedding, and upserting to Pinecone..."):
            count = ingest_single_pdf(save_path, reg_body, doc_name)

        st.success(f"✅ Ingested '{doc_name}' — {count} chunks embedded under {reg_body}.")


def admin_manage_ui():
    st.subheader("🗂️ Manage Existing Documents")
    reg_body = st.selectbox("View documents for", REG_BODIES, key="manage_reg_body")
    docs = list_docs_by_body(reg_body)

    if not docs:
        st.info(f"No documents found for {reg_body}.")
        return

    doc_choice = st.selectbox("Select document", list(docs.keys()), key="manage_doc_choice")
    st.caption(f"{docs[doc_choice]} chunks indexed")

    if st.button("🗑️ Delete This Document", type="secondary"):
        delete_doc(doc_choice)
        st.success(f"Deleted '{doc_choice}' from index.")
        st.rerun()