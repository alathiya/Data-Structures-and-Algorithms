from collections import defaultdict 

class Graph: 
  def __init__(self, vertices): 
    self.V  = vertices
    self.graph = defaultdict(list)
    self.stack = []

  def add_edge(self, u, v): 
    self.graph[u].append(v)

  def topologicalsortutil(self, node, visited, stack):

    visited[node] = True

    for i in self.graph[node]: 
      if visited[i] == False: 
        self.topologicalsortutil(i, visited, stack)

    self.stack.append(node)    

g = Graph(7)
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('E', 'C')
g.add_edge('D', 'F')
g.add_edge('C', 'G')

stack = []
visited = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False, 'G': False}

for key in visited:
  if visited[key] == False: 
    g.topologicalsortutil(key, visited, stack)

print(g.stack[::-1])