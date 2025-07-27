

# --- Sample 5: Basic Error Handling (try-except) ---

print("\n--- Simple Division Calculator with Error Handling ---")

try:
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str) # Try converting to float

    num2_str = input("Enter the second number: ")
    num2 = float(num2_str)

    result = num1 / num2
    print(f"The result of {num1} / {num2} is: {result}")

except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero second number.")
except Exception as e: # Catch any other unexpected errors
    print(f"An unexpected error occurred: {e}")
finally:
    print("Calculation attempt finished.")