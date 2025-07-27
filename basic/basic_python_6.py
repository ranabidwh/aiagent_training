

# --- Sample 6: Working with Dictionaries (Intermediate) ---

print("\n--- Student Grade Management ---")

# Creating a dictionary
student_grades = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 72,
    "David": 90
}

print("Initial grades:")
print(student_grades)

# Accessing values by key
print(f"Alice's grade: {student_grades['Alice']}")

# Adding a new entry
student_grades["Eve"] = 85
print("\nGrades after adding Eve:")
print(student_grades)

# Updating an existing entry
student_grades["Charlie"] = 75
print("\nGrades after updating Charlie:")
print(student_grades)

# Iterating through a dictionary
print("\nAll student grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Checking if a key exists
if "Bob" in student_grades:
    print("\nBob is in the grade book.")

# Removing an entry
del student_grades["David"]
print("\nGrades after removing David:")
print(student_grades)