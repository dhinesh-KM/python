class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class tree:
    def createnode(self,new):
        return node(new)

    def insert(self,node,data):
        if node == None:
            return self.createnode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    
    def preorder_traverse(self,node):
        if node:
            print(node.data,end=" ")
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)
            
    def inorder_traverse(self,node):
        if node:
            self.inorder_traverse(node.left)
            print(node.data,end=' ')
            self.inorder_traverse(node.right)
    
    def postorder_traverse(self,node):
        if node:
            self.inorder_traverse(node.left)
            self.inorder_traverse(node.right)
            print(node.data,end=' ')
            
    def levelorder_traverse(self,node):
        if node:
            print(node.data,end=' ')
            
            
        

t=tree()
l=[2,10,7,15,12,20,30,6,8]
n=len(l)
a=int(input("enter first value:"))
root=t.createnode(a)
for i in l:
    t.insert(root,i)    
t.preorder_traverse(root)
print()
t.inorder_traverse(root)
t.insert(root,3)