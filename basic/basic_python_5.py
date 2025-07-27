

# --- Sample 5: Basic Error Handling (try-except) ---

# Print a header for this section to make the output clear.
print("\n--- Simple Division Calculator with Error Handling ---")

# --- The 'try' Block ---
# The 'try' block contains the code that might cause an error (or "exception").
# Python will execute this code. If an error occurs, it immediately stops
# executing the rest of the 'try' block and jumps to the appropriate 'except' block.
try:
    # Prompt the user to enter the first number. The input is initially a string.
    num1_str = input("Enter the first number: ")
    # Attempt to convert the input string to a floating-point number (a number with decimals).
    # This line can cause a ValueError if the user types something that's not a valid number (e.g., "hello").
    num1 = float(num1_str)

    # Prompt the user for the second number, also initially a string.
    num2_str = input("Enter the second number: ")
    # Attempt to convert the second input string to a float.
    # This can also raise a ValueError.
    num2 = float(num2_str)

    # Perform the division.
    # This line can cause a ZeroDivisionError if 'num2' is 0.
    result = num1 / num2
    # If division is successful, print the result.
    print(f"The result of {num1} / {num2} is: {result}")

# --- The 'except' Blocks ---
# 'except' blocks catch specific types of errors that might occur in the 'try' block.
# If a ValueError happens (e.g., input couldn't be converted to a number),
# this block will execute.
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
# If a ZeroDivisionError happens (e.g., attempting to divide by zero),
# this specific block will execute.
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero second number.")
# This is a general 'except' block. It catches any other type of error
# that wasn't caught by the more specific 'except' blocks above.
# 'as e' captures the error message provided by Python, which can be helpful for debugging.
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# --- The 'finally' Block ---
# The 'finally' block always executes, regardless of whether an error occurred
# in the 'try' block or not. It's often used for cleanup operations,
# like closing files or network connections.
finally:
    print("Calculation attempt finished.")
