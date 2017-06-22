    # def DFT(capacity):
    #     source = 0
    #     sink = len(capacity)-1
    #     assert(len(capacity) == len(capacity[source]) == len(capacity[sink])) #capacity is a square matrix
    #     side_len = len(capacity)

    #     summation = 0

    #     def DFT_rec(capacity, walk, minimum):
    #         source = 0
    #         sink = len(capacity)-1
    #         assert(len(capacity) == len(capacity[source]) == len(capacity[sink])) #capacity is a square matrix
    #         side_len = len(capacity)

    #         summation = 0
    #         current = walk[-1]

    #         def is_valid(walk, minimum):
    #             # determining validity of walk
    #             return (walk[-1] == sink and
    #                 minimum > 0)

    #         if (minimum == 0 or
    #             len(walk) == side_len or
    #             current == sink):
    #             return capacity, walk, minimum, summation

    #         for j in xrange(side_len):
    #             interim_minimum = min(minimum, capacity[current][j])
    #             interim_walk = walk + [j]
    #             residual = capacity.copy()
    #             residual[current][j] -= interim_minimum

    #             residual, interim_walk, interim_minimum, interim_sum = DFT_rec(capacity=residual, walk=interim_walk, minimum=interim_minimum)

    #             if is_valid(walk=interim_walk, minimum=interim_minimum):
    #                 capacity, walk, minimum = residual, interim_walk, interim_minimum
    #                 summation += interim_sum

    #         return capacity, walk, minimum, summation

    #     for i in xrange(side_len):