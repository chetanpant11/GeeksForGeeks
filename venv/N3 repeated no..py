n= list(map(int , input().split(" ")))
print(len(n))
me=n[0]
count=0
count1=0
me1=0
q=0
count2=0
for i in range(0, len(n)):
    if me==n[i]:
        continue
    else:
        me1=n[i]
        break
for i in range(0, len(n)):
    if me==n[i]:
        count+=1
    elif me1==n[i]:
        count1+=1
    elif count==0 and n[i]!=me1:
        me=n[i]
    elif count1==0 and n[i]!=me:
        me1=n[i]
    else:
        count-=1
        count1-=1
if count<count1:
    q=me1
elif count>count1:
    q=me
elif count1==count:
    q=me
for i in range(0, len(n)):
    if n[i]==q:
        count2+=1
if count2>len(n)//3:
    print(q)
else:
    print(-1)
