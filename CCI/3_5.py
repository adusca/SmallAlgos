from linkedlist import Stack


def sort_stack(stack):
    """
    1  _  -> _  _ -> _  _ -> _  _ -> _  3 -> 1  _
    3  _     3  _    _  3    _  2    _  2    2  _
    2  _     2  1    2  1    3  1    _  1    3  _
    """
    helper = Stack()
    while not stack.empty():
        current = stack.pop()

        while not helper.empty() and helper.peek() > current:
            stack.push(helper.pop())
        helper.push(current)

    while not helper.empty():
        stack.push(helper.pop())

a = Stack()
for i in [1, 4, 5, 3, 2]:
    a.push(i)

sort_stack(a)
while not a.empty():
    print a.pop()
