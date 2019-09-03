import math
a = int(input())
b= int(math.sqrt(a))
flag=False
for i in range(2,b+1):
    p=i
    while(p<=a):
        p=p*i
        if p==a:
            print("True")
            flag=True
            break


if flag==False:
    print("False")