import streamlit as st
from agents.graph import app_graph
from core.gap_analyzer import analyze_gap
from ui.styles import CUSTOM_CSS, HERO_IMAGE_CSS, FLIP_CARDS_CSS, SECTION_BG_CSS
from ui.auth import admin_gate
from ui.admin_upload import admin_upload_ui, admin_manage_ui

st.set_page_config(page_title="RegRadar UAE", layout="wide", page_icon="🇦🇪")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
st.markdown(HERO_IMAGE_CSS, unsafe_allow_html=True)
st.markdown(FLIP_CARDS_CSS, unsafe_allow_html=True)
st.markdown(SECTION_BG_CSS, unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown('<div class="flag-stripe"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero-bg">
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

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["🔍 Ask a Question", "📋 Compliance Gap Analyser", "🔐 Admin: Upload Docs"])

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
    feature_desc = st.text_area(
        "Paste product feature description:", height=150,
        placeholder="e.g. A mobile app feature allowing UAE residents to buy crypto using facial recognition for KYC, storing biometric data on-device..."
    )
    if st.button("Analyse Gaps", type="primary"):
        if not feature_desc.strip():
            st.warning("Paste a feature description first.")
        else:
            with st.spinner("Analysing applicable clauses and gaps..."):
                result = analyze_gap(feature_desc)

            st.markdown(result["analysis"])
            st.subheader("📚 Sources")
            st.text(result["citations"])

with tab3:
    if admin_gate():
        admin_upload_ui()
        st.divider()
        admin_manage_ui()
    else:
        st.info("Admin login required to upload documents.")

# ---------- SAMPLE OUTPUT ----------
st.markdown("""
<div class="example-card" style="max-width:900px; margin:30px auto;">
    <span class="tag">Sample Output</span>
    <div class="q">Q: Does VARA require KYC for crypto exchange onboarding?</div>
    <div class="a">Yes. VASPs must screen clients and UBOs for illicit activity risk, verify identity via the Federal Authority for Identity & Citizenship gateway, and classify ML/FT risk before onboarding [1][2].</div>
    <div class="cite">📄 VARA Rulebook, p.25 · CBUAE Regulation, p.50</div>
</div>
""", unsafe_allow_html=True)

# ---------- FLIP CARDS ----------
st.markdown("""
<div class="section-features">
<div class="flip-grid">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80">
        <h4>📍 Multi-Agent Routing</h4>
      </div>
      <div class="flip-card-back">
        <strong>How it works</strong>
        A Supervisor Agent classifies each query into DFSA, CBUAE, VARA, and/or PDPL — then routes to dedicated Retrieval Agents per regulator, avoiding one-size-fits-all search.
      </div>
    </div>
  </div>
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80">
        <h4>⚖️ Conflict Detection</h4>
      </div>
      <div class="flip-card-back">
        <strong>Cross-regulatory analysis</strong>
        When a query spans multiple regulators, a dedicated Conflict Agent cross-examines retrieved clauses and explicitly flags contradictions — critical for GCC multi-jurisdiction compliance.
      </div>
    </div>
  </div>
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="flip-card-front">
        <img src="https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80">
        <h4>📄 Citation-First</h4>
      </div>
      <div class="flip-card-back">
        <strong>Hallucination guard</strong>
        Every answer is grounded with exact document name, article/section, and page number. If no clause supports a claim, the system says so instead of guessing.
      </div>
    </div>
  </div>
</div>
</div>
""", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
  <h3>About RegRadar UAE</h3>
  <p>RegRadar UAE is an agentic AI platform that turns hours of manual regulatory research into seconds — built for fintech PMs, compliance officers, and digital banking teams navigating the UAE's fragmented financial regulatory landscape across DFSA, CBUAE, VARA, and UAE PDPL.</p>
  <p style="margin-top:20px; font-weight:600; color:#00754A;">Why it matters: UAE fintech compliance today means manually cross-referencing four regulatory bodies with no unified source of truth. RegRadar closes that gap — faster diligence, fewer blind spots, and a defensible audit trail for every answer.</p>
  <p style="font-size:0.8rem; color:#999; margin-top:16px;">⚠️ For informational purposes only — not legal advice. Verify with official regulator sources.</p>
</div>
""", unsafe_allow_html=True)