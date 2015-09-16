from linkedlist import Node


def find_first_in_loop(node):
    tortoise = node

    # If the list has no cycle and exactly one node, we would get an
    # error accessing tortoise.next.next
    if tortoise.next is not None:
        hare = tortoise.next.next
    else:
        return -1

    while tortoise:
        if tortoise == hare:
            break
        tortoise = tortoise.next
        if hare.next is not None:
            hare = hare.next.next
        else:
            return -1

    # Now that the tortoise and the hare are both inside the cycle, we
    # can find the cycle length by keeping the tortoise still and
    # moving the hare
    size = 1
    hare = hare.next
    while hare != tortoise:
        hare = hare.next
        size += 1

    # Let k be the size of the cycle. Let the hare be exactly k steps
    # in front of the tortoise, and move both one step at a time. When
    # the tortoise gets to the first node in the cycle the hare will
    # also be there because N + k = N for every N in the
    # cycle. Since they cannot meet before the cycle, the first place
    # they meet is the beginning of the cycle
    tortoise = node
    hare = node
    for i in range(size):
        hare = hare.next
    while True:
        if hare == tortoise:
            return hare
        hare = hare.next
        tortoise = tortoise.next

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

print find_first_in_loop(n3)
