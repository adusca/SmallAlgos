import collections


n, m = map(int, raw_input().split(' '))

adj = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1)]
colors = [[0 for _ in xrange(n+3)] for _ in xrange(n+3)]
# 1 = persians, 2 = romans
for i in xrange(1, n + 1):
    colors[1][1+i] = 1
    colors[1+i][1] = 2

for i in xrange(m):
    x, y = map(int, raw_input().strip().split(' '))
    colors[1+x][1+y] = 2 - (i & 1)


def bfs(v, color):
    seen = [[False for _ in xrange(n+1)] for _ in xrange(n+1)]
    line = collections.deque()
    line.append(v)
    seen[v[0]][v[1]] = True
    while line:
        current = line.popleft()
        for di, dj in adj:
            w0, w1 = current[0] + di, current[1] + dj
            if color == 1 and w0 == n or color == 2 and w1 == n:
                return True
            if colors[1+w0][1+w1] != color:
                continue
            if not seen[w0][w1]:
                line.append((w0, w1))
                seen[w0][w1] = True
    return False


if bfs((1, 0), 2):
    print "ROMANS"
elif bfs((0, 1), 1):
    print "PERSIANS"
else:
    print "NEITHER"
