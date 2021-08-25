class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cachekeys = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cachekeys.remove(key)
            self.cachekeys.append(key)
            return self.cache[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cachekeys.remove(key)
            self.cachekeys.append(key)
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            poped_key = self.cachekeys.pop(0)
            del self.cache[poped_key]
        self.cache[key] = value
        self.cachekeys.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)