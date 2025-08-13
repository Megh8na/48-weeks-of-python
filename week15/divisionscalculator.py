# Week 15: Try/Except - Handle divide-by-zero error

# Step 1: Get input from user
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    # Step 2: Try to divide
    result = num1 / num2
    print(f"The result of {num1} ÷ {num2} is {result}")

except ZeroDivisionError:
    print(" Error: Cannot divide by zero!")

except ValueError:
    print(" Error: Please enter valid numbers.")

except Exception as e:
    print(f" Unexpected error: {e}")
