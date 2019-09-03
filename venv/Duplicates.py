a=list(map(int, input().split()))
n=len(a)
b={i: 0 for i in a}
for i in range(0, n):
    if b[a[i]]==0:
        print(a[i],end=" ")
        b[a[i]]=1
    elif b[a[i]]==1:
        continue
