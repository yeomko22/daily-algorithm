class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        

    def insert(self, key: str, val: int) -> None:
        self.m[key] = val
        

    def sum(self, prefix: str) -> int:
        cursum = 0
        for key in self.m:
            if key.startswith(prefix):
                cursum += self.m[key]
        return cursum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)