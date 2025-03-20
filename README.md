# CSV-to-Parquet

README: Data Processing for The Data Mine - Elevance Health Project

# Overview

This Python script is designed to process large-scale CSV datasets for The Data Mine project at Purdue University, in collaboration with Elevance Health. The script automates data cleaning and transformation, ensuring high-quality input for cybersecurity threat detection and anomaly recognition.

# Key features include:

1. Removing completely empty rows

2. Handling missing numerical values using column averages (for continuous data)

3. Handling missing categorical values using the most frequent entry (for discrete data)

4. Converting cleaned data into an optimized Parquet format for efficient storage and analysis

# Prerequisites

1. Python 3.x

2. Pandas library (pip install pandas)
   

# Usage

1. Place all CSV files in the designated project directory.

2. Modify the script to include the relevant file names in the file_list variable.

3. Execute the script to produce a structured, combined Parquet file for further cybersecurity data analysis.


# Relevance to The Data Mine - Elevance Health Project


1. Data Retrieval: Aggregating and preprocessing raw cybersecurity log data.

2. Model Training & Analysis: Ensuring clean, high-quality datasets for machine learning models detecting security threats.

3. Live/Scheduled Anomaly Detection: The conversion to Parquet format allows real-time threat detection systems to efficiently access and process structured datasets.
