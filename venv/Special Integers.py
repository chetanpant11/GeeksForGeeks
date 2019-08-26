A=list(map(int, input().split()))
B=int(input())
n = len(A)
l = 0
h = n
k = 0

while l <= h:
    m = (l + h) // 2
    sum = 0
    for i in range(0, m):
        sum = sum + A[i]
    if sum > B:
        h = m - 1

    for i in range(m, n):
        sum = sum + A[i] - A[i - m]
        if sum > B:
            h = m - 1
            break
    if sum <= B:
        k = m
        l = m + 1

print(k)