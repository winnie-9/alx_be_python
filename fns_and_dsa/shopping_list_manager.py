def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list(shopping_list):
    print("\nCurrent shopping list:")
    for item in shopping_list:
        print(f"- {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1,2,3,4): ")
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()
