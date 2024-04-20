# System packages
import os.path # In-build python module, os system for opening files etc

# External packages

# Imports of our own functions
from to_do_functions import add_todo, remove_todo, mark_todo, view_todo

print("Welcome to your to-do list application")

def create_menu():
    print("1. Enter 1 to add item to the list")
    print("2. Enter 2 to remove item from the list")
    print("3. Enter 3 to mark any item as complete")
    print("4. Enter 4 to view to-do list items")
    print("5. Enter 5 to exit")

    user_choice = input("Enter your selection: ")
    return user_choice

file_name = "list.csv"

# We only want to run this if the file does not exist
if (not os.path.isfile(file_name)): # This is used to check whether a file exists or not
    print("Creatinf file as it doesn't exist")
    # Create the file
    todo_file = open(file_name, "w")
    # We will enter the headings into the file
    todo_file.write("title, completed")
    # Close the file
    todo_file.close


choice = ""

while choice != "5": # Necessary to keep the application open until the user chooses to exit by selecting 5
    choice = create_menu()

    if (choice == "1"):
        add_todo(file_name)
    elif (choice == "2"):
        remove_todo(file_name)
    elif (choice == "3"):
        mark_todo(file_name)
    elif (choice == "4"):
        view_todo(file_name)
    elif (choice == "5"):
        print("You entered 5")
    else:
        print("Please only enter the options shown above.")


print("Thank you for using our to-do list application")