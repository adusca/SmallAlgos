from collections import deque


def is_balanced(tree):
    if abs(height(tree.left) - height(tree.right)) > 1:
        return False
    return is_balanced(tree.left) and is_balanced(tree.right)

heights = {}


def height(tree):
    if tree in heights:
        return heights[tree]
    if not tree.left and not tree.right:
        heights[tree] = 0
