from collections import deque


def topsort(G):
    """
    input: A directed acyclic graph G, represented as a list of adj
    output: A list containing G nodes in topological ordering
    """
    ans = []
    next_node = deque()

    # inbound[i] is how many edges arrive at the node i
    inbound = [0 for i in xrange(len(G))]
    for node in G:
        for v in node:
            inbound[v] += 1

    # At least one element will have 0 inbound edges
    for i in xrange(len(inbound)):
        if inbound[i] == 0:
            next_node.append(i)

    while next_node:
        nxt = next_node.pop()
        ans.append(nxt)
        for node in G[nxt]:
            inbound[node] -= 1
            if inbound[node] == 0:
                next_node.append(node)
    return ans
