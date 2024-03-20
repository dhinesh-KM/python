from multipledispatch import dispatch
 
@dispatch(int,int)
def mul(a,b):
    print("product=",a*b)
    
@dispatch(float,float,float)
def mul(a,b,c):
    print("product=",a*b*c)
    
mul(5,6)
mul(9.8,5.6,4.3)