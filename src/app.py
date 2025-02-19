import sys
import os
import streamlit as st
import pandas as pd

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import functions from modularized scripts
from data_preprocessing import preprocess_data
from geo_location_patient import create_geo_dataframe, create_map
from filtering import filter_data
from data_analysis import plot_data_analysis

# 🏥 Streamlit Page Config
st.set_page_config(page_title="🏥 Medical AI Dashboard", layout="wide")

# 🌟 Title & Introduction
st.title("🏥 Medical AI Dashboard")
st.markdown("""
### 📌 Overview:
This dashboard allows you to **analyze medical data**, apply **filters**, visualize **patient locations**, and gain **automated insights** for better decision-making.
Upload a **CSV file** containing patient data to get started! 🩺📊
""")

# 📂 File Upload Widget
st.sidebar.header("📂 Upload Data")
st.sidebar.markdown("Upload a CSV file containing **patient records** for processing.")
uploaded_file = st.sidebar.file_uploader("📤 Upload your medical data CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)  # Load dataset
        
        if df.empty:
            st.warning("⚠️ Uploaded file is empty. Please upload a valid dataset.")
        else:
            # 📌 Step 1: Preprocess Data
            st.subheader("🛠️ Step 1: Data Preprocessing")
            st.markdown("Cleaning and transforming raw data to ensure consistency and usability.")
            cleaned_df = preprocess_data(df)
            
            # 📌 Step 2: Sidebar Filtering Section
            st.sidebar.header("🔍 Filter Data")
            st.sidebar.markdown("Use filters to refine the dataset based on patient attributes like **gender** and **race**.")
            filtered_df = filter_data(cleaned_df)  # Apply gender & race filters
            
            # 📌 Step 3: Display Processed Data
            st.subheader("📊 Step 3: Data Preview")
            st.markdown("Showing **filtered and preprocessed** data for review.")
            st.dataframe(filtered_df)
            
            # 📌 Step 4: Geo-Visualization
            st.subheader("🗺️ Step 4: Patient Location Map")
            st.markdown("Visual representation of **patient distribution** based on geographical data.")
            geo_df = create_geo_dataframe(filtered_df)
            map_visual = create_map(geo_df)
            if map_visual:
                st.pydeck_chart(map_visual)
            else:
                st.warning("⚠️ No valid location data to display on the map.")
            
            # 📌 Step 5: Data Analysis & Insights
            st.subheader("📈 Step 5: Automated Data Analysis")
            st.markdown("Exploring trends, patterns, and key insights from the medical data.")
            plot_data_analysis(filtered_df)
            
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
else:
    st.info("ℹ️ Please upload a CSV file containing patient data to begin analysis.")
