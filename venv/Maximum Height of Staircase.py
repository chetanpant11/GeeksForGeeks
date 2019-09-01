n = int(input())
low = 0
high = n
while(low<=high):
    mid = low+(high-low)//2
    if (mid*(mid+1))//2 < n:
        low = mid+1
    elif (mid*(mid+1))//2 > n:
        high = mid-1
    elif (mid*(mid+1))//2 == n:
        print(mid)
        break

if (mid*(mid+1))//2 > n:
    print(mid-1)
else:
    print(mid)