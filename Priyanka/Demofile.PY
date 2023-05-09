x = input(" Enter  number:")
x=int(x)
f = open("demofile.txt", "a")
for i in range(1,11):
    t= f"{x}*{i}={x*i}\n"
    f.write(t)
f.close()    