from collections import UserDict
class dict(UserDict):
    def pop(s,a=None):
        raise RuntimeError("updation not allowed")
d=dict({'a':1,'b':2,'c':3})
print(d)
d.pop(1)

    
