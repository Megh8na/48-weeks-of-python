# Week 12: Lambda + Map with User Input

# Step 1: Get input from user
user_input = input("Enter numbers separated by spaces: ")

# Step 2: Convert input string to a list of integers
numbers = list(map(int, user_input.split()))

# Step 3: Use map + lambda to square each number
squared = list(map(lambda x: x ** 2, numbers))

# Step 4: Print the result
print("Original list:", numbers)
print("Squared list:", squared)
