class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = set(nums)
        l =[]
        for i in m:
            if nums.count(i)>len(nums)//3:
                 l.insert(nums.index(i),i)
        return l