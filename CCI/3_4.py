from linkedlist import Stack


class MyQueue:
    def __init__(self):
        self.data = Stack()
        self.reverse_data = Stack()

    def push(self, value):
        self.data.push(value)

    def _fill_reverse_data(self):
        while not self.data.empty():
            value = self.data.pop()
            self.reverse_data.push(value)

    def pop(self):
        if self.reverse_data.empty():
            self._fill_reverse_data()
        return self.reverse_data.pop()

    def peek(self):
        if self.reverse_data.empty():
            self._fill_reverse_data()
        return self.reverse_data.peek()


a = MyQueue()
a.push(1)
a.push(2)
a.push(3)
print a.pop()
a.push(4)
print a.pop()
a.push(5)
print a.pop()
print a.pop()
print a.pop()
