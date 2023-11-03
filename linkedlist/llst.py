class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedlist():
    def __init__(self):
        self.head=None
        
    def dis(self):
        d=self.head
        while d:
            print(d.data,end="->")
            d=d.next
        print()
        
    def atbeg(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
            return
        new_node.next=self.head
        self.head=new_node
        
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
        
    def atend(self,new_data):
        new_node=node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        
    def delbeg(self):
        if self.head==None:
            print("there is node to delete")
            return
        self.head=self.head.next
        
    
    def delpos(self, position):
        if position < 1:
            return
        current = self.head
        for i in range(position-1):
            current = current.next
        if not current:
            print("Position exceeds the length")
            return

        if current.next:
            current.next = current.next.next
        else:
            print("Position exceeds the length")
            
    def delend(self):
        if self.head is None:
            return
        last = self.head
        if last.next is None:  # Check if there's only one node
            self.head = None    # If so, set the head to None
            return
        while last.next.next:
            last = last.next
        last.next = None

        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev    
        
    
        
       
        
l=linkedlist()
l.atbeg(1)
l.atend(2)
l.atend(3)
l.atbeg(4)
l.atpos(5,3)
l.dis()
l.reverse()
l.dis()
l.delbeg()
l.delend()
l.dis()
l.delpos(1)
l.dis()
