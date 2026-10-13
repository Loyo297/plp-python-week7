
# Shopping List Manager

# Start with an empty shopping list
shopping_list = []

def show_menu():
    print("\n===== SHOPPING LIST MANAGER =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip()

    if item:
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")
    else:
        print("Please enter a valid item.")

def remove_item():
    item = input("Enter the item to remove: ").strip()

    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        print("Thank you for using Shopping List Manager!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
