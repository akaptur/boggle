"""
Generate a graph of the boggle board
"""

def make_board(letters, board_dimensions):
	"""
	Returns a 2D matrix of the n x n board that is padded with None 
	and returns a dictionary of the positioning of the letters on the board 
	"""
	board = [[None for i in xrange(board_dimensions+2)] for i in xrange(board_dimensions+2)]
	position = {}
	x = 0
	y = 0
	for letter in letters:
		position[x, y] = letter.lower()
		y += 1
		if y >= board_dimensions:
			y = 0
			x += 1

	for (x, y) in position:
		board[x+1][y+1] = position[(x,y)]
	return board, position

def get_neighbors(current_position, mapping):
	"""
	Returns a list of the reachable neighbors of a certain node at position (x,y) on the board
	"""
	neighbors = []
	for other_position in mapping:
		if reachable(current_position, other_position):
			neighbors.append((mapping[other_position], other_position))
	return neighbors

def reachable(current_position, other_position):
	x1, y1 = current_position
	x2, y2 = other_position
	x_dist = abs(x2-x1)
	y_dist = abs(y2-y1)
	x_reachable = (x_dist <= 1)
	y_reachable = (y_dist <= 1)
	return x_reachable and y_reachable and (x_dist + y_dist > 0)


def make_graph(board, mapping):
	"""
	Returns a dictionary with the nodes as the keys and the reachable neighbors
	as the values
	"""
	graph = {}
	graph['*'] = [(mapping[node], node) for node in mapping] # wildcard node - can start at any point on board
	for node in mapping:
		graph[(mapping[node], node)] = get_neighbors(node, mapping)
	return graph	

