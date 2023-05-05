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

def fileops(command:str, todo:dict) -> list:
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
        todos = fileops("show", None)
        for tempTodo in todos:
            if tempTodo.get("todo_id") == todo.get("todo_id"):
                tempTodo["todo_name"] = todo.get("todo_name")
                tempTodo["todo_status"] = todo.get("todo_status")
                tempTodo["todo_due_date"] = todo.get("todo_due_date")
                break
        with open("todos.csv", "w") as f:
            f.write("todo_id,todo_name,todo_status,todo_due_date\n")
            for todo in todos:
                f.write(f"{todo.get('todo_id')},{todo.get('todo_name')},{todo.get('todo_status')},{todo.get('todo_due_date')}\n")
        return "done"
    elif command == "delete":
        todos = fileops("show", None)
        for tempTodo in todos:
            if tempTodo.get("todo_id") == todo.get("todo_id"):
                todos.remove(tempTodo)
                break
        with open("todos.csv", "w") as f:
            f.write("todo_id,todo_name,todo_status,todo_due_date\n")
            for todo in todos:
                f.write(f"{todo.get('todo_id')},{todo.get('todo_name')},{todo.get('todo_status')},{todo.get('todo_due_date')}\n")
        return "done"

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
                                "todo_due_date": todo_due_date})
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

def show_update_todo_menu():
    temp_todos = fileops("show", None)
    for todo in temp_todos:
        print(
            f"ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
        )
    todo_id = input("Select ToDo ID: ")
    todo_ids = [todo.get("todo_id") for todo in temp_todos]
    if todo_id not in todo_ids:
        print("Invalid ToDo ID, Please try again later :(")
        time.sleep(3)
        print("Returning to Main Menu...")
        time.sleep(2)
        clear()
        return ""
    clear()
    user_selected_todo = {}
    for todo in temp_todos:
        if todo.get("todo_id") == todo_id:
            print(
                f"Selected ToDo is: ==> ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
            )
            user_selected_todo = todo
            break
    print(
    """
    *** left blank if you don't want to update ***
    """
    )
    todo_name = input("Enter New Todo Name:").strip()
    todo_staus = input("Enter New Todo Status:").strip()
    todo_due_date = input("Enter New Todo Due Date:").strip()

    if todo_name != "":
        user_selected_todo["todo_name"] = todo_name
    elif todo_staus != "":
        user_selected_todo["todo_status"] = todo_staus
    elif todo_due_date != "":
        user_selected_todo["todo_due_date"] = todo_due_date
    
    result = fileops("update", user_selected_todo)
    if result == "done":
        print(
                f"Updated ToDo is: ==> ID: {user_selected_todo.get('todo_id')}, Name: {user_selected_todo.get('todo_name')}, Status: {user_selected_todo.get('todo_status')}, Due Date: {user_selected_todo.get('todo_due_date')}"
            )
        time.sleep(5)
        print("Returning to Main Menu...")
        time.sleep(1)
        clear()
    else:
        print("Something went wrong, Please try again later :(")
        time.sleep(1)
        print("Returning to Main Menu...")
        time.sleep(1)
        clear()

def show_delete_todo_menu():
    temp_todos = fileops("show", None)
    for todo in temp_todos:
        print(
            f"ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
        )
    todo_id = input("Select ToDo ID: ")
    todo_ids = [todo.get("todo_id") for todo in temp_todos]
    if todo_id not in todo_ids:
        print("Invalid ToDo ID, Please try again later :(")
        time.sleep(3)
        print("Returning to Main Menu...")
        time.sleep(2)
        clear()
        return ""
    clear()
    user_selected_todo = {}
    for todo in temp_todos:
        if todo.get("todo_id") == todo_id:
            print(
                f"Selected ToDo is: ==> ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
            )
            user_selected_todo = todo
            break
    result = fileops("delete", user_selected_todo)
    if result == "done":
        print("ToDo Deleted Successfully :)")
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
        for todo in fileops("show", None):
            print(
                f"ID: {todo.get('todo_id')}, Name: {todo.get('todo_name')}, Status: {todo.get('todo_status')}, Due Date: {todo.get('todo_due_date')}"
            )
        input("press enter key to go to main menu: ")

        main()
    elif selected_choice == "2":
        show_create_todo_menu()
        main()
    elif selected_choice == "3":
        show_update_todo_menu()
        main()
    elif selected_choice == "4":
        show_delete_todo_menu()
        main()


main()
