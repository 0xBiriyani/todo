def multiplication():
    num1=input("Please enter first number: ")
    num2=input("Please enter second number to do multiplication: ")

    try:
            num1 = float(num1)
            num2= float(num2)
            print(num1 * num2)
    except:
        print("Please enter a valid number")
        if __name__ == "__main__":
             multiplication()