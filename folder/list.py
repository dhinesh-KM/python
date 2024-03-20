n=int(input("enter n value:"))
l=[] 
a=0
for i in range(n):
    a=int(input(f"enter element {i}:"))
    l.append(a)
print(l) 
#ascending sort
l.sort()
print("ascending sort:",l)

#descending sort
l.sort(reverse=True)
print("descending sort:",l)

#insertion
l.insert(2,100)
print("insertion:",l)

#accessing list
print("accessing:",l[1])

#changing list
l[2]=10000

#pack & unpack list
x,y,*z,a=l
print("unpack:",x,"pack:",z)

#removing list
l.pop(3)

