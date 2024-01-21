class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums)==n:
            return n-1
        left=right=0
        max_length=0
        count_of_zero =0
        while right<n:
            if count_of_zero<1:
                if nums[right]==0:
                    count_of_zero+=1
                right+=1
            elif count_of_zero==1:
                if nums[right]==0:
                    max_length = max(max_length,right-left-1)
                    while count_of_zero==1:
                        if nums[left]==0:
                            count_of_zero-=1
                        left+=1
                else:
                    right+=1
        max_length = max(max_length,right-left-1)
        return max_length
