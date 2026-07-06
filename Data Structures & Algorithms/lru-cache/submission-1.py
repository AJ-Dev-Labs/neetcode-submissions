class LRUCache:

    class Node:
        def __init__(self, key=-1, value=-1):
            self.key = key
            self.val = value
            self.prev = None
            self.next = None
    
    def remove_node(self, n: Node):
        prev = n.prev
        next = n.next
        prev.next = next
        next.prev = prev
        n.next = None
        n.prev = None
    
    def add_to_head(self, n: Node):
        first = self.head.next
        n.next = first
        first.prev = n
        n.prev = self.head
        self.head.next = n

    def move_to_head(self, n: Node):
        self.remove_node(n)
        self.add_to_head(n)

    def __init__(self, capacity: int):
        self.count = 0
        self.cache = {}
        self.capacity = capacity
        self.head = self.Node()
        self.tail = self.Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        n = self.cache.get(key)
        self.move_to_head(n)
        return n.val
    
    def remove_from_last(self):
        lru = self.tail.prev
        self.remove_node(lru)
        del self.cache[lru.key]
        self.count -= 1

        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            n.val = value
            self.move_to_head(n)
            return
        if self.count == self.capacity:
            self.remove_from_last()
        n = self.Node(key, value)
        self.add_to_head(n)
        self.count += 1
        self.cache[key] = n
        

        
