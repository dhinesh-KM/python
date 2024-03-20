class animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
        print("first executed")
    def dis(e):
        print("name:",e.name,"\ncolor:",e.color)
        
class dog(animal):
    def __init__(s,name,color,breed,age):
        super().__init__(name,color)
        s.breed=breed
        s.age=age
    def dis(e):
        return e.breed,e.name,e.color,e.age
    
class lion(animal):
    def __init__(self,name,color,gender,age):
        animal.__init__(self,name,color)
        self.gender=gender
        self.age=age
        
    def dis(f):
        print("name:",f.name,"gender:",f.gender,"age:",f.age,"color:",f.color)
        
class dl(dog,lion):
    def __init__(s,name,color,gender,age,breed,horn,):
        super().__init__(name,color,gender,age)
        s.breed=breed
        s.horn=horn
    def dis(f):
        print("name:",f.name,"gender:",f.gender,"age:",f.age,"color:",f.color,"breed:",f.breed,"horn:",f.horn)
    

s=dl("jack","red","male",23,"labroder",4)
s.dis()


