import heapq 

class PriorityQueue: 

    def __init__(self): 
      self.element = []
    
    def is_empty(self):
      return not self.element
    
    def put(self, item, priority):
      heapq.heappush(self.element, (priority, item))

    def get(self): 
      return heapq.heappop(self.element)[1]       


def is_legal_move(N, M, neighor): 

  if 0<=neighor[0]<N and 0<=neighor[1]<M: 
    return True

def get_offset(direction): 

   x = [2, -2, -2, 2, 1, -1, -1, 1]
   y = [1, 1, -1, -1, 2, -2, 2, -2]

   return (x[direction], y[direction])         

def heuristic(start, goal): 
  x1, y1 = start
  x2, y2 = goal

  return abs(x2-x1) + abs(y2-y1)

def minpath(predecessor, start, goal):

  current = goal
  count = 0 

  while current != start: 
    count = count + 1
    current = predecessor[current]

  return count     

def moves(N, M, start, goal): 

    pq = PriorityQueue()
    pq.put(start, 0)
    predecessor = {start: 0}
    g_value = {start: 0}

    while not pq.is_empty(): 

      current_cell = pq.get()

      if current_cell == goal:
        return minpath(predecessor, start, goal)

      for i in range(8):

        offset_row, offset_col = get_offset(i)
        neighor = (current_cell[0] + offset_row, current_cell[1] + offset_col)

        if is_legal_move(N, M, neighor) and neighor not in g_value:
          new_cost = g_value[current_cell] + 1
          g_value[neighor] = new_cost
          f_value = new_cost + heuristic(neighor, goal)
          pq.put(neighor, f_value)
          predecessor[neighor] = current_cell

    return -1 

def main(): 
    
    N = 4
    M = 7

    s1 = 2
    s2 = 6
    d1 = 2
    d2 = 4

    start = (s1, s2)
    goal =  (d1, d2)
    
    
    print(moves(N, M, start, goal))
    

main()