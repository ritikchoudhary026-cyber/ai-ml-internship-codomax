#Import Libraries and Load Data----------

import pandas as pd
import matplotlib.pyplot as plt

# Load the clean dataset
df = pd.read_csv("student_scores_clean.csv")
print(df)


#Scatter Plot (Study Hours vs Score)------

plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Score"], color="blue", marker="o")

plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)

plt.savefig("scatter_plot.png")   # saves the chart as an image
plt.show()



#Bar Chart (Score per Student)--------

plt.figure(figsize=(8, 5))

# Using index as student number
students = [f"Student {i+1}" for i in range(len(df))]

plt.bar(students, df["Score"], color="orange")

plt.title("Scores of Each Student")
plt.xlabel("Students")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()



#Line Chart (Study Hours Trend)------

plt.figure(figsize=(8, 5))

plt.plot(df["Study_Hours"], marker="o", linestyle="-", color="green", label="Study Hours")
plt.plot(df["Score"], marker="s", linestyle="--", color="red", label="Score")

plt.title("Study Hours and Score Trend")
plt.xlabel("Student Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

plt.savefig("line_chart.png")
plt.show()



#Bonus: Combine Multiple Charts in One Figure (Subplots)-------

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Scatter plot
axes[0].scatter(df["Study_Hours"], df["Score"], color="blue")
axes[0].set_title("Scatter: Study Hours vs Score")
axes[0].set_xlabel("Study Hours")
axes[0].set_ylabel("Score")
axes[0].grid(True)

# Bar chart
axes[1].bar(students, df["Score"], color="orange")
axes[1].set_title("Bar: Score per Student")
axes[1].set_xlabel("Students")
axes[1].set_ylabel("Score")
axes[1].tick_params(axis='x', rotation=45)

# Line chart
axes[2].plot(df["Study_Hours"], marker="o", label="Study Hours", color="green")
axes[2].plot(df["Score"], marker="s", label="Score", color="red")
axes[2].set_title("Line: Trend Comparison")
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.savefig("combined_charts.png")
plt.show()


#Full Combined Script (Everything Together)------

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("student_scores_clean.csv")
students = [f"Student {i+1}" for i in range(len(df))]

# --- Scatter Plot ---
plt.figure(figsize=(8, 5))
plt.scatter(df["Study_Hours"], df["Score"], color="blue")
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True)
plt.savefig("scatter_plot.png")
plt.show()

# --- Bar Chart ---
plt.figure(figsize=(8, 5))
plt.bar(students, df["Score"], color="orange")
plt.title("Scores of Each Student")
plt.xlabel("Students")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# --- Line Chart ---
plt.figure(figsize=(8, 5))
plt.plot(df["Study_Hours"], marker="o", label="Study Hours", color="green")
plt.plot(df["Score"], marker="s", label="Score", color="red")
plt.title("Study Hours and Score Trend")
plt.xlabel("Student Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.savefig("line_chart.png")
plt.show()

print("All charts created and saved successfully!")



