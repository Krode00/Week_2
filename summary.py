import pandas as pd 

#load the csv file into a pandas dataframe
df = pd.read_csv('Student_data.csv')

#print structural information about the dataframe(rows, columns, data types, missing values)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data Types:")
print(df.dtypes)
print("Missing Values:")
print(df.isnull().sum())

#print("Summary Statistics:")
print(df.describe(include='all'))
