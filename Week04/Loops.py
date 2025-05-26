# Week 4 Assignment: Using both for and while loops
even_numbers = []
print("Even numbers from 1 to 25 using for loop:")
for num in range(1, 26):  
    if num % 2 == 0:
        print(num)
        even_numbers.append(num)

print("\nEven numbers from 26 to 50 using while loop:")
num = 26
while num <= 50:
    if num % 2 == 0:
        print(num)
        even_numbers.append(num)
    num += 1

# Final Output
print("All even numbers from 1 to 50 are:")
print(even_numbers)