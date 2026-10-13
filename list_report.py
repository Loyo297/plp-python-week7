
# Shopping List Manager - Smart Report

# Create a shopping list with sample items
shopping_list = [
    "Bread",
    "Milk",
    "Eggs",
    "Rice",
    "Sugar",
    "Bread"
]

print("===== SHOPPING LIST REPORT =====")

# Display all items
print("\nItems in your shopping list:")

for index, item in enumerate(shopping_list, start=1):
    print(f"{index}. {item}")

# Count the total number of items
total_items = len(shopping_list)
print(f"\nTotal items: {total_items}")

# Count unique items
unique_items = []

for item in shopping_list:
    if item not in unique_items:
        unique_items.append(item)

print(f"Unique items: {len(unique_items)}")

# Display unique items
print("\nUnique shopping items:")

for item in unique_items:
    print(f"- {item}")

# Check for duplicate items
print("\nDuplicate items:")

duplicates = []

for item in shopping_list:
    if shopping_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if duplicates:
    for item in duplicates:
        print(f"- {item}")
else:
    print("No duplicate items found.")

# Final summary
print("\n===== SUMMARY =====")
print(f"Total entries: {total_items}")
print(f"Different items: {len(unique_items)}")
print(f"Duplicate item types: {len(duplicates)}")
