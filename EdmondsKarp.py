import collections
INFINITY = 2000000
 
class Flow:
  
    def __init__(self, residual_graph):
        self.residual_graph = residual_graph
        self.side_len = len(residual_graph)
  
    def BFS(self, source, sink, parent):

        visited = [False] * self.side_len
        queue = collections.deque()
         
        queue.append(source)
        visited[source] = True
         
        while queue:
            current = queue.popleft()

            for i in xrange(len(self.residual_graph[current])):
                val = self.residual_graph[current][i]
                if visited[i] or val == 0:
                    continue

                queue.append(i)
                visited[i] = True
                parent[i] = current

        return visited[sink]
             
    def _Edmonds_Karp(self, source, sink):
 
        parent = [-1] * self.side_len
        max_flow = 0
 
        while self.BFS(source, sink, parent):
            flow = INFINITY
            node = sink
            while node != source:
                flow = min(flow, self.residual_graph[parent[node]][node])
                node = parent[node]
 
            max_flow += flow
 
            v = sink
            while v != source:
                u = parent[v]
                self.residual_graph[u][v] -= flow
                self.residual_graph[v][u] += flow
                v = parent[v]
 
        return max_flow

    def max_bunnies_flow(self):
        return self._Edmonds_Karp(source=0, sink=self.side_len-1)

def answer(entrances, exits, path):

    def do_single_source(entrances, path):
        assert(len(path) == len(path[0]) == len(path[-1]))

        new_row = [0] * len(path[0])
            
        for entrance in entrances:
            new_row[entrance] = sum(path[entrance])
            
        path = [new_row] + path

        for i in xrange(len(path)):
            path[i] = [0] + path[i]

        return path
        
    def do_single_sink(exits, path):
        assert(len(path) == len(path[0]) == len(path[-1]))

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

    path = do_single_sink(exits=exits, path=path)
    path = do_single_source(entrances=entrances, path=path)

    flow = Flow(residual_graph=path)

    return flow.max_bunnies_flow()


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