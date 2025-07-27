

# --- Sample 2: Conditional Statements (if/elif/else) ---

print("\n--- Age Eligibility Checker ---")
age_str = input("Please enter your age: ")
age = int(age_str)

if age < 0:
    print("That's an invalid age. Age cannot be negative.")
elif 0 <= age < 13:
    print("You are a child.")
elif 13 <= age < 20:
    print("You are a teenager.")
elif 20 <= age < 60:
    print("You are an adult.")
else: # age >= 60
    print("You are a senior citizen.")

print("Thank you for using the age checker!")