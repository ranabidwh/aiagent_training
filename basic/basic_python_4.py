

# --- Sample 4: Functions and Return Values ---

# Print a header for this section to make the output clear.
print("\n--- Function Examples ---")

# --- Function without Parameters and No Return Value ---
# This defines a function named 'greet_user'.
# 'def' is the keyword used to define a function.
# Functions are blocks of reusable code that perform a specific task.
def greet_user():
    # This line of code will be executed whenever greet_user() is called.
    print("Hello there! This message is from a function.")

# --- Calling the Function ---
# To execute the code inside a function, you 'call' it by its name followed by parentheses.
greet_user() # This will print "Hello there! This message is from a function."

# --- Function with Parameters and a Return Value ---
# This defines a function 'calculate_area_rectangle' that takes two inputs (parameters):
# 'length' and 'width'.
def calculate_area_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.
    Returns:
        float or int: The calculated area.
    """
    # --- Docstring ---
    # The triple-quoted string right after the function definition is called a "docstring".
    # It provides a brief explanation of what the function does, its arguments (Args),
    # and what it returns (Returns). This is good practice for documenting your code.

    # Perform the calculation inside the function.
    area = length * width
    # The 'return' statement sends a value back to the place where the function was called.
    # Without a 'return' statement, a function implicitly returns `None`.
    return area

# --- Call the Function and Store the Result ---
# Define variables to hold the dimensions of our rectangle.
rect_length = 10.5
rect_width = 5.0
# Call the 'calculate_area_rectangle' function, passing our dimensions as arguments.
# The value returned by the function (the calculated area) is stored in the 'rectangle_area' variable.
rectangle_area = calculate_area_rectangle(rect_length, rect_width)
# Print the result using an f-string for easy formatting.
print(f"The area of a rectangle with length {rect_length} and width {rect_width} is: {rectangle_area}")

# --- Function with Default Parameter Value ---
# This function 'say_hello' has one parameter 'name'.
# It has a default value "Guest". This means if no value is provided for 'name'
# when the function is called, it will automatically use "Guest".
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

# Call the function, providing a value for 'name'.
say_hello("Alice") # This will print "Hello, Alice!"

# Call the function without providing a value for 'name'.
# Since no argument is given, the default value "Guest" will be used for 'name'.
say_hello() # This will print "Hello, Guest!"
