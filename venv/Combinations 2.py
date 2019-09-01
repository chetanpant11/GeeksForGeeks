def combination(n,s,ans,finalans,sum):
    if sum==0:
        ans=list(ans)
        finalans.append(ans)
    if sum<0:
        return
    for i in range(s, len(n)):
        if i>s and n[i]==n[i-1]:
            continue
        ans.append(n[i])
        combination(n,i+1,ans,finalans,sum-n[i])
        ans.pop()
    return


n=list(map(int, input().split()))
b=int(input())
s=0
a=len(n)
# n.sort()
ans=[]
finalans=[]
combination(n,s,ans,finalans,b)
print(finalans)
# 10 1 2 7 6 1 5