import sys
import os

# Add the 'src' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Import the preprocessing function
from data_preprocessing import preprocess_data  # No need to use 'src.' here

import streamlit as st
import pandas as pd
import pydeck as pdk

st.title('Medical AI Dashboard')

# Add File Upload Widget for user-uploaded dataset
uploaded_file = st.file_uploader("Upload your medical data CSV", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # Read the uploaded CSV into a DataFrame
    
    # Perform data preprocessing by calling the function from the separate file
    geo_df = preprocess_data(df)  # Get GeoDataFrame with lat-long

    # Show a preview of the cleaned data
    st.write("Data preview (after preprocessing):")
    st.dataframe(geo_df.head())  # Display the first few rows of the processed dataset

    # Visualization - Geo Map
    st.header('Patient Location Map')
    
    # Use pydeck to create the map
    if 'geometry' in geo_df.columns:
        view_state = pdk.ViewState(
            latitude=geo_df['Latitude'].mean(),
            longitude=geo_df['Longitude'].mean(),
            zoom=11,
            pitch=50
        )
        
        # Define the layer to show the points on the map
        layer = pdk.Layer(
            'ScatterplotLayer',
            geo_df,
            get_position='[Longitude, Latitude]',
            get_radius=1000,
            get_color=[255, 0, 0],
            pickable=True
        )
        
        # Create the deck map
        deck = pdk.Deck(layers=[layer], initial_view_state=view_state)
        st.pydeck_chart(deck)  # Display the map

else:
    st.write("Please upload a CSV file containing patient data.")
