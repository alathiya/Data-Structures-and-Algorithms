import math 


def bellmanford(edges, V): 

  parent = []
  cost = []

  for i in range(len(V)): #O(V)
    parent.append(0)

  parent[0] = -1

  for i in range(len(V)): #O(V)
    if i==0: 
      cost.append(0)
    else:  
      cost.append(math.inf)

   
  for i in range(len(V)-1): #O(V)
      #bellmanford(edges, V)

      for j in edges: #O(E)

        #relaxation
        if cost[j[0]] + j[2] < cost[j[1]]:
           cost[j[1]] = cost[j[0]] + j[2]
           parent[j[1]] = parent[j[0]]
           updated_flag = True

      if not updated_flag: 
        break    

  if i == len(V)-2:
    updated_flag = False

    for j in edges: 

        #relaxation
        if cost[j[0]] + j[2] < cost[j[1]]:
           cost[j[1]] = cost[j[0]] + j[2]
           parent[j[1]] = parent[j[0]]
           updated_flag = True

    if updated_flag: 
      print("Graph has negative weighted cycle")
    else:   
      print("Cost of each vertex", cost)
  else: 
    print("Cost of each vertex", cost)              

edges = []

#Test Case 1
edges.append((0,1,6))
edges.append((0,2,7))
edges.append((2,3,9))
edges.append((3,4,7))
edges.append((4,1,-2))
edges.append((1,4,5))
edges.append((2,4,-3))
edges.append((1,2,8))
edges.append((1,3,-4))

V = [0,1,2,3,4]

#Test Case 2
#edges.append((0,1,2))
#edges.append((1,2,3))
#edges.append((2,0,-7))

#V = [0,1,2]

bellmanford(edges, V)
print("Time Complexity O(V)+O(E)")