############################################
#      Welcome To Python Calculator App    #
#                                          #
############################################
import sys
from getsqurt import getsqurt
from Multiplication import multiplication
from subtraction import subtraction
from addition import addition

def show_menu() -> str:
    choice = input("""
    Welcome To Python Calculator

    1. Addtion
    2. Division
    3. Subtraction
    4. Multiplication
    5. Squreroot
    6. Exit
    Select your choice:"""
    )
    if choice == '1':
        addition()
        show_menu()
    elif choice == '2':
        pass
    elif choice == '3':
        subtraction()
        show_menu()
    elif choice == '4':
        multiplication()
        show_menu()
    elif choice == '5':
        getsqurt()
        show_menu()
    elif choice == '6':
        sys.exit("Bye Bye")

show_menu()