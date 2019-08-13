t=int(input())
for itr in range(t):
    r=list(map(int, input().split()))
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))

    n=len(a)
    m=len(b)
    for i in range(m-1,-1 ,-1 ):
        last = a[n-1]
        j = n - 2
        while(j>=0 and a[j]>b[i]):
            a[j+1]=a[j]
            j=j-1

        if (j!=n-2 or last>b[i]):
            a[j+1]=b[i]
            b[i]=last

    for i in range(n):
        print(a[i],end=" ")
    for i in range(m):
        print(b[i],end=" ")
        
