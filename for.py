n=int(input("enter a number:"))
b=-1
p=n+(n-1)
for i in range(n):
    a=1
    b+=2
    for x in range(i,n):
        print(' ',end=' ')
    for y in range(b):
        print(a,end=' ')
        a+=1
    print()
for z in range(n):
    v=1
    p-=2
    for q in range(z+2):
        print(' ',end=' ')
    for e in range(p):
        print(v,end=' ')
        v+=1
    print()
    
        
    