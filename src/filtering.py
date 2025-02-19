import streamlit as st
import pandas as pd

def filter_data(df):
    """
    Function to filter data based on user-selected criteria in Streamlit sidebar.
    Handles cases where columns may be missing.
    """

    def safe_multiselect(label, column_name):
        """ Helper function to check column existence before filtering """
        if column_name in df.columns:
            options = df[column_name].dropna().unique()
            return st.sidebar.multiselect(label, options, default=options)
        return None

    # Filter by available columns
    selected_gender = safe_multiselect("Select Gender", "Gender")
    selected_religion = safe_multiselect("Select Religion", "Religion")
    selected_payer = safe_multiselect("Select Payer", "Payer")
    selected_nationality = safe_multiselect("Select Nationality", "Nationality")
    selected_patient_type = safe_multiselect("Select Patient Type", "Patient Type")
    selected_race = safe_multiselect("Select Race", "Race")

    # Age Grouping (if "Age" column exists)
    if "Age" in df.columns:
        df["Age Group"] = pd.cut(df["Age"], bins=[0, 18, 35, 50, 65, 100], labels=["<18", "18-35", "36-50", "51-65", "66+"])
        selected_age = safe_multiselect("Select Age Group", "Age Group")
    else:
        selected_age = None

    # Apply filters only for columns that exist
    filters = []
    if selected_gender is not None:
        filters.append(df["Gender"].isin(selected_gender))
    if selected_religion is not None:
        filters.append(df["Religion"].isin(selected_religion))
    if selected_payer is not None:
        filters.append(df["Payer"].isin(selected_payer))
    if selected_nationality is not None:
        filters.append(df["Nationality"].isin(selected_nationality))
    if selected_patient_type is not None:
        filters.append(df["Patient Type"].isin(selected_patient_type))
    if selected_race is not None:
        filters.append(df["Race"].isin(selected_race))
    if selected_age is not None:
        filters.append(df["Age Group"].isin(selected_age))

    # Apply all filters
    if filters:
        filtered_df = df.loc[pd.concat(filters, axis=1).all(axis=1)]
    else:
        filtered_df = df  # If no filters, return original dataset

    return filtered_df
