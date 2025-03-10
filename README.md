# Streamlit Data Analytics App

## Overview

This interactive web app, built with Streamlit, empowers users to upload datasets, perform exploratory data analysis (EDA), and generate time-series forecasts using Facebook Prophet.

## Features

* **Data Upload:** Upload and analyze datasets in CSV, Excel, or JSON formats.
* **Exploratory Data Analysis (EDA):**
    * Preview the dataset.
    * Check data types.
    * Detect and display null and duplicate values.
    * Generate descriptive statistics.
* **Time-Series Forecasting:**
    * Forecast trends by selecting a date column and a target variable.
    * Visualize predicted values using Facebook Prophet.

## Installation

1.  **Prerequisites:** Ensure Python is installed on your system.
2.  **Install Dependencies:**
    ```
    pip install streamlit pandas matplotlib prophet
    ```

## Usage

1.  **Run the App:**
    ```
    streamlit run app.py
    ```
2.  **Upload Data:** Upload your dataset (CSV, Excel, or JSON) using the file uploader.
3.  **Select Analysis:** Choose the desired analysis type (EDA or Forecasting) from the dropdown menu.
4.  **Explore Insights:**
    * For EDA, view the generated statistics and insights.
    * For forecasting, select the date column and target variable to generate and visualize predictions.
