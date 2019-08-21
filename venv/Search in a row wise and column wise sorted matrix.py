R=int(input())
C=int(input())
mat = [[int(input()) for x in range (R)] for y in range(R)]
m=int(input())
i=0
j= C-1
while (i!=R-1 and j!=0):
    print("1")
    if mat[i][j]==m:
        print(i,j)
        break
    elif mat[i][j]<m:
        i+=1
        continue
    elif mat[i][j]>m:
        j-=1
        continue