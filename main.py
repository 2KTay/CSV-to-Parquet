'''
Code description:

Python

Adapt the data to be stored in parquet files

10-20 lines python

2-3 functions

Input: list of files names of csvs
Output: pandas dataframe to concatenate all the csv file names data together,

Remove all the empty rows,
find empty cells, and if row is not completely empty, find average and put it in the empty cell.

Continuous ->find average
Discrete numbers->pick most frequent


the files in this folder are an example to use


Author:Taemoor Hasan
'''

import pandas as pd

#read and concatenate the CSV files into a dataframe
def loadConcatCSV(files):
    df = pd.concat((pd.read_csv(file) for file in files), ignore_index=True)
    return df


#removes empty rows and fills in missing cells
def cleanData(df):
    #remove empty rows
    df.dropna()

    #fill in the missing cells
    for column in df.columns:

        #check if the column is numeric
        if df[column].dtype in [int, float]:

            #fill empty values with average continuous value
            avg= df[column].mean()
            df[column] = df[column].fillna(avg)
        else:
            #fill empty values with the most frequent value
            most_frequent = df[column].mode()[0]
            df[column] = df[column].fillna(most_frequent)

    return df


csvFiles = ['file1.csv', 'file2.csv']
#csvFiles=['customers-100.csv','customers-1000.csv']

df = loadConcatCSV(csvFiles)
cleaned_df = cleanData(df)

#had to pip install pyarrow

#converted new CSV file to parquet file
cleaned_df.to_parquet('output.parquet')
print(cleaned_df)

