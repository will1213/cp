class RandomizedSet:
    # have better solution which is use list instead of set
    # so getrandom will be constant time
    # but w/e for now
    def __init__(self):
        self.randomSet = set()
        self.myDict = defaultdict(bool)
        self.count = 0

    def insert(self, val: int) -> bool:
        if self.myDict[val]:
            return False
        self.myDict[val] = True
        self.count += 1
        self.randomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if self.myDict[val]:
            del self.myDict[val]
            self.randomSet.remove(val)
            self.count -= 1
            return True
        return False
    
    def getRandom(self) -> int:
        temp = random.randint(0, self.count-1)
        return list(self.randomSet)[temp]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()