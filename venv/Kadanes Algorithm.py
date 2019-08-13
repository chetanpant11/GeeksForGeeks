a=int(input())
k=0
for i in range(a):
    b=int(input())
    arr = list(map(int, input().strip().split()))
    max_value=0
    max_so_far=0
    for j in range(b):
        max_value += arr[j]
        if max_value<0:
            max_value = 0
        if max_so_far<max_value:
            max_so_far = max_value
    if max_so_far>0:
        print(max_so_far)
    else:
        print(max(arr))



















# def sum1(a):
#     b=sum(a)
#     return b
#
# a=[1,2,3,4,5,5,6,7]
# c = sum1(a)
# print(c)