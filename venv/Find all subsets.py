def subset(n,s,ans,finalans):
    finalans.append(list(ans))
    for i in range(s,len(n)):
        ans.append(n[i])
        subset(n,i+1,ans,finalans)
        ans.pop()
    return

n=list(input())
s=0
a=len(n)
ans=[]
finalans=[]
subset(n,s,ans,finalans)
# ans1.sort()
print(finalans)
sum=0
for i in range(1,len(finalans)):
    a=max(finalans[i])
    b=min(finalans[i])
    c=int(a)-int(b)
    sum+=c
print(sum)