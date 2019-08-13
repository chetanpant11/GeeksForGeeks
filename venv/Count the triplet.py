a=int(input())
for i in range(a):
    count=0
    b=int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    arr_set=set(arr)
    a=arr[-1]
    for j in range(b-1):
        for k in range(j+1, b-1):
            s=arr[j] + arr[k]
            if s>a:
                break
            if s in arr_set:
                count=count+1
    if count>0:
        print(count)
    else:
        print(-1)
        # for k in range(j+1, b):
        #     if arr[j]+arr[k] in arr:
        #         count=count+1


    # if count==0:
    #     print(-1)
    # else:
    #     print(count)