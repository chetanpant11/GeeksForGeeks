n=list(map(int, input().split()))
b=int(input())
n.sort()
i=0
j=b-1
min1=+2147483647
while(j!=len(n)-1):
    a1=n[j]-n[i]
    min1=min(a1,min1)
    i+=1
    j+=1
print(min1)