import streamlit as st
import pandas as pd
import plotly.express as px


def plot_data_analysis(df):
    """
    Function to generate interactive exploratory data analysis (EDA)
    visualizations using Plotly.
    """
    st.subheader("📊 Patient Data Analysis")

    # Ensure Age column is numeric
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    
    # Define Age Groups
    bins = [0, 18, 30, 45, 60, 75, 100]
    labels = ['<18', '18-29', '30-44', '45-59', '60-74', '75+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    
    # Creating columns layout
    col1, col2 = st.columns(2)

    # 📌 Gender Distribution (Pie Chart)
    with col1:
        st.subheader("👥 Gender Distribution")
        gender_fig = px.pie(df, names='Gender', title='Gender Distribution', color_discrete_sequence=px.colors.qualitative.Set3)
        st.plotly_chart(gender_fig, use_container_width=True)

    # 📌 Race Distribution (Pie Chart)
    with col2:
        st.subheader("🎭 Race Distribution")
        race_fig = px.pie(df, names='Race', title='Race Distribution', color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(race_fig, use_container_width=True)
    
    # 📌 Nationality Distribution (Bar Chart)
    st.subheader("🌍 Nationality Distribution")
    nationality_fig = px.bar(df, x=df['Nationality'].value_counts().index, y=df['Nationality'].value_counts().values,
                             labels={'x': 'Nationality', 'y': 'Count'},
                             color=df['Nationality'].value_counts().index,
                             title='Nationality Distribution')
    st.plotly_chart(nationality_fig, use_container_width=True)
    
    # 📌 Patient Type Distribution (Bar Chart)
    st.subheader("🏥 Patient Type Distribution")
    patient_type_fig = px.bar(df, x=df['Patient Type'].value_counts().index, y=df['Patient Type'].value_counts().values,
                              labels={'x': 'Patient Type', 'y': 'Count'},
                              color=df['Patient Type'].value_counts().index,
                              title='Patient Type Distribution')
    st.plotly_chart(patient_type_fig, use_container_width=True)
    
    # 📌 Age Group Distribution (Histogram)
    st.subheader("📅 Age Group Distribution")
    age_hist_fig = px.histogram(df, x='Age', nbins=10, title='Age Distribution', color_discrete_sequence=['green'])
    st.plotly_chart(age_hist_fig, use_container_width=True)

    # 📌 Geolocation Map (if Latitude & Longitude exist)
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        st.subheader("🗺️ Patient Geolocation Map")
        map_fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', hover_name='Patient Name',
                                    color_discrete_sequence=['red'], zoom=6, height=500)
        map_fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(map_fig, use_container_width=True)
