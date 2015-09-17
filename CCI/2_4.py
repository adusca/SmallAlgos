from linkedlist import LinkedList


def partition(ll, k):
    larger_list = LinkedList()
    previous = ll.head
    node = previous.next
    while node is not None:
        if node.value >= k:
            previous.next = node.next
            larger_list.add(node.value)
        else:
            previous = previous.next
        node = node.next
    previous.next = larger_list.head
    return ll

l = LinkedList.create_from_array([3, 5, 8, 5, 10, 2, 1])
partition(l, 5).print_list()
