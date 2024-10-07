#Assignment 2

# Tasks 1, 2, 3

# User can add items to the list
def add_item(shopping_list, item):
    shopping_list.append(item)
    return shopping_list

# User can remove items from the list
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} is not in the list.")
    return shopping_list

# User can view the list
def view_list(shopping_list):
    return shopping_list

shopping_list = []
while True:
    try:
        user_input = input("Enter 'add' to add an item, 'remove' to remove an item, 'view' to view the list, or 'quit' to exit: ").lower()
        if user_input == 'add':
            item = input("Enter the item you would like to add: ")
            shopping_list = add_item(shopping_list, item)
        elif user_input == 'remove':
            item = input("Enter the item you would like to remove: ")
            shopping_list = remove_item(shopping_list, item)
        elif user_input == 'view':
            print(f"Your shopping list: {view_list(shopping_list)}")
        elif user_input == 'quit':
            break
        else:
            raise ValueError("Invalid input.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
