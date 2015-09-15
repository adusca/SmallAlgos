class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add(self, value):
        node = Node(value, self.head)
        self.head = node
        self.length += 1

    def pop(self):
        ret = self.head.value
        self.head = self.head.next
        self.length -= 1
        return ret

    def append(self, value):
        node = self.head
        if node is None:
            self.head = Node(value, None)
            self.length += 1
            return

        while True:
            if node.next is None:
                node.next = Node(value, None)
                self.length += 1
                break
            node = node.next

    def print_list(self):
        node = self.head
        while node:
            print node,
            node = node.next
        print ""

    @staticmethod
    def create_from_array(array):
        l = LinkedList()
        for i in xrange(len(array)):
            l.add(array[-1 - i])

        return l

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.print_list()

a = LinkedList.create_from_array([1, 2, 3, 4, 5])
a.print_list()
print a.length
