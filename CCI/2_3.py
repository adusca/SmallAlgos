from linkedlist import Node, print_list_from_node


def remove_middle(node):
    node.value = node.next.value
    node.next = node.next.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print_list_from_node(node1)
remove_middle(node3)
print_list_from_node(node1)
