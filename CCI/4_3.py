from linkedlist import LinkedList
from collections import deque


def bfs(node):
    ans = []
    line = deque()
    dist = -1
    line.append((node, 0))
    new_l = None
    while line:
        current, cur_dist = line.popleft()
        if cur_dist == dist:
            new_l.add(current)
        else:
            new_l = LinkedList()
            ans.append(new_l)
            new_l.add(current)
            dist = cur_dist

        for v in (current.left, current.right):
            if v:
                line.append((v, cur_dist + 1))
    return ans
