

# --- Sample 1: Basic Input, Output, and Variables ---

# --- Output: Using the print() function ---
# The 'print()' function is used to display output to the console.
# Here, it prints a welcoming message.
print("Hello! Welcome to our Python training.")

# --- Input: Getting data from the user ---
# The 'input()' function prompts the user for information.
# Whatever the user types is captured as a string (text) and stored in the 'user_name' variable.
user_name = input("What's your name? ")

# --- Input and Type Conversion ---
# First, we ask the user for their age. Again, 'input()' returns a string.
user_age_str = input("How old are you? ")
# Numbers entered by the user are initially treated as text (strings).
# To perform mathematical operations, we need to convert the string to a number.
# The 'int()' function converts a string to an integer (a whole number).
# The result is stored in 'user_age_int'.
user_age_int = int(user_age_str)

# --- Output: Personalized Greeting using an f-string ---
# An f-string (formatted string literal) provides a concise way to embed
# expressions inside string literals. You put an 'f' before the opening quote,
# and then use curly braces {} to include variables directly.
print(f"Nice to meet you, {user_name}!")

# --- Variables and Simple Calculation ---
# A variable is a named storage location for data.
# Here, we perform a simple subtraction using the 'user_age_int' variable.
# The result of the calculation is stored in a new variable called 'years_to_100'.
years_to_100 = 100 - user_age_int
# We then print the result using another f-string.
print(f"You will turn 100 in {years_to_100} years.")

# --- Type Checking (Optional, but good for understanding) ---
# The 'type()' function returns the data type of a variable.
# This helps in understanding what kind of data your variables are holding.
print(f"Type of user_name: {type(user_name)}")       # This will show <class 'str'> because input() returns strings.
print(f"Type of user_age_int: {type(user_age_int)}") # This will show <class 'int'> because we converted it to an integer.
