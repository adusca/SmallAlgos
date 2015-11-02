N = int(raw_input())

cache = [[-1, -1] for _ in xrange(N)]
parents = [-1] + map(int, raw_input().split())
children = [[] for _ in xrange(N)]

for i in xrange(1, N):
    children[parents[i]].append(i)


def max_coloring(root, painted):
    """
    How many nodes can be painted on a tree, assuming that no
    adjacent nodes can be colored and the root's state is painted (true or false)
    """
    # Using Python bool coercion, True = 1, False = 0
    if cache[root][painted] != -1:
        return cache[root][painted]
    if painted:
        babies = [max_coloring(u, painted=False) for u in children[root]]
        cache[root][painted] = 1 + sum(babies)
    else:
        babies = [max(max_coloring(u, True), max_coloring(u, False))
                  for u in children[root]]
        cache[root][painted] = sum(babies)
    return cache[root][painted]

print max(max_coloring(0, True), max_coloring(0, False))
