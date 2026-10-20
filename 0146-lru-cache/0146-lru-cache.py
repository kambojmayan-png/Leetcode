class Node:
    def __init__(self , key , value):
        self.key = key
        self.value = value
        self.next , self.prev = None , None

class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next , self.right.prev = self.right , self.left 
        
    def remove(self , node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self , node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key):
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key , value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)