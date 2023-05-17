import time
#import datetime
import os

#file =open ("passsecondsfile.txt","w")
#file.write(input("write a number in file:"))
file= open("passsecondsfile.txt", "r")
seconds=int(file.read())
print(seconds)
while True:
    time.sleep(seconds)
    for i in range (seconds):
        print(i)
    
    print(time.ctime())    
    
    