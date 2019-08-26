a=list(map(int, input().split()))
n=len(a)
low=0
high=n-1
while(low<=high):
    mid = low + (high - low) // 2
    if mid==n-1 and low==high:
        print(a[mid])
        break
    if mid==0 and low==high:
        print(a[mid])
        break
    if a[mid]>a[mid+1] and a[mid]>a[mid-1]:
        print(a[mid])
        break
    elif a[mid]>a[mid-1] and a[mid]<a[mid+1]:
        low=mid+1
    elif a[mid]<a[mid-1] and a[mid]>a[mid+1]:
        high=mid-1
    elif a[mid] < a[mid - 1] and a[mid] < a[mid + 1]:
        low = mid + 1
