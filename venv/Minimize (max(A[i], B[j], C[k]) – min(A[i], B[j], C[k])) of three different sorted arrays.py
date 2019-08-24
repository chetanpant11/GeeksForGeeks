a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))
i=0
j=0
k=0
ans=2147483647
while(i!=len(a) and j!=len(b) and k!=len(c)):
    a1=max(a[i],b[j],c[k])
    b1=min(a[i],b[j],c[k])
    ans=min(ans, a1-b1)
    if b1==a[i]:
        i+=1
    elif b1==b[j]:
        j+=1
    elif b1==c[k]:
        k+=1
print(ans)
