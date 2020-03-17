class Node:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.next = None
        self.prev = None


class Solution:

    """
    Design and implement a data structure for Least Recently Used (LRU) cache. 
    It should support the following operations: get and put.
    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    put(key, value) - Set or insert the value if the key is not already present. 
    When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    The cache is initialized with a positive capacity.

    """

    """
    Using map and double linked list 
    
    """

    def __init__(self, capacity):
        self.d = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.d:
            n = self.d[key]
            self._remove(n)
            self._add(n)
            return n.v

        return -1

    def put(self, key, value):

        if key in self.d:
            self._remove(self.d[key])
            del self.d[key]

        n = Node(key, value)
        self._add(n)
        self.d[key] = n
        if len(self.d) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.d[n.k]

    def _add(self, node):
        n = self.tail.prev
        n.next = node
        node.prev = n
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p


if __name__ == "__main__":

    cache = Solution(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))         # returns 1
    cache.put(3, 3)    # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    print(cache.get(1))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))       # returns 4
