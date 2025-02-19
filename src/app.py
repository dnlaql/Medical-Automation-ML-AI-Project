import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import preprocessing and geolocation functions
from data_preprocessing import preprocess_data
from geo_location_patient import create_geo_dataframe, create_map

import streamlit as st
import pandas as pd

st.title('Medical AI Dashboard')

# Add File Upload Widget for user-uploaded dataset
uploaded_file = st.file_uploader("Upload your medical data CSV", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read the uploaded CSV into a DataFrame
    
    # Perform data cleaning
    cleaned_df = preprocess_data(df)

    # Convert to GeoDataFrame
    geo_df = create_geo_dataframe(cleaned_df)

    # Show a preview of the cleaned data
    st.write("Data preview (after preprocessing):")
    st.dataframe(geo_df.head())  # Display the first few rows of the processed dataset

    # Visualization - Geo Map
    st.header('Patient Location Map')
    
    # Use pydeck to create the map
    patient_map = create_map(geo_df)
    if patient_map:
        st.pydeck_chart(patient_map)
    else:
        st.write("No valid geolocation data available.")

else:
    st.write("Please upload a CSV file containing patient data.")
