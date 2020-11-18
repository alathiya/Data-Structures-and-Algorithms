from helper import get_path, offsets, is_legal_pos, read_maze
from stack import Stack

def dfs(maze, start, goal): 

	stack = Stack()
	stack.push(start)
	predecessors = {start: None}

	while not stack.is_empty(): 
		#print(stack)
		current_cell = stack.pop()

		if current_cell == goal: 
			return get_path(predecessors, start, goal)
		
		for directions in ["up","right","down","left"]: 
			row_offset, col_offset = offsets[directions] 
			neighbor = (current_cell[0]+row_offset, current_cell[1]+col_offset)
			
			if is_legal_pos(maze, neighbor) and neighbor not in predecessors: 
				stack.push(neighbor)
				#print(stack)
				predecessors[neighbor] = current_cell
				
	return None

if __name__ == "__main__": 

	#Test1
	maze = [[0] * 4 for row in range(4)]
	start = (0,0)
	goal = (3,3)
	print(maze)	
	result = dfs(maze, start, goal)

	#assert result == [(0,0), (1,0), (2,0), (3,0), (3,1), (3,2), (3,3)]
	
	print(result)
	