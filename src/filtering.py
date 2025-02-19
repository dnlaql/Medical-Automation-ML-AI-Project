import streamlit as st
import pandas as pd

def filter_data(df):
    """
    Function to filter data based on user-selected criteria in Streamlit sidebar.
    """

    # Filter by Gender
    gender_options = df["Gender"].dropna().unique()
    selected_gender = st.sidebar.multiselect("Select Gender", gender_options, default=gender_options)

    # Filter by Religion
    religion_options = df["Religion"].dropna().unique()
    selected_religion = st.sidebar.multiselect("Select Religion", religion_options, default=religion_options)

    # Filter by Payer
    payer_options = df["Payer"].dropna().unique()
    selected_payer = st.sidebar.multiselect("Select Payer", payer_options, default=payer_options)

    # Filter by Nationality
    nationality_options = df["Nationality"].dropna().unique()
    selected_nationality = st.sidebar.multiselect("Select Nationality", nationality_options, default=nationality_options)

    # Filter by Patient Type
    patient_type_options = df["Patient Type"].dropna().unique()
    selected_patient_type = st.sidebar.multiselect("Select Patient Type", patient_type_options, default=patient_type_options)

    # Filter by Race
    race_options = df["Race"].dropna().unique()
    selected_race = st.sidebar.multiselect("Select Race", race_options, default=race_options)

    # Age Grouping
    df["Age Group"] = pd.cut(df["Age"], bins=[0, 18, 35, 50, 65, 100], labels=["<18", "18-35", "36-50", "51-65", "66+"])

    age_options = df["Age Group"].dropna().unique()
    selected_age = st.sidebar.multiselect("Select Age Group", age_options, default=age_options)

    # Apply filters
    filtered_df = df[
        (df["Gender"].isin(selected_gender)) &
        (df["Religion"].isin(selected_religion)) &
        (df["Payer"].isin(selected_payer)) &
        (df["Nationality"].isin(selected_nationality)) &
        (df["Patient Type"].isin(selected_patient_type)) &
        (df["Race"].isin(selected_race)) &
        (df["Age Group"].isin(selected_age))
    ]

    return filtered_df
