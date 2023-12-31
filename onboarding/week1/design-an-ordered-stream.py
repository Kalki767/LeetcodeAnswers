class OrderedStream:
    def __init__(self, n: int):
        self.order = [""]*n #initializing an empty list
        self.ptr =0 # pointing to the first element

    def insert(self, idKey: int, value: str) -> list[str]:
        start = self.ptr #the satrting index of the returned answer
        self.order[idKey-1] = value #initializing the list at the given index
        while self.ptr<len(self.order) and self.order[self.ptr]!="": #checking list index out of bounds and if the current element is different from none 
            self.ptr+=1
        return self.order[start:self.ptr]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)