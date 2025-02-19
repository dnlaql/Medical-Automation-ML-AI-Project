# filtering.py

import streamlit as st

def filter_data(df):
    """
    Function to filter data based on Gender and Race only.
    """
    # Filter by Gender
    gender_options = df["Gender"].dropna().unique()
    selected_gender = st.sidebar.multiselect("Select Gender", gender_options, default=gender_options)

    # Filter by Race
    race_options = df["Race"].dropna().unique()
    selected_race = st.sidebar.multiselect("Select Race", race_options, default=race_options)
    
    # Apply filters
    filtered_df = df[
        (df["Gender"].isin(selected_gender)) &
        (df["Race"].isin(selected_race))
    ]
    
    return filtered_df
