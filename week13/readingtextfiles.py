# Week 13: Reading & Writing Files - Count Words in a File

# Step 1: Ask user for the file name
file_name = input("Enter the file name (with extension): ")

try:
    # Step 2: Open the file in read mode
    with open(file_name, "r") as file:
        # Step 3: Read the entire file content
        content = file.read()
        
        # Step 4: Split the content into words
        words = content.split()
        
        # Step 5: Count the number of words
        word_count = len(words)
        
        # Step 6: Print the result
        print(f"The file '{file_name}' contains {word_count} words.")

except FileNotFoundError:
    print("Error: The file was not found. Please check the file name.")
