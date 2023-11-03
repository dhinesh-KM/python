def fun(n):
    return lambda a,b,c:a*b*c*n
    
    
a=fun(10)
print(a(2,3,4))



