import time 
#import datetime
import os

def get_user_input():
    choice=(input("Do you want to modify passsecondsfile.txt? Y/N:")).lower()
    if(choice =="y"):
        file = open("passsecondsfile.txt","w")
        seconds = input("write a number in file:")
        file.write(seconds)
        file.close()
    elif(choice=="n"):
        file = open("passsecondsfile.txt", "r")
        seconds=(file.read())
        
    else:
        choice=input("Enter valid input")
        get_user_input()
    return seconds
       
def print_timestamps(seconds):
    while True:
        time.sleep(int(seconds))
        print(time.ctime())    
        
user_seconds=get_user_input() 
print_timestamps(user_seconds)     