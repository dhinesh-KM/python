from graph1 import graph

    
q = graph(8)
#exit()

q.addedge('a','b')
q.addedge('c','d')
q.addedge('a','e')
q.addedge('e','f')
q.addedge('a','g')
q.addedge('b','f')
q.addedge('b','c')
q.addedge('b','h')
q.addedge('b','g')
q.addedge('c','h')
q.addedge('e','d')


q.print_a_list()
q.bfs('a')
print()
q.dfs('a')
print()