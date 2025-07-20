class Node():
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} #maps keys to nodes
        self.left, self.right = Node(0, 0), Node(0, 0) #allows for easy left and right access
        self.left.next, self.right.prev = self.right, self.left


    #insert at right
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node 
        node.next, node.prev = nxt, prv

        
    #remove node
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv


    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1


    def put(self, key, value):
        node = Node(key, value)

        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]

            
        if len(self.cache) == self.capacity:
            start = self.left.next
            del self.cache[start.key]
            self.remove(start)


        self.insert(node)
        self.cache[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)