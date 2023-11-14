class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        self.height=0

class avl_tree:
    def createnode(self,new):
        return Node(new)

    def getheight(self,node):
        if node is None:
            return -1
        return node.height
    
    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left=self.insert(node.left,data)
        elif data > node.data:
            node.right=self.insert(node.right,data)
        else:
            return node
        
        node.height=1+max(self.getheight(node.left),self.getheight(node.right))
        #if data == 40:
        #     print("height of ",node.data,"is",node.height)
            
        bf=self._bal_factor(node)
        #ll 
        if bf > 1 and data < node.left.data:
            return self._rightrotate(node)
        #lr
        if bf > 1 and data > node.left.data:
            node.left = self._leftrotate(node.left)
            return self._rightrotate(node)
        #rr
        if bf < -1 and data > node.right.data:
            return self._leftrotate(node)
        #rl
        if bf < -1 and data < node.right.data:
            node.right = self._rightrotate(node.right)
            return self._leftrotate(node)
        return node
    
    def _bal_factor(self,node):
        return self.getheight(node.left)-self.getheight(node.right)
    
    def _rightrotate(self,z):
        y=z.left
        t3=y.right
        
        y.right=z
        z.left=t3
        
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))

        return y
        
    def _leftrotate(self,z):
        y=z.right
        t3=y.left
    
        y.left=z
        z.right=t3
        
        z.height=1+max(self.getheight(z.left),self.getheight(z.right))
        y.height=1+max(self.getheight(y.left),self.getheight(y.right))

        return y
    def create_bst(self):
        node = None
        while True:
            u_i = input("Enter a number to insert into the BST (or 'q' to quit): ")
            if u_i.lower() == 'q':
                break
            data = int(u_i)
            node = self.insert(node, data)
        return node
    
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
                
t=avl_tree()
root=t.create_bst()
t.levelorder_traverse(root)
print()