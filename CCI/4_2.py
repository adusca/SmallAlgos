class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.adj = [self.left, self.right]


def create_from_array(array):
    """
    input: a sorted array
    output: a binary search tree of minimum height
    """
    if len(array) == 0:
        return
    n = len(array)/2
    root = Node(array[n])
    root.left = create_from_array(array[:n])
    root.right = create_from_array(array[n+1:])
    return root


def print_tree(a):
    if a is None:
        return
    print a.value
    print_tree(a.left)
    print_tree(a.right)

a = create_from_array([1, 2, 3, 4, 5, 6])
print_tree(a)
