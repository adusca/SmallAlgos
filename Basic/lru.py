class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.end = None
        self.cache = {}

    def remove(self, node):
        if node.prev:
            node.prev.nxt = node.nxt
        else:
            self.head = node.nxt

        if node.nxt:
            node.nxt.prev = node.prev
        else:
            self.end = node.prev

    def set_head(self, node):
        node.nxt = self.head
        node.prev = None

        if self.head:
            self.head.prev = node

        self.head = node

        if self.end is None:
            self.end = self.head

    def get_node(self, key):
        node = self.cache[key]
        self.remove(node)
        self.set_head(node)
        return node

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.get_node(key)
        return node.value

    def set(self, key, value):
        if key in self.cache:
            old = self.get_node(key)
            old.value = value
        else:
            new = Node(key, value)
            if len(self.cache) >= self.capacity:
                del self.cache[self.end.key]
                self.remove(self.end)
            self.set_head(new)
            self.cache[key] = new

LRU = LRUCache(5)
s = 'qwertyuiojgfdsxcvbnkliuytrsdcvbnjytredfv'
for i in xrange(len(s)):
    LRU.set(i, s[i])
    print len(LRU.cache)
    print LRU.get(i)
