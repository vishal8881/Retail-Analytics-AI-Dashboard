import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Session setup
# -----------------------------
if "login" not in st.session_state:
    st.session_state["login"] = False

if "user" not in st.session_state:
    st.session_state["user"] = ""

# -----------------------------
# Login Page
# -----------------------------
if not st.session_state["login"]:

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state["login"] = True
            st.session_state["user"] = username
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.write("Logged in as:", st.session_state["user"])

    if st.button("Logout"):
        st.session_state["login"] = False
        st.rerun()

# -----------------------------
# Dashboard
# -----------------------------
st.title("Retail Sales Analytics Dashboard")

st.write("Upload your dataset to analyze sales insights.")

# -----------------------------
# Upload Dataset
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload CSV dataset",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    if "Category" in data.columns and "Sales" in data.columns:

        st.subheader("Sales by Category")

        fig = px.bar(
            data,
            x="Category",
            y="Sales",
            color="Category"
        )

        st.plotly_chart(fig)

    else:
        st.warning("Dataset must contain 'Category' and 'Sales' columns.")