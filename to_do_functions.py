import csv

def add_todo(file_name):
    print("Add to-do")
    todo_name = input("Enter a to-do item: ")
    with open(file_name, "a") as f: # Append mode to append to the end of the file
        writer = csv.writer(f) # This is a csv method, allowing us to write several roes of data at a time into the file
        writer.writerow([todo_name, "False"]) # Appending the item in list form

def remove_todo(file_name):
    todo_name = input("Enter the to-do item that you would like to delete: ") # Laundry
    # Create a new python list
    todo_list = []
    # Put all the previous items into the list except the one they want to delete
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        is_exist = False
        for row in reader: # [Grocery shopping, False]
            if (todo_name != row[0]): # != Laundry, which means Grocery shjopping --> True
                todo_list.append(row) # Grocery will be appended to new list
    # Write the entire list/csv file with this new list
            else:
                is_exist = True
    if not is_exist:
        print("Item name given does not exist.")
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(todo_list) # writerows for multiple list items

def mark_todo():
    print("Mark to-do")

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # [
            #   [title,completed],
            #   [do grocery,False],
            #   [do laundry,False],
            #   [complete assignment,False]
            # ]
            reader.__next__()
            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is complete.")
                else:
                    print(f"{row[0]} is not complete.")
    
    except FileNotFoundError:
        print("File not found")