class RandomizedSet:

    def __init__(self):
        self.RandomSet = set() #initializing set

    def insert(self, val: int) -> bool:
        if val in self.RandomSet: #checking if the value exists in the set
            return False
        self.RandomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.RandomSet: # checking if the value exists in the set
            return False
        self.RandomSet.discard(val)
        return True

    def getRandom(self) -> int:
       
        return random.choice(list(self.RandomSet)) #picking random value from the set
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()