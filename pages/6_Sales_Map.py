import streamlit as st
import pandas as pd
import plotly.express as px

st.title("India Sales Heatmap")

# Load dataset
df = pd.read_csv("data/superstore.csv")

# Fake latitude longitude mapping for demo
city_coords = {
    "New York": [40.7128, -74.0060],
    "Los Angeles": [34.0522, -118.2437],
    "Chicago": [41.8781, -87.6298],
    "Houston": [29.7604, -95.3698],
    "Phoenix": [33.4484, -112.0740]
}

# Add coordinates
df["Latitude"] = df["City"].map(lambda x: city_coords.get(x,[0,0])[0])
df["Longitude"] = df["City"].map(lambda x: city_coords.get(x,[0,0])[1])

# Plot map
fig = px.scatter_geo(
    df,
    lat="Latitude",
    lon="Longitude",
    size="Sales",
    color="Sales",
    hover_name="City",
    title="Sales Map"
)

st.plotly_chart(fig, use_container_width=True)