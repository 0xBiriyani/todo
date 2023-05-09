def addition():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
        print(num1+num2)
    except ValueError:
        print("please enter a valid number")
        addition()

if __name__ == "__main_":
    addition()