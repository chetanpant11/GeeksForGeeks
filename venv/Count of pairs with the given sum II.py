arr=list(map(int, input().split()))
n=int(input())
i=0
j=len(arr)-1
ans=0
ans1=0
while(i<j):
    if arr[i]+arr[j]<n:
        i+=1
    elif arr[i]+arr[j]>n:
        j-=1
    elif arr[i]+arr[j]==n:
        count1 = 0
        count2 = 0
        k=i
        l=j
        if arr[i]!=arr[j]:
            while arr[k]==arr[i] :
                count1+=1
                i+=1
            while arr[l]==arr[j]:
                count2+=1
                j-=1
        elif arr[i]==arr[j]:
            ans1=(j-i+1)*(j-i)//2
            break
        ans+=count2*count1
print(ans+ans1)