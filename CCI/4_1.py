from collections import deque


def bfs(node):
    line = deque()
    line.append(node)
    node.visited = True
    while line:
        current = line.popleft()
        for v in current.adj:
            if not v.visited:
                line.append(v)
                v.visited = True


def exist_route(v, w):
    bfs(v)
    return w.visited
