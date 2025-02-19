import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Importing necessary functions from modularized scripts
from data_preprocessing import preprocess_data
from geo_location_patient import plot_patient_map
from filtering import filter_data
from data_analysis import plot_data_analysis

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Medical AI Dashboard", layout="wide")

st.title('🏥 Medical AI Dashboard')

# 📂 File Upload Widget
uploaded_file = st.file_uploader("📤 Upload your medical data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Load dataset

    # 📌 Step 1: Preprocess Data
    geo_df = preprocess_data(df)

    # 📌 Step 2: Filtering Section
    st.sidebar.header("🔍 Filter Data")
    filtered_df = filter_data(geo_df)  # Apply filters

    # 📌 Step 3: Display Processed Data (with better table formatting)
    st.subheader("📊 Data Preview (After Preprocessing & Filtering)")
    st.dataframe(filtered_df.style.set_properties(**{'background-color': '#f5f5f5', 'border-color': 'black'}))

    # 📌 Step 4: Geo-Visualization
    st.subheader("🗺️ Patient Location Map")
    plot_patient_map(filtered_df)

    # 📌 Step 5: Data Analysis & Insights
    st.subheader("📈 Automated Data Analysis")
    plot_data_analysis(filtered_df)

else:
    st.info("Please upload a CSV file containing patient data.")
