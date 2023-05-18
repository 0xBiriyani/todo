import time 
#import datetime
import os

choice=(input("Do you want to modify passsecondsfile.txt? Y/N:")).lower()
if(choice =="y"):
    file = open("passsecondsfile.txt","w")
    seconds = input("write a number in file:")
    file.write(seconds)
    file.close()

file = open("passsecondsfile.txt", "r")
seconds=int(file.read())
while True:
    time.sleep(seconds)
    for i in range (seconds):
        print(i)
    
    print(time.ctime())    
    
    