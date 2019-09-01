def subset(n,s,ans,finalans):
    # ans=list(ans)
    finalans.append("".join(ans))
    for i in range(s,len(n)):
        ans.append(n[i])
        subset(n,i+1,ans,finalans)
        # print(ans.pop())
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