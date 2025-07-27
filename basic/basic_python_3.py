

# --- Sample 3: Loops (for loop with range() and Lists) ---

print("\n--- Counting and List Operations ---")

# Using a for loop with range()
print("Counting from 1 to 5:")
for i in range(1, 6): # range(start, stop) goes up to stop-1
    print(i)

# Creating and iterating through a list
fruits = ["apple", "banana", "orange", "grape"]
print("\nMy favorite fruits are:")
for fruit in fruits:
    print(fruit.capitalize()) # .capitalize() makes the first letter uppercase

# Adding an item to a list
fruits.append("kiwi")
print("\nAfter adding kiwi:")
print(fruits)

# Accessing elements by index
print(f"The first fruit is: {fruits[0]}")
print(f"The last fruit is: {fruits[-1]}")
