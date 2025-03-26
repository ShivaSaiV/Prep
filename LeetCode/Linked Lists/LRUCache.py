# Hashmap for key,vaue lookup in O(1); val = pointer to node
# Double linked list: reorder for most/least recent used

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # map key to node

        self.left = Node(0) # LRU
        self.right = Node(0) # MRU

        self.left.next = self.right
        self.right.prev = self.left

    # Helper; remove from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # Helper; insert into linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove and delete the least recently used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


