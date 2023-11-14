from collections import deque
class graph:
    def __init__(self,n_vertex):
        self.vertex={}
        self.a_matrix= [[0] * n_vertex for i in range(n_vertex)]
        self.n_vertex=n_vertex
        #print(self.a_matrix)
        
    
    def add_vertex(self, label):
        if label not in self.vertex:
            index = len(self.vertex)
            self.vertex[label] = index
    
    def addedge(self, a, b):
        if a not in self.vertex:
            self.add_vertex(a)
        if b not in self.vertex:
            self.add_vertex(b)

        index_a = self.vertex[a]
        index_b = self.vertex[b]

        self.a_matrix[index_a][index_b] = 1
        self.a_matrix[index_b][index_a] = 1 
        
    def bfs(self,start_vertex):
        visited=[False]*self.n_vertex
        queue=deque()
        
        index_s=self.vertex[start_vertex]
        queue.append(index_s)
        visited[index_s]=True
        
       
        while queue:
            current_vertex=queue.popleft()
            print(list (self.vertex.keys()) [list(self.vertex.values()).index(current_vertex)], end=" ")
            
            for i in range(self.n_vertex):
                if  not visited[i] and self.a_matrix[current_vertex][i]==1:
                    queue.append(i)
                    visited[i]=True
                    
    def dfs(self,start_vertex):
        visited=set()
        self.dfs1(start_vertex,visited)
        
    def dfs1(self,start_vertex,visited): 
        index_s=self.vertex[start_vertex]
        visited.add(index_s)
        print(start_vertex,end=' ')
        for i in self.a_list[start_vertex]:
            if i not in visited:
                self.dfs1(i,visited)
             
    
        
    def print_a_matrix(self):
        for i in range(self.n_vertex):
            for j in range(self.n_vertex):
                #print(list (self.vertex.keys()) )
                print(self.a_matrix[i][j],end=" ")
            print()