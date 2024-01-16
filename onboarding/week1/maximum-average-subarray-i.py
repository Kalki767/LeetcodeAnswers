class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window approach
        maxSum=currSum=sum(nums[:k])
        left,right=0,k
        while right<len(nums):
            currSum=currSum-nums[left]+nums[right]
            maxSum = max(maxSum,currSum)
            right+=1
            left+=1
        return maxSum/k