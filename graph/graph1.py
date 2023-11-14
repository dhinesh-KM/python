from collections import deque
class graph:
    def __init__(self,vertex):
        self.vertex=vertex
        self.a_list={}
        print(self.a_list)
    def addedge(self,x,y):
        if x not in self.a_list:
            self.a_list[x] = []
        if y not in self.a_list:
            self.a_list[y] = []

        self.a_list[x].append(y)
        self.a_list[y].append(x)
        
    def print_a_list(self):
        for i in self.a_list.items():
            print(i)
            
    def bfs(self,start_vertex):
        visited=set()
        queue=deque()
        queue.append(start_vertex)
        
        while queue:
            current_vertex=queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex,end=" ")
            for i in self.a_list[current_vertex]:
                if i not in visited:
                    queue.append(i)
               
    def dfs1(self,start_vertex,visited): 
        visited.add(start_vertex)
        print(start_vertex,end=' ')
        for i in self.a_list[start_vertex]:
            if i not in visited:
                self.dfs1(i,visited)
        
        
    def dfs(self,start_vertex):
        visited=set()
        self.dfs1(start_vertex,visited)
        
            
        
                
            
            