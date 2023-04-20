import calc
import strings

def mainmenu():
    operate  = 'y'
    while (operate == 'y'):
        print("1. Addition \n 2. Subtraction \n 3. Multipulication \n 4. Division\n 5. Printfullname  \n")
        choice=int(input("Enter Choice: "))
        if(choice==1):
            x= int(input("Enter input1:"))
            y= int(input("Enter input2:"))
            print("Sum of two numbers:",calc.add(x,y))
        elif(choice==2):
            x= int(input("Enter input1:"))
            y= int(input("Enter input2:"))
            print("Substraction of two numbers:",calc.sub(x,y))
        elif(choice==3):
            x= int(input("Enter input1:"))
            y= int(input("Enter input2:"))
            print("Multiplication of two numbers:",calc.mul(x,y))
        elif(choice==4):
            x= int(input("Enter input1:"))
            y= int(input("Enter input2:"))
            print("Division of two numbers:",calc.div(x,y))
        elif(choice==5):
            x= input("Enter Firstname:")
            y= input("Enter Lastname:")
            print("Full Name:",strings.getfullname(x,y))
        else:
            print("wrong input")
        operate = input("Do you want to continue y/n?")
mainmenu()

        

    
