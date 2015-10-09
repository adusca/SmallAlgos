n, m = map(int, raw_input().split(' '))
G = []
for i in xrange(m):
    x, y, w = map(int, raw_input().split(' '))
    G.append((w, x, y))

parent = range(n + 1)
rank = [0]*(n + 1)


def find(u):
    global parent
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]


def union(u, v):
    global parent
    global rank
    u = find(u)
    v = find(v)
    if rank[v] < rank[u]:
        v, u = u, v
    parent[u] = v
    if rank[v] == rank[u]:
        rank[v] += 1


def kruskal(graph):
    graph.sort()
    mst = 0
    for w, u, v in graph:
        if find(u) != find(v):
            union(u, v)
            mst += w
    return mst

print kruskal(G)
