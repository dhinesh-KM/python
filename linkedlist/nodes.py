class days:
    def __init__(self,dv):
        self.dv=dv
        self.nv=None
n1=days("mon")
n2=days("tue")
n3=days("wed")
n4=days("thrs")
n1.nv=n3
n3.nv=n2
n2.nv=n4

d=n1
while d:
    print(d.dv)
    d=d.nv
    

