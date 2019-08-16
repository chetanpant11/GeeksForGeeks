t=int(input())
for i in range(0,t):
    c=int(input())
    n=input().split()
    for i in range(0,len(n)):
        n[i]=int(n[i])
    n.sort()
    b=[]
    for i in range(0, len(n)-1):
        a=n[i]^n[i+1]
        if a==0:
            b.append(n[i])
        else:
            a=0
    for i in range(0,len(n)):
        if n[abs(n[i])-1]>0:
            n[abs(n[i])-1]=-n[abs(n[i])-1]
    for  i in range(0, len(n)):
        if n[i]>0:
            b.append(i+1)
    for i in range(0,len(b)):
        print(b[i],end=" ")
    print()