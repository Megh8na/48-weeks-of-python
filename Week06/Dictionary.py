# Week 6: phonebook Dictionary

# Step 1: Create the dictionary
phonebook = {
    "Meghana": "987-654-3210",
    "Ravi": "123-456-7890",
    "Anjali": "555-123-4567"
}

# 2. Access a value (lookup)
print("Lookup Meghana:", phonebook["Meghana"])

# 3. Add a new contact
phonebook["Karthik"] = "222-333-4444"
print("\nAfter adding Karthik:")
print(phonebook)

# 4. Update an existing contact
phonebook["Ravi"] = "000-000-0000"
print("\nAfter updating Ravi:")
print(phonebook)

# 5. Delete a contact
del phonebook["Anjali"]
print("\nAfter deleting Anjali:")
print(phonebook)

# 6. Check if a name exists
print("\nIs 'Meghana' in phonebook?", "Meghana" in phonebook)
print("Is 'Anjali' in phonebook?", "Anjali" in phonebook)

# 7. Use get() to avoid KeyError
print("\nSafe lookup using get():", phonebook.get("Anjali", "Not found"))

# 8. List all keys (names)
print("\nAll names in phonebook:")
print(list(phonebook.keys()))

# 9. List all values (numbers)
print("\nAll phone numbers in phonebook:")
print(list(phonebook.values()))

# 10. List all items (key-value pairs)
print("\nAll contacts (name → number):")
for name, number in phonebook.items():
    print(f"{name} → {number}")

# 11. Copy the phonebook
backup = phonebook.copy()
print("\nBackup copy of phonebook:")
print(backup)

# 12. Clear the original phonebook
phonebook.clear()
print("\nAfter clearing the phonebook:")
print(phonebook)
