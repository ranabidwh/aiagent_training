

# --- Sample 4: Functions and Return Values ---

print("\n--- Function Examples ---")

# Function without parameters and no return value
def greet_user():
    print("Hello there! This message is from a function.")

greet_user() # Calling the function

# Function with parameters and a return value
def calculate_area_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    Args:
        length (float or int): The length of the rectangle.
        width (float or int): The width of the rectangle.
    Returns:
        float or int: The calculated area.
    """
    area = length * width
    return area

# Call the function and store the result
rect_length = 10.5
rect_width = 5.0
rectangle_area = calculate_area_rectangle(rect_length, rect_width)
print(f"The area of a rectangle with length {rect_length} and width {rect_width} is: {rectangle_area}")

# Function with default parameter value
def say_hello(name="Guest"):
    print(f"Hello, {name}!")

say_hello("Alice")
say_hello() # Uses the default value "Guest"
