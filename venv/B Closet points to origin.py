import math
A = [[1, 3],
     [-2, 2]]
# dict={i:0 for i in range(0,len(A))}
# for i in
dict={}
for i in range(0,len(A)):
    a=pow(A[i][0],2)
    b=pow(A[i][1],2)
    c=math.sqrt(a+b)
    dict[c]=[A[i][0],A[i][1]]
for i in sorted(dict):
    print(dict[i])

print(dict)