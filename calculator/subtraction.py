def subtraction():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = num1-num2
        print(f"The result of {num1} - {num2} is {result}")
    except ValueError:
        print("Invalid input")
        subtraction()

if __name__ == "__main__":
    subtraction()

