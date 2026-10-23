
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="AI Anomaly Agent",
    page_icon="📊",
    layout="wide"
)

st.title("🤖 AI Anomaly Intelligence Dashboard")
st.caption("Business Performance | Machine Learning | Anomaly Monitoring")

# Load project dataset
file_path = Path("sales_data.xlsx")

if not file_path.exists():
    st.error("sales_data.xlsx not found. Keep it in the project folder.")
    st.stop()

df = pd.read_excel(file_path)
df["Date"] = pd.to_datetime(df["Date"])

# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"{df['Revenue'].sum():,.0f}")

with col2:
    st.metric("Total Orders", f"{df['Orders'].sum():,.0f}")

with col3:
    st.metric("Total Refunds", f"{df['Refunds'].sum():,.0f}")

st.divider()

# Revenue chart

# Machine Learning Anomaly Detection
from sklearn.ensemble import IsolationForest

features = df[["Revenue", "Orders", "Cost", "Refunds"]].copy()

model = IsolationForest(
    contamination=0.10,
    random_state=42
)

df["Anomaly"] = model.fit_predict(features)

# -1 means anomaly, 1 means normal
anomalies = df[df["Anomaly"] == -1].copy()

st.divider()
st.subheader("🚨 AI Anomaly Detection")

col1, col2 = st.columns(2)

with col1:
    st.metric("Anomalies Detected", len(anomalies))

with col2:
    st.metric("Records Analysed", len(df))

if anomalies.empty:
    st.success("No anomalies detected.")
else:
    st.warning("Potential unusual business activity detected.")
    st.dataframe(
        anomalies[["Date", "Revenue", "Orders", "Cost", "Refunds"]],
        use_container_width=True
    )


# Refund chart
st.subheader("💳 Refund Monitoring")

fig_refunds = px.bar(
    df,
    x="Date",
    y="Refunds",
    title="Daily Refunds",
    template="plotly_dark"
)

st.plotly_chart(fig_refunds, use_container_width=True)

# Dataset preview
with st.expander("🔍 View Sales Data"):
    st.dataframe(df, use_container_width=True)

st.success("Dashboard loaded successfully!")
