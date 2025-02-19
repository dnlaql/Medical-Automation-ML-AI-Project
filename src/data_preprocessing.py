import pandas as pd

def preprocess_data(df):
    """Cleans dataset: fills missing values, drops unnecessary columns, formats NRIC."""

    # Fill missing values for numeric columns with mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Handle categorical columns
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Drop unnecessary columns
    df = df.drop(columns=['Address'], errors='ignore')

    # Format NRIC/Passport No
    if 'NRIC/Passport No' in df.columns:
        df['NRIC/Passport No'] = df['NRIC/Passport No'].apply(format_nric)

    return df

def format_nric(nric):
    """Formats NRIC/Passport No into a readable format."""
    nric = str(nric)
    if len(nric) == 12:
        return f"{nric[:6]}-{nric[6:8]}-{nric[8:]}"
    return nric
