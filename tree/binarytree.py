class node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class tree: 
    def createnode(self,new):
        return node(new)
    
    def minvalue(self,node):
        c=node
        while c.left is not None:
            c=c.left
        return c.data
        
    def maxvalue(self,node):
        c=node
        while c.right is not None:
            c=c.right
        return c.data
    
    def search(self,node,data):
        
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search(node.left,data)
        else:
            return self.search(node.right,data)
                 
    def insert(self,node,data):
        if node == None:
            return self.createnode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
    
    def delete(self,node,data):
        if node == None:
            print("nothing to delete,list is empty")
        if data < node.data:
            node.left=self.delete(node.left,data)
        elif data > node.data:
            node.right=self.delete(node.right,data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #inorder predescesssor
            node.data = self.maxvalue(node.left)
        
            node.left = self.delete(node.left, node.data)

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
            self.postorder_traverse(node.left)
            self.postorder_traverse(node.right)
            print(node.data,end=' ')
            
    def levelorder_traverse(self,node):
        if node is None:
            print("tree is empty")
            return
        q=[]
        q.append(node)
        while len(q)!=0:
            node=q.pop(0)
            print(node.data,end=' ')
            
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

t=tree()
l=[5,2,10,7,15,12,20,30,6,8]
n=len(l)
root=t.createnode(5)
for i in range(1,n):
    t.insert(root,l[i]) 
t.insert(root,100)   
t.preorder_traverse(root)
print()
t.inorder_traverse(root)
print()
t.insert(root,3)
t.levelorder_traverse(root)
print()
t.postorder_traverse(root)
print()
data=100
k=t.search(root,data)
print(k)
if k:
    print(f"search element  {data} exist")
else:
    print(f"search element  {data} not exist")
t.delete(root,5)
t.levelorder_traverse(root)
print()
print(t.minvalue(root))
print(t.maxvalue(root))

