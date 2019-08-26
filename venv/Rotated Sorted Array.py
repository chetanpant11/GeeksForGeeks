a=list(map(int, input().split()))
k=int(input())
n=len(a)
low=0
high1=n-1
high=high1
a1=0
while(low<=high1):
    mid=low+(high1-low)//2
    if a[mid]<a[high]:
        high1= mid-1
    elif a[mid]>a[high]:
        low=mid+1
    if a[mid]>a[mid+1]:
        a1=mid+1
        break
a2=a1
low1=0
a3=a1-1
while(low1<=a3):
    mid1=(low1+a3)//2
    if a[mid1]>k:
        a3=mid1-1
    if a[mid1]<k:
        low1=mid1+1
    if a[mid1]==k:
        print(mid1)
        break
a4=n-1
while(a2<=a4):
    mid1=(a2+a4)//2
    if a[mid1]<k:
        a2=mid1+1
    if a[mid1]>k:
        a4=mid1-1
    if a[mid1]==k:
        print(mid1)
        break