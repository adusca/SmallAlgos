def read():
    n = int(raw_input())
    parents = [0]*n
    heights = [0]*n

    for i in xrange(1, n):
        parents[i] = int(raw_input())
        heights[i] = heights[parents[i]] + 1

    def lca(a, b):
        if heights[a] > heights[b]:
            a, b = b, a
        for i in xrange(heights[b] - heights[a]):
            b = parents[b]
        while b != a:
            b = parents[b]
            a = parents[a]
        return b

    q = int(raw_input())
    for i in xrange(q):
        print lca(*map(int, raw_input().split()))

read()
