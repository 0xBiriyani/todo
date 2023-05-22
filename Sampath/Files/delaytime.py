import time
import os

file_path = 'E:\github.com\todo\Sampath\Files\secondsfile.py'

while True:
    os.system(f'python {file_path}')

# Read the delay value from 'second.txt' file
    file = open('seconds.txt', 'r')
    delay = int(file.read())
    time.sleep(delay)

# Print current time with the specified delay
    for i in range(delay):
        print(time.ctime())
        time.sleep(1)

'''
import time
import os

# Specify the file path to read the delay value
file_path = 'E:\github.com\todo\Sampath\Files\secondsfile.py'

while True:
    # Read the delay value from the file
    with open(file_path, 'r') as file:
        delay = float(file.read())

    # Print the current time
    print(time.ctime())

    # Wait for the specified delay
    time.sleep(delay)'''
file = open("passsecondsfile.txt", "r")
seconds=int(file.read())
while True:
    time.sleep(seconds)
    for i in range (seconds):
        print(i)
    
    print(time.ctime())    
    
