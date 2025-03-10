import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# File Upload
uploaded_file = st.file_uploader("Upload your dataset (CSV, Excel, JSON)", type=["csv", "xlsx", "json"])

if uploaded_file:
    file_extension = uploaded_file.name.split(".")[-1]
    
    # Read Data Based on File Type
    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        df = pd.read_excel(uploaded_file)
    elif file_extension == "json":
        df = pd.read_json(uploaded_file)
    
    # Dropdown for user to select analysis type
    analysis_type = st.selectbox("Select Analysis Type", [
        "Show Dataset", "Check Data Types", "Dataset Shape", "Null Values", "Duplicate Values", "Descriptive Statistics", "Forecasting"
    ])
    
    if analysis_type == "Show Dataset":
        st.subheader("📂 Dataset Preview")
        st.write(df.head())
    
    elif analysis_type == "Check Data Types":
        st.subheader("🔍 Data Types of Each Column")
        st.write(df.dtypes)
    
    elif analysis_type == "Dataset Shape":
        st.subheader("📏 Dataset Shape (Rows, Columns)")
        st.write(df.shape)
    
    elif analysis_type == "Null Values":
        st.subheader("⚠️ Null Values in Dataset")
        st.write(df.isnull().sum())
    
    elif analysis_type == "Duplicate Values":
        st.subheader("🔄 Duplicate Values in Dataset")
        st.write(df.duplicated().sum())
    
    elif analysis_type == "Descriptive Statistics":
        st.subheader("📊 Descriptive Statistics")
        st.write(df.describe())
    
    elif analysis_type == "Forecasting":
        st.subheader("📈 Forecasting")
        
        # Check if the dataset has a Date/Time column
        date_column = st.selectbox("Select Date Column", df.columns)
        value_column = st.selectbox("Select Column to Forecast", df.columns)
        
        if st.button("Run Forecasting"):
            df[date_column] = pd.to_datetime(df[date_column])
            df = df[[date_column, value_column]].dropna()
            df.columns = ["ds", "y"]  # Prophet requires columns to be named 'ds' (date) and 'y' (value)
            
            model = Prophet()
            model.fit(df)
            
            # Create Future DataFrame
            future = model.make_future_dataframe(periods=30)  # Forecast next 30 days
            forecast = model.predict(future)
            
            # Plot Forecast
            fig, ax = plt.subplots()
            model.plot(forecast, ax=ax)
            st.pyplot(fig)
        
            st.write("Forecasted Data:")
            st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(10))