class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class circular_sl:
    def __init__(self):
        self.head=self.tail=None
        
    def isempty(self):
        l=self.get_size()
        if l == 0:
            print("the list is empty")
            return
        print("the list is not empty")
    
    def get_size(self):
        if not self.head:
            return 0
        size = 1
        d = self.head
        while d.next != self.head:
            size += 1
            d = d.next
        return size
        #print("length of the list",size)
        
    def dis(self):
        if self.head is None:
            print("empty list")
            return
        d=self.head
        print(d.data,end=' -> ') 
        while d.next != self.head:
            d=d.next
            print(d.data,end=' -> ') 
        print(d.next.data)   
    
    def at_beg(self,data):
        n=node(data)
        if self.head is None:
            self.head=self.tail=n
            n.next=self.head
            return
        n.next=self.head
        self.head=n
        self.tail.next=n
        
    def at_pos(self,pos,data):
        n=node(data)
        if self.head is None:
            self.head=self.tail=n
            n.next=self.head
        else:
            if pos==1:
                self.at_beg(data)
                return     
            temp=self.head
            for i in range(1,pos-1):
                temp=temp.next
            n.next=temp.next
            temp.next=n     
        
    def at_end(self,data):
        n=node(data)
        if self.head == None:
            self.head=self.tail=n
            n.next=self.head
            return
        self.tail.next=n
        self.tail=n 
        n.next=self.head   
    
    def del_0_1(self):
        if self.head is None:
            print("list is empty,no data to delete")
            return    
        elif self.head == self.tail:
            self.head = None
            return
        
    def del_beg(self):
        self.del_0_1()
        temp=self.head
        self.head=temp.next
        self.tail.next=self.head
        temp=None
        
    def del_end(self):
        self.del_0_1()
        temp=self.head
        while temp.next!=self.tail:
            temp=temp.next
        self.tail.next=None
        temp.next=self.head
        self.tail=temp
    
    def del_pos(self,pos):
        self.del_0_1()
        l=self.get_size()
        if pos==1:
            self.del_beg()
        
        elif pos>l:
            print("position exceeds")
            return
        
        temp1=self.head
        temp2=self.head.next
        for i in range(1,pos-1):
            temp1=temp1.next
            temp2=temp2.next
        if temp2.next == self.tail:
            temp1.next=temp2.next
            temp2=None
            self.tail=temp1
            return
        temp1.next=temp2.next
        temp2=None
        
    def reverse(self):     
        if not self.head:
            print("there is no elements in the list to reverse")
        prev=None
        current=self.head
        next=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
            
        self.tail=self.head
        self.head=prev
            
c=circular_sl()
c.at_beg(20)
c.at_beg(10)
c.at_end(30)
c.at_end(40)
c.at_pos(3,50)
c.dis()

c.del_beg()
c.dis()
c.del_end()
c.dis()
print(c.get_size())
c.del_pos(4)
c.dis()
c.reverse()
c.dis()