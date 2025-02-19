import streamlit as st
import pandas as pd

def filter_data(df):
    """
    Function to filter data based on user-selected criteria in Streamlit sidebar.
    Now only filters by Gender and Race.
    """

    def safe_multiselect(label, column_name):
        """ Helper function to check column existence before filtering """
        if column_name in df.columns:
            options = df[column_name].dropna().unique()
            return st.sidebar.multiselect(label, options, default=options)
        return None

    # Filter by Gender & Race only
    selected_gender = safe_multiselect("Select Gender", "Gender")
    selected_race = safe_multiselect("Select Race", "Race")

    # Apply filters
    filters = []
    if selected_gender is not None:
        filters.append(df["Gender"].isin(selected_gender))
    if selected_race is not None:
        filters.append(df["Race"].isin(selected_race))

    # Apply all filters
    if filters:
        filtered_df = df.loc[pd.concat(filters, axis=1).all(axis=1)]
    else:
        filtered_df = df  # If no filters selected, return the full dataset

    return filtered_df
