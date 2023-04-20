def even_or_odd():
    num = int(input("Enter a number: "))
    if num %2 ==0:
       return num
    else:
       return num
    
        
result = even_or_odd()
if result%2==0:
    print(result, "is a even number")
if result%2==1:
    print(result,"is a odd numebr")