class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity

        # key -> Node
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left


    def remove(self, node):
        # Remove node from linked list
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    def insert(self, node):
        # Insert node right before self.right
        # This makes it the most recently used node
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt


    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]

            # Move node to MRU position
            self.remove(node)
            self.insert(node)

            return node.val

        return -1


    def put(self, key: int, value: int) -> None:

        # If key already exists, remove its old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create/update node
        node = Node(key, value)
        self.cache[key] = node

        # Make it most recently used
        self.insert(node)

        # Remove LRU if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]