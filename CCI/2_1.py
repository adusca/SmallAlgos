from linkedlist import LinkedList


def remove_dups(ll):
    seen = set()
    previous = ll.head
    node = ll.head.next
    seen.add(previous.value)
    while node is not None:
        if node.value in seen:
            previous.next = node.next
        else:
            seen.add(node.value)
            previous = previous.next
        node = node.next

    return ll


def remove_dups_lean(ll):
    first = ll.head
    while first is not None:
        second = first.next
        previous = first
        while second is not None:
            if first.value == second.value:
                previous.next = second.next
            else:
                previous = previous.next
            second = second.next
        first = first.next

    return ll

l = LinkedList.create_from_array([2, 3, 1, 1, 3, 4, 5, 6, 7])
remove_dups(l).print_list()
l2 = LinkedList.create_from_array([2, 3, 1, 1, 3, 4, 5, 6, 7])
remove_dups_lean(l2).print_list()
