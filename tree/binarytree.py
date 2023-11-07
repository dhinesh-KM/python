class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
class bs_tree:
    def insert(self,node,data):
        if node == None:
            return Node(data)
        #k=t.search(node,data)
        #if data == k:
        #    return
        if data < node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node
        
    def create_bst(self):
        node = None
        while True:
            u_i = input("Enter a number to insert into the BST (or 'q' to quit): ")
            if u_i.lower() == 'q':
                break
            #try:
            data = int(u_i)
            node = self.insert(node, data)
            #except ValueError:
             #   print("Invalid input. Please enter a valid number or 'q' to quit.")
        return node
    
    def minvalue(self,node):
        if node is None:
            print("There is no minimum value in list, because it is empty")
            return
        c=node
        while c.left is not None:
            c=c.left
        return c.data
        
    def maxvalue(self,node):
        if node is None:
            print("There is no minimum value in list, because it is empty")
            return
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
                 
    
    def delete(self,node,data):
        if node is None:
            print("nothing to delete,list is empty")
            return
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

t=bs_tree()
root=t.create_bst()
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
#print(k)
if k:
    print(f"search element  {data} exist")
else:
    print(f"search element  {data} not exist")
    
print(t.minvalue(root))
print(t.maxvalue(root))

t.delete(root,5)
t.levelorder_traverse(root)
