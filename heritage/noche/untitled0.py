from random import *
r=0
for i in range(10 ):
    a=randint(0,5) 
    b=randint(0,5)
    c=int(input(str(a)+"*"+str(b)+"="))
    if a*b==c :
        r=r+1
        print(r)
    else:
        r=r-1
print("Vous avez",r,"point(s)")
    