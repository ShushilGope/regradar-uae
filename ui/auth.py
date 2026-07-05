import streamlit as st
from config import get_secret

def admin_gate() -> bool:
    if st.session_state.get("is_admin"):
        return True
    pwd = st.text_input("Admin password", type="password", key="admin_pwd")
    if st.button("Login", key="admin_login"):
        if pwd == get_secret("ADMIN_PASSWORD"):
            st.session_state["is_admin"] = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    return False