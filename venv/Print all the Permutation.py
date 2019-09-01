def permute(n,s,ans):
    a=len(n)
    if s==a-1:
        ans.append("".join(n))
        print(n)

    for i in range(s,a):
        n[s],n[i]=n[i],n[s]
        permute(n,s+1,ans)
        n[s], n[i] = n[i], n[s]
c=list(map(str,input()))
a=len(c)
s=0
ans=[]
permute(c,s,ans)
print(ans)
