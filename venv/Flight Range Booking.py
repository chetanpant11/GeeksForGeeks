b = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
a=[0 for i in range(0,5)]
for i in range(0,3):
    a[b[i][0]-1] += b[i][2]
    if b[i][1]!=len(a):
        a[b[i][1]] += -b[i][2]

for i in range(1,len(a)):
    a[i]+=a[i-1]
print(a)

