# Week 16: Custom Exceptions - Negative Age Checker

# Step 1: Define your custom exception
class NegativeAgeError(Exception):
    pass  

# Step 2: Take age input from user
try:
    age = int(input("Enter your age: "))

    # Step 3: Raise custom exception if age is negative
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")

    print(f"Your age is {age}")

# Step 4: Handle the custom exception
except NegativeAgeError as e:
    print(f"❌ Custom Error: {e}")

# Optional: Handle non-integer input
except ValueError:
    print("❌ Please enter a valid number.")
