Streamlit Data Analytics App

Overview

This interactive web app, built with Streamlit, allows users to upload datasets, perform exploratory data analysis (EDA), and generate time-series forecasts using Facebook Prophet.

Features

Upload and analyze CSV, Excel, or JSON files.

Perform EDA: view dataset preview, check data types, detect null/duplicate values, and generate statistics.

Forecast trends by selecting a date column and target variable, with visualizations of predicted values.

Installation

Ensure Python is installed, then install dependencies:

pip install streamlit pandas matplotlib prophet

Run the app with:

streamlit run app.py

Usage

Upload a dataset, select an analysis type from the dropdown menu, and explore insights. For forecasting, choose the date column and target variable to generate predictions.
