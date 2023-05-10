############################################
#      Welcome To Python Calculator App    #
#                                          #
############################################
import sys

from mathoperations import *



def show_menu() -> str:
    
    num1=input("Enter a number1:")
    num2=input("Enter a number2:")
    
    choice = input("""
    Welcome To Python Calculator

    1. Addtion
    2. Subtraction
    3. Multiplication
    4. Division
    5. Squreroots
    6. Exit
    Select your choice:"""
    )
    
    if choice == '1':
        getaddition(num1,num2)
        ch= input("Do you want to continue (Y/N):")
        if(ch=='y'or ch=='Y'):
            show_menu()
    elif choice == '2':
        getsubtraction(num1,num2)
        ch= input("Do you want to continue (Y/y):")
        if(ch=='y'or ch=='Y'):
            show_menu()
    elif choice == '3':
        getmultiplication(num1,num2)
        ch= input("Do you want to continue (Y/y):")
        if(ch=='y'or ch=='Y'):
            show_menu()
    elif choice == '4':
        getdivision(num1,num2)
        ch= input("Do you want to continue (Y/y):")
        if(ch=='y'or ch=='Y'):
            show_menu()
    elif choice == '5':
        getsqurt(num1,num2)
        ch= input("Do you want to continue (Y/y):")
        if(ch=='y'or ch=='Y'):
            show_menu()
    elif choice == '6':
        sys.exit("Bye Bye")
    else:
        print("invalid choice")
        ch= input("Do you want to continue (Y/y):")
        if(ch=='y'or ch=='Y'):
            show_menu()
            
    
    
show_menu()