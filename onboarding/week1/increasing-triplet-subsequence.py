class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        i,j = float('inf'),float('inf')
        for index in range(len(nums)):
            if nums[index]<=i:
                i = nums[index]
            elif nums[index]<=j:
                j = nums[index]
            else:
                return True
        return False