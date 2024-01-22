class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Approach: Sliding Window
        #Step1: assign two pointers to the start of the array and min size and current sum to zero
        left=right=0
        min_size,current_sum=float('inf'),0

        #Step2: iterate through the array until the right pointer reaches it's end
        while right<len(nums):

            #Step3: check if the current sum is less than the target and expand the window size
            if current_sum<target:
                current_sum+=nums[right]
                right+=1

            #Step4: if the current sum is greater than or equal to the target then take the minimum window size and shrink it by one until it's less than the target
            while current_sum>=target:
                min_size = min(min_size,right-left)
                current_sum-=nums[left]
                left+=1
        #Step5: check if the window size has never been updated and return 0
        if min_size==float('inf'):
            return 0
        return min_size
        #Time Complexity: O(n)
        #Space Complexity: O(1)