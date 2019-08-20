n=list(map(int, input().split()))
count=0
l=[]
count1=0
me=n[0]
for i in range(0, len(n)):
    if me==n[i]:
        count += 1
    elif count==0:
        m=n[i]
    else:
        count-=1
for i in range(0, len(n)):
    if n[i]==me:
        count1+=1
if count1>len(n)//2:
    print(me)
else:
    print("BC")

