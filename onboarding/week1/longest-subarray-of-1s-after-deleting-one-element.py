class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #Approach: Sliding window
        n = len(nums)
        #Step1: check for edge cases if all elements are 1 return n-1
        if sum(nums)==n:
            return n-1
        #Step2: assign two pointers to the start of the array and set max_length to zero
        left=right=0
        max_length=0
        count_of_zero =0
        #Step3: iterate through the array while checking if the count_of_zero is either less than one or equal to one if it's then calculate max_length by right-left-1 if not just increment the right pointer
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
        #Step4: last check if the array goes out of bound before calculating the max_length
        max_length = max(max_length,right-left-1)
        return max_length
