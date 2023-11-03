l = [1, 1, 1, 64, 23, 64, 22, 22, 22,23]
a=[]
n=len(l)
i=0
j=1
k=2
if n%2!=0:
    n-=2
else:
    n-=1
for q in range(0,n):
    if l[i]==l[j]==l[k]:
        d=l[i]
        a.append(d)
    i+=1
    j+=1
    k+=1
print(a)
