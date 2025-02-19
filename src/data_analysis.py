# data_analysis.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data_analysis(df):
    """Generate data analysis visualizations."""
    col1, col2 = st.columns(2)
    
    # Gender Distribution
    with col1:
        st.subheader("Gender Distribution")
        fig, ax = plt.subplots()
        df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'pink'], ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)
    
    # Race Distribution
    with col2:
        st.subheader("Race Distribution")
        fig, ax = plt.subplots()
        df['Race'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)
