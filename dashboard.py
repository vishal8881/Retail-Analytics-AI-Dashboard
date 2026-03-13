import streamlit as st
from login import login

st.set_page_config(page_title="Retail Sales Analytics", layout="wide")

# Session check
if "login" not in st.session_state:
    st.session_state["login"] = False

# Login page
if not st.session_state["login"]:
    login()
    st.stop()

# Sidebar logout
with st.sidebar:

    st.write("Logged in as:", st.session_state["user"])

    if st.button("Logout"):
        st.session_state["login"] = False
        st.rerun()

# Dashboard main page
st.title("Retail Sales Analytics Dashboard")

st.write("Use sidebar to explore analytics.")