import streamlit as st
from agents.graph import app_graph
from ui.styles import CUSTOM_CSS

st.set_page_config(page_title="RegRadar UAE", layout="wide", page_icon="🇦🇪")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

st.markdown('<div class="flag-stripe"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
  <h1>🇦🇪 RegRadar UAE</h1>
  <p>Ask compliance questions across UAE's financial regulators — get cited, conflict-checked answers instantly.</p>
  <div class="badge-row">
    <span class="badge">DFSA</span>
    <span class="badge">CBUAE</span>
    <span class="badge">VARA</span>
    <span class="badge">UAE PDPL</span>
  </div>
</div>
""", unsafe_allow_html=True)
st.divider()



tab1, tab2 = st.tabs(["🔍 Ask a Question", "📋 Compliance Gap Analyser"])

with tab1:
    query = st.text_area("Enter your compliance question:", height=100)
    if st.button("Get Answer", type="primary"):
        if not query.strip():
            st.warning("Enter a question first.")
        else:
            with st.spinner("Routing → Retrieving → Checking conflicts → Answering..."):
                result = app_graph.invoke({"query": query})

            st.subheader("📍 Routed to")
            st.write(", ".join(result["reg_bodies"]))

            if len(result["reg_bodies"]) > 1:
                st.subheader("⚠️ Conflict Check")
                st.info(result["conflict_report"])

            st.subheader("✅ Answer")
            st.markdown(result["answer"])

            st.subheader("📚 Sources")
            st.text(result["citations"])

with tab2:
    feature_desc = st.text_area("Paste product feature description:", height=150,
                                  placeholder="e.g. A mobile app feature allowing UAE residents to buy crypto using facial recognition for KYC, storing biometric data on-device...")
    if st.button("Analyse Gaps", type="primary"):
        if not feature_desc.strip():
            st.warning("Paste a feature description first.")
        else:
            with st.spinner("Analysing applicable clauses and gaps..."):
                from core.gap_analyzer import analyze_gap
                result = analyze_gap(feature_desc)

            st.markdown(result["analysis"])
            st.subheader("📚 Sources")
            st.text(result["citations"])