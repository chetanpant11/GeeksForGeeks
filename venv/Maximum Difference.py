n = list(map(int, input().split()))
b = int(input())
n.sort()
arrSum=sum(n)
sum1=0
for i in range(0,b):
    sum1+=n[i]

sum2=0
for j in range(len(n)-1,(len(n)-1)-b,-1):
    sum2+=n[j]
# print(sum1)
# print(sum2)
# print(arrSum)

a1=arrSum-sum1
b1=arrSum-sum2
print(max(abs(a1-sum1),abs(b1-sum2)))



