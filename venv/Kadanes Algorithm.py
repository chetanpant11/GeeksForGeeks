t=int(input())
for i in range(0, t):
    c=int(input())
    n=list(map(int, input().split()))
    count_max=0
    flag=False
    max_count=0
    for i in range(0,c):
        count_max += n[i]
        if count_max<0:
            count_max=0
        if max_count<count_max:
            max_count=count_max

    if max_count==0:
        print(max(n))
    else:
        print(max_count)