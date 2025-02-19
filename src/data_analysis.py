import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_data_analysis(df):
    """
    Function to generate comprehensive exploratory data analysis visualizations
    using Plotly for a more interactive and visually appealing dashboard.
    """
    
    # Define Age Groups
    bins = [0, 18, 30, 45, 60, 75, 100]
    labels = ['<18', '18-29', '30-44', '45-59', '60-74', '75+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    
    st.subheader("📊 Demographic Distribution")
    
    # 📌 Gender Distribution (Pie Chart)
    fig_gender = px.pie(df, names='Gender', title='Gender Distribution', 
                         color_discrete_sequence=['#636EFA', '#EF553B'])
    st.plotly_chart(fig_gender, use_container_width=True)
    
    # 📌 Race Distribution (Bar Chart)
    fig_race = px.bar(df, x=df['Race'].value_counts().index, y=df['Race'].value_counts().values, 
                       labels={'x': 'Race', 'y': 'Count'}, title='Race Distribution', 
                       color=df['Race'].value_counts().index, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig_race, use_container_width=True)
    
    # 📌 Age Group Distribution (Histogram)
    fig_age = px.histogram(df, x='Age', nbins=20, title='Age Distribution', 
                            color_discrete_sequence=['#00CC96'])
    st.plotly_chart(fig_age, use_container_width=True)
    
    # 📌 Age Group Breakdown (Bar Chart)
    fig_age_group = px.bar(df, x=df['Age Group'].value_counts().index, y=df['Age Group'].value_counts().values, 
                            labels={'x': 'Age Group', 'y': 'Count'}, title='Age Group Breakdown',
                            color=df['Age Group'].value_counts().index, color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_age_group, use_container_width=True)
    
    # 📌 Gender vs Age (Box Plot)
    fig_gender_age = px.box(df, x='Gender', y='Age', title='Age Distribution by Gender', 
                             color='Gender', color_discrete_sequence=['#636EFA', '#EF553B'])
    st.plotly_chart(fig_gender_age, use_container_width=True)
    
    # 📌 Nationality Distribution (Bar Chart)
    fig_nationality = px.bar(df, x=df['Nationality'].value_counts().index, y=df['Nationality'].value_counts().values, 
                              labels={'x': 'Nationality', 'y': 'Count'}, title='Nationality Breakdown', 
                              color=df['Nationality'].value_counts().index, color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_nationality, use_container_width=True)
    
    st.success("✅ Data Analysis Completed Successfully!")
