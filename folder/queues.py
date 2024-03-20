from collections import deque
class queue:
    def __init__(self,msize):
        self.queue = deque()
        self.msize=msize
        
    def isempty(self):
        return len(self.queue)==0
        
    def push(self,data):
        if len(self.queue)< self.msize:
            self.queue.append(data) 
        else:
            print("queue is already full,no item can be pushed")
        
    def pop(self):
        if len(self.queue)>0:
            self.queue.popleft()
        else:
            print("queue is empty,no item can be popped")
        
    def size(self):
        print("length",len(self.queue))
           
    def dis(self):
        for i in self.queue:
            print(i,end=" ")
        print()
        
    def full(self):
        return len(self.queue)>=self.msize
    
    def front(self):
        if not self.isempty():
            print("front element:",self.queue[0])
        else:
            print("Queue is empty. Cannot retrieve the front element.")
            return None
        
    def rear(self):
        if not self.isempty():
            print("rear element:",self.queue[-1])
        else:
            print("Queue is empty. Cannot retrieve the rear element.")
            return None
       
        
n=int(input("enter n value:"))
s=queue(n)
for i in range(5):
    if not s.full():
        a=int(input(f"enter {i} element:" ))
        s.push(a)
    else:
        print("Queue is full. Stopping the iteration.")
        break
s.push(4)

s.dis()
s.pop()


s.dis()

print("queue is empty") if s.isempty()==True else print("queue is not empty")
s.size()
s.dis()

#s.pop()
#s.pop()
s.front()
s.rear()    
