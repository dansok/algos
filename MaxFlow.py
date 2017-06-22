import sys
INFINITY = sys.maxint
INFINITY = 2000000

def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print col,
        print

def answer(entrances, exits, path):

    def do_single_source(entrances, path):
        assert(len(path) == len(path[0]))

        new_row = [0] * len(path[0])
            
        for entrance in entrances:
            new_row[entrance] = sum(path[entrance])
            
        path = [new_row] + path

        for i in xrange(len(path)):
            path[i] = [0] + path[i]

        return path
        
    def do_single_sink(exits, path):
        assert(len(path) == len(path[0]))

        def sum_col(matrix, col):
            s = 0
            for i in xrange(len(matrix)):
                s += matrix[i][col]
            
            return s
            
        new_row = [0] * len(path[0])
        path.append(new_row)
        
        for i in xrange(len(path)):
            path[i].append(0)
        
        for exit in exits:
            path[exit][-1] = sum_col(matrix=path, col=exit)

        return path

    def Edmonds_Karp(E, C, s, t):
        assert(len(C) == len(C[0]) == len(C[-1]))

        def BFSEK(E, C, s, t, F, P, M, BFSq):

            while (len(BFSq) > 0):
                u = BFSq.pop(0)
                for v in E[u]:
                    if C[u][v] - F[u][v] > 0 and P[v] == -1:
                        P[v] = u
                        M[v] = min(M[u], C[u][v] - F[u][v])
                        if v != t:
                            BFSq.append(v)
                        else:
                            return M[t], P
            return 0, P

        n = len(C)
        flow = 0
        F = [[0 for y in range(n)] for x in range(n)]
        while True:
            P = [-1 for x in range(n)]
            P[s] = -2
            M = [0 for x in range(n)]
            M[s] = INFINITY
            BFSq = []
            BFSq.append(s)
            pathFlow, P = BFSEK(E, C, s, t, F, P, M, BFSq)
            if pathFlow == 0:
                break
            flow = flow + pathFlow
            v = t
            while v != s:
                u = P[v]
                F[u][v] = F[u][v] + pathFlow
                F[v][u] = F[v][u] - pathFlow
                v = u
        return flow

    print_matrix(matrix=path)
    path = do_single_sink(exits=exits, path=path)
    path = do_single_source(entrances=entrances, path=path)
    print_matrix(matrix=path)

    edges = []
    for i in xrange(len(path)):
        edges_row = []
        for j in xrange(len(path[0])):
            if path[i][j] > 0:
                edges_row.append(j)
        edges.append(edges_row)


    return Edmonds_Karp(E=edges,
        C=path,
        s=0,
        t=len(path)-1)


def main():
    entrances = [0, 1]
    exits = [4, 5]
    # path = [
    #     [0, 10, 7, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 4, 6, 0, 0, 0],  # Room 0: Bunnies
    #     [0, 0, 0, 5, 2, 0, 0, 0],  # Room 1: Bunnies
    #     [0, 0, 0, 0, 0, 4, 4, 0],  # Room 2: Intermediate room
    #     [0, 0, 0, 0, 0, 6, 6, 0],  # Room 3: Intermediate room
    #     [0, 0, 0, 0, 0, 0, 0, 10],  # Room 4: Escape pods
    #     [0, 0, 0, 0, 0, 0, 0, 10],  # Room 5: Escape pods
    #     [0, 0, 0, 0, 0, 0, 0, 0]
    # ]
    path = [
        [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
        [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
        [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
        [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
        [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
        [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
    ]
    print answer(entrances=entrances, exits=exits, path=path)

    entrances = [0]
    exits = [3]
    path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
    print answer(entrances=entrances, exits=exits, path=path)

if __name__ == "__main__":
    main()


def fib(n):
    fib_0, fib_1 = 1, 1
    for i in xrange(n-2):
        temp = fib_0
        fib_0 = fib_0 + fib_1
        fib_1 = temp
    return fib_0


table = table = {0: 1, 1: 1}
def fib(n):
    global table
    if n in table:
        return table[n]
    fib_n1 = fib(n-1)
    table[n-1] = fib_n1
    return fib_n1 + table[n-2]
