###################################################
# This is todo Application which creates, updates,#
# delete todo task.                               #
#                                                 #
###################################################
import sys
import os
import time

clear = lambda: os.system("cls")  # clear terminal
todos = []

def get_new_id():
    id = None
    with open("todos.csv","r") as f:
        f.readline() # skip header
        for line in f.readlines():
            id = int(line.split(",")[0])
    return id + 1

def fileops(command:str, todo:dict, id:int) -> list:
    # command = "show, create, update, delete"
    # retrive todos from file
    temp_todos = []
    if command == "show":
        with open("todos.csv", "r") as f:
            f.readline() # skip header
            for line in f.readlines():
                todo_id, todo_name, todo_status, todo_due_date = line.strip().split(",")
                temp_todos.append({"todo_id": todo_id,
                                   "todo_status": todo_status,
                                   "todo_name": todo_name,
                                   "todo_due_date": todo_due_date})
        return temp_todos

    elif command == "create":
        with open("todos.csv", "a") as f:
            id = get_new_id()
            f.write(f"{id},{todo.get('todo_name')},{todo.get('todo_status')},{todo.get('todo_due_date')}\n")
        return "done"
    elif command == "update":
        pass
    elif command == "delete":
        pass

def show_main_menu():
    print("Welcome to TODO Application")
    print(
        """ 
    1. View Todo
    2. Create Todo
    3. Update Todo
    4. Delete Todo
    5. Exit
    """
    )
    choice = input("Choose number to perform action:").strip()
    if choice in ["1", "2", "3", "4", "5"]:
        if choice == "5":
            print("Bye")
            sys.exit()
        else:
            return choice
    else:
        clear()
        print("Invalid Section, Please Select Proper Choice")


def show_create_todo_menu():
    """_summary_"""
    clear()
    todo_name = input("Enter Todo Name:")
    todo_due_date = input("Enter Todo Due Date(YYYY-MM-DD):")
    result = fileops("create", {"todo_name": todo_name,
                                "todo_status": 'created',
                                "todo_due_date": todo_due_date}, None)
    if result == "done":
        print("Todo Added to your list :)")
        time.sleep(1)
        print("Returning to Main Menu...")
        time.sleep(1)
        clear()
    else:
        print("Something went wrong, Please try again later :(")
        time.sleep(1)
        print("Returning to Main Menu...")
        time.sleep(1)
        clear()

def main():
    clear()
    selected_choice = show_main_menu()
    while selected_choice is None:
        selected_choice = show_main_menu()

    if selected_choice == "1":
        for todo in fileops("show", None, None):
            print(
                f"ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
            )
        input("press enter key to go to main menu: ")

        main()
    elif selected_choice == "2":
        show_create_todo_menu()
        main()


main()
