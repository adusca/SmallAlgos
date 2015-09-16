from linkedlist import LinkedList


def reverse_in_place(ll):
    """
    Steps:
             a -> b -> c
          <- a    b -> c  * When we are changing b we need references to a and c
          <- a <- b    c
          <- a <- b <- c
    """
    if ll.length < 2:
        return ll

    previous = ll.head
    current = previous.next
    later = current.next
    previous.next = None

    while True:
        current.next = previous
        previous = current
        current = later
        if current is not None:
            later = current.next
        else:
            break

    reverse_list = LinkedList()
    reverse_list.head = previous
    return reverse_list


def reverse(ll):
    """
    Return a new LinkedList that is the reverse of ll without altering ll
    """
    new = LinkedList()
    node = ll.head
    while node:
        new.add(node.value)
        node = node.next
    return new


def is_palindrome(ll):
    rl = reverse(ll)
    node1 = ll.head
    node2 = rl.head
    while node1:
        if node1.value != node2.value:
            return False
        node1 = node1.next
        node2 = node2.next
    return True


def is_palindrome2(ll):
    nl = LinkedList()
    size = ll.length/2
    node = ll.head

    for i in range(size):
        nl.add(node.value)
        node = node.next

    node2 = nl.head

    if ll.length % 2 == 1:
        node = node.next

    while node:
        if node.value != node2.value:
            return False
        node = node.next
        node2 = node2.next
    return True

l = LinkedList.create_from_array([1, 2, 3, 4, 5, 6, 7])
t = LinkedList.create_from_array(list('abacacaba'))
assert is_palindrome(l) is False
assert is_palindrome(t) is True
assert is_palindrome2(l) is False
assert is_palindrome2(t) is True
