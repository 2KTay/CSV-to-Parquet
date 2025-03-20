# CSV-to-Parquet

README: Data Processing for The Data Mine - Elevance Health Project

Overview

This Python script is designed to process large-scale CSV datasets for The Data Mine project at Purdue University, in collaboration with Elevance Health. The script automates data cleaning and transformation, ensuring high-quality input for cybersecurity threat detection and anomaly recognition.

Key features include:

Removing completely empty rows

Handling missing numerical values using column averages (for continuous data)

Handling missing categorical values using the most frequent entry (for discrete data)

Converting cleaned data into an optimized Parquet format for efficient storage and analysis

Prerequisites

Python 3.x

Pandas library (pip install pandas)

Usage

Place all CSV files in the designated project directory.

Modify the script to include the relevant file names in the file_list variable.

Execute the script to produce a structured, combined Parquet file for further cybersecurity data analysis.

Example

Script Features

Automated data preprocessing for cybersecurity applications

Intelligent missing value imputation

Conversion to Parquet format for scalable data handling

Relevance to The Data Mine - Elevance Health Project

This script plays a crucial role in:

Data Retrieval: Aggregating and preprocessing raw cybersecurity log data.

Model Training & Analysis: Ensuring clean, high-quality datasets for machine learning models detecting security threats.

Live/Scheduled Anomaly Detection: Providing structured data to support real-time cybersecurity event monitoring and anomaly detection.
