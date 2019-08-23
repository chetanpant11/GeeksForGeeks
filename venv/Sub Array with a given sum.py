arr=list(map(int, input().split()))
k=int(input())
sum=0
flag=False
for i in range(0, len(arr)):
    sum+=arr[i]
if sum<k:
    print("-1")
sum1=0
j=0
i=0
while(i<= len(arr)):
    if sum1<k:
        sum1+=arr[i]
    elif sum1>k :
        sum1-=arr[j]
        j+=1
    elif sum1==k:
        print(arr[j:i])
        break
    i+=1
print("-1")