import sys

INFINITY = sys.maxint
INFINITY = 401

# def permute(l):
# 	if l == []:
# 		return []

# 	permutations = []

# 	for i in xrange(len(l)):
# 		e = l[i]
# 		permutation_less_e = permute(l[:i] + l[i+1:])

# 		for perm in permutation_less_e:
# 			permutations.append([e] + perm)

# 	return permutations

def my_permute(l, stack=[]):
	if l == []:
		print stack
		return

	for i in xrange(len(l)):
		e = l[i]
		permutation_less_e = l[:i] + l[i+1:]

		stack.append(e)
		my_permute(permutation_less_e, stack)
		stack.pop()


# A=[['X', ' ', 'X'],['X', ' ', ' '],[' ', 'X', 'X']]
# B=[['X', ' ', 'X'], [' ', ' ', ' '], ['X', ' ', ' '],[' ', 'X', 'X']]
# C=[['X', 'X', 'X'],
#    ['X', ' ', ' '],
#    [' ', 'X', 'X']]
# from misc import enum_comps
# enum_comps(A)
# enum_comps(B)
# enum_comps(C)


def enum_comps(graph):
    counter = 0

    marked_row = [False] * len(graph[0])
    marked = [marked_row] * len(graph)
    
    for i in xrange(len(graph)):
        for j in xrange(len(graph[0])):
            if marked[i][j]:
                continue
            if graph[i][j] == 'X':
                counter += 1
                marked = mark_component(i, j, graph, marked)
                
    return counter
    
def mark_component(r, c, graph, marked):
	if not (0 <= r < len(graph) and 0 <= c < len(graph[0])):
		return marked

	if marked[r][c]:
		return marked

	if graph[r][c] == ' ':
		return marked

	marked[r][c] = True

	marked = mark_component(r-1, c, graph, marked)
	marked = mark_component(r+1, c, graph, marked)
	marked = mark_component(r, c-1, graph, marked)
	marked = mark_component(r, c+1, graph, marked)

	return marked


def answer(l):
    l = sorted(l)
    triples = 0
    
    divisors = [0] * len(l)
    
    for i in xrange(len(l)):
        for j in xrange(i):
            if l[i] % l[j] == 0:
                divisors[i] += divisors[j]+1
        triples += (divisors[i])/2
    
    print divisors
    return triples


# from misc import *
# l1=[1,2,3,4,5,6]
# l2=[1,1,1]
# l3=[1,1]
# l4=[3,4,6,8,12,24]
# answer(l1)
# answer(l2)
# answer(l3)
# answer(l4)


def answer_2(l):
    l = sorted(l)
    triples = 0
    divisors = {}
    
    for i in xrange(len(l)):
        for j in xrange(i):
            if l[i] % l[j] == 0:
            	i_divisors = divisors.setdefault(i, [])
                i_divisors.append(j)
    
    for i in xrange(len(l)):
    	for divisor in divisors.get(i, []):
    		triples += len(divisors.get(divisor, []))

    print divisors
    return triples

# from misc import *
# matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
# maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
# answer(maze=matrix)
# answer(maze=maze)

def print_matrix(matrix):
	for row in matrix:
		for e in row:
			print e,
		print
	print

# def Dijkstra(grid):
# 	marked_row = [False] * len(grid[0])
# 	marked = [marked_row] * len(grid)

# 	distances_row = [INFINITY] * len(grid[0])
# 	distances = [distances_row] * len(grid)

# 	initial = (0, 0)
# 	final = (len(grid)-1, len(grid[0])-1)

# 	print
# 	print_matrix(matrix=marked)
# 	print_matrix(matrix=grid)
# 	print_matrix(matrix=distances)
# 	print "-----------------------------------------"

# 	def find_distances(row, col, distance):
# 		# row = current[0]
# 		# col = current[1]
# 		# print "current: %r" % (current)
# 		print "(AAAAAA) row: %s. col: %s" % (row, col)
# 		if not (0 <= row <= final[0] and 0 <= col <= final[1]):
# 			print "(BBBBBB) row: %s. col: %s" % (row, col)
# 			return
# 		if marked[row][col]:
# 			return
# 		print "grid[%r][%r]: %r" % (row, col, grid[row][col])
# 		print "*******************************************"
# 		print_matrix(matrix=grid)
# 		print "*******************************************"
# 		if grid[row][col] == 1:
# 			print "(CCCCCC) row: %s. col: %s" % (row, col)
# 			return
# 		distances[row][col] = min(distances[row][col], distance)
# 		next_distance = distances[row][col]+1
# 		marked[row][col] = True

# 		find_distances(row=row-1, col=col, distance=next_distance)
# 		find_distances(row=row+1, col=col, distance=next_distance)
# 		find_distances(row=row, col=col-1, distance=next_distance)
# 		find_distances(row=row, col=col+1, distance=next_distance)

# 	find_distances(row=0, col=0, distance=0)

# 	print
# 	print_matrix(matrix=distances)
# 	print_matrix(matrix=marked)


# def answer(maze):
# 	unvisited = set()
# 	row_walls = set()
# 	col_walls = set()
# 	distances = {}
# 	lower_bound = len(maze) + len(maze[0]) - 1

# 	for row in xrange(len(maze)):
# 		for col in xrange(len(maze[0])):
# 			distances.setdefault((row, col), INFINITY)
# 			if maze[row][col] == 0:
# 				unvisited.add((row, col))
# 			else:
# 				row_walls.add(row)
# 				col_walls.add(col)

# 	initial = (0, 0)
# 	final = (len(maze)-1, len(maze[0])-1)
# 	distances[initial] = 0

