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

def answer(entrances, exits, path):
    def do_single_source():
        if len(entrances) == 1:
            entrance = entraces[0]
            if entrance == 0:
                return
            temp = path[0]
            path[0] = path[entrance]
            path[entrance] = temp
        
        new_row = [0] * (len(path[0])+1)
        
        for i in xrange(len(path)):
            path[i] = [0] + path[i]
            
        for entrance in entrances:
            new_row[entrance] = sum(path[entrance])
            
        path = [new_row] + path
        
    def do_single_sink():
        def sum_col(col):
            s = 0
            for i in xrange(len(path)):
                s += path[i][col]
            
            return s
                
        if len(exits) == 1:
            last = len(path)-1
            exit = exits[0]
            if exit == last:
                return
            temp = path[last]
            path[last] = path[exit]
            path[exit] = temp
            
        new_row = [0] * (len(path[0])+1)
        
        for i in xrange(len(path)):
            path[i].append(0)
            
        path.append(new_row)
        
        for exit in exits:
            path[exit][len(path[0])-1] = sum_cols(exit)
     