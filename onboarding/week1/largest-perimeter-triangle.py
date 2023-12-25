class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i=0
        while i<n-2:
            if nums[n-i-3]+nums[n-i-2]>nums[n-i-1]:
                return nums[n-i-3]+nums[n-i-2]+nums[n-i-1]
            i+=1
        return 0