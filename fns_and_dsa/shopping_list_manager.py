shopping_list = []
def display_menu():
    print("\nShopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the name of the item to add: ").strip()
    shopping_list.append(item)
    print(item, "has been added to the list.")

def remove_item(shopping_list):
    item = input("Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(item, "has been removed from the list.")
    else:
        print(item, "is not in the list.")

def view_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
