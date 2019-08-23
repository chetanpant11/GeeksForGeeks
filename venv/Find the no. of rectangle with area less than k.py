arr=list(map(int, input().split()))
n=len(arr)
k=int(input())
i=0
j=n-1
ans=0
while(i<=j):
    if arr[i]*arr[j]>=k:
        j-=1
    elif arr[i]*arr[j]<k:
        ans+=2*(j-i+1)-1
        i+=1
print(ans%(10**9+7))
