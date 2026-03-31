class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.cache = {}
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_tail(node)
            return node.val
        
        return -1

    def _add_tail(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        # remove specific key
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        prev_node = None
        next_node = None


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self._add_tail(self.cache[key])
        
        # check if at capacity
        if len(self.cache) > self.capacity:
            # pop head
            lru_node = self.head.next
            self._remove(lru_node)
            del self.cache[lru_node.key]
