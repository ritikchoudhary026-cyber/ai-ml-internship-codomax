#Create a Messy Dataset---------

import pandas as pd
import numpy as np

# Creating a messy dataset with missing values and duplicates
data = {
    "Study_Hours": [1, 2, 3, 4, 5, np.nan, 7, 8, 8, 10],
    "Score": [35, 40, np.nan, 55, 65, 70, 78, 85, 85, 95]
}

df = pd.DataFrame(data)

# Save as CSV
df.to_csv("student_scores_messy.csv", index=False)
print("Messy dataset created and saved!")
print(df)


#Load the Dataset------------

import pandas as pd

df = pd.read_csv("student_scores_messy.csv")
print("Dataset loaded:\n", df)




#Check for Missing Values--------

# Check missing values column-wise
print("Missing values per column:\n", df.isnull().sum())

# Total missing values
print("\nTotal missing values:", df.isnull().sum().sum())

# Show rows with missing values
print("\nRows with missing values:\n", df[df.isnull().any(axis=1)])


#Handle Missing Values---------

#Option A: Remove rows with missing values---------

df_dropped = df.dropna()
print("After dropping missing rows:\n", df_dropped)



#Option B: Fill missing values with mean (recommended for numeric data)------

df_filled = df.copy()

df_filled["Study_Hours"] = df_filled["Study_Hours"].fillna(df_filled["Study_Hours"].mean())
df_filled["Score"] = df_filled["Score"].fillna(df_filled["Score"].mean())

print("After filling missing values with mean:\n", df_filled)


#Option C: Fill with median (better if data has outliers)--------

df_median_filled = df.copy()
df_median_filled["Study_Hours"] = df_median_filled["Study_Hours"].fillna(df_median_filled["Study_Hours"].median())
df_median_filled["Score"] = df_median_filled["Score"].fillna(df_median_filled["Score"].median())

print("After filling with median:\n", df_median_filled)



#Check for Duplicate Rows--------

# Check duplicates
print("Number of duplicate rows:", df.duplicated().sum())

# Show which rows are duplicates
print("\nDuplicate rows:\n", df[df.duplicated()])




#Remove Duplicates-------

df_no_duplicates = df_filled.drop_duplicates()
print("After removing duplicates:\n", df_no_duplicates)

print("\nShape before:", df_filled.shape)
print("Shape after removing duplicates:", df_no_duplicates.shape)




#Understand Dataset Statistics-----------

# Statistical summary
print("Statistical Summary:\n", df_no_duplicates.describe())

# Individual statistics
print("\nMean Study Hours:", df_no_duplicates["Study_Hours"].mean())
print("Mean Score:", df_no_duplicates["Score"].mean())
print("Median Study Hours:", df_no_duplicates["Study_Hours"].median())
print("Standard Deviation of Score:", df_no_duplicates["Score"].std())
print("Min/Max Study Hours:", df_no_duplicates["Study_Hours"].min(), "/", df_no_duplicates["Study_Hours"].max())
print("Min/Max Score:", df_no_duplicates["Score"].min(), "/", df_no_duplicates["Score"].max())

# Correlation between columns
print("\nCorrelation:\n", df_no_duplicates.corr())




#Save the Clean Dataset-------

df_no_duplicates.to_csv("student_scores_clean.csv", index=False)
print("Clean dataset saved as student_scores_clean.csv")





#Full Combined Script (Everything Together)-------

import pandas as pd
import numpy as np

# Step 1: Load messy dataset
df = pd.read_csv("student_scores_messy.csv")
print("===== ORIGINAL DATASET =====")
print(df)

# Step 2: Check missing values
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Handle missing values (fill with mean)
df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Score"] = df["Score"].fillna(df["Score"].mean())

# Step 4: Check and remove duplicates
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 5: Final statistics
print("\n===== CLEAN DATASET =====")
print(df)
print("\nStatistics:\n", df.describe())

# Step 6: Save clean dataset
df.to_csv("student_scores_clean.csv", index=False)
print("\nClean dataset saved successfully!")