n=int(input())
a=n*(n+1)//2
c=list(map(int, input().split()))
su=0
for i in range(0, len(c)):
    su=su+c[i]
q=a-su
print(q)
