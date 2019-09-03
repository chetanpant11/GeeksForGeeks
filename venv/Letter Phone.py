def dic(n,dict,l,i,temp):
    if i>len(n)-1:
        l.append("".join(temp))
        return

    save=dict[n[i]]
    for j in range(0, len(save)):
        temp.append(save[j])
        dic(n,dict,l,i+1,temp)
        temp.pop()


n=str(input())

print(len(n))
dict={'1':"1",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz",'0':"0"}

l=[]
i=0
temp=[]
dic(n,dict,l,i,temp)
print(l)