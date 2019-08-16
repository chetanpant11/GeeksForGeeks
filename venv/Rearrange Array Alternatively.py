a = input()
n = list(input().split()) 
i = 0
j = len(n) - 1
while i <= j:
    if i == j:
        print(n[j], end="")
        break
    print(n[j], end=" ")
    j -= 1
    print(n[i], end=" ")
    i += 1
print()
#Here We Didn't Use => list(map(int,input().split()))
#because map takes more space in int where as in string
#the space is less(int take 4 byte And string char take 1 byte)