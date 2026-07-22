#Student Score Dataset------
import pandas as pd

# Creating a sample dataset
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 40, 50, 55, 65, 70, 78, 85, 90, 95]
}

df = pd.DataFrame(data)

# Save it as a CSV file
df.to_csv("student_scores.csv", index=False)
print("Dataset created and saved as student_scores.csv")

#Pandas and Load the Dataset-------

import pandas as pd

# Load the dataset
df = pd.read_csv("student_scores.csv")

print("Dataset loaded successfully!")
print(df)

#Explore Rows-----

# First 5 rows
print("First 5 rows:\n", df.head())

# Last 5 rows
print("\nLast 5 rows:\n", df.tail())

# Specific number of rows
print("\nFirst 3 rows:\n", df.head(3))

# Random sample rows
print("\nRandom 3 rows:\n", df.sample(3))


#Explore Columns-------

# Column names
print("Column names:", df.columns.tolist())

# Access a single column
print("\nStudy Hours column:\n", df["Study_Hours"])

# Access multiple columns
print("\nBoth columns:\n", df[["Study_Hours", "Score"]])

# Number of columns
print("\nNumber of columns:", len(df.columns))



#Explore Dataset Information-------

# Shape of dataset (rows, columns)
print("Shape of dataset:", df.shape)

# Basic info (data types, non-null counts)
print("\nDataset Info:")
df.info()

# Statistical summary
print("\nStatistical Summary:\n", df.describe())

# Data types of each column
print("\nData types:\n", df.dtypes)

# Check for missing values
print("\nMissing values:\n", df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

#Basic Row/Column Selection (Indexing--------

# Select a specific row by index
print("Row at index 0:\n", df.iloc[0])

# Select a specific row and column
print("\nScore at index 3:", df.iloc[3]["Score"])

# Select using loc (label-based)
print("\nUsing loc:\n", df.loc[0:2])

# Select rows based on a condition
high_scorers = df[df["Score"] > 70]
print("\nStudents scoring above 70:\n", high_scorers)



#Quick Exploration Summary (Put it all together)--------

import pandas as pd

# Load dataset
df = pd.read_csv("student_scores.csv")

print("===== DATASET OVERVIEW =====")
print("\nShape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())
print("\nDataset Info:")
df.info()
print("\nStatistical Summary:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())