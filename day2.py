#operators
a = 10
b = 3

# Arithmetic operators
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

#loops--------
 
 
# Comparison operators
print(a > b)
print(a == b)
print(a != b)

# Logical operators
x = True
y = False
print(x and y)
print(x or y)
print(not x)
 

 # For loop
print("For loop example:")
for i in range(1, 6):
    print("Count:", i)

# While loop
print("\nWhile loop example:")
n = 1
while n <= 5:
    print("Number:", n)
    n += 1

# Loop with condition (skip even numbers)
print("\nOnly odd numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


#functions-----

# Simple function
def greet(name):
    return f"Hello, {name}! Welcome to Day 2."

print(greet("Rahul"))

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

result = add_numbers(15, 25)
print("Sum:", result)

# Function with default parameter
def calculate_area(length, width=5):
    return length * width

print("Area:", calculate_area(10))
print("Area with custom width:", calculate_area(10, 8))


