import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Login Check
# -----------------------------

if "login" not in st.session_state:
    st.session_state["login"] = False

if not st.session_state["login"]:
    st.stop()


# -----------------------------
# Sidebar Logout
# -----------------------------

with st.sidebar:

    st.write("Logged in as:", st.session_state["user"])

    if st.button("Logout"):
        st.session_state["login"] = False
        st.rerun()


# -----------------------------
# Dashboard Title
# -----------------------------

st.title("Retail Sales Analytics Dashboard")

st.write("Upload your dataset to analyze sales insights.")


# -----------------------------
# Dataset Upload Section
# -----------------------------

st.subheader("Upload Your Sales Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(data.head())


# -----------------------------
# Sales Analysis Chart
# -----------------------------

    if "Category" in data.columns and "Sales" in data.columns:

        st.subheader("Sales by Category")

        fig = px.bar(
            data,
            x="Category",
            y="Sales",
            color="Category",
            title="Sales Distribution by Category"
        )

        st.plotly_chart(fig)

    else:
        st.warning("Dataset must contain 'Category' and 'Sales' columns.")