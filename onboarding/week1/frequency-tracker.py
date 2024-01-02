class FrequencyTracker:

    def __init__(self):
        self.frequency = {}
        self.frequency_tracker = {}

    def add(self, number: int) -> None:
        if number in self.frequency:
            self.frequency_tracker[self.frequency[number]]-=1
            self.frequency[number]+=1
            if self.frequency[number] in self.frequency_tracker:
                self.frequency_tracker[self.frequency[number]]+=1
            else:
                self.frequency_tracker[self.frequency[number]]=1
        else:
            self.frequency[number]=1
            if 1 in self.frequency_tracker:
                self.frequency_tracker[1]+=1
            else:
                self.frequency_tracker[1]=1
            
    def deleteOne(self, number: int) -> None:
        if number in self.frequency:
            self.frequency_tracker[self.frequency[number]]-=1
            self.frequency[number]-=1
            if self.frequency[number] in self.frequency_tracker:
                self.frequency_tracker[self.frequency[number]]+=1
            else:
                self.frequency_tracker[self.frequency[number]]=1
            if self.frequency[number]==0:
                self.frequency.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        if frequency not in self.frequency_tracker:
            return False
        if self.frequency_tracker[frequency]>0:
            return True
        return False

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)