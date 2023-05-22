import os
import time

file_path = 'E:\github.com\todo\Sampath\Files\secondsfile.py'

os.system(f'python {file_path}')
file = open('seconds.txt', 'r')
delay = int(file.read())

count = 0

while True:
     time.sleep(delay)
     for i in range(delay):
        print(time.ctime())
        time.sleep(1)
        count +=1
        