n=int(input())
low=0
high=n
flag=False
while(low<=high):
    mid = low+(high-low)//2
    if (mid*mid<n):
        low=mid+1
    elif(mid*mid>n):
        high=mid-1
    elif(mid*mid==n):
        print(mid)
        flag=True
        break
if mid*mid<n:
    print(mid)
else:
    print (mid-1)