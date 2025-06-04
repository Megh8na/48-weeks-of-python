# Week 5 Assignment: Lists and List Methods

# Create a list of 5 subjects
subjects = ["Python programming", "WebApps", "Mobile computing", "Generative AI", "Big data"]

# Print original list
print("Original list of subjects:")
print(subjects)

# 1. sort() - Sort alphabetically
subjects.sort()
print("\nAfter sort():")
print(subjects)

# 2. reverse() - Reverse the list
subjects.reverse()
print("\nAfter reverse():")
print(subjects)

# 3. append() - Add a new subject at the end
subjects.append("Cybersecurity")
print("\nAfter append('Cybersecurity'):")
print(subjects)

# 4. insert(index, value) - Insert at specific position
subjects.insert(2, "Cloud Computing")
print("\nAfter insert(2, 'Cloud Computing'):")
print(subjects)

# 5. remove(value) - Remove a specific value
subjects.remove("WebApps")
print("\nAfter remove('WebApps'):")
print(subjects)

# 6. pop() - Remove last item
popped_subject = subjects.pop()
print(f"\nAfter pop(): removed '{popped_subject}'")
print(subjects)

# 7. index(value) - Find index of an item
index_ai = subjects.index("Generative AI")
print(f"\nIndex of 'Generative AI': {index_ai}")

# 8. count(value) - Count how many times a value appears
count_math = subjects.count("Math")  # returns 0
print(f"\nCount of 'Math': {count_math}")

# 9. copy() - Create a shallow copy
copied_list = subjects.copy()
print("\nCopied list:")
print(copied_list)

# 10. clear() - Remove all items from the list
subjects.clear()
print("\nAfter clear():")
print(subjects)