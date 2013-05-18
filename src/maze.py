

def Is_maze_solvable(maze):
	
	""" given a maze as matrix tell whether this maze Is solvable """
	"""@param maze """
	"""@return true if solvable"""

	start_x=-1
	start_y=-1
	"""

	if x =='S' for x in range(len(y)) for y in range(len(maze)) :
		start_x=x
		start_y=y
	else :
		return False
	"""
	for y in range(len(maze)):
		for x in range(len(maze[0])):
			if maze[x][y]=='S':
				start_x=x
				start_y=y
				return exploreMaze(maze,start_x,start_y)
	if start_x==-1:
		return False

def printmaze(maze):
	#print x for x in range(len(y)) for y in range(len(maze)):
	for y in range(len(maze)):
		print 
		for x in range(len(maze[0])):
			print maze[x][y],
			print '\t'
	return

def exploreMaze(maze,x,y):
	""" explore Maze going DFS"""

	# if we are moving from maze 
	if x >len(maze[0])-1 or y >len(maze)-1 or x <0 or y <0:
		return False

	# if can not continue this path
	if maze[x][y]=='*':
		return False
	# if we have reachced the destination

	if maze[x][y]=='E':
		return True

	if maze[x][y]=='':
		maze[x][y]='*'

	if exploreMaze(maze,x,y-1) :
		return True  # search up
	if exploreMaze(maze,x,y+1) : 
		return True  #search down
	if exploreMaze(maze,x-1,y) :
		return True  # search left
	if exploreMaze(maze,x+1,y) :
		return True  # search right

	#None of the options worked, so we can't solve the maze
	return False

if __name__ == "__main__":

	arr = [["S", "*","*"],["", "", ""],["*", "", "E"]]
	arr1 = [["S", "*","*","*"],
			["*", "*", "",""],
			["", "", "",""],
			["*", "", "E",""]]
	#print arr
	printmaze(arr)
	print Is_maze_solvable(arr1)