# 	def Dijkstra(unvisited, distances):
# 		current = initial
# 		def neighbors(position):
# 			row = position[0]
# 			col = position[1]

# 			if (row-1, col) in unvisited:
# 				yield (row-1, col)
# 			if (row+1, col) in unvisited:
# 				yield (row+1, col)
# 			if (row, col-1) in unvisited:
# 				yield (row, col-1)
# 			if (row, col+1) in unvisited:
# 				yield (row, col+1)

# 		def next_current():
# 			smallest_distance = INFINITY
# 			smallest_tuple = ()
# 			for x, y in unvisited:
# 				distance = distances.get((x, y), INFINITY)
# 				if distance < smallest_distance:
# 					smallest_distance = distance
# 					smallest_tuple = (x, y)

# 			return smallest_tuple

# 		while final in unvisited:
# 			for neighbor in neighbors(current):
# 				distances[neighbor] = min(distances[neighbor], distances[current]+1)

# 			unvisited.remove(current)
# 			current = next_current()
# 			if current == ():
# 				break

# 		return distances.get(final, INFINITY)+1

# 	min_distance = Dijkstra(unvisited=unvisited.copy(), distances=distances)

# 	for row in row_walls:
# 		if min_distance == lower_bound:
# 			break

# 		# unvisited.add(wall)
# 		wall_cells = set()
# 		for col in xrange(len(maze[0])):
# 			wall_cells.add((row, col))
# 		candidate_distance = Dijkstra(unvisited=unvisited | wall_cells, distances=distances)
# 		# unvisited.remove(wall)

# 		if candidate_distance < min_distance:
# 			min_distance = candidate_distance

# 	for col in col_walls:
# 		if min_distance == lower_bound:
# 			break

# 		# unvisited.add(wall)
# 		wall_cells = set()
# 		for row in xrange(len(maze)):
# 			wall_cells.add((row, col))
# 		candidate_distance = Dijkstra(unvisited=unvisited | wall_cells, distances=distances)
# 		# unvisited.remove(wall)

# 		if candidate_distance < min_distance:
# 			min_distance = candidate_distance

# 	return min_distance


def answer(maze):
	unvisited = set()
	walls = []
	distances = {}
	lower_bound = len(maze) + len(maze[0]) - 1

	for row in xrange(len(maze)):
		for col in xrange(len(maze[0])):
			distances.setdefault((row, col), INFINITY)
			if maze[row][col] == 0:
				unvisited.add((row, col))
			else:
				walls.append((row, col))

	initial = (0, 0)
	final = (len(maze)-1, len(maze[0])-1)
	distances[initial] = 0

	def Dijkstra(unvisited, distances):
		current = initial
		def neighbors(position):
			row = position[0]
			col = position[1]

			if (row-1, col) in unvisited:
				yield (row-1, col)
			if (row+1, col) in unvisited:
				yield (row+1, col)
			if (row, col-1) in unvisited:
				yield (row, col-1)
			if (row, col+1) in unvisited:
				yield (row, col+1)

		def next_current():
			smallest_distance = INFINITY
			smallest_tuple = ()
			for x, y in unvisited:
				distance = distances.get((x, y))
				if distance < smallest_distance:
					smallest_distance = distance
					smallest_tuple = (x, y)

			return smallest_tuple

		while final in unvisited:
			for neighbor in neighbors(current):
				distances[neighbor] = min(distances[neighbor], distances[current]+1)

			unvisited.remove(current)
			current = next_current()
			if current == ():
				break

		return distances.get(final)+1

	min_distance = Dijkstra(unvisited=unvisited.copy(), distances=distances.copy())

	for wall in walls:
		print "distances: %r" % (distances)
		if min_distance == lower_bound:
			break

		candidate_distance = Dijkstra(unvisited=unvisited | set([wall]), distances=distances.copy())

		if candidate_distance < min_distance:
			min_distance = candidate_distance

	return min_distance

# from misc import *
# m='1110111011101011101'
# n='1111000111110111'
# add_binary(m=m, n=n)

def add_binary(m, n):
	def add_bits(x, y, carry_in):
		bit_out = '0'
		carry_out = '0'
		if x == '0' and y == '0':
			bit_out = '0'
		if (x == '1' and y == '0' or
			x == '0' and y == '1'):
			bit_out = '1'
		if x == '1' and y == '1':
			bit_out = '0'
			carry_out = '1'

		if carry_in == '1':
			if bit_out == '0':
				bit_out = '1'
			else:
				bit_out = '0'
				carry_out = '1'

		return bit_out, carry_out

	def pad(a, b):
		diff = abs(len(a) - len(b))
		padding = '0' * diff
		if len(a) > len(b):
			b = padding + b
		elif len(a) < len(b):
			a = padding + a
		a = '0' + a
		b = '0' + b

		return a, b

	result = ''
	carry = '0'
	m, n = pad(a=m, b=n)

	i = len(m) - 1

	while i >= 0:
		bitwise_result, carry = add_bits(m[i], n[i], carry)
		result = bitwise_result + result

		i -= 1

	return result


def gens(M, F):
    m = long(M)
    f = long(F)

    generations = 0
    no_dice = "impossible"
    while m >= 1 and f >= 1:
    	if m == f:
    		break
    	if m == 1 or f == 1:
    		generations += abs(m-f)
    		m = f = 1
    		break
        times = 1
        if m > f:
        	times = m / f
        	m -= times*f
        else:
            times = f / m
            f -= times*m
        
        generations += times

    if m == f == 1:
        return str(generations)
    return no_dice
