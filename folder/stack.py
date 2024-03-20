from collections import deque

class stack:
    def __init__(self):
        self.stack = deque()
        
    def isempty(self):
        if len(self.stack)==0:
            print("stack is empty")  
        else:
            print("stack is not empty")
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        self.stack.pop()
        
    def size(self):
        print("length",len(self.stack))
           
    def dis(self):
        for i in self.stack:
            print(i,end=" ")
        print()
    
    def top(self):
        print("top element",self.stack[-1])
        
    def bottom(self):
        print("bottom element:",self.stack[0])        
    
        
        
        
s=stack()
#n=int(input("enter n value:"))
#for i in range(n):
#    a=int(input(f"enter {i} element:" ))
#    s.push(a)
s.push(0) 
s.push(1)
s.push(2)
s.push(3)   

s.dis()

s.pop()
s.pop()

s.dis()

s.isempty()
s.size()
s.dis()
s.top()
s.bottom()