class A:
    c_variable="class variable"
    def instance_method(self,n):
        self.i_variable=n
        print("instance method")
        print("instance variable",self.i_variable)
        
    @classmethod
    def class_method(cls):
        return "class method"
        return c_variable

    @staticmethod
    def stat_method():
        c_variable=50
        print("static method","static variable=",c_variable)
        
a=A()
a.instance_method(10)
print(A.class_method(),A.c_variable)
A.stat_method()