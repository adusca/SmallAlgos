def read():
    n = int(raw_input())
    log = n.bit_length()

    # parents[i][j] = 2^j-esimo ancestor of i
    parents = [[0] * log for _ in xrange(n)]
    heights = [0]*n

    for i in xrange(1, n):
        parents[i][0] = int(raw_input())
        heights[i] = heights[parents[i][0]] + 1

    for j in xrange(1, log):
        for i in xrange(n):
            parents[i][j] = parents[parents[i][j-1]][j-1]

    def lca(a, b):
        if heights[a] > heights[b]:
            a, b = b, a

        diff = heights[b] - heights[a]
        for j in xrange(log):
            if diff & (1 << j):
                b = parents[b][j]

        if a == b:
            return a

        # Let d be the maximum jump such that jump(a, d) != jump(b, d)
        # Then d can be represented in binary, and the loop below jumps
        # to the 2^j-th parent exactly when the j-th bit of d is 1.
        for j in xrange(log - 1, -1, -1):
            if parents[a][j] != parents[b][j]:
                a = parents[a][j]
                b = parents[b][j]

        assert parents[a][0] == parents[b][0]
        return parents[b][0]

    q = int(raw_input())
    for i in xrange(q):
        print lca(*map(int, raw_input().split()))

read()
