class RandomizedSet:

    def __init__(self):
        self.l = []
        self.d = {}
        
    def search(self, val):
        return val in self.d

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False
        self.l.append(val)
        self.d[val] = len(self.l) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False
        i = self.d[val]
        self.l[i] = self.l[-1]
        self.d[self.l[-1]] = i
        self.l.pop()
        del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()