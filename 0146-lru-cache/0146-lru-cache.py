class ListNode:
    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1,-1)
        self.tail = ListNode(-1,-1, None, self.head)
        self.head.next = self.tail
        self.d = {}     

    def delete(self, key:int):
        node = self.d[key]  
        prev = node.prev 
        prev.next = node.next
        node.next.prev = prev
        val = node.val
        del self.d[key]
        return val

    def get(self, key: int) -> int:
        if key in self.d:
            value = self.delete(key)
            self.put(key, value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.delete(key)
        if len(self.d) == self.capacity:
            self.delete(self.tail.prev.key)
        new_node = ListNode(key, value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.d[key] = new_node

            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)