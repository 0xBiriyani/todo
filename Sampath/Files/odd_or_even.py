#even_or_odd
"""a = int(input("Enter the number: "))
if a % 2 == 0:
    print(f"Entered number is {a}. And it is even number.")
else:
    print(f"Entered number is {a}. And it is odd number.")"""
#even_or_odd using fuction
"""def odd_or_even(a):
    return  a
a = int(input("Enter the number: "))
if a % 2 == 0:
    print(f"Entered number is {a}. And it is even number.")
else:
    print(f"Entered number is {a}. And it is odd number.")"""
#even_or_odd numbers in given range
"""def even_or_odd(num1, num2):
    return num1, num2

num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

even_numbers = [i for i in range(num1, num2) if i%2 == 0]
print("Even number: ")
print(even_numbers,"-->>:)")

odd_numbers = [i for i in range(num1,  num2) if i% 2 != 0]
print("Odd numbers: ")
print(odd_numbers,"-->>:)")"""
# alternative even_or_odd numbers in given range
def alternative_evenorodd(num1, num2):
    return num1, num2


num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

"""alternative_numbers = [num for num in range(num1, num2+1)]
print("Alternative even/odd numbers within the range:", num1, "to", num2)
print(*alternative_numbers)"""

even_numbers = [num for num in range(num1, num2+1) if num % 2 == 0]
print("Even numbers within the range:", num1, "to", num2())
print(*even_numbers)

odd_numbers = [num for num in range(num1, num2+1) if num % 2 != 0]
print("Odd numbers within the range:", num1, "to", num2())
print(*odd_numbers)
