import streamlit as st

def filter_data(df):
    """Filters data based on user-selected criteria in the sidebar."""

    # Sidebar Filters
    selected_gender = st.sidebar.multiselect("Select Gender", df["Gender"].dropna().unique())
    selected_religion = st.sidebar.multiselect("Select Religion", df["Religion"].dropna().unique())
    selected_payer = st.sidebar.multiselect("Select Payer", df["Payer"].dropna().unique())

    # Apply Filters
    if selected_gender:
        df = df[df["Gender"].isin(selected_gender)]
    if selected_religion:
        df = df[df["Religion"].isin(selected_religion)]
    if selected_payer:
        df = df[df["Payer"].isin(selected_payer)]

    return df
