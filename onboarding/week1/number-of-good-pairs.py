class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count =0
        store = {}
        for i in nums:
            if i in store:
                store[i]+=1
            else:
                 store[i]=1
        for i in store:
            count+=store[i]*(store[i]-1)/2
        return int(count)