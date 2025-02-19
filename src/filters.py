import pandas as pd

def filter_data(df, gender=None, religion=None, payor=None, nationality=None, patient_type=None, race=None, age_group=None):
    """
    Function to filter the dataset based on specified criteria.
    
    Parameters:
    - df (DataFrame): The dataset to filter.
    - gender (str): Filter by gender (e.g., "Male", "Female").
    - religion (str): Filter by religion (e.g., "Islam", "Christianity").
    - payor (str): Filter by payor type (e.g., "Insurance", "Self-Pay").
    - nationality (str): Filter by nationality (e.g., "Malaysian", "Foreigner").
    - patient_type (str): Filter by patient type (e.g., "Outpatient", "Inpatient").
    - race (str): Filter by race (e.g., "Malay", "Chinese").
    - age_group (str): Filter by predefined age groups.
    
    Returns:
    - DataFrame: Filtered dataset.
    """

    if gender:
        df = df[df['Gender'] == gender]
    
    if religion:
        df = df[df['Religion'] == religion]
    
    if payor:
        df = df[df['Payor'] == payor]

    if nationality:
        df = df[df['Nationality'] == nationality]

    if patient_type:
        df = df[df['Patient Type'] == patient_type]
    
    if race:
        df = df[df['Race'] == race]

    if age_group:
        df = df[df['Age Group'] == age_group]

    return df

def categorize_age(df):
    """
    Function to create an 'Age Group' column based on age ranges.
    """
    bins = [0, 12, 17, 35, 50, 65, 100]
    labels = ["Child", "Teenager", "Young Adult", "Middle-aged Adult", "Senior Adult", "Elderly"]
    
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
    
    return df
