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
        print(i)