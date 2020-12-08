from collections import defaultdict
import heapq

class Graph: 

  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v, w): 
    self.graph[u].append((v, int(w)))

def ShortestPath(graph, src, dest):

    h = []

    heapq.heappush(h, (0, src))

    while h!=0:

      curr_cost, currvertex = heapq.heappop(h)

      if currvertex == dest:
        return curr_cost

      for v, edge in graph.graph[currvertex]:

          heapq.heappush(h, (curr_cost+edge, v))


def main():

  g = Graph()
  g.add_edge('A', 'B', 2)
  g.add_edge('A', 'C', 4)
  g.add_edge('B', 'D', 7)
  g.add_edge('B', 'C', 1)
  g.add_edge('C', 'E', 3)
  g.add_edge('E', 'D', 2)
  g.add_edge('D', 'F', 1)
  g.add_edge('E', 'F', 5)

  print("Shortest path from Source node 'A'  to destination node 'F' is {}".format(ShortestPath(g, 'A', 'F')))

if __name__=="__main__":

  main()