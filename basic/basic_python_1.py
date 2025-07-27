

# --- Sample 1: Basic Input, Output, and Variables ---

print("Hello! Welcome to our Python training.")

# Get user's name as input
user_name = input("What's your name? ")

# Get user's age and convert it to an integer
user_age_str = input("How old are you? ")
user_age_int = int(user_age_str)

# Display a personalized greeting
print(f"Nice to meet you, {user_name}!")

# Perform a simple calculation and display it
years_to_100 = 100 - user_age_int
print(f"You will turn 100 in {years_to_100} years.")

# Demonstrate type checking (optional for beginners, but good for understanding)
print(f"Type of user_name: {type(user_name)}")
print(f"Type of user_age_int: {type(user_age_int)}")
