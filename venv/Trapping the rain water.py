t=int(input())
for i in range(0, t):
    q=int(input())
    n=list(map(int, input().split()))
    a=len(n)
    left=[0]*a
    right=[0]*a
    left[0]=n[0]
    right[a-1]=n[a-1]
    water=0
    for i in range(1,a):
        left[i]=max(left[i-1],n[i])
    for i in range(a-2,-1,-1):
        right[i]=max(right[i+1],n[i])
    for i in range(0, len(n)):
        water+=min(left[i],right[i])-n[i]
    print(water)