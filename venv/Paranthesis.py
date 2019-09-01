def paran(n,ans1,openB,closeB,ans):
    if closeB==n:
        ans.append("".join(ans1))
    if openB<n:
        ans1.append("(")
        paran(n,ans1,openB+1,closeB,ans)
        ans1.pop()
    if closeB<openB:
        ans1.append(")")
        paran(n, ans1, openB , closeB+1, ans)
        ans1.pop()
    return

n=int(input())
ans=[]
ans1=[]
openB=0
closeB=0
paran(n,ans1,openB,closeB,ans)
print(ans)