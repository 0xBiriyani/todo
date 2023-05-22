import os

file_name = 'seconds.txt'
with open(file_name,'w') as file:
    seconds = (input("Enter the number: "))
    file.write(seconds)
    file.close()
