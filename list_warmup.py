
# Shopping List Manager - List Warmup

# Create a shopping list
shopping_list = ["Bread", "Milk", "Eggs", "Rice"]

# Display the original list
print("Original shopping list:", shopping_list)

# Access an item using its index
print("First item:", shopping_list[0])
print("Third item:", shopping_list[2])

# Add a new item
shopping_list.append("Sugar")
print("After adding sugar:", shopping_list)

# Remove an item
shopping_list.remove("Milk")
print("After removing milk:", shopping_list)

# Check whether an item exists
if "Eggs" in shopping_list:
    print("Eggs are on the shopping list.")
else:
    print("Eggs are not on the shopping list.")

# Display the total number of items
print("Total items:", len(shopping_list))
