import pandas as pd
import plotly.express as px
import streamlit as st

def plot_data_analysis(df):
    """
    Generate exploratory data analysis using Plotly with improved visuals.
    """

    # 📌 Ensure 'Age' column exists before processing
    if 'Age' not in df.columns:
        st.error("❌ 'Age' column is missing from the dataset!")
        return

    # 📌 Define Age Groups (Ensure bins match labels)
    bins = [0, 18, 30, 45, 60, 75, 100]  # 6 bins
    labels = ['<18', '18-29', '30-44', '45-59', '60-74', '75+']  # 6 labels

    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)  # Fix binning issue

    # 📊 Gender Distribution
    st.subheader("📊 Gender Distribution")
    gender_fig = px.pie(df, names="Gender", title="Gender Distribution", hole=0.3, color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(gender_fig, use_container_width=True)

    # 📊 Race Distribution
    st.subheader("🌍 Race Distribution")
    race_fig = px.bar(df, x=df["Race"].value_counts().index, y=df["Race"].value_counts().values,
                      labels={'x': 'Race', 'y': 'Count'},
                      title="Race Distribution", color=df["Race"].value_counts().index,
                      color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(race_fig, use_container_width=True)

    # 📊 Age Group Distribution
    st.subheader("📊 Age Group Distribution")
    age_fig = px.histogram(df, x="Age Group", title="Age Group Distribution",
                           color="Age Group", color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(age_fig, use_container_width=True)

