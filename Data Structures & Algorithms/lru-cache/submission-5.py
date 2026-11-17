class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # Dummy boundary nodes
        self.head = Node(0, 0)  # LRU end
        self.tail = Node(0, 0)  # MRU end

        # Connect head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # Disconnect the node by linking its neighbors to each other
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
       # Always insert right before tail (MRU position)

        # Step 1: New node remembers the previous last node
        node.prev = self.tail.prev

        # Step 2: New node points to tail
        node.next = self.tail

        # Step 3: Previous last node points to new node
        self.tail.prev.next = node

        # Step 4: Tail points back to new node
        self.tail.prev = node

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
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
