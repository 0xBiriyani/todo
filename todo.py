###################################################
# This is todo Application which creates, updates,#
# delete todo task.                               #  
#                                                 #
###################################################
import sys
import os
import time
clear = lambda: os.system('cls')  # clear terminal
todos = []
def show_main_menu():
    print("Welcome to TODO Application")
    print(""" 
    1. View Todo
    2. Create Todo
    3. Update Todo
    4. Delete Todo
    5. Exit
    """)
    choice = input("Choose number to perform action:").strip()
    if choice in ["1","2","3","4","5"]:
        if choice == "5":
            print("Bye")
            sys.exit()
        else:
            return choice
    else:
        clear()
        print("Invalid Section, Please Select Proper Choice")
 
def show_create_todo_menu():
    clear()
    todo_name = input("Enter Todo Name:")
    todo_due_date = input("Enter Todo Due Date(YYYY-MM-DD):")
    todos.append({"todo_name":todo_name,"todo_due_date":todo_due_date})
    print("Todo Added to your list :)")
    time.sleep(1)
    print("Returning to Main Menu...")
    time.sleep(1)
    clear()
 
def main_menu():
    clear()
    selected_choice = show_main_menu()
    while selected_choice is None:
        selected_choice = show_main_menu()
 
    if selected_choice == "1":
        for id,todo in enumerate(todos):
            print(f"ID: {id}, Name: {todo.get('todo_name')}, Due_Date: {todo.get('todo_due_date')}")
        input("press enter key to go to main menu: ")
        main_menu()
    elif selected_choice == "2":
        show_create_todo_menu()
        main_menu()


main_menu()
