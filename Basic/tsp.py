cities = 10
cache = [[-1]*2**cities for _ in xrange(cities)]
for i in xrange(cities):
    cache[i][1 << i] = 0


def tsp(v, visiting, G):
    """The minimum path ending in v and passing once through every node in visiting"""
    if cache[v][visiting] != -1:
        return cache[v][visiting]
    ans = 10**9
    for u in xrange(cities):
        if u == v:
            continue
        if (1 << u) & visiting:
            ans = min(ans, tsp(u, visiting ^ (1 << v), G) + G[u][v])
    cache[v][visiting] = ans
    return ans

G = [[1] * cities for _ in xrange(cities)]
#for i in xrange(cities):
#    for j in xrange(i):
print min(tsp(v, (1 << cities) - 1, G) for v in xrange(cities))
