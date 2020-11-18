from helper import get_path, offsets, is_legal_pos, read_maze
from PriorityQueue import PriorityQueue

def heuristic(current, destination):

	x1, x2 = current[0], destination[0]
	y1, y2 =  current[1], destination[1]

	return abs(x2-x1) + abs(y2-y1)

def astar(maze, start, goal): 

	pq = PriorityQueue()
	pq.put(start, 0)
	predecessor = {start: None}
	g_value = {start: 0}
	

	while not pq.is_empty(): 
		
		current_cell = pq.get()

		if current_cell == goal: 
			return get_path(predecessor, start, goal)
		
		for directions in ["up","right","down","left"]: 
			row_offset, col_offset = offsets[directions] 
			neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset)
			
			if is_legal_pos(maze, neighbor) and neighbor not in g_value: 
				g_value[neighbor] = g_value[current_cell] + 1
				f_value = g_value[neighbor] + heuristic(neighbor, goal)
				pq.put(neighbor, f_value)
				predecessor[neighbor] = current_cell 
				
	return None

if __name__ == "__main__": 

	#Test1
	maze = [[0] * 4 for row in range(4)]
	start = (0,0)
	goal = (3,3)
	
	maze[0][2] = '*'
	maze[2][1] = '*'
	maze[2][3] = '*'
	
	print(maze)	
	
	result = astar(maze, start, goal)

	#assert result == [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3)]
	
	print(result)
	