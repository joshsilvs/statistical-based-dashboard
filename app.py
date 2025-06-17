import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("variable_raw.csv", parse_dates=["Date"])

# Sidebar filters
st.sidebar.title("Filters")
days = st.sidebar.multiselect("Day of Week", options=df["Day"].unique(), default=df["Day"].unique())
ny1_status = st.sidebar.multiselect("NY1 Model Status", options=df["NY1ModelStatus"].unique(), default=df["NY1ModelStatus"].unique())
london_status = st.sidebar.multiselect("London Model Status", options=df["LondonModelStatus"].unique(), default=df["LondonModelStatus"].unique())

# Filtered data
filtered_df = df[
    df["Day"].isin(days) &
    df["NY1ModelStatus"].isin(ny1_status) &
    df["LondonModelStatus"].isin(london_status)
]

st.title("📊 Statistical Based Dashboard")

# Percentile summary
st.header("Percentile Tables")

def display_percentiles(series, name):
    st.subheader(f"{name} Percentiles")
    p70, p80, p90 = series.quantile([0.7, 0.8, 0.9])
    p30, p20, p10 = series.quantile([0.3, 0.2, 0.1])
    st.write(f"70th: {p70:.2f}, 80th: {p80:.2f}, 90th: {p90:.2f}")
    st.write(f"30th: {p30:.2f}, 20th: {p20:.2f}, 10th: {p10:.2f}")

if "HighOfDay%" in filtered_df.columns:
    display_percentiles(filtered_df["HighOfDay%"], "High of Day")
if "LowOfDay%" in filtered_df.columns:
    display_percentiles(filtered_df["LowOfDay%"], "Low of Day")

# Scatter plots
st.header("HOD & LOD Distributions")

fig, ax = plt.subplots()
ax.scatter(filtered_df["Date"], filtered_df["HighOfDay%"], label="High of Day", color="green", alpha=0.6)
ax.set_ylabel("HighOfDay%")
ax.set_title("High of Day % Over Time")
ax.grid(True)
st.pyplot(fig)

fig, ax = plt.subplots()
ax.scatter(filtered_df["Date"], filtered_df["LowOfDay%"], label="Low of Day", color="red", alpha=0.6)
ax.set_ylabel("LowOfDay%")
ax.set_title("Low of Day % Over Time")
ax.grid(True)
st.pyplot(fig)

# Show table
st.header("Filtered Data Sample")
st.dataframe(filtered_df.head(20))
