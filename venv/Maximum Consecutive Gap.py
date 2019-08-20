n=list(map(int, input().split()))
n.sort()
max=0
for i in range(0, len(n)-1):
    j=i+1
    if (n[j]-n[i])>max:
        max=n[j]-n[i]
    else:
        continue
if len(n)<2:
    return 0

