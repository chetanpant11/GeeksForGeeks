t = int(input())
for i in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    a = set(arr)
    b = len(a)
    c = arr[-1]
    count = 0
    for i in range(0, b):
        for j in range(i+1, b):
            s = arr[i]+arr[j]
            if s > c:
                break
            if s in a:
                count += 1
    if count > 0:
        print(count)
    else:
        print(-1)