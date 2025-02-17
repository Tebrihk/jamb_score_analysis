from re import template
from turtle import left
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

# Set up the Streamlit page
st.set_page_config(
    page_title="JAMB Analysis",
    page_icon=":bar_chart:",
    layout="wide",
)

# Sidebar
st.sidebar.title("SIDEBAR CONTROL  :control_knobs:")

x_axis_options = ["Study_Hours_Per_Week", "Attendance_Rate", "Distance_To_School", "Teacher_Quality"]
selected_x = st.sidebar.selectbox("scattered plot X-axis options:", x_axis_options)

#flitering the data to get a much more exciting detail
filter_category = st.sidebar.selectbox("Filter by Category:", ["None", "Gender", "School_Type"])

@st.cache_data  #for better performance and a good practise
def load_data():
    df = pd.read_csv("jamb_exam_results.csv")
    return df

df = load_data()

if filter_category != "None":
    unique_values = df[filter_category].unique()
    selected_filter = st.sidebar.multiselect(f"Select {filter_category}:", unique_values, default=unique_values)
    df = df[df[filter_category].isin(selected_filter)]
    
fig = px.scatter(df, x=selected_x, y="JAMB_Score", color=filter_category if filter_category != "None" else "Gender",
                 title=f"JAMB Score vs {selected_x}",
                 hover_data=df.columns)

# Scatter Plot to display on maian page
st.title(":bar_chart: JAMB DASHBOARD")
st.subheader(f"Scatter Plot of JAMB Score vs {selected_x}")
st.plotly_chart(fig)


#  main page for quick reference
st.subheader("Raw Data Preview")
st.write(df.head())  # This now appears in the main content area
