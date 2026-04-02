import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.title("📈 Stock Market Dashboard")

# Fetch data from backend
data = requests.get("http://127.0.0.1:5000/data").json()
df = pd.DataFrame(data)

# Show data
st.subheader("Recent Stock Data")
st.write(df)

# Line Chart
fig = px.line(df, x="Date", y="Close", title="Stock Price")
st.plotly_chart(fig)

# Moving Average
fig2 = px.line(df, x="Date", y=["MA50", "MA100"], title="Moving Averages")
st.plotly_chart(fig2)
