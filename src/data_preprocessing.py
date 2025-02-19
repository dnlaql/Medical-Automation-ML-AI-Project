import pandas as pd

def preprocess_data(df):
    """
    Function to clean the dataset by:
    - Filling missing values with the mean for numeric columns
    - Filling missing values with the mode for categorical columns
    - Formatting NRIC/Passport No with dashes
    - Dropping unnecessary columns (like 'Address')
    """

    # Fill missing values for numeric columns with the mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Handle non-numeric columns (e.g., categorical columns)
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])  # Fill missing categorical values with the mode

    # Drop unnecessary columns (like 'Address')
    df = df.drop(columns=['Address'], errors='ignore')

    # Format NRIC/Passport No column
    if 'NRIC/Passport No' in df.columns:
        df['NRIC/Passport No'] = df['NRIC/Passport No'].apply(lambda x: format_nric(x))

    return df

def format_nric(nric):
    """
    Function to format NRIC/Passport No to include dashes.
    Example: 857682437877 -> 857682-43-7877
    """
    nric = str(nric)  # Convert to string if it is not already
    if len(nric) == 12:
        return f"{nric[:6]}-{nric[6:8]}-{nric[8:]}"
    return nric  # If not a valid NRIC, return it as is
