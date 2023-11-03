
class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class double:
    def __init__(self):
        self.head=self.tail=None
        
    def isempty(self):
        if (self.head == None): return True
        return False
        
    def dis(self):
        if self.isempty():
            print('List is Empty')
            return
        last = self.head
        while last:
            print(last.data,end = ' ')
            last = last.next
        print()
    
    def atbeg(self,new):
        new_n=node(new)
        if self.head is None:
            self.head=self.tail=new_n
            return
        new_n.next=self.head
        self.head.prev=new_n
        self.head=new_n
    
    def atend(self,new):
        new_node=node(new)
        if self.head is None:
            self.head=self.tail=new_node
            return
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node
    
    def atpos(self, data, position):
        new_node = node(data)
        if position <= 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            if not current:
                print("Position out of bounds. Inserting at the end.")
                return
            new_node.next = current.next
            current.next = new_node
    
    def delbeg(self):
        if self.head is None:
            return  
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        
    def delpos(self, position):
        if position < 1:
            return
        current = self.head
    
        for i in range(position):
            current = current.next
        if current:
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev
            if current == self.head:
                self.head = current.next
            if current == self.tail:
                self.tail = current.prev

    def delend(self):
        if self.tail is None:
            return  
        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail.prev

    def reverse(self):
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            if not current.prev:  
                self.head = current
            current = current.prev 
        self.head, self.tail = self.tail, self.head

    


    
d=double()
d.atbeg(2)
d.atbeg(3)
d.atend(8)
d.atpos(4,2)
d.dis()
d.reverse()
d.dis()
d.delbeg()
d.delend()
d.delpos(2)
d.dis()