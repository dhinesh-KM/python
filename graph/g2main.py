from graph2 import graph

g = graph(8)
#exit()


g.addedge('a','b')
g.addedge('c','d')
g.addedge('a','e')
g.addedge('e','f')
g.addedge('a','g')
g.addedge('b','f')
g.addedge('b','c')
g.addedge('b','h')
g.addedge('b','g')
g.addedge('c','h')
g.addedge('e','d')


g.print_a_matrix()
print()
g.bfs('b')