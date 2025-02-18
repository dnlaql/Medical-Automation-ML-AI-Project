import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def preprocess_data(df):
    """
    Function to preprocess the dataset by:
    - Filling missing values with the mean of numeric columns
    - Dropping unnecessary columns (like 'Address')
    - Formatting NRIC/Passport No with dashes
    - Creating a GeoDataFrame from latitude and longitude columns
    """

    # Fill missing values for numeric columns with the mean
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Handle non-numeric columns (e.g., categorical columns)
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])  # Fill missing categorical values with the mode

    # Drop unnecessary columns (like 'Address')
    df = df.drop(columns=['Address'], errors='ignore')  # Drop the 'Address' column if it exists

    # Format NRIC/Passport No column
    if 'NRIC/Passport No' in df.columns:
        df['NRIC/Passport No'] = df['NRIC/Passport No'].apply(lambda x: format_nric(x))

    # Create a GeoDataFrame from latitude and longitude columns
    if 'Latitude' in df.columns and 'Longitude' in df.columns:
        geometry = [Point(lon, lat) for lon, lat in zip(df['Longitude'], df['Latitude'])]
        geo_df = gpd.GeoDataFrame(df, geometry=geometry)
        return geo_df

    return df

def format_nric(nric):
    """
    Function to format NRIC/Passport No to include dashes.
    Example: 857682437877 -> 857682-43-7877
    """
    nric = str(nric)  # Convert to string if it is not already
    # Format NRIC if the length is valid (12 characters for the NRIC)
    if len(nric) == 12:
        return f"{nric[:6]}-{nric[6:8]}-{nric[8:]}"
    return nric  # If not a valid NRIC, return it as is
