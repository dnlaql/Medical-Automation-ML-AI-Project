import pandas as pd
import plotly.express as px
import streamlit as st

def plot_data_analysis(df):
    # Ensure Age is numeric
    df.loc[:, "Age"] = pd.to_numeric(df["Age"], errors='coerce')
    
    # Drop NaN values after conversion
    df = df.dropna(subset=["Age", "Gender", "Race"])
    
    st.subheader("📊 Data Analysis & Visualization")
    
    # Gender Distribution
    gender_counts = df["Gender"].value_counts().reset_index()
    gender_counts.columns = ["Gender", "Count"]
    fig_gender = px.pie(gender_counts, names="Gender", values="Count", title="Gender Distribution", color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_gender)
    
    # Race Distribution
    race_counts = df["Race"].value_counts().reset_index()
    race_counts.columns = ["Race", "Count"]
    fig_race = px.bar(race_counts, x="Race", y="Count", title="Race Distribution", color="Race", color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_race)
    
    # Age Distribution
    fig_age = px.histogram(df, x="Age", nbins=20, title="Age Distribution", color_discrete_sequence=["#636EFA"])
    st.plotly_chart(fig_age)
    
    # Age vs Gender Breakdown
    fig_age_gender = px.box(df, x="Gender", y="Age", title="Age Distribution by Gender", color="Gender", color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig_age_gender)
    
    # Age vs Race Breakdown
    fig_age_race = px.box(df, x="Race", y="Age", title="Age Distribution by Race", color="Race", color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_age_race)
    
    st.success("✅ Data Analysis Successfully Processed!")
