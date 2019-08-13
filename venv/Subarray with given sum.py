t=int(input())
for i in range(0,t):
    q,n=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    a=len(arr)
    # for i in range(0,a):
    cur_sum=arr[0]
    start=0
    i=1
    flag=False
    while i<=a:
        if i<a and cur_sum<n:
            cur_sum+=arr[i]

        while (cur_sum>n):
            cur_sum-=arr[start]
            start+=1

        if cur_sum==n:
            print(start+1, i+1)
            flag=True
            break
        i=i+1

    if flag==False:
        print("-1")
