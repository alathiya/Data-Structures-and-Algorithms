from helper import get_path, offsets, is_legal_pos, read_maze
from queue_ll import Queue

def bfs(maze, start, goal): 

	q = Queue()
	q.enqueue(start)
	predecessors = {start: None}

	while not q.is_empty(): 
		
		current_cell = q.dequeue()

		if current_cell == goal: 
			return get_path(predecessors, start, goal)
		
		for directions in ["up","right","down","left"]: 
			row_offset, col_offset = offsets[directions] 
			neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset)
			
			if is_legal_pos(maze, neighbor) and neighbor not in predecessors: 
				q.enqueue(neighbor)
				predecessors[neighbor] = current_cell
				
	return None

if __name__ == "__main__": 

	#Test1
	#maze = [[0] * 3 for row in range(3)]
	#start = (0,0)
	#goal = (2,2)

	#result = bfs(maze, start, goal)
	#print(result)
	
	#assert result == [(0,0), (1,0), (1,1), (1,2), (2,2)]
	
	maze = [[''] * 4 for row in range(4)]
	
	maze[0][2] = '*'
	maze[2][1] = '*'
	maze[2][3] = '*'

	for row in maze:
		print(row)

	start = (0,0)
	goal = (3,3)

	result = bfs(maze, start, goal)
	
	print(result)
	
	assert result == [(0,0), (1,0), (1,1), (1,2), (2,2)]
		