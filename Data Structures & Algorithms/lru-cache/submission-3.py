class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # Creates two dummy nodes with arbitrary key/val (0, 0)
        # left: marks the least recently used end
        # right: marks the most recently used end
        self.left, self.right = Node(0, 0), Node(0,0)

        # Connects them: left ↔ right
        # This creates an empty circular structure
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        # Disconnect the node by linking its neighbors to each other
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        # Insert node right before self.right (at the end of the list)
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
