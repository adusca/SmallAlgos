import heapq


def dijkstra(G, origin):
    """
    input: a graph G represented as an adj list and a node origin
    output: a dict with the distances from the origin to each node

    G[1] = [(0, 2), [2, 1]] means that there is an edge of weight 2
    from 1 to 0 and a edge of weight 1 from 1 to 2.
    """
    dist = {}
    remaining = []
    seen = set()
    heapq.heappush(remaining, (0, origin))
    while remaining:
        cost, node = heapq.heappop(remaining)
        if node in seen:
            continue
        dist[node] = cost
        seen.add(node)

        for v, cost_v in G[node]:
            if v not in seen:
                heapq.heappush(remaining, (cost + cost_v, v))
    return dist


G = [[(1, 2), [2, 1]], [(3, 5)], [(3, 1)], [(1, 2)], []]
print dijkstra(G, 0)
