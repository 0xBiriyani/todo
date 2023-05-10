import math
    


def getsqurt():
    num1=input("Enter a number:")
    try:
        num1=float(num1)
        print (math.sqrt(num1))
    except:
        print("invalid input")
        getsqurt()
        
if __name__=="__main__":      
    getsqurt()       