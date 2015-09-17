from linkedlist import LinkedList


def sum_lists(l, t):
    node1 = l.head
    node2 = t.head
    carry = 0
    result = LinkedList()
    while node1 is not None or node2 is not None:
        first_parcel = 0
        second_parcel = 0

        if node1 is not None:
            first_parcel = node1.value
            node1 = node1.next

        if node2 is not None:
            second_parcel = node2.value
            node2 = node2.next

        sum_value = first_parcel + second_parcel + carry
        result.append(sum_value % 10)
        carry = sum_value/10

    if carry > 0:
        result.append(carry)
    return result


def sum_lists_forward(l, t):
    shorter, longer = sorted([l, t],
                             key=lambda x: x.length)
    for i in xrange(longer.length - shorter.length):
        shorter.add(0)

    result, carry = sum_lists_forward_aux(shorter.head, longer.head)
    if carry > 0:
        result.add(carry)
    return result


def sum_lists_forward_aux(a, b):
    """
    Example Input:  4 -> 3 -> 2
                    9 -> 8 -> 7

    Example Output: 4 -> 1 -> 9, 1
    """
    if a is None:
        return LinkedList(), 0

    tmp, carry = sum_lists_forward_aux(a.next, b.next)
    value = a.value + b.value + carry
    tmp.add(value % 10)
    return tmp, value/10


l = LinkedList.create_from_array([5, 4, 1, 1])
t = LinkedList.create_from_array([2, 8, 9])
sum_lists(l, t).print_list()
sum_lists_forward(l, t).print_list()
