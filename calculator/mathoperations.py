##############################
#  Square root Module  #
##############################

import math
    


def getsqurt(num1,num2):
   # num1=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num2)
        print (math.sqrt(num1))
        print (math.sqrt(num2))
    except:
        print("invalid input")
        #ch=input("If you want to continue(y/n):")
        #if(ch=='Y' or ch=='y'):
            #getsqurt(num1,num2)
        
#if __name__=="__main__":
   #getsqurt()   5
   
def getaddition(num1,num2):
   # num1=input("Enter a number:")
   # num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num2)
        print (num1+num2)
    except:
        print("invalid input")
        #getaddition(num1,num2)
        
def getsubtraction(num1,num2):
   # num1=input("Enter a number:")
   # num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num2)
        print (num1-num2)
    except:
        print("invalid input")
        #getsubtraction(num1,num2)
        
def getmultiplication(num1,num2):
    #num1=input("Enter a number:")
    #num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num2)
        print (num1*num2)
    except:
        print("invalid input")
        #getmultiplication(num1,num2)
     
def getdivision(num1,num2):
    #num1=input("Enter a number:")
   # num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num2)
        print (num1/num2)
    except:
        print("invalid input")
       # getdivision(num1,num2)                
    
