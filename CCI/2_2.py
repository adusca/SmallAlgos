from linkedlist import LinkedList


def kth_to_last(ll, k):
    index = size(ll) - k
    node = ll.head
    for i in xrange(index - 1):
        node = node.next
    return node


def size(ll):
    ans = 0
    node = ll.head
    while node is not None:
        ans += 1
        node = node.next
    return ans


def kth_without_size(ll, k):
    node = ll.head
    runner = ll.head

    # Why this + 1?
    for i in xrange(k + 1):
        runner = runner.next
    while runner is not None:
        node = node.next
        runner = runner.next
    return node

l = LinkedList.create_from_array([1, 2, 3, 4, 5, 6, 7])
print kth_to_last(l, 3)
print kth_without_size(l, 0)
