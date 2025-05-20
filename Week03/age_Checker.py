# week03 - Age checker using conditional statements

# Get user input
age = input("Enter your age: ")

# Convert input to integer
age = int(age)

# Conditional logic
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior.")
