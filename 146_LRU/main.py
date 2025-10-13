class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.pre = self.dummy
    
    def get_node(self, key):
        if key in self.dic:
            node = self.dic.get(key)
            self.remove(node)
            self.put_top(node)
            return node
        return None
    
    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
    
    def put_top(self, node):
        old_head = self.dummy.next

        self.dummy.next = node
        node.pre = self.dummy

        old_head.pre = node
        node.next = old_head

    def get(self, key: int) -> int:
        node = self.get_node(key)
        if node:
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)

        if node:
            node.val = value
            return 

        node = self.dic[key] = Node(key, value)
        self.put_top(node)
        if len(self.dic) > self.capacity:
            bottom = self.dummy.pre
            self.remove(bottom)
            del self.dic[bottom.key] 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)