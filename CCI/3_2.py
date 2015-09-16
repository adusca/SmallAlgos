from linkedlist import LinkedList


class Stack:

    def __init__(self):
        self.stack = LinkedList()
        self.min_stack = LinkedList()

    def push(self, value):
        self.stack.add(value)
        if self.min_stack.head is not None:
            self.min_stack.add(min(value, self.min_stack.head.value))
        else:
            self.min_stack.add(value)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack.head.value

    def empty(self):
        return self.stack.head is None


a = Stack()
a.push(10)
a.push(3)
a.push(12)
a.push(4)

while not a.empty():
    print "min:", a.min()
    print a.pop()
