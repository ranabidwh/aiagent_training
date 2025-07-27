

# --- Sample 2: Conditional Statements (if/elif/else) ---

# Print a header for this section to make the output clear.
print("\n--- Age Eligibility Checker ---")

# --- Get User Input ---
# The `input()` function prompts the user to enter text and returns whatever they type as a string.
age_str = input("Please enter your age: ")
# --- Type Conversion ---
# The `int()` function converts a string (or other data types) to an integer (a whole number).
# This is necessary because we need to perform numerical comparisons with the age.
age = int(age_str)

# --- Conditional Logic (if/elif/else) ---
# Conditional statements allow your program to make decisions and execute different code
# blocks based on whether certain conditions are true or false.

# The 'if' statement is the first condition checked.
# If 'age' is less than 0, this block executes.
if age < 0:
    print("That's an invalid age. Age cannot be negative.")
# The 'elif' (short for "else if") statement is checked only if the preceding 'if' (or 'elif')
# condition was false. You can have multiple 'elif' blocks.
# This checks if 'age' is between 0 (inclusive) and 13 (exclusive).
elif 0 <= age < 13:
    print("You are a child.")
# This checks if 'age' is between 13 (inclusive) and 20 (exclusive).
elif 13 <= age < 20:
    print("You are a teenager.")
# This checks if 'age' is between 20 (inclusive) and 60 (exclusive).
elif 20 <= age < 60:
    print("You are an adult.")
# The 'else' statement is the fallback. It executes if none of the 'if' or 'elif'
# conditions above it were true.
# In this case, if 'age' is not less than 0, not between 0-12, not between 13-19, and not between 20-59,
# then it must be 60 or greater.
else: # This condition implies age >= 60
    print("You are a senior citizen.")

# This line will always execute after the conditional statements have finished.
print("Thank you for using the age checker!")
