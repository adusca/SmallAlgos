from linkedlist import Node


def intersection(node1, node2):
    s1, s2 = size(node1), size(node2)

    for i in range(s2 - s1):
        node2 = node2.next
    for i in range(s1 - s2):
        node1 = node1.next
    return intersection_same_length(node1, node2)


def intersection_same_length(node1, node2):
    """
    If both lists have the same total length, this means there is the
    same number of nodes before the intersection
    """
    while node1:
        if node1 is node2:
            return node2
        node1 = node1.next
        node2 = node2.next
    return -1


def size(node):
    ans = 0
    while node:
        node = node.next
        ans += 1
    return ans


def intersection_with_hash_table(node1, node2):
    """
    input: 2 singly linked lists
    output: their intersecting node or -1
    """
    hash_table = set()
    while node1:
        hash_table.add(node1)
        node1 = node1.next

    while node2:
        if node2 in hash_table:
            return node2
        node2 = node2.next
    return -1


def intersection_AxB(node1, node2):
    while node1 is not None:
        n = node2
        while n is not None:
            if node1 == n:
                return node1
            n = n.next
        node1 = node1.next
    return -1


def intersection_indicator(node1, node2):
    """
    Return a boolean indicating if 2 linked lists intersect
    """
    while node1.next is not None or node2.next is not None:
        if node1.next is not None:
            node1 = node1.next
        if node2.next is not None:
            node2 = node2.next
    return node1 == node2

n5 = Node(5)
n3 = Node(3, n5)
n1 = Node(1, n3)
n2 = Node(1, n5)
n4 = Node(4)
n7 = Node(7)
print intersection_with_hash_table(n1, n2)
print intersection(n1, n2)
print intersection(n1, n7)
print intersection_indicator(n1, n2)
print intersection_indicator(n1, n4)
