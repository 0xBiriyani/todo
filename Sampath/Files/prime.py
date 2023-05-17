"""#prime numbers in range
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

print("Prime numbers within the range:", num1, "to", num2)

for num in range(num1, num2+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)"""
#check given number is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


