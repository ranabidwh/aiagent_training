

# --- Sample 6: Working with Dictionaries (Intermediate) ---

# Print a header for this section to make the output clear.
print("\n--- Student Grade Management ---")

# --- Creating a Dictionary ---
# Dictionaries are like real-world dictionaries or phone books. They store
# information in key-value pairs. Each unique 'key' maps to a 'value'.
# Here, student names are the keys (strings) and their grades are the values (integers).
student_grades = {
    "Alice": 95,      # "Alice" is the key, 95 is her grade (value)
    "Bob": 88,        # "Bob" is the key, 88 is his grade
    "Charlie": 72,    # "Charlie" is the key, 72 is his grade
    "David": 90       # "David" is the key, 90 is his grade
}

# Print the initial state of our dictionary to see what's inside.
print("Initial grades:")
print(student_grades)

# --- Accessing Values by Key ---
# To get a student's grade, you use their name (the key) inside square brackets [].
# This is similar to how you look up a definition using a word in a dictionary.
print(f"Alice's grade: {student_grades['Alice']}")

# --- Adding a New Entry ---
# You can add a new student and their grade by simply assigning a value to a new key.
# If "Eve" doesn't exist as a key, Python adds her with the grade 85.
student_grades["Eve"] = 85
print("\nGrades after adding Eve:")
print(student_grades)

# --- Updating an Existing Entry ---
# If a key already exists, assigning a new value to it will update the existing value.
# Here, Charlie's grade is changed from 72 to 75.
student_grades["Charlie"] = 75
print("\nGrades after updating Charlie:")
print(student_grades)

# --- Iterating Through a Dictionary ---
# You can loop through a dictionary to access both its keys and values.
# The `.items()` method returns pairs of (key, value) for each entry.
print("\nAll student grades:")
for student, grade in student_grades.items():
    # For each pair, 'student' will hold the key (name) and 'grade' will hold the value.
    print(f"{student}: {grade}")

# --- Checking if a Key Exists ---
# You can use the 'in' keyword to quickly check if a key is present in the dictionary.
# This is useful before trying to access or modify a value, preventing errors.
if "Bob" in student_grades:
    print("\nBob is in the grade book.")

# --- Removing an Entry ---
# The `del` keyword is used to remove a key-value pair from the dictionary.
# Here, David and his grade are removed entirely.
del student_grades["David"]
print("\nGrades after removing David:")
print(student_grades)
