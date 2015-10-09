import heapq


def main():
    n, m = map(int, raw_input().split(' '))
    G = [[] for i in xrange(n)]
    for i in xrange(m):
        a, b, w = map(int, raw_input().split(' '))
        G[a - 1].append((b - 1, w))
        G[b - 1].append((a - 1, w))
    origin = input()
    print prim(G, origin - 1)


def prim(G, origin):
    remaining = []
    seen = set()
    mst = 0
    heapq.heappush(remaining, (0, origin))
    while remaining:
        w, node = heapq.heappop(remaining)
        if node in seen:
            continue
        mst += w
        seen.add(node)

        for v, wv in G[node]:
            if v not in seen:
                heapq.heappush(remaining, (wv, v))
    return mst


main()
