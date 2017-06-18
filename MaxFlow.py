# from MaxFlow import *
# entrances = [0, 1]
# exits = [4, 5]
# path = [
#   [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
#   [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
#   [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
#   [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
#   [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
#   [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
# ]
# answer(entrances, exits, path)

# entrances = [0]
# exits = [3]
# path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
# answer(entrances, exits, path)

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print col,
        print

def answer(entrances, exits, path):
    print_matrix(path)
    print
    def do_single_source(entrances, exits, path):
        if len(entrances) == 1:
            entrance = entrances[0]
            if entrance == 0:
                return path
            temp = path[0]
            path[0] = path[entrance]
            path[entrance] = temp
        
        new_row = [0] * (len(path[0])+1)
        
        for i in xrange(len(path)):
            path[i] = [0] + path[i]
            
        for entrance in entrances:
            new_row[entrance] = sum(path[entrance])
            
        path = [new_row] + path

        return path
        
    def do_single_sink(entrances, exits, path):
        def sum_col(path, col):
            s = 0
            for i in xrange(len(path)):
                s += path[i][col]
            
            return s
                
        if len(exits) == 1:
            last = len(path)-1
            exit = exits[0]
            if exit == last:
                return path
            temp = path[last]
            path[last] = path[exit]
            path[exit] = temp
            
        new_row = [0] * (len(path[0])+1)
        
        for i in xrange(len(path)):
            path[i].append(0)
            
        path.append(new_row)
        
        for exit in exits:
            path[exit][len(path[0])-1] = sum_col(path, exit)

        return path

    path = do_single_sink(entrances, exits, path)
    path = do_single_source(entrances, exits, path)

    print_matrix(matrix=path)
