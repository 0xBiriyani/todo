##############################
#  Square root Module  #
##############################

import math
    


def getsqurt():
    num1=input("Enter a number:")
    try:
        num1=float(num1)
        print (math.sqrt(num1))
    except:
        print("invalid input")
        getsqurt()
        
getsqurt()    
def getaddition():
    num1=input("Enter a number:")
    num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num1)
        print (num1+num1)
    except:
        print("invalid input")
        getaddition()
        
def getsubtraction():
    num1=input("Enter a number:")
    num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num1)
        print (num1-num1)
    except:
        print("invalid input")
        getsubtraction()
        
def getmultiplication():
    num1=input("Enter a number:")
    num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num1)
        print (num1*num1)
    except:
        print("invalid input")
        getmultiplication()
     
def getdivision():
    num1=input("Enter a number:")
    num2=input("Enter a number:")
    try:
        num1=float(num1)
        num2=float(num1)
        print (num1/num1)
    except:
        print("invalid input")
        getdivision()                
    
