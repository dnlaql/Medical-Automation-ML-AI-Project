import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import the preprocessing function
from data_preprocessing import preprocess_data  # No need to use 'src.' here

import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.title('Medical AI Dashboard')

# Add File Upload Widget for user-uploaded dataset
uploaded_file = st.file_uploader("Upload your medical data CSV", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read the uploaded CSV into a DataFrame
    
    # Perform data preprocessing by calling the function from the separate file
    df = preprocess_data(df)

    # Show a preview of the cleaned data
    st.write("Data preview (after preprocessing):")
    st.dataframe(df.head())  # Display the first few rows of the processed dataset

    # Create Folium Map to visualize the geo data
    st.header('Patient Location Map')

    # Filter rows with non-null Latitude and Longitude
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        df = df.dropna(subset=['Latitude', 'Longitude'])

        # Create a base Folium map centered around the mean latitude and longitude
        map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
        patient_map = folium.Map(location=map_center, zoom_start=12)

        # Add markers for each patient
        for _, row in df.iterrows():
            folium.Marker([row['Latitude'], row['Longitude']],
                          popup=row['NRIC/Passport No']).add_to(patient_map)

        # Display the Folium map in the Streamlit app
        folium_static(patient_map)

else:
    st.write("Please upload a CSV file containing patient data.")
