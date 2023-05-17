def myFun1(*argv):
    for arg in argv:
        print(arg)
 
 
myFun1('Hello', 'Welcome', 'to', 'Python world')

def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun2(first='welcome to', mid='python', last='wolrd')

def myFun3(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
 

args = ("welcome ", "to", "python world")
myFun3(*args)
 
kwargs = {"arg1": "welcome ", "arg2": "to ", "arg3": "world"}
myFun3(**kwargs)