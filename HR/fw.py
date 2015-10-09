import sys


def solve():
    INF = 350*401

    n, m = map(int, input().split(' '))

    dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n + 1):
        dist[i][i] = 0

    for i in range(m):
        x, y, w = map(int, sys.stdin.readline().split(' '))
        dist[x][y] = w

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dist[i][k] < INF:
                for j in range(1, n + 1):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][j] == INF:
                dist[i][j] = -1

    q = input()
    for i in range(q):
        x, y = map(int, sys.stdin.readline().split(' '))
        print(dist[x][y])

solve()
