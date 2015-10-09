from collections import deque


def main():
    n, m = map(int, raw_input().split(' '))
    G = [[] for i in xrange(n)]
    for i in xrange(m):
        a, b = map(int, raw_input().split(' '))
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    origin = input()
    print " ".join(map(str, filter(lambda x: x!= 0, bfs(G, origin - 1))))


def bfs(G, origin):
    dist = [-1 for _ in xrange(len(G))]
    dist[origin] = 0
    a = deque()
    a.append(origin)
    while a:
        current = a.popleft()
        for v in G[current]:
            if dist[v] == -1:
                dist[v] = dist[current] + 6
                a.append(v)
    return dist

t = input()
for i in xrange(t):
    main()
