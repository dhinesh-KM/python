class A:
    def __init__(self,name,age,dob):
       self._name=name
       self._age=age
       self.__dob=dob
    def _display(self):
        print(self._name,self._age,self.__dob)
    def __dis(self):
        print(self._name,self._age,self.__dob)
    def dip(self):
        self.__dis()        
class B(A):
    def __init__(self,name,age,dob):
        A.__init__(self,name,age,dob)
    def func(self):
        self._display()
        self.dip()
        
        
q=A("tp",3,"12/09/2003")
q._display()
q.dip()

a=B("vijay",25,"11/11/2002")
a.func()

        
        
        
        
        