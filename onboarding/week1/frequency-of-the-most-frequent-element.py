class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        if len(nums)==1:
            return 1
        nums.sort()
        frequency = []
        for i in range(1,len(nums)):
            frequency.append(nums[i]-nums[i-1])
        prefix_sum =0
        print(frequency)
        print(nums)
        count = 0
        right = 1
        left = 0
        max_ = 0
        while right < len(nums):
            count += (nums[right] - nums[right - 1])*(right-left)
            prefix_sum+= nums[right] - nums[right - 1]
            while count > k:
                count -= prefix_sum
                prefix_sum-=frequency[left]
                left += 1
            max_ = max(max_, right - left + 1)
            right += 1
        return max_
                
        
        