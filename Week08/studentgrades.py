# Week 8: Nested Structures 

# Step 1: Create a list of student dictionaries
students = [
    {"name": "Meghana", "grade": 82},
    {"name": "Ravi", "grade": 67},
    {"name": "Anjali", "grade": 91},
    {"name": "Karthik", "grade": 74},
    {"name": "Nisha", "grade": 88}
]

# Step 2: Print names of students with grade > 75
print("Students with grades greater than 75:")

for student in students:
    if student["grade"] > 75:
        print(student["name"])
