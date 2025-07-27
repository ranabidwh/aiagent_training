

# --- Sample 3: Loops (for loop with range() and Lists) ---

# Print a header for this section to make the output clear.
print("\n--- Counting and List Operations ---")

# --- Using a for loop with range() ---
# A 'for' loop is used to iterate over a sequence (like numbers, strings, lists, etc.).
print("Counting from 1 to 5:")
# The `range(start, stop)` function generates a sequence of numbers.
# It starts at 'start' (inclusive) and goes up to 'stop' (exclusive).
# So, range(1, 6) will generate numbers 1, 2, 3, 4, 5.
for i in range(1, 6):
    # In each iteration, 'i' takes on the next value from the range.
    print(i)

# --- Creating and Iterating Through a List ---
# A list is an ordered collection of items. Items are enclosed in square brackets [].
# Lists can hold items of different data types, but here we have all strings.
fruits = ["apple", "banana", "orange", "grape"]
print("\nMy favorite fruits are:")
# You can use a 'for' loop to iterate directly over the items in a list.
# In each iteration, 'fruit' will take on the value of the next item in the 'fruits' list.
for fruit in fruits:
    # The `.capitalize()` string method returns a copy of the string
    # with its first character capitalized and the rest lowercase.
    print(fruit.capitalize())

# --- Adding an Item to a List ---
# The `.append()` method is used to add an item to the very end of a list.
fruits.append("kiwi")
print("\nAfter adding kiwi:")
print(fruits) # Print the updated list to see "kiwi" added.

# --- Accessing Elements by Index ---
# Elements in a list are accessed using their "index" (their position).
# Indices start from 0 for the first element.
# So, `fruits[0]` refers to the first item ("apple").
print(f"The first fruit is: {fruits[0]}")
# Negative indices count from the end of the list.
# `fruits[-1]` refers to the last item ("kiwi").
# `fruits[-2]` would be the second to last, and so on.
print(f"The last fruit is: {fruits[-1]}")
