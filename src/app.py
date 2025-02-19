import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Importing necessary functions from modularized scripts
from data_preprocessing import preprocess_data
from geo_location_patient import create_geo_dataframe, create_map
from filtering import filter_data
from data_analysis import plot_data_analysis

import streamlit as st
import pandas as pd

# 🏥 Streamlit Page Config
st.set_page_config(page_title="Medical AI Dashboard", layout="wide")

# 🌟 Title
st.title('🏥 Medical AI Dashboard')

# 📂 File Upload Widget
uploaded_file = st.file_uploader("📤 Upload your medical data CSV", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)  # Load dataset
        
        if df.empty:
            st.warning("⚠️ Uploaded file is empty. Please upload a valid dataset.")
        else:
            # 📌 Step 1: Preprocess Data
            geo_df = preprocess_data(df)

            # 📌 Step 2: Sidebar Filtering Section
            st.sidebar.header("🔍 Filter Data")
            st.sidebar.write("Use the filters below to refine the dataset for analysis.")
            filtered_df = filter_data(geo_df)  # Apply filters

            # 📌 Step 3: Display Processed Data (with better table formatting)
            st.subheader("📊 Data Preview (After Preprocessing & Filtering)")
            st.dataframe(filtered_df)

            # 📌 Step 4: Geo-Visualization
            st.subheader("🗺️ Patient Location Map")
            map_visual = create_map(filtered_df)  # FIXED: Correct function name
            if map_visual:
                st.pydeck_chart(map_visual)
            else:
                st.warning("⚠️ No valid location data to display on the map.")

            # 📌 Step 5: Data Analysis & Insights
            st.subheader("📈 Automated Data Analysis")
            plot_data_analysis(filtered_df)

    except Exception as e:
        st.error(f"❌ An error occurred: {e}")

else:
    st.info("ℹ️ Please upload a CSV file containing patient data.")
