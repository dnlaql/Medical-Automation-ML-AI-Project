import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import preprocessing, geolocation, and filtering functions
from data_preprocessing import preprocess_data
from geo_location_patient import create_geo_dataframe, create_map
from filters import filter_data, categorize_age

import streamlit as st
import pandas as pd

st.title('Medical AI Dashboard')

# File Upload
uploaded_file = st.file_uploader("Upload your medical data CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Data Preprocessing
    df = preprocess_data(df)

    # Categorize Age into Age Groups
    df = categorize_age(df)

    # Convert to GeoDataFrame
    geo_df = create_geo_dataframe(df)

    # Show preview of cleaned data
    #st.write("Data preview (after preprocessing):")
    #st.dataframe(geo_df.head())

    # Sidebar Filters
    st.sidebar.header("Filter Options")

    gender_filter = st.sidebar.selectbox("Gender", options=["All"] + list(df["Gender"].unique()), index=0)
    religion_filter = st.sidebar.selectbox("Religion", options=["All"] + list(df["Religion"].unique()), index=0)
    payor_filter = st.sidebar.selectbox("Payor", options=["All"] + list(df["Payor"].unique()), index=0)
    nationality_filter = st.sidebar.selectbox("Nationality", options=["All"] + list(df["Nationality"].unique()), index=0)
    patient_type_filter = st.sidebar.selectbox("Patient Type", options=["All"] + list(df["Patient Type"].unique()), index=0)
    race_filter = st.sidebar.selectbox("Race", options=["All"] + list(df["Race"].unique()), index=0)
    age_group_filter = st.sidebar.selectbox("Age Group", options=["All"] + list(df["Age Group"].unique()), index=0)

    # Apply Filters
    filtered_df = filter_data(
        df,
        gender=None if gender_filter == "All" else gender_filter,
        religion=None if religion_filter == "All" else religion_filter,
        payor=None if payor_filter == "All" else payor_filter,
        nationality=None if nationality_filter == "All" else nationality_filter,
        patient_type=None if patient_type_filter == "All" else patient_type_filter,
        race=None if race_filter == "All" else race_filter,
        age_group=None if age_group_filter == "All" else age_group_filter
    )

    # Display Filtered Data
    st.write("Filtered Data:")
    st.dataframe(filtered_df)

    # Visualization - Geo Map
    st.header('Patient Location Map')
    filtered_geo_df = create_geo_dataframe(filtered_df)
    patient_map = create_map(filtered_geo_df)

    if patient_map:
        st.pydeck_chart(patient_map)
    else:
        st.write("No valid geolocation data available.")

else:
    st.write("Please upload a CSV file containing patient data.")

from data_analysis import plot_data_analysis

# After filtering
plot_data_analysis(filtered_df)  # Display Data Analysis

