#Creating NumPy Arrays-------------

import numpy as np

# 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# 2D array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

# Array of zeros
zeros = np.zeros((2, 3))
print("Zeros array:\n", zeros)

# Array of ones
ones = np.ones((3, 3))
print("Ones array:\n", ones)

# Array with a range of values
range_arr = np.arange(1, 11)
print("Range array:", range_arr)

# Array with evenly spaced values
linspace_arr = np.linspace(0, 10, 5)
print("Linspace array:", linspace_arr)

# Random array
random_arr = np.random.rand(3, 3)
print("Random array:\n", random_arr)



#Array Properties--------

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Shape:", arr.shape)      # rows, columns
print("Size:", arr.size)        # total elements
print("Dimensions:", arr.ndim)  # number of dimensions
print("Data type:", arr.dtype)  # data type of elements



#Indexing and Slicing--------

arr = np.array([10, 20, 30, 40, 50])

# Basic indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("First three elements:", arr[0:3])
print("Every alternate element:", arr[::2])

# 2D array indexing
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Element at row 1, col 2:", arr2d[1, 2])
print("First row:", arr2d[0, :])
print("First column:", arr2d[:, 0])
print("Sub-matrix:\n", arr2d[0:2, 0:2])





#Mathematical Operations--------

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise operations
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# Scalar operations
print("Add 5 to all:", a + 5)
print("Multiply all by 2:", a * 2)

# Square root and power
print("Square root:", np.sqrt(a))
print("Power (squared):", np.power(a, 2))

# Statistical operations
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Max:", np.max(a))
print("Min:", np.min(a))
print("Standard Deviation:", np.std(a))
print("Variance:", np.var(a))





#Array-Based Calculations (Practical Practice)----------
#(a) Study Hours & Score Calculation using NumPy

import numpy as np

# Sample data: study hours and scores
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
scores = np.array([35, 40, 50, 55, 65, 70, 78, 85])

print("Study Hours:", study_hours)
print("Scores:", scores)

# Basic statistics
print("\nAverage study hours:", np.mean(study_hours))
print("Average score:", np.mean(scores))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))

# Correlation between hours and scores
correlation = np.corrcoef(study_hours, scores)
print("\nCorrelation matrix:\n", correlation)

# Predicted score using simple formula (practice)
predicted_scores = study_hours * 10 + 5
print("\nPredicted scores (simple formula):", predicted_scores)

# Difference between actual and predicted
difference = scores - predicted_scores
print("Difference (actual - predicted):", difference)

#(b) Matrix Operations)----

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# Matrix addition
print("Matrix Addition:\n", matrix_a + matrix_b)

# Matrix multiplication (element-wise)
print("Element-wise Multiplication:\n", matrix_a * matrix_b)

# Matrix multiplication (dot product)
print("Dot Product:\n", np.dot(matrix_a, matrix_b))

# Transpose
print("Transpose of A:\n", matrix_a.T)


#(d) Conditional Filtering (Boolean Indexing)-----

scores = np.array([35, 40, 50, 55, 65, 70, 78, 85])

# Filter scores above 60
high_scores = scores[scores > 60]
print("Scores above 60:", high_scores)

# Count how many students scored above 60
count = np.sum(scores > 60)
print("Number of students scoring above 60:", count)

# Replace scores below 40 with 40 (minimum passing)
adjusted_scores = np.where(scores < 40, 40, scores)
print("Adjusted scores:", adjusted_scores)