import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data_analysis(df):
    """Function to generate exploratory data analysis visualizations."""

    # Define Age Groups
    bins = [0, 18, 30, 45, 60, 75, 100]
    labels = ['<18', '18-29', '30-44', '45-59', '60-74', '75+']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

    # Create Streamlit Layout with 2 Columns
    col1, col2 = st.columns(2)

    # 📌 Gender Distribution (Pie Chart)
    with col1:
        st.subheader("Gender Distribution")
        fig, ax = plt.subplots()
        df['Gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['lightblue', 'pink'], ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    # 📌 Religion Distribution (Bar Chart)
    with col2:
        st.subheader("Religion Distribution")
        fig, ax = plt.subplots()
        sns.countplot(data=df, y='Religion', order=df['Religion'].value_counts().index, palette='viridis', ax=ax)
        st.pyplot(fig)

    # 📌 Additional Charts
    with col1:
        st.subheader("Payer Type Distribution")
        fig, ax = plt.subplots()
        df['Payer'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)
        ax.set_ylabel("")
        st.pyplot(fig)

    with col2:
        st.subheader("Nationality Distribution")
        fig, ax = plt.subplots()
        sns.countplot(data=df, y='Nationality', order=df['Nationality'].value_counts().index, palette='coolwarm', ax=ax)
        st.pyplot(fig)
