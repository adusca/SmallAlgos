from collections import deque


def dfs(node):
    visit(node)
    node.visited = True
    for v in node.adjacents:
        if not v.visited:
            dfs(node)


def visit(node):
    pass


def bfs(node):
    line = deque()
    line.append(node)
    while line:
        current = line.popleft()
        visit(current)
        for v in current.adjacents:
            if not v.visited:
                v.visited = True
                line.append(v)
