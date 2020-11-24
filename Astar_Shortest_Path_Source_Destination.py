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

  offset = {"up": (-1, 0), 
            "right": (0, 1), 
            "down": (1, 0), 
            "left": (0, -1)}
  
  return offset[direction]         

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

      for directions in ["up", "right", "down", "left"]: 
        offset_row, offset_col = get_offset(directions)
        neighor = (current_cell[0] + offset_row, current_cell[1] + offset_col)

        if is_legal_move(N, M, neighor) and neighor not in g_value:
          new_cost = g_value[current_cell] + 1
          g_value[neighor] = new_cost
          f_value = new_cost + heuristic(start, goal)
          pq.put(neighor, f_value)
          predecessor[neighor] = current_cell

    return None 

def main(): 
    
    N = 7
    M = 13

    s1 = 2
    s2 = 8
    d1 = 3
    d2 = 4

    start = (s1, s2)
    goal =  (d1, d2)
    
    #chess_maze = [[0] * M for row in range(N)]
    
    return moves(N, M, start, goal)
    

main()